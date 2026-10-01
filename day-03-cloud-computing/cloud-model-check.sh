#!/usr/bin/env bash

model="${1:-}"

case "${model,,}" in
  on-prem)
    echo "Customer manages: hardware, networking, OS, runtime, applications, and data"
    ;;
  iaas)
    echo "Provider manages: hardware, networking, and virtualization"
    echo "Customer manages: OS, runtime, applications, and data"
    ;;
  paas)
    echo "Provider manages: infrastructure, OS, and runtime"
    echo "Customer manages: applications and data"
    ;;
  saas)
    echo "Provider manages: the complete application platform"
    echo "Customer manages: users, access, configuration, and data"
    ;;
  *)
    echo "Usage: $0 {on-prem|iaas|paas|saas}" >&2
    exit 2
    ;;
esac
