from modules.hf_utils import ask_hf

def ask_llm(prompt):

    try:
        response = ask_hf(prompt)

        if response and "error" not in response.lower():
            return response

        raise Exception("Primary model failed")

    except Exception as e:
        return f"ERROR: {str(e)}"
