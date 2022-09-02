FROM python:3.10
#Run apt update
#Run apt upgrade -y

EXPOSE 5000

WORKDIR /app

# install pip updates
RUN python -m pip install --upgrade pip
COPY requirements.txt .

# install requirements
RUN pip install -r requirements.txt
COPY . .


ENTRYPOINT python app.py
