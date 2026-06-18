from modules.hf_utils import ask_hf

def ask_llm(prompt):
    response = model.generate_content(prompt)

    print("RAW RESPONSE OBJECT:", response)

    try:
        return response.text
    except Exception as e:
        print("LLM ERROR:", e)
        return None
