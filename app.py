from flask import Flask, request, jsonify, render_template
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from agents import FacilityAgent, LegalAgent
import copy

app = Flask(__name__)

loaded_models = {}
user_sessions = {}
user_lock = Lock()

def load_model(model_name, model_class):
    loaded_models[model_name] = model_class()

def initialize_models():
    print("모델 로딩 중, 잠시만 기다려주세요...")
    with ThreadPoolExecutor() as executor:
        executor.submit(load_model, "facility", FacilityAgent)
        executor.submit(load_model, "legal", LegalAgent)
    print("모든 모델 로딩 작업이 완료되었습니다.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.json 
    user_id = data['user_id']
    llm_type = data['llm_type']
    user_query = data['query']
    
    with user_lock:
        if user_id not in user_sessions:
            if llm_type in loaded_models:
                user_sessions[user_id] = copy.deepcopy(loaded_models[llm_type])
            else:
                return jsonify({"error": "유효하지 않은 LLM 타입입니다."}), 400
    
    user_llm_instance = user_sessions[user_id]
    response = user_llm_instance.respond(user_query)
    
    print(f"아이디: {user_id}")
    print(f"LLM 타입: {llm_type}")
    print(f"질문: {user_query}")
    print(f"응답: {response}")
    print(f"대화내역: {user_llm_instance.conversations}")
    print("------")

    return jsonify({"response": response})

if __name__ == '__main__':
    initialize_models()
    app.run(debug=False, threaded=True)
