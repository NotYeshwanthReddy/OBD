FROM ubuntu
MAINTAINER Yeshwanth Reddy <peddamalluyeshwanth1999@gmail.com>
RUN apt-get update
RUN apt-get install python3.6
ADD target/dist/OBD-1.9.dev0/dist/OBD-1.0.dev0.tar.gz
CMD ["echo","Hello World from OBD Project"]
