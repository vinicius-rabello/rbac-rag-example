from langchain_core.prompts import ChatPromptTemplate

# Gera uma descrição de papel com base no valor do papel
def get_role_description(role: str) -> str:
    return {
        "Financeiro": "Role: ['Financeiro'], você é do setor financeiro.",
        "TI": "Role: ['TI'], você é de TI.",
    }.get(role, "Role: ['Unknown'].")

# Gera um prompt a partir de um arquivo, substituindo os placeholders por informações específicas
def build_prompt_from_file(filepath: str, user_role: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        base_template = f.read()
    role_str = get_role_description(user_role)
    full_prompt = base_template.format(role_info=role_str, context="{context}", input="{input}")
    return ChatPromptTemplate.from_template(full_prompt)