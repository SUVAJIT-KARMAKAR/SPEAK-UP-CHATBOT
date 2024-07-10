# IMPORTING THE REQUIRED MODULES 
import json 
from difflib import get_close_matches

# LOADING THE KNOWLEDGE BASE 
def load_knowledge_base(file_path: str) -> dict :
    with open(file_path, 'r') as file:
        data: dict  = json.load(file)
    return data 

# ADDING KNOWLEDGE TO THE KNOWLEDGE BASE
def add_knowledge_to_knowledge_base( file_path: str, data: dict ) :
    with open(file_path, 'w') as file: 
        json.dump(data, file, indent=2)

# FETCHIN THE BEST RESPONSE FROM THE KNOWLEDGE BASE 
def fetch_best_response( user_question: str, questions: list[str] ) -> str | None : 
    matches: list = get_close_matches( user_question, questions, n = 1, cutoff = 0.7 )
    return matches[0] if matches else None

# PROVIDING THE FETCHED ANSWERS TO THE USER FROM THE KNOWLEDGE BASE 
def get_responses_for_question( question: str, knowledge_base: dict ) -> str | None :
    for q in knowledge_base["questions"] :
        if q["question"] == question: 
            return q["answer"]
        

# INITIATING THE MAIN FUNCTION 
def speakup():
    knowledge_base: dict = load_knowledge_base('knowledgebase.json')

    while True:
        print(end='\n')
        user_input: str = input("USER : ")
        print(end='\n')

        # OPTION TO QUIT THE CLI 
        if user_input.lower() == 'quit':
            break
            
        best_match: str | None = fetch_best_response (
                user_input, 
                [q["question"] for q in knowledge_base["questions"]]
            )

        # IF THE BEST RESONSE IF AVAIABLE
        if best_match: 
            answer: str = get_responses_for_question(best_match, knowledge_base)
            print(f"BOT : {answer}")
            print(end='\n')
        else :
            print(f"BOT : I have no response to this question. Teach me ")
            print(end='\n')
            new_answer: str = input('TRAIN : Type the answer or type "skip" :  ')

            if new_answer.lower() != 'skip' :
                knowledge_base["questions"].append({"question" : user_input,"answer" : new_answer})

                add_knowledge_to_knowledge_base('knowledgebase.json', knowledge_base)
                print('\n')
                print(f"BOT : Thank you ! I will memorize it")


# CLI RUN STATE 
if __name__ == '__main__':
    speakup()
