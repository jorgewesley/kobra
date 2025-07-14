from sqlmodel import SQLModel, Field

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None