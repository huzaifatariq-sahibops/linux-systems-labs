# Day 1 — Linux and Client-Server Foundations

## Objective

Practise basic Linux navigation and demonstrate a client-server exchange on the local machine.

## Part 1 — Inspect the Linux environment

```bash
whoami
pwd
uname -srm
cat /etc/os-release
```

These commands identify the current user and directory, show the Linux kernel and processor architecture, and display the operating-system release information.

## Part 2 — Create and inspect a file

```bash
mkdir -p ~/linux-systems-labs/day-01-foundations/demo
cd ~/linux-systems-labs/day-01-foundations/demo
touch file.txt
printf 'Hello from Huzaifa Day 1 Linux lab\n' > file.txt
ls -la
cat file.txt
```

`mkdir -p` creates the required directory path. `touch` creates the file, `printf` writes its contents, `ls -la` displays it with permissions and metadata, and `cat` prints the contents.

## Part 3 — Parent versus previous directory

- `cd ..` moves one level upward to the parent directory.
- `cd -` switches to the previous working directory stored by the shell.

These may produce the same destination in a simple example, but they mean different things.

## Part 4 — Run a local HTTP server

From the `demo` directory:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

This Python process acted as the **server** because it listened on port `8000`, received requests, and returned files. Binding to `127.0.0.1` restricted access to programs on the same machine.

From a second terminal:

```bash
curl -i http://127.0.0.1:8000/file.txt
```

`curl` acted as the **client** because it initiated the request and displayed the response.

## Request and response flow

```text
curl client
    |
    | GET /file.txt
    v
Python HTTP server on 127.0.0.1:8000
    |
    | 200 OK + file contents
    v
curl displays the response
```

`200 OK` means the server successfully handled the request and returned the requested resource.

## Verified result

- The server recorded `GET /file.txt`.
- The response status was `HTTP/1.0 200 OK`.
- The returned body matched the expected text.
- The response reported a content length of 35 bytes.

See the [sanitized terminal evidence](evidence/terminal-output.txt).

## Troubleshooting notes

- The server must remain running while `curl` sends its request.
- Both commands must use the same port number.
- Run the server from the directory containing the file to be served.
- A `404 File not found` response means the server was reached but the requested path was unavailable.
- Stop the temporary server with `Ctrl+C` after testing.

## What I learned

A server is defined by what it does, not by special hardware. In this lab, an ordinary Python process became a server by listening for requests and returning a resource. `curl` was the client because it started the communication.
