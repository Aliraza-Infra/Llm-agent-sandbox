# LLM Agent Sandbox

This project simulates a sandbox environment for testing prompt-based LLM agents.  
It accepts YAML-defined tasks via a FastAPI endpoint and logs simulated responses for further evaluation.

## Features
- FastAPI server to receive and process YAML tasks
- Simulated agent response logging
- YAML task templates
- CI integration with GitHub Actions

## Usage

```bash
uvicorn main:app --reload
