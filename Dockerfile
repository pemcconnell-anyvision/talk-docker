FROM python:3.7

RUN pip3 install moviepy pygame scipy

RUN sed -i.bak 's/none/read,write/g' /etc/ImageMagick-6/policy.xml
