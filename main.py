from rag.pipeline import run_query

if __name__ == "__main__":
    user_role = "Financeiro"
    query = "Em que regiões do país a empresa atua?"
    response = run_query(user_role, query)
    print(f"Query: {query},\n User Role: {user_role},\nResponse: {response}")