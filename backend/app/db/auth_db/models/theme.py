from enum import Enum
from sqlmodel import SQLModel, Field


class Brightness(str, Enum):
    DARK = "dark"
    LIGHT = "light"


class Theme(SQLModel, table=True):
    """
    Theme model for storing UI theme configurations.
    This model stores color schemes and brightness settings that can be
    used by a Flutter frontend application.

    Attributes:
        id (int): Unique identifier for the theme.
        name (str): Name of the theme.
        brightness (str): Theme brightness (dark or light).

    @date 2025-05-01
    """

    __tablename__ = "themes"

    id: int = Field(default=None, primary_key=True)

    name: str = Field(default="Default Theme")
    description: str = Field(default="Default theme for the application.")

    brightness: str = Field(default=Brightness.DARK.value)

    # Primary colors
    primary: str = Field(default="1E2A38")  # New deep navy blue
    on_primary: str = Field(default="FFFFFF")  # White for contrast
    primary_container: str = Field(default="314150")  # Lighter shade of primary
    on_primary_container: str = Field(default="FFFFFF")  # White for readability

    # Secondary colors (Cool gray-blue)
    secondary: str = Field(default="607D8B")  # Blue gray
    on_secondary: str = Field(default="FFFFFF")
    secondary_container: str = Field(default="78909C")
    on_secondary_container: str = Field(default="FFFFFF")

    # Tertiary colors (Warm accent)
    tertiary: str = Field(default="FF7043")  # Deep orange
    on_tertiary: str = Field(default="000000")
    tertiary_container: str = Field(default="FFAB91")
    on_tertiary_container: str = Field(default="000000")

    # Fixed colors (Aligned to primary/secondary/tertiary)
    primary_fixed: str = Field(default="3A4A5A")  # Mid-tone blue-gray
    primary_fixed_dim: str = Field(default="2A3744")
    on_primary_fixed: str = Field(default="FFFFFF")
    on_primary_fixed_variant: str = Field(default="C5D1DB")

    secondary_fixed: str = Field(default="90A4AE")
    secondary_fixed_dim: str = Field(default="62757F")
    on_secondary_fixed: str = Field(default="000000")
    on_secondary_fixed_variant: str = Field(default="ECEFF1")

    tertiary_fixed: str = Field(default="FF8A65")
    tertiary_fixed_dim: str = Field(default="D84315")
    on_tertiary_fixed: str = Field(default="000000")
    on_tertiary_fixed_variant: str = Field(default="FFF3E0")

    # Surfaces and backgrounds
    surface: str = Field(default="121212")
    on_surface: str = Field(default="FFFFFF")
    surface_dim: str = Field(default="0D0D0D")
    surface_bright: str = Field(default="1F1F1F")
    surface_container_lowest: str = Field(default="0C0C0C")
    surface_container_low: str = Field(default="141414")
    surface_container: str = Field(default="1C1C1C")
    surface_container_high: str = Field(default="242424")
    surface_container_highest: str = Field(default="2C2C2C")

    # Error (retained as-is for now)
    error: str = Field(default="ED1C24")
    on_error: str = Field(default="FFFFFF")
    error_container: str = Field(default="660003")
    on_error_container: str = Field(default="FFD6D6")

    # Inverse
    inverse_surface: str = Field(default="E6E1E5")
    on_inverse_surface: str = Field(default="322F35")
    inverse_primary: str = Field(default="90A4AE")  # Match secondary for harmony

    # Other
    outline: str = Field(default="4D5C6B")  # Muted blue-gray
    outline_variant: str = Field(default="2C3A49")
    shadow: str = Field(default="000000")
    scrim: str = Field(default="000000")
    surface_tint: str = Field(default="1E2A38")  # Match primary