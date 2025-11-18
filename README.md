# Rexus Agent Mesh

This project brings together the full AI modality stack — reasoning (LLMs), tool-based planning, OCR, object detection, speech recognition, and GPU-driven TTS — into a single coordinated agent mesh. Each subsystem acts as a sensor or actuator: the brain (LLM), eyes (OCR/vision models), ears (Whisper), and voice (Orpheus TTS).
A Python-based orchestration layer maintains shared state, manages multi-step workflows, and enables tool-use reasoning across services.
All agents and pipelines are custom-built, modular, and container-ready, designed to provide accessibility automation and real-time assistance for complex digital tasks. This work demonstrates systems-level design, cross-model integration, and practical agentic automation driven entirely by Python.


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
