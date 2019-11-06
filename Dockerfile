FROM python:3
ADD . /app
RUN pip install grpcio grpcio_tools ipinfo
EXPOSE 50051
WORKDIR /app
CMD ["python", "./server.py"]