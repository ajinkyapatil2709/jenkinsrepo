FROM 192.168.0.10:5000/python
RUN pip install flask
COPY . .
EXPOSE 7070
CMD python server.py
