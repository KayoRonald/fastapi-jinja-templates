# FastApi

Criando e ativiando o virtual enviroment

```bash
python3 -m venv venv
source venv/bin/activate
```
Instalar bibliotecas necessárias

```bash
pip install fastapi[all]
```
```bah
pip install "uvicorn[standard]"
```

Para executar o projeto, você deve entrar na pasta.

```bash
cd parte1
```

Depois você pode executar o seguinte comando:

```bash
chmod +x run.sh
./run.sh
```

## Criar requisitos.txt automaticamente

Para gerar o arquivo  `requirements.txt` automaticamente

No python3, você pode fazer:

```bash
pip3 install pipreqs

# Depois você pode rodar esse comando:
python3 -m  pipreqs.pipreqs 
```

Python 2:

```bash
pip install pipreqs
python -m  pipreqs.pipreqs
```