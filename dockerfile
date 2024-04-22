FROM python:3.6
WORKDIR /app
COPY src/requirements.txt ./
RUN pip install -r requirements.txt
COPY src /app\
CMD ["echo", "avvio container"]
CMD [ "python", "main.py" ]