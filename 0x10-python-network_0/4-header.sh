#!/bin/bash
# Get result and display output
user_id_header="X-School-User-Id: 98"
curl -X GET -H "$user_id_header" "$1"
