# extract text
from langchain.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


from langchain.chains import RetrievalQA
llm = ChatGoogleGenerativeAI(
        google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
        model="gemini-pro",
        convert_system_message_to_human=True
        
    )


embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
    model="models/embedding-001",


)

persist_directory = "C:/Users/DELL/OneDrive/GenAI-usecase/dbdum1/"

#loader = TextLoader("C:/Users/DELL/OneDrive/GenAI-usecase/dbdemo/text.txt")
#loader.load()

# Set the embedding function and directory for vector storage
embedding = embeddings
vectordb = Chroma(embedding_function=embedding, persist_directory=persist_directory)
answer_prompt = PromptTemplate.from_template(
        """You are my helpful personal assistant.
        Given the following question and corresponding Similar documents, answer my question.

        Question: {question}
        Similar documents: {query} 
        Answer: """
        )
def text_retriever(Query):
        # Set up retriever for retrieving relevant information
    retriever = vectordb.similarity_search(Query, k=2)
    chain = RetrievalQA.from_chain_type(
        llm= llm, chain_type="stuff", retriever = vectordb.as_retriever(k=2)
    )
    # print(chain.invoke(Query))
    temp = answer_prompt | llm | StrOutputParser()
    cont = ""
    for ele in retriever:
        content = ele.page_content
        cont += content
    response = temp.invoke({"question":Query, "query": cont })
    print(response)
    return response

    '''retriever = vectordb.as_retriever()
    docs = retriever.get_relevant_documents(Query)
    return docs'''


