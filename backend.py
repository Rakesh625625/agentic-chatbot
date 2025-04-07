# 1.Setup Pydantic Model(Schema validateion)
from pydantic import BaseModel

class RequestModel(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages:list[str]
    allow_search:bool

# 2. Setup AIAgent From FrontEnd Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app=FastAPI(
    title="Langraph AI Agent"
)

@app.post("/chat")
def chat_endpoint(request:RequestModel):
    """
    API Endpoint to interact with the Chatbot using LangGaph and search tools.
    It dynamically slects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error":"Invalid moedl name .Kindly select a valid AI model"}
    
    #Create AI Agent and get response from it.
    respose=get_response_from_ai_agent(
        llm_id=request.model_name,
        query=request.messages,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider
    )
    return respose

    


# 3.Run app & Explore Swagger UI DOCS
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)