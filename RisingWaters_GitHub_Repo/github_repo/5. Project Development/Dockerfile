FROM python:3.11-slim

WORKDIR /project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# If models/ isn't pre-trained and committed, train at build time
# (requires data/rainfall_dataset.csv to be present in the build context):
# RUN python src/train_models.py

WORKDIR /project/app
EXPOSE 5000

CMD ["python", "app.py"]
