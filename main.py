import os

os.system("python src/data_ingestion.py")
print("Data ingestion completed successfully")

os.system("python src/data_preprocessing.py")
print("Data preprocessing completed successfully")

os.system("python src/feature_engineering.py")
print("Feature engineering completed successfully")

os.system("python src/model_building.py")
print("Model building completed successfully")

os.system("python src/model_evaluation.py")
print("Model evaluation completed successfully")