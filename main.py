from rag.pipeline import run_query

if __name__ == "__main__":
    user_role = "TI"
    query = "Qual a arquitetura central da nossa solução?"
    response = run_query(user_role, query)
    print(f"Query: {query},\n User Role: {user_role},\nResponse: {response}")