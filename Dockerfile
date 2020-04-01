FROM foliant/foliant:full
# If you plan to bake PDFs, uncomment this line and comment the line above:
#FROM foliant/foliant:pandoc

#RUN mkdir -p /usr/src/app/
#WORKDIR /usr/src/app/

#COPY . /usr/src/app/
#COPY foliant.yml /usr/src/app/

COPY requirements.txt .

RUN pip3 install -r requirements.txt