# ── Config ─────────────────────────────────────────────────────────────────
PROJECT_ID  ?= $(shell grep GCP_PROJECT .env 2>/dev/null | cut -d= -f2)
REGION      ?= us-west2
SERVICE     ?= huehunt
REPO        ?= huehunt
IMAGE       := $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(REPO)/$(SERVICE)
PORT        ?= 8080

# Load .env vars (used by deploy targets)
ifneq (,$(wildcard .env))
  include .env
  export
endif

# Always use absolute path for creds so it works regardless of working dir
export GOOGLE_APPLICATION_CREDENTIALS := $(CURDIR)/db-creds.json

.PHONY: help install run build run-docker push deploy logs

help:
	@echo ""
	@echo "  Local dev"
	@echo "    make install          Install Python dependencies"
	@echo "    make run              Run Flask dev server (uses .env)"
	@echo ""
	@echo "  Container"
	@echo "    make build            Build Docker image"
	@echo "    make run-docker       Run container locally (uses .env)"
	@echo ""
	@echo "  Cloud Run"
	@echo "    make push             Push image to Artifact Registry"
	@echo "    make deploy           Build, push, and deploy to Cloud Run"
	@echo "    make logs             Tail Cloud Run logs"
	@echo ""

# ── Local dev ───────────────────────────────────────────────────────────────
install:
	pip install -r requirements.txt

run:
	cd src && flask --app app run --debug --port $(PORT)
