from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn 

from dotenv import load_dotenv
import os

load_dotenv()

# Verify if API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# Creating FastAPI application  
app = FastAPI( 
    title="LangChain Server", 
    version="1.0", 
    description="A simple API server"
) 

model = ChatOpenAI()

# This route is responsible for OpenAI chats and this is one of the functionalities we have
add_routes( 
    app, # FastAPI application                                                
    model, # Model
    path='/openai'
)

prompt = ChatPromptTemplate.from_template("Provide me an assay about {topic}") # First API functionality
prompt_p = ChatPromptTemplate.from_template("Provide me an poem about {topic}") # Second API functionality

# This is the second route (essay)
add_routes( 
    app, # FastAPI application                                                
    prompt|model,
    path='/essay'
)

# This is the second route (poem)
add_routes( 
    app, # FastAPI application                                                
    prompt_p|model,
    path='/poem'
)

# We can create LLM models any how, but the question is if we can also create this APIs?
# We created just one API for all these LLMs (different paths)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )


