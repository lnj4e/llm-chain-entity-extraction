## Cursor Cloud specific instructions

### Project overview

Python CLI tool that uses LLM chains to extract clinical/medical entities from free-text clinical notes and map them to SNOMED CT codes. No build step, no frontend, no database — single-process CLI.

### Dependencies

`pip install -r requirements.txt` — installs `python-dotenv`, `bardapi`, `openai`, `requests`.

**httpx version conflict**: `bardapi` pulls in `httpx>=0.28` which breaks `openai==1.25.2` (removed `proxies` kwarg). After installing requirements, downgrade httpx: `pip install 'httpx>=0.23.0,<0.28.0'`.

### Running the tool

```
python3 entity_extractor.py --api openai --model gpt-4o --sentences=example_cases/clinical_text.txt
```

Requires an `openai.key` file in the project root containing a valid OpenAI API key. The tool reads this file and sets `OPENAI_API_KEY` at startup.

### Important caveats

- **FHIR server**: The hardcoded Snowstorm Lite server (`snowstorm-lite.nw.r.appspot.com/fhir`) is **down as of May 2026**. An alternative that works is `https://tx.fhir.org/r4`, but it does not support Snowstorm's fuzzy match (`~` suffix on filter terms). To use the alternative, change `server_url` in `entity_extractor.py`.
- **No automated tests**: There is no test suite or linter configured. `timing_accuracy_test.py` is a manual timing comparison script, not an automated test. `test-request.py` tests FHIR connectivity.
- **No lint/format config**: No `.flake8`, `pyproject.toml`, `ruff.toml`, or similar. Run `python3 -m py_compile <file>.py` for basic syntax checks.
- **LLM backends**: The default/recommended backend is OpenAI (`--api openai`). The LLaMA backend requires `llama-cpp-python` (not in `requirements.txt`) plus a local model file. The Bard backend is deprecated.
- **Module-level side effects**: `completion_openai.py` instantiates the OpenAI client at import time, so importing it without `OPENAI_API_KEY` set raises an error.
