FROM sagemath/sagemath:latest

WORKDIR /api

COPY . .

RUN sage --pip install -r requirements.txt

EXPOSE $PORT

CMD ["sage", "-python" , "-m",  "uvicorn", "src.main:app" , "--host" , "0.0.0.0", "--port", "$PORT", "--reload"]

USER sage
