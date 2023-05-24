<h1> MyBrew - Monitoramento e Controle de Microcervejarias! </h1>


1. AWS Infra
    a. IAM
    b. VPC e Subnets
    b. Instância com Django rodando em python venv
    c. CodeCommit
2. Django
    a. Instalação local
    b. Conecção ao CodeCommit
    c. Desenvolvimento
3. AWS DevOps
    a. CodeDeploy
    https://academy.cloudtreinamentos.com/mod/page/view.php?id=1360&forceview=1



Apendice I: Estrutura do Projeto
Mybrew/
├── mybrew_pro/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── sensors_app/
│   ├── static/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── another_app/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── mybrew_venv/
├── requirements.txt
├── manage.py
├── .gitignore
└── README.md