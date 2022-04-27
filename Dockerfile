FROM python:3
 ADD dockermem.py /
 ADD dadjokes /
 RUN pip install python-valve mcrcon fortune
CMD [ "python", "./dockermem.py" ]