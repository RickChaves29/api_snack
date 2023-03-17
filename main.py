from fastapi import FastAPI, Path, HTTPException, Body
from pydantic import BaseModel

app = FastAPI()


class Snack():
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class SnackModel(BaseModel):
    id: int
    name: str


# def SnackCons(id: int, name: str):
#    id = id
#    name = name
#    return {"id": id, "name": name}

snacks = [Snack(1, "any 1"), Snack(2, "any 2"), Snack(3, "any 3")]


@app.get("/")
async def get_all():
    return snacks


@app.get("/{id}", status_code=200)
async def get_one(id: int = Path(title="id snack")):
    if id > len(snacks):
        raise HTTPException(status_code=404, detail="id not found")
    result: Snack
    for snack in snacks:
        if snack.id == id:
            result = Snack(snack.id, snack.name)
    return result


@app.post("/", status_code=201)
async def create(newSnack: SnackModel = Body()):
    snacks.append(Snack(newSnack.id, newSnack.name))
    return newSnack
