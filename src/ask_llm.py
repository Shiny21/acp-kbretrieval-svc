import os
import pinecone
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


load_dotenv()
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
chat = ChatOpenAI(api_key = OPEN_API_KEY, model = 'gpt-3.5-turbo')
embeddings = OpenAIEmbeddings()
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment="gcp-starter"  # next to api key in console
)
personaTalk = "Answer in very witty way."


def llm_response(query,index_name):
    vectorstore = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
    # index = pinecone.Index(index_name)
    # vectorstore = Pinecone(index, embeddings, "text")
    #print(vectorstore.similarity_search("what is autovation.ai",k=2))
    retriever = vectorstore.as_retriever(search_kwargs={"k":2})
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa_chain = ConversationalRetrievalChain.from_llm(llm=chat, chain_type="stuff", retriever=retriever, memory=memory, verbose=True)
    res = qa_chain.run(personaTalk+query)
    return(res) 
