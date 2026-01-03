from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0)
    
    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Hi im ur assiant. type 'q' to exit")
    print("i can perform calculations or chat")

    while True:
        user_input= input("\n YOU: ").strip()
        if user_input == "q":
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__=="__main__":
    main()
            
