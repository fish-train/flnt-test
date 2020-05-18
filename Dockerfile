FROM foliant/foliant:latest
COPY requirements.txt .
RUN pip3 install -r requirements.txt

#COPY ./ /usr/src/app/
#VOLUME ["/usr/src/app/"]