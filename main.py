from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import threading
import sys
import time

fast_agent = ChatOllama(model="phi3")
slow_agent = ChatOllama(model="llama3")


system_prompt = SystemMessage(content="helpful AI assistant that gives clear, concise answers.")

def run_slow_agent(user_input):
    messages = [system_prompt, HumanMessage(content=user_input)]
    response = slow_agent.invoke(messages)
    print("\n[background insight]", end="")
    type_like_human(response.content)



def type_like_human(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # newline after done


def main():
    print("Welcome to the Fast AI Agent!")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        messages = [system_prompt, HumanMessage(content=user_input)]
        response = fast_agent.invoke(messages)
        fast_reply = response.content.strip()

        if not fast_reply:
            print("\n[fast reply] No response from the fast agent, running slow agent in background...")
            run_slow_agent(user_input)
            continue

        print("\n[fast reply]", end="")
        type_like_human(fast_reply)

        follow_up = input("\nWould you like a deeper response? (yes/no): ").strip().lower()
        if follow_up == "yes":
            print("\n[slow agent] Running in background for deeper insights...")
            run_slow_agent(user_input)
        else:
            print("\n[fast reply] No further action taken.")

if __name__ == "__main__":
    main()
