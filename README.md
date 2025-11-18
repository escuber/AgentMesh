# Rexus Agent Mesh

This monorepo contains multiple AI microservices designed to work together:

- **tts-service**: Full GPU-based TTS orchestration
- **vision-service**: Screen/OCR processing (scaffold)
- **form-agent**: Form automation agent (scaffold)
- **job-agent**: Job description + resume processing agent (scaffold)

## Running the Mesh

Use docker-compose to start all services:

```bash
docker-compose up --build
```

Services will be available on the following ports:
- TTS Service: 8099
- Vision Service: 8101
- Form Agent: 8102
- Job Agent: 8103
