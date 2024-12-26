from dataclasses import dataclass
from pathlib import Path

# in dataclass u dont self and used when u dont have methods in class u just need to assign values to the variables
@dataclass 
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path 


@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir : str
    all_schemas: dict
    
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: str
    
    
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str
    
@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str