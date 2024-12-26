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