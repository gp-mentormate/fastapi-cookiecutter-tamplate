#!/bin/sh

set -e

hypercorn src.main:app --bind 0.0.0.0:8000