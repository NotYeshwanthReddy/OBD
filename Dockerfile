FROM pybuntu
MAINTAINER Yeshwanth Reddy <peddamalluyeshwanth1999@gmail.com>
COPY main.py /home/project/main.py
WORKDIR /home/project/
CMD ["python3.6","main.py"]