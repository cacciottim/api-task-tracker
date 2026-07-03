<p align="right">
  <a href="README.md">🇬🇧 English</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="LICENSE">License</a>
</p>

```
              .__            __                 __               __                        __
_____  ______ |__|         _/  |______    _____|  | __         _/  |_____________    ____ |  | __ ___________
\__  \ \____ \|  |  ______ \   __\__  \  /  ___/  |/ /  ______ \   __\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \
 / __ \|  |_> >  | /_____/  |  |  / __ \_\___ \|    <  /_____/  |  |  |  | \// __ \\  \___|    <\  ___/|  | \/
(____  /   __/|__|          |__| (____  /____  >__|_ \          |__|  |__|  (____  /\___  >__|_ \\___  >__|
     \/|__|                           \/     \/     \/                           \/     \/     \/    \/
```

# api-task-tracker

Una semplice API REST per tenere traccia delle attività giornaliere, realizzata con **FastAPI** e **pandas**. Le task vengono salvate in un file CSV e possono essere create, elencate (per il giorno corrente) e contrassegnate come completate tramite semplici endpoint HTTP.

Il progetto è stato realizzato come esercizio per esercitarmi nella progettazione di API REST, nella validazione delle richieste e nella persistenza dei dati in Python.

## Funzionalità

- Creazione di task con nome, descrizione e data di scadenza (giorno/mese, con anno opzionale)
- Recupero delle task in scadenza **oggi**
- Contrassegnare una task come completata (viene rimossa dal tracker)
- Validazione delle richieste con Pydantic (lunghezza dei campi, range delle date, ecc.)
- Documentazione API interattiva automatica tramite Swagger UI (`/docs`)
- Storage basato su CSV — nessun database da configurare

## Stack Tecnologico

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.139.0-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.13.4-E92063?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.49.0-2A308B?style=flat)](https://www.uvicorn.org/)
[![pandas](https://img.shields.io/badge/pandas-3.0.3-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Storage](https://img.shields.io/badge/Storage-CSV-lightgrey?style=flat)](data/Tasks.csv)

## Screenshot

<details>
<summary>Clicca per espandere</summary>

**Avvio del server**
![Avvio del server](assets/screenshot_1.png)

**Documentazione interattiva (Swagger UI) — endpoint disponibili**
![Panoramica Swagger UI](assets/screenshot_2.png)

**Aggiunta di una task — richiesta `POST /tasks`**
![Richiesta aggiunta task](assets/screenshot_3.png)

**Aggiunta di una task — risposta**
![Risposta aggiunta task](assets/screenshot_4.png)

**Elenco delle task odierne — `GET /todo`**
![Task odierne](assets/screenshot_5.png)

**Completamento di una task — richiesta `POST /done`**
![Richiesta eliminazione task](assets/screenshot_6.png)

**Completamento di una task — risposta**
![Risposta eliminazione task](assets/screenshot_7.png)

</details>

## Per Iniziare

### Prerequisiti

- Python 3.11+ (sviluppato e testato con Python 3.14)
- pip

### Clonare la repository

```bash
git clone https://github.com/cacciottim/api-task-tracker.git
cd api-task-tracker
```

### Creare un ambiente virtuale

```bash
python -m venv .venv
```

Attivarlo:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### Installare le dipendenze

```bash
pip install -r requirements.txt
```

### Avviare l'applicazione

```bash
python src/main.py
```

Il server si avvia su `http://127.0.0.1:8000`. La documentazione interattiva è disponibile su `http://127.0.0.1:8000/docs`.

## Utilizzo delle API

| Metodo | Endpoint | Descrizione                                |
|--------|----------|----------------------------------------------|
| GET    | `/`      | Route di health-check / benvenuto             |
| GET    | `/todo`  | Restituisce le task in scadenza oggi          |
| POST   | `/tasks` | Aggiunge una nuova task                       |
| POST   | `/done`  | Contrassegna una task come completata (la elimina) |

### Aggiungere una task

```bash
curl -X POST 'http://127.0.0.1:8000/tasks' \
  -H 'Content-Type: application/json' \
  -d '{
    "day": 3,
    "month": 7,
    "name": "Project",
    "year": 2026,
    "description": "Remember to complete the project!"
  }'
```

`year` è opzionale (di default viene usato l'anno corrente) e `description` è opzionale. `day`, `month` e `name` sono obbligatori.

### Elencare le task odierne

```bash
curl 'http://127.0.0.1:8000/todo'
```

### Contrassegnare una task come completata

```bash
curl -X POST 'http://127.0.0.1:8000/done?task_id=1'
```

## Struttura del Progetto

```
api-task-tracker/
├── assets/          # Screenshot usati in questo README
├── data/            # Storage CSV (Tasks.csv)
├── src/
│   ├── main.py      # Entry point — avvia l'applicazione
│   ├── utils.py     # Factory dell'app, route e logica applicativa
│   └── schemas.py   # Modelli Pydantic per la validazione delle richieste
└── requirements.txt # Dipendenze del progetto
```

## Contribuire

Contributi, segnalazioni e suggerimenti sono benvenuti — consulta [CONTRIBUTING.md](CONTRIBUTING.md) per le linee guida.

## Licenza

Questo progetto è distribuito con licenza MIT — vedi [LICENSE](LICENSE) per i dettagli.

## Ringraziamenti

Alcune parti di questo progetto sono state revisionate e debuggate con l'aiuto di [Claude](https://claude.com/) (Anthropic).
