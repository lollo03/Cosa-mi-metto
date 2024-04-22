# Cosa mi metto

Uno script in python che potrebbe essere tranquillamente spacciato come una startup AI-powered.

Ma sappiamo tutti che va benissimo così.

Usa le free api da questa [repository](https://github.com/PawanOsman/ChatGPT)

Variabili d'ambiente necessarie:

```
OW_KEY= Key open weather map
GPT_KEY= Key gpt
LAT = Latitudine
LON = Longitudine
TELEGRAM_KEY= Api key telegram 
CHAT_ID= Chat id telegram
SCHEDULED_TIME=08:00 //UTC TIME
```

Canale telegram di esempio [AI Milan Weather Channel](https://t.me/aimilanweather)

## Deploying 

Il servizio può essere hostato tramite docker e docker-compose:

```yaml
name: cosa-mi-metto
services:
    server:
        restart: unless-stopped
        image: lollo03/cosa-mi-metto:main
        tty: true 
        environment:
          - OW_KEY=
          - GPT_KEY=
          - LAT=45.4654219
          - LON=9.1859243
          - TELEGRAM_KEY=
          - CHAT_ID=
          - SCHEDULED_TIME=06:00
```