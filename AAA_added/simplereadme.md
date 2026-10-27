Run this command from repo folder to run with GPU acceleration:
```
docker run --rm --gpus all \
  -v "$PWD/AAA_added/input:/audio:ro" \
  -v "$PWD/AAA_added/output:/output" \
  -v "$PWD/AAA_added/models:/models" \
  local-transcriber
```
- Tweak `transcriber.py` to suit your needs and choose the best model based on your workflow.