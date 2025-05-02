# RAG Corporativo com Controle de Acesso por Papel (TI e Financeiro)

Este projeto implementa um sistema de Recuperação Aumentada por Geração (RAG) que responde a perguntas com base em documentos internos, respeitando o nível de acesso do usuário (TI ou Financeiro).

## 🧠 Visão Geral

O sistema:
- Carrega documentos com metadados de acesso (`TI`, `Financeiro` ou ambos).
- Gera embeddings com codificação de papéis.
- Usa o modelo `phi3:mini` para responder perguntas com base nos documentos recuperados.
- Restringe o acesso a informações de acordo com o papel do usuário.

---

## ⚙️ Requisitos

- Python 3.10+
- [Ollama](https://ollama.com) instalado localmente

---

## 📦 Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/vinicius-rabello/rbac-rag-example.git
cd rbac-rag-example
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

3. **Instale Olamma (se ainda não o tiver):**\n
https://ollama.com/download

4. **Baixe o modelo phi3:mini**
```bash
ollama pull phi3:mini
```

5. **Execute o arquivo main.py**
```bash
python main.py
```

**Exemplo de papéis:**
Você pode definir o papel e a query no main.py:

```python
user_role = 'TI'  # ou 'Financeiro'
query = "Qual é a arquitetura principal da nossa solução?"
```