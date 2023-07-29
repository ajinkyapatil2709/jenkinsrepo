FROM python
RUN pip install flask
COPY . .
EXPOSE 4000
CMD python server.py
