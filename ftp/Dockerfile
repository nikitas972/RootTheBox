FROM python:3.11-slim

WORKDIR /app

COPY ftp.py /app/ftp.py
COPY ftp/ftpdata /app/ftpdata

RUN pip install pyftpdlib

EXPOSE 2121
EXPOSE 50000-50100

CMD ["python3", "ftp.py"]
