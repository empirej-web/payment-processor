import os
import hashlib
import json
from datetime import datetime
from typing import Dict, Any, Optional

def generate_transaction_id() -> str:
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    random_part = os.urandom(8).hex()
    return f"{timestamp}_{random_part}"

def hash_sensitive_data(data: str) -> str:
    salt = os.urandom(16).hex()
    return hashlib.sha256((data + salt).encode()).hexdigest()

def validate_input(data: Dict[str, Any], required_fields: list) -> bool:
    return all(field in data for field in required_fields)

def load_config(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_config(file_path: str, config: Dict[str, Any]) -> bool:
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
        return True
    except Exception:
        return False

def log_transaction(transaction_id: str, details: Dict[str, Any], log_file: str = 'transaction_logs.txt') -> bool:
    try:
        with open(log_file, 'a') as file:
            log_entry = json.dumps({"transaction_id": transaction_id, "details": details, "timestamp": datetime.utcnow().isoformat()})
            file.write(log_entry + '\n')
        return True
    except Exception:
        return False