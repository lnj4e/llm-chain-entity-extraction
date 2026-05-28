# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This is a Python CLI tool that uses LLM chains to extract clinical entities from free-text clinical notes and map them to SNOMED CT codes via a FHIR Terminology Server. There is no web server, database, or build step.

### Running the application

```
python3 entity_extractor.py --api openai --model gpt-4o --sentences=example_cases/clinical_text.txt
```

Requires an `openai.key` file in the project root containing a valid OpenAI API key. The key file is gitignored (`*.key`).

### External dependencies

- **OpenAI API**: Required (default LLM backend). Needs `OPENAI_API_KEY` secret or `openai.key` file.
- **FHIR Terminology Server**: The hardcoded URL (`https://snowstorm-lite.nw.r.appspot.com/fhir`) in `entity_extractor.py` is **no longer available** (returns 404). A working alternative is `https://tx.fhir.org/r4` — change `server_url` in `entity_extractor.py` to use it. **Caveat**: `tx.fhir.org` does not support fuzzy matching (the `~` suffix that `fhir_api.py` appends). Fuzzy queries return zero results; exact-match queries work fine. To get fuzzy matching, you'd need a Snowstorm instance.

### Gotchas

- **httpx version**: `openai==1.25.2` is incompatible with `httpx>=0.28`. The update script pins `httpx<0.28`. If you see `TypeError: Client.__init__() got an unexpected keyword argument 'proxies'`, re-run the update script.
- The FHIR API module (`fhir_api.py`) uses `curl` as a subprocess rather than the `requests` library for HTTP calls. `curl` must be available on `PATH`.
- `entity_extractor.py` unconditionally reads `openai.key` from the project root at startup (line 26-28), even when using `--api llama`. This will crash with `FileNotFoundError` if the file doesn't exist. Create it with `echo "$OPENAI_API_KEY" > openai.key`.
- There is no formal test suite (no pytest). `test-request.py` is an accuracy harness that also requires OpenAI + FHIR. `timing_accuracy_test.py` compares `requests` vs `curl` latency against the FHIR endpoint.
- No linter is configured in the repo. You can run `python3 -m py_compile <file>.py` to check syntax.

### Dependencies

Installed via `pip install -r requirements.txt`. See README for details.
