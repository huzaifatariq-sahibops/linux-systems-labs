# Day 2 — Networking Foundations

## Objective

Connect basic networking concepts to observable Linux commands: name resolution, interfaces, routes, ports, loopback access, HTTP, HTTPS, and the Secure Shell (SSH) client.

## Learning-source scope

The concept check for this milestone was grounded in the official Day 2 portal questions and verified with this lab. The separate video transcript and presentation were not accessible during review, so this page does not claim to reproduce their specific wording or complete coverage.

## Part 1 — Create the test resource

```bash
mkdir -p ~/linux-systems-labs/day-02-networking
cd ~/linux-systems-labs/day-02-networking
printf 'Day 2 networking lab\n' > index.html
```

The Python server later served this file as the default page.

## Part 2 — Inspect name resolution and networking

```bash
getent ahostsv4 example.com
ip -4 -brief address
ip route
ssh -V
```

- `getent ahostsv4` asked the system's configured name-resolution service for IPv4 addresses associated with the domain.
- `ip -4 -brief address` displayed the local IPv4 interfaces and addresses.
- `ip route` displayed the routing table, including the default route.
- `ssh -V` printed the installed OpenSSH **client** version. It did not prove that an SSH server was running or reachable.

## Part 3 — Run and inspect a local service

In the first terminal:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

In a second terminal:

```bash
curl -I http://127.0.0.1:8080/
ss -ltn 'sport = :8080'
curl -I https://example.com/
```

- Python listened on the loopback address `127.0.0.1` and port `8080`.
- `curl -I` requested response headers without downloading the response body.
- `ss` confirmed that a TCP socket was listening on local port `8080`.
- The final `curl` command tested an HTTPS response from a public website.

## How to read the results

### Domain Name System (DNS)

The returned IPv4 addresses showed that the domain name was resolved successfully.

**Memory line:** DNS changes a name into an IP address.

### Private address and default route

The WSL interface used a private IPv4 address. The route beginning with `default via` identified the fallback gateway and interface for destinations without a more specific matching route.

**Memory line:** Unknown destination? Send it through the default gateway.

### Loopback and ports

`127.0.0.1` is the loopback address, so the service was available only from the same machine. The IP address selected the machine or interface, while port `8080` selected the service.

**Memory line:** The IP finds the machine; the port finds the service.

### HTTP status

Both tested requests returned a `200` status, meaning each server successfully handled its request.

## Verified result

- A domain name resolved to IPv4 addresses.
- Local interfaces included loopback, WSL, and Docker networking.
- The routing table included a default gateway through the WSL Ethernet interface.
- The OpenSSH client was installed.
- Python listened on `127.0.0.1:8080`.
- The local HTTP request returned `HTTP/1.0 200 OK`.
- The public HTTPS request returned `HTTP/2 200`.

See the [sanitized terminal evidence](evidence/terminal-output.txt).

## Troubleshooting and privacy notes

- Start the Python server before running the local `curl` and `ss` commands.
- Use the same port number in the server, client, and socket-inspection commands.
- Stop the temporary server with `Ctrl+C` after testing.
- DNS results, private WSL addresses, gateways, and timestamps can change between runs.
- The public evidence generalizes the Windows hostname, private addresses, transient DNS results, timestamps, and unique Content Delivery Network request metadata.

## What I learned

DNS resolves names to addresses, routes decide where traffic should go, and ports direct traffic to the intended service. A version command proves that the SSH client is installed; it does not prove a successful remote connection or a running SSH server.
