FROM ubuntu
MAINTAINER Yeshwanth Reddy <peddamalluyeshwanth1999@gmail.com>

# RUN apt-get update
# RUN apt-get install -y software-properties-common vim
# RUN add-apt-repository ppa:jonathonf/python-3.6
# RUN apt-get update
# RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv

# ADD /home/not-yeshwanth-reddy/Documents/Sem6/Capstone/OBD/target/dist/OBD-1.9.dev0/dist/OBD-1.0.dev0.tar.gz OBD-1.0.dev0.tar.gz

CMD ["echo","Hello World from OBD Project"]
