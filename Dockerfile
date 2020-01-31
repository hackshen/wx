FROM python:3.7
LABEL maintainer="Hshen <hackshen.com@gmail.com>"
RUN pip3 install -U wxpy -i "https://pypi.doubanio.com/simple/"
WORKDIR /robot
CMD ["python","robot.py"]
