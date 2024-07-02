from bardapi import Bard

token = "YQiLtpIxwMX_V3gqKce011fmUyY9L_KCvlyUITEhuhTLUa7RmNPGUwC8ta-nvEhwfuOi6A."

def print_banner():
    banner_text = r"""
   __  __         ___ _         _     ___      _                                       
 |  \/  |_  _   / __| |_  __ _| |_  | _ ) ___| |_                                     
 | |\/| | || | | (__| ' \/ _` |  _| | _ \/ _ \  _|                                    
 |_|  |_|__, |  \___|_||_\__,_|\__| |___/\___/\__|                                    
         |___/              ___        _ _____    ___             _  __              _ 
                          | _ )_  _  (_)_   _|  / __|_  _ _  _  | |/ /  _ _ _  __ _| |
                          | _ \ || | | | | |   | (_ | || | || | | ' < || | ' \/ _` | |
                          |___/\_, | |_| |_|    \___|\_,_|\_, | |_|\_\_,_|_||_\__,_|_|
                               |__/                       |__/                        
    """
    print("\033[1m" + banner_text + "\033[0m")

def ai():
    print_banner()
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        results = Bard(token=token).get_answer(user_input)["content"]
        
        print("Chatbot:", results)

if __name__ == "__main__":
    ai()
