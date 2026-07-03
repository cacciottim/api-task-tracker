import pandas as pd
from datetime import datetime as dt
from fastapi import FastAPI, HTTPException
import schemas
import uvicorn

FILE_PATH = 'data/Tasks.csv'

def data_prep() -> pd.DataFrame:
    try:
        df = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        raise RuntimeError("File not found.")
    except Exception as e:
        raise RuntimeError("Unknown error has occurred.") from e

    df = df.set_index('ID')

    df = df.drop_duplicates(['Date', 'Name'])

    df = df.fillna(value='null') # Fill empty cells with 'null' (Description can be missing)

    return df

def get_today_tasks(df: pd.DataFrame) -> dict:
    df2 = df.reset_index()
    
    year = dt.now().year
    month = dt.now().month
    day = dt.now().day
    
    date = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2) # Convert date to string ('Date' has a str dtype)
    tasks = df2.query('Date == @date')
    
    tasks_records = tasks.to_dict('records')
    tasks_data = {"tasks": tasks_records}

    return tasks_data

def create_app() -> FastAPI:
    app = FastAPI()

    root_text = {
        "Text": (
            "API Task Tracker: a simple web app for managing a list of tasks stored in a CSV file. "
            "Available endpoints: "
            "GET /todo to retrieve today's tasks; "
            "POST /tasks to add a new task, sending a JSON body with the fields 'day', 'month', 'name' (required) and 'year', 'description' (optional); "
            "POST /done?task_id=<id> to mark the task with the given id as done (deleting it), passed as a query parameter."
        )
    }

    df = data_prep()

    @app.get("/")
    def root() -> dict:
        return root_text

    @app.get("/todo")
    def show_tasks():
        tasks_data = get_today_tasks(df)

        return tasks_data

    @app.post("/tasks")
    def add_task(new_task: schemas.Task):
        if not df.empty:
            id_task = df.index.max() + 1
        else:
            id_task = 0
        
        if new_task.year == None:
            year = dt.now().year
            date = str(year) + '-' + str(new_task.month).zfill(2) + '-' + str(new_task.day).zfill(2)
            df.loc[id_task] = [date, new_task.name, new_task.description]
            df.to_csv(FILE_PATH)
            msg = {"added_task": new_task}

            return msg
        elif new_task.year is not None:
            if new_task.year < 100:
                new_task.year = 2000 + new_task.year
            
            date = str(new_task.year) + '-' + str(new_task.month).zfill(2) + '-' + str(new_task.day).zfill(2)
            df.loc[id_task] = [date, new_task.name, new_task.description]
            df.to_csv(FILE_PATH)
            msg = {"added_task": new_task}

            return msg
        else:
            raise HTTPException(status_code=400, detail='Bad reequest.')
        
    @app.post("/done")
    def delete_task(task_id: int):
        try:
            if not df.empty:
                df.drop(task_id, inplace=True)
                msg = {"Text": f"Task with id {task_id} eliminated."}
                df.to_csv(FILE_PATH)

                return msg
            else:
                msg = {"Text": "There are no tasks to be eliminated."}

                return msg
        except KeyError:
            raise HTTPException(status_code=404, detail="Resource not found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error.") from e
    
    return app

def run_app() -> None:
    try:
        uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
    except AttributeError:
        raise RuntimeError("Attribute not found.")
    except Exception as e:
        raise RuntimeError("Unknown error has occurred") from e
