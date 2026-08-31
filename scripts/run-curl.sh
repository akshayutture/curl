#!/bin/sh
# Copyright (C) Daniel Stenberg, <daniel@haxx.se>, et al.
# SPDX-License-Identifier: curl

# Usage: run-curl.sh [URL [METHOD [ACCEPT]]] [curl options...]
# CURL_URL, CURL_METHOD, CURL_ACCEPT, and CURL_BIN can override the defaults.
set -eu

URL="${1:-${CURL_URL:-https://example.com}}"
METHOD="${2:-${CURL_METHOD:-GET}}"
ACCEPT="${3:-${CURL_ACCEPT:-application/json}}"
CURL_BIN="${CURL_BIN:-curl}"

if test "$#" -gt 0; then shift; fi
if test "$#" -gt 0; then shift; fi
if test "$#" -gt 0; then shift; fi

exec "$CURL_BIN" \
  --request "$METHOD" \
  --header "Accept: $ACCEPT" \
  "$@" \
  "$URL"
