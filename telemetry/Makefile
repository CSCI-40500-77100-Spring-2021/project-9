REVISION := $(shell git rev-parse HEAD 2>/dev/null)
IMAGE := registry.digitalocean.com/cs405/telemetry

release:
	docker build -t $(IMAGE):$(REVISION) .
	docker push $(IMAGE):$(REVISION)
	docker build -t $(IMAGE):latest .
	docker push $(IMAGE):latest

.PHONY: release
