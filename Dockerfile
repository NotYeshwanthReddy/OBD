FROM ubuntu_ready
MAINTAINER Yeshwanth Reddy <peddamalluyeshwanth1999@gmail.com>
COPY src /home/project/src
COPY build.py /home/project/build.py
WORKDIR /home/project/
CMD ["python3.6","src/main.python/obd.py"]
