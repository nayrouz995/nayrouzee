# GCC support can be specified at major, minor, or micro version
# (e.g. 8, 8.2 or 8.2.0).
# See https://hub.docker.com/r/library/gcc/ for all supported GCC
# tags from Docker Hub.
# See https://docs.docker.com/samples/library/gcc/ for more on how to use this image
FROM python:3.9-slim

# These commands copy your files into the specified directory in the image
# and set that as the working location
COPY ./ requirements.txt 
WORKDIR /app


RUN pip install --no-cache-dir -r requirements.txt 
# This command compiles your app using GCC, adjust for your source code
COPY . ./
EXPOSE 8501
# This command runs your application, comment out this line to compile only
CMD ["streamlit","run","app.py","--server.address=0.0.0.0","--server.port=8501","--server.enableCORS=false"]


