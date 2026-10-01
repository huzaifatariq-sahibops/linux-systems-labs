# Day 4 — Software Application

## Objective

Connect a browser-facing frontend, a Python backend, and persistent database storage in one small local application.

## Learning-source scope

The concept diagnostic for this milestone was grounded in the official Miseacademy Day 4 portal questions for **Software, Apps, and Infrastructure**. The trainer video was blocked by YouTube's automated bot check, and the presentation required an authorized Google session. This page therefore does not claim full coverage of the trainer's video or slides.

## Application flow

```text
Browser requests /
  -> Python backend returns index.html
  -> frontend requests /api/visits
  -> backend updates SQLite app.db
  -> backend returns JSON
  -> frontend displays the visit count
```

The three application layers are:

- **Frontend — `index.html`:** the interface displayed by the browser. Its JavaScript requests the visit count.
- **Backend — `app.py`:** the local HTTP server, route handling, and application logic.
- **Database — generated `app.db`:** the SQLite file that stores the `counter` table and visit value on disk.

`app.db` is generated when the application starts and is excluded from Git because it is runtime data, not source code.

## Run the application

From this directory:

```bash
python3 app.py
```

Open <http://127.0.0.1:8004> in a browser. The service binds to the loopback address, so it is intended for access from the same machine.

## Verify the behavior

In another terminal:

```bash
curl -i http://127.0.0.1:8004/
curl -s http://127.0.0.1:8004/api/visits
curl -s http://127.0.0.1:8004/api/visits
python3 -c 'import sqlite3; print(sqlite3.connect("app.db").execute("SELECT visits FROM counter WHERE id = 1").fetchone()[0])'
curl -i http://127.0.0.1:8004/missing
```

## Verified result

- `/` returned the HTML frontend with `200 OK`.
- `/api/visits` updated the SQLite record and returned the count as JavaScript Object Notation (JSON).
- Two API requests returned visit counts `1` and `2`; querying SQLite directly confirmed `2`.
- After stopping and restarting Python, the API later returned `4`. The process ended, but the value survived in the on-disk `app.db` file. This is **persistence**.
- `/missing` returned `404 Not Found`: the server was reachable, but no route matched that path.
- A connection failure would be different—it means the client could not reach a listening server and therefore received no HTTP response.

See the [sanitized terminal evidence](evidence/terminal-output.txt).

## Troubleshooting

The first frontend response began with an unintended standalone `html` line copied from a Markdown code-block label. Inspecting the response with `curl` exposed it. After deleting that line, the document correctly began with `<!doctype html>`.

A browser also requested `/favicon.ico`, which returned `404` because this learning application does not include an icon route. That did not affect the application.

## Scope and limitations

This is a local learning application, not a production web service. It has no authentication, encrypted transport, concurrency design, deployment configuration, input validation, or production security hardening. Its purpose is to demonstrate the frontend-backend-database request path and persistent storage.

## AI assistance disclosure

I created, ran, tested, and corrected the guided application in my Ubuntu/WSL environment and supplied the terminal output. SAHIB, my AI learning assistant, provided the exercise and starter code, checked my understanding through MCQs, identified the copied-line defect, helped sanitize the evidence, and structured this documentation.
