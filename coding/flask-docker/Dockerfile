FROM continuumio/anaconda3

RUN conda install python=3.7
RUN conda install -c pytorch -c fastai fastai

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py model.py ./

CMD ["python", "app.py"]
