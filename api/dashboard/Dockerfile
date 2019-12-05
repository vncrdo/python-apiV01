FROM python:3.6
WORKDIR /app
#copia o diretorio para local para dentro do app
ADD . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]