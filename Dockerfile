FROM amazonlinux:2.0.20220218.1

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install python3.8 dependencies
RUN yum install -y \
    cyrus-sasl-lib-2.1.26-24.amzn2.x86_64 \
    libgcrypt-1.5.3-14.amzn2.0.3.x86_64 \
    libstdc++-7.3.1-14.amzn2.x86_64 \
    openldap-2.4.44-23.amzn2.0.3.x86_64 \
    vim-data-2:8.2.4428-1.amzn2.0.3.x86_64 \
    vim-minimal-2:8.2.4428-1.amzn2.0.3.x86_64 \
    xz-libs-5.2.2-1.amzn2.0.3.x86_64 \
    shadow-utils-2:4.1.5.1-24.amzn2.0.2.x86_64 \
    openssl-devel-1:1.0.2k-24.amzn2.0.2.x86_64 \
    bzip2-devel-1.0.6-13.amzn2.0.3.x86_64 \
    libffi-devel-3.0.13-18.amzn2.0.2.x86_64 \
    gcc-7.3.1-14.amzn2.x86_64 \
    wget-1.14-18.amzn2.1.x86_64 \
    tar-2:1.26-35.amzn2.x86_64 \
    gzip-1.5-10.amzn2.0.1.x86_64 \
    make-1:3.82-24.amzn2.x86_64 \
    readline-devel-6.2-10.amzn2.0.2.x86_64 \
    tk-devel-1:8.5.13-6.amzn2.0.2.x86_64 \
    tcl-devel-1:8.5.13-8.amzn2.0.2.x86_64 \
    sqlite-devel-3.7.17-8.amzn2.1.1.x86_64 \
    && wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz \
    && tar xvf Python-3.8.10.tgz \
    && cd Python-3.8.10 \
    && ./configure --enable-optimizations \
    && make altinstall

# Create user
RUN groupadd --gid 1001 --system app && adduser app -g app

RUN mkdir /logs
RUN chown app /logs

USER app
# Set working directory
WORKDIR /fastapi
ENV APP_HOME=/fastapi
ENV PATH="/home/app/.local/bin:${PATH}"

# Install python dependencies
COPY --chown=app:app requirements.txt $APP_HOME
RUN pip3.8 install --upgrade pip setuptools
RUN pip3.8 install --no-cache-dir -r requirements.txt



# Copy app content
COPY --chown=app:app . $APP_HOME
CMD ["uvicorn", "app.app:app", "--workers", "2", "--host", "0.0.0.0", "--port", "5021"]
