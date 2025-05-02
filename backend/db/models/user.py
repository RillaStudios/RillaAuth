import json
import os
from datetime import datetime
from typing import Type, Dict
from pydantic import create_model
from sqlmodel import SQLModel, Field

# Define default required fields
# Core fields that cannot be removed
CORE_USER_FIELDS = {
    "user_id": (int, Field(default=None, primary_key=True)),
    "date_created": (str, Field(default_factory=lambda: datetime.now().isoformat()))
}

# Load custom fields from configuration
def load_custom_fields() -> Dict[str, tuple]:
    config_path = os.environ.get("USER_MODEL_CONFIG", "config/user_fields.json")
    custom_fields = {}

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                config = json.load(f)

            for field_name, field_config in config.items():
                field_type = eval(field_config.get("type", "str"))
                field_args = field_config.get("args", {})

                if field_args:
                    field_args = Field(**field_args)
                else:
                    field_args = ...

                custom_fields[field_name] = (field_type, field_args)

        except Exception as e:
            print(f"Error loading user field configuration: {e}")

    return custom_fields


# Create the User class dynamically
def create_user_model() -> Type[SQLModel]:
    # Load custom fields
    custom_fields = load_custom_fields()

    # Define the base model with core fields including primary key
    class UserBase(SQLModel, table=True):
        __tablename__ = "users"

        # Include core fields directly in the base class
        id: int = Field(default=None, primary_key=True)
        date_created: str = Field(default_factory=lambda: datetime.now().isoformat())

    # Create extended model with only custom fields
    user_model = create_model(
        "User",
        __base__=UserBase,
        **custom_fields,
        __module__="db.models.user"
    )

    # Add __repr__ method
    def __repr__(self) -> str:
        return f"User(id={self.id}, username={getattr(self, 'username', 'N/A')}, email={getattr(self, 'email', 'N/A')})"

    user_model.__repr__ = __repr__

    return user_model


# Create the User model
User = create_user_model()