from typing import Union, List
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pandas as pd
from dateutil import parser
from typing import List
import pyarrow.parquet as pq
import numpy as np  # Agregamos la importación de numpy
import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

# Creacion de una aplicacion FastApi

app = FastAPI()