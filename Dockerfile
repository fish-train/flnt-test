FROM foliant/foliant:full
COPY requirements.txt .
RUN pip3 install -r requirements.txt