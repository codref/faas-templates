export version=$(shell cat ./VERSION)
export registry=gitlab.evouser.com:5005

# START CHANGE HERE
export fname=my-function-name # function name
export image=portal/faas/$(fname)-faas # without leading /
# STOP CHANGE HERE

export secret=vault-faas-env # vault secret name

build_dev:
	faas build -f $(fname).yml

up_staging:
	TOKEN_VALIDATION_URL=staging-api.evouser.com faas up -f $(fname).yml 

up_prod:
	TOKEN_VALIDATION_URL=api.evouser.com faas up -f $(fname).yml 

serve:
	docker run --rm -it \
		--env-file $(shell pwd)/.env \
		-v $(shell pwd)/$(fname)/:/home/app/function/ \
		-v $(shell pwd)/.env:/var/openfaas/secrets/$(secret) \
		-p 8081:8080 $(registry)/$(image):latest sh -c 'fwatchdog'

shell:
	docker run --rm -it \
		--env-file $(shell pwd)/.env \
		-v $(shell pwd)/$(fname)/:/home/app/function/ \
		-v $(shell pwd)/.env:/var/openfaas/secrets/$(secret) \
		-p 8081:8080 $(registry)/$(image):latest sh
				