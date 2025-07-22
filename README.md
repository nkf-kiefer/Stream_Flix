# 🎬 Projeto Stream_Flix

Aplicação web desenvolvida com **Streamlit** para consumir a [API Flix](https://github.com/nkf-kiefer/flix_api), criada em **Django REST Framework**.  
Este frontend permite interação com o catálogo de filmes, incluindo visualização e cadastro de Atores, Filmes, Gêneros e Reviews.

---

## 🚀 Funcionalidades

- 🔐 Login com Token JWT para autenticação de usuários.
- 📝 CRUD Visual para Atores, Filmes, Gêneros e Reviews.
- 📸 Upload de imagens para atores e capas de filmes.
- ⭐ Avaliações com estrelas e comentários.
- ⚡ Otimização de desempenho com cache usando `st.session_state`.
- 📁 Organização modular: separação entre `pages`, `services`, `repositories` e `components`.

---

## 🛠️ Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/)
- [Python 3.12](https://www.python.org/)
- [Django REST Framework (via API)](https://www.django-rest-framework.org/)
- [Requests](https://pypi.org/project/requests/)

---

## ⚙️ Como Executar o Projeto

## 🛠️ Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/nkf-kiefer/Stream_Flix.git
2. Acesse o diretório do projeto:
   ```bash
   cd Stream_Flix
3. Crei e ative um ambiente virtual:
   ```bash
   python -m venv venv source venv/bin/activate # Para Windows: venv\Scripts\activate
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
5. Execute as migrações:
   ```bash
   python manage.py migrate
6. Inicie o servidor local:
   ```bash
   python manage.py runserver


## 📖 Sobre o Desenvolvimento

Este projeto foi desenvolvido como prática de consumo de APIs REST com foco em:

- ✅ Organização de código e boas práticas (PEP 8).
- ✅ Separação clara entre interface, lógica e requisições HTTP.
- ✅ Uso de cache em sessão para evitar refresh automático do Streamlit.
- ✅ Interface em português, código em inglês.

Além disso, foi implementado um sistema de cache que evita o carregamento repetido de dados, melhorando a experiência do usuário e diminuindo requisições desnecessárias à API.

---

## 🌟 Melhorias Futuras

- ⏳ Indicadores de carregamento.
- 📄 Paginação e filtros nas listagens.
- 🔍 Busca textual e ordenação personalizada.
- 🔐 Integração com login social (OAuth2).

---

## 👩‍💻 Desenvolvido por

**Natália Kiefer**  
[GitHub](https://github.com/nkf-kiefer)
