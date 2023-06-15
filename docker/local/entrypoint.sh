#!/bin/sh

set -e

hypercorn src.main:app --reload --debug --bind 0.0.0.0:8000
