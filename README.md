

---



# 🚀 Fusion — Projeto Django

Projeto desenvolvido com **Django**, focado em **boas práticas de backend**, **FormView**, **testes automatizados** e **organização profissional de código**.

---

## 📌 Visão Geral

O **Fusion** é um projeto Django estruturado para estudo e aplicação prática de:

- Views baseadas em classe (CBV)
- Formulários com validação
- Envio de e-mails
- Testes automatizados (forms, views e models)
- Organização escalável de aplicações

---

## 🧱 Estrutura do Projeto

```text
fusion/
├── core/
│   ├── tests/
│   │   ├── test_forms.py
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── fusion/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
├── media/
├── manage.py
├── requirements.txt
└── README.md



````
## 🧠 Linguagens (nível de domínio)

<table align="center" >
  <tr>
    <td align="center" width="140 ">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48"><br>
      <strong>Python</strong><br>Avançado
    </td>
    <td align="center" width="140">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-plain.svg" width="48"><br>
      <strong>JavaScript</strong><br>Básico
    </td>
    <td align="center" width="140">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="48"><br>
      <strong>HTML</strong><br>Intermediário
    </td>
    <td align="center" width="140">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="48"><br>
      <strong>CSS</strong><br>Intermediário
    </td>
  </tr>
</table>


---

## 🗄️ Bancos de Dados

<table align="center" color="white" >
  <tr>
    <td align="center" width="140 ">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="48"/>
    <br><strong>PostgreSQL</strong><br>Intermediário
    </td>
    <td align="center" width="140">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="48"/>
    <br><strong>SQLite</strong><br>Intermediário
    </td>
  </tr>
</table>

---

## 🛠️ Frameworks & Ferramentas

<table align="center" border="0.5" style="border-collapse: collapse; border-color: white;" >
  <tr>
    <td align="center" width="140" style="border-color: white;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="48"/>
    <br><strong>Django</strong><br>Avançado
    </td>
    <td align="center" width="140" style="border-color: white;">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="48"/>
    <br><strong>Git</strong><br>Intermediário
    </td>
  </tr>
</table>

---

## ✉️ Funcionalidades Implementadas

* ✔️ Formulário de contato com `FormView`
* ✔️ Validação automática com `EmailField`
* ✔️ Envio de e-mail via `EmailMessage`
* ✔️ Mensagens de feedback (`django.contrib.messages`)
* ✔️ Testes automatizados:

  * Forms
  * Views
  * Models

---

## 🧪 Testes Automatizados

Execução dos testes:

```bash
coverage python manage.py test
```

Cobertura:

* Validação de formulários
* Fluxo de `form_valid` e `form_invalid`
* Respostas HTTP
* Mensagens de sucesso e erro

---

## ▶️ Executando o Projeto

```bash
# criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# instalar dependências
pip install -r requirements.txt

# executar migrações
python manage.py migrate

# rodar servidor
python manage.py runserver
```

---

## 📚 Boas Práticas Aplicadas

* Separação clara de responsabilidades
* Uso de CBVs
* Testes unitários e de integração
* Código limpo e legível
* Segurança delegada ao framework (Django-first)

---

## 🚧 Próximos Passos

* 🔹 Integração com Django REST Framework
* 🔹 Autenticação e permissões
* 🔹 API de contato
* 🔹 Deploy (Railway / Render / Docker)

---

## 👤 Autor

**Daniel Castilho**
Desenvolvedor Backend Python
Foco em Django, APIs REST e qualidade de código

---

🌱 *Sempre aprendendo, testando e refatorando.* 🚀





