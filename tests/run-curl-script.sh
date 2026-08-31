#!/bin/sh
# Copyright (C) Daniel Stenberg, <daniel@haxx.se>, et al.
# SPDX-License-Identifier: curl

set -eu

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RUN_CURL="$SCRIPT_DIR/../scripts/run-curl.sh"
TEMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TEMP_DIR"' EXIT

cat > "$TEMP_DIR/curl" <<'FAKE_CURL'
#!/bin/sh
printf '%s\n' "$@" > "$OUTPUT"
FAKE_CURL
chmod +x "$TEMP_DIR/curl"

OUTPUT="$TEMP_DIR/default.actual" CURL_BIN="$TEMP_DIR/curl" "$RUN_CURL"
printf '%s\n' --request GET --header 'Accept: application/json' \
  https://example.com > "$TEMP_DIR/default.expected"
cmp "$TEMP_DIR/default.expected" "$TEMP_DIR/default.actual"

OUTPUT="$TEMP_DIR/custom.actual" CURL_BIN="$TEMP_DIR/curl" \
  "$RUN_CURL" https://api.example.test POST text/plain --fail
printf '%s\n' --request POST --header 'Accept: text/plain' --fail \
  https://api.example.test > "$TEMP_DIR/custom.expected"
cmp "$TEMP_DIR/custom.expected" "$TEMP_DIR/custom.actual"

OUTPUT="$TEMP_DIR/environment.actual" CURL_BIN="$TEMP_DIR/curl" \
  CURL_URL=https://env.example.test CURL_METHOD=HEAD CURL_ACCEPT='text/*' \
  "$RUN_CURL"
printf '%s\n' --request HEAD --header 'Accept: text/*' \
  https://env.example.test > "$TEMP_DIR/environment.expected"
cmp "$TEMP_DIR/environment.expected" "$TEMP_DIR/environment.actual"
