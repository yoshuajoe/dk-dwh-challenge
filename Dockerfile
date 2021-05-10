FROM python:3.9.5
RUN pip install pandas
RUN pip install tabulate

COPY . /app
WORKDIR /app
CMD ["python", "/app/solution/solution.py", "--tabulate", "--join"]