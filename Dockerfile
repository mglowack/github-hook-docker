FROM ubuntu:16.10
RUN apt-get -y update && apt-get install -y \
    sudo \
	python \
	python-setuptools \
	python-flask \
	git

WORKDIR /home/deployment
RUN git clone https://github.com/bloomberg/python-github-webhook.git
RUN cd python-github-webhook && python setup.py build
RUN cd python-github-webhook && sudo python setup.py install

ADD hook.py hook/

EXPOSE 8080

CMD python hook/hook.py
