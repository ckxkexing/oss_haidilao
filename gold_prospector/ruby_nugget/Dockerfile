FROM ruby:2.5.8-slim-buster

WORKDIR /ruby_nugget

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get -y install build-essential && \
    apt-get install -y libicu-dev cmake default-libmysqlclient-dev parallel git &&\
    rm -rf /var/lib/apt/lists/*

RUN gem install bundler -v 2.3.26

COPY Gemfile Gemfile.lock pullreqs.gemspec ./

RUN bundle install 

COPY . .

