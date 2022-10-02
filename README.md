# Custom OpenFaaS Templates

This repository contains templates for [OpenFaaS](https://openfaas.com).

```
$ faas-cli template pull https://github.com/codref/faas-templates.git
$ faas-cli new --list

Languages available as templates:
- python3.10-microservice
```

## python3.x-microservice

The template _python3-microservice_ is equivalent to [`python3`](https://github.com/openfaas/python-flask-template) with the exception that it supports a *microservice* architecture, rather than a pure Function As A Service one (more freedom in defining the functions).


### Using the templates

```
$ faas-cli template pull https://github.com/codref/faas-templates.git
$ faas-cli new --lang <template> <fn-name>
```

The above commands will create a folder with the name of your function and a set of files containing the templates


```
# The command
faas-cli build -f stacks.yml
```
