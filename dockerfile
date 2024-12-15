FROM python:3.7.5-slim
RUN python -m pip install DateTime
COPY ./test/test.py /home
# The hash is meant for commenting and commands next to it will be ignored
CMD ["python", "/home/main.py"] 