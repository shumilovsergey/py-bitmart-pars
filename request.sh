#!/bin/bash

url="https://www.bitmart.com/nft/en-US/collectible?collectibleId=203"  # replace with your URL

# Set browser-like headers
headers=(
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
  "Accept-Language: en-US,en;q=0.5"
  "Connection: keep-alive"
)

# Join headers into a single string
headers_string=$(printf "%s" "-H '$header' " "${headers[@]}")

# Send GET request and echo response code
response_code=$(curl -s -o /dev/null $url -H "${headers[@]}")

response_body=$(echo "$response" | sed -n '/^$/,$p' | tail -n +2)


echo "Response Code: $response_code"

echo "Response Body:"
echo "$response_body"