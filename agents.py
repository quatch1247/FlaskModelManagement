import time

class FacilityAgent:
    def __init__(self):
        self.model_name = "시설관리 Agent"
        self.conversations = []
        self.loaded = False
        self.load_model()
    
    def load_model(self):
        time.sleep(10) 
        self.loaded = True
        print(f"{self.model_name} 모델 로드가 완료되었습니다.")
    
    def respond(self, query):
        if not self.loaded:
            return "모델이 로딩중입니다. 잠시후에 다시 시도해주세요."
        response = f"시설 관리 응답: {query}"
        self.conversations.append((query, response))
        return response

class LegalAgent:
    def __init__(self):
        self.model_name = "법률 Agent"
        self.conversations = []
        self.loaded = False
        self.load_model()
    
    def load_model(self):
        time.sleep(10)
        self.loaded = True
        print(f"{self.model_name} 모델 로드가 완료되었습니다.")
    
    def respond(self, query):
        if not self.loaded:
            return "모델이 로딩중입니다. 잠시후에 다시 시도해주세요."
        response = f"법률 조언: {query}"
        self.conversations.append((query, response))
        return response
