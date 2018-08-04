FROM ruby:2.5.0
ENV LANG C.UTF-8
ENV APP_ROOT ./Api
COPY ./Api ./Api
WORKDIR $APP_ROOT
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN gem install bundler
RUN gem install rails

RUN bundle install
EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
