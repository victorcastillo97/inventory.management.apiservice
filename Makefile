.DEFAULT_GOAL := help

TYPE_APP 		= service-management
SERVICE_NAME 	= inventory
ENV 			= dev

PROJECT_NAME 	= ${TYPE_APP}-${SERVICE_NAME}-${ENV}

#Params ECR
NAME_PROJECT_APP = app-${PROJECT_NAME}
PORT_APP = 8000

build.image: ## Build image for application.: make build.image
	@ docker build  \
		-f docker/Dockerfile \
		-t ${NAME_PROJECT_APP}:latest \
		./app \
		--no-cache

run.app: ## Run image for application.: make run.app
	@docker run \
		-p 8000:${PORT_APP} -d ${NAME_PROJECT_APP}:latest\
