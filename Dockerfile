FROM python
RUN pip install flask
COPY ..
EXPOSE 7070
CMD python server.py
