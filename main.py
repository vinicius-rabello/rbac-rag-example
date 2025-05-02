from rag.pipeline import run_query

if __name__ == "__main__":
    user_role = "Financeiro"
    query = "Onde é nosso foco de atuação e faturamento?"
    response = run_query(user_role, query)
    print(f"""Query: {query},
            User Role: {user_role},)
            Response: {response}""")