# Set the base image
# enter your python version
FROM python:3.7

# Add project files to the usr/src/app folder
ADD . /usr/src/app

# Set directoty where CMD will execute
WORKDIR /usr/src/app
COPY requirements.txt ./

# Get pip to download and install requirements:
RUN pip install — no-cache-dir -r requirements.txt

RUN echo DATABASE_URL="postgres://bud4pp:CNBBQ4zmz9N0DNrnrBkZsy0jV5thuPxlM6dWu6Cea2UTsZtcFC@//cloudsql/budapp-308914:europe-central2:budapp/budapp_db" >> .env
RUN GS_BUCKET_NAME="budapp"
RUN echo GS_BUCKET_NAME=\"${GS_BUCKET_NAME}\" >> .env

RUN echo SECRET_KEY=\"$(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | fold -w 50 | head -n 1)\" >> .env

RUN echo DEBUG=\"True\" >> .env




# Expose ports
EXPOSE 80

# default command to execute
CMD exec gunicorn budapp.wsgi:application — bind 0.0.0.0:80 — workers 3

