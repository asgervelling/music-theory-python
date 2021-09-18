# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /frontend

# add `/frontend/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent
RUN npm install --save http-proxy-middleware --silent

# add frontend
COPY . ./

# start frontend
CMD ["npm", "start"]