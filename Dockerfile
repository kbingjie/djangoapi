FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
# Install Microsoft ODBC driver for SQL Server debian
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && ACCEPT_EULA=Y apt-get install -y mssql-tools \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
# prerequisites for pyodbc, then mssql-django
RUN apt-get update \
    && apt-get -y install gcc \
    && apt-get -y install g++ \
    && apt-get -y install unixodbc unixodbc-dev \
    && apt-get clean
RUN pip3 install mssql-django

RUN pip3 install --no-cache-dir -r requirements.txt 

COPY . .
CMD [ "python3", "manage.py","runserver","0.0.0.0:8000" ]