"""
Configuration management for the hyperparameter optimization engine.
Centralized config with validation and type safety.
"""
import os
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from enum import Enum
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OptimizationMethod(Enum):
    """Supported optimization algorithms"""
    BAYESIAN = "bayesian"
    GENETIC = "genetic"
    GRID = "grid"
    RANDOM = "random"

class RiskLevel(Enum):
    """Risk profiles for optimization"""
    CONSERVATIVE = "conservative"
    MODERATE = "moderate"
    AGGRESSIVE = "aggressive"

@dataclass
class FirebaseConfig:
    """Firebase configuration with validation"""
    project_id: str = field(default_factory=lambda: os.getenv('FIREBASE_PROJECT_ID', ''))
    private_key_id: str = field(default_factory=lambda: os.getenv('FIREBASE_PRIVATE_KEY_ID', ''))
    private_key: str = field(default_factory=lambda: os.getenv('FIREBASE_PRIVATE_KEY', '').replace('\\n', '\n'))
    client_email: str = field(default_factory=lambda: os.getenv('FIREBASE_CLIENT_EMAIL', ''))
    client_id: str = field(default_factory=lambda: os.getenv('FIREBASE_CLIENT_ID', ''))
    client_x509_cert_url: str = field(default_factory=lambda: os.getenv('FIREBASE_CLIENT_X509_CERT_URL', ''))
    
    def validate(self) -> bool:
        """Validate Firebase configuration"""
        required_fields = ['project_id', 'private_key', 'client_email']
        for field_name in required_fields