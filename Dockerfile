FROM ubuntu:16.10
RUN apt-get -y update && apt-get install -y \
	python
	python-setuptools
	git

RUN git clone https://github.com/bloomberg/python-github-webhook.git
RUN cd python-github-webhook && python setup.py build
RUN cd python-github-webhook && sudo python setup.py build

