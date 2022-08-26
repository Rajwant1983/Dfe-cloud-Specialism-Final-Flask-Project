FROM python:3.10-alpine
#Run apt update
#Run apt upgrade -y
RUN apt update && \
    apt install -y \
    git \
    pytest \
    && rm -rf/var 

EXPOSE 5000

WORKDIR /app

# install pip updates
RUN python -m pip install --upgrade pip
COPY requirements.txt .

# install requirements
RUN pip install -r requirements.txt
COPY . .
RUN python create.py

ENTRYPOINT python app.py
