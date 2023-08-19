# A "cookiecutter" for Ansible Kubernetes projects

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/informaticsmatters/cookiecutter-ansible-kubernetes)

![GitHub](https://img.shields.io/github/license/informaticsmatters/cookiecutter-ansible-kubernetes)
[![Cut and lint](https://github.com/InformaticsMatters/cookiecutter-ansible-kubernetes/actions/workflows/test.yaml/badge.svg)](https://github.com/InformaticsMatters/cookiecutter-ansible-kubernetes/actions/workflows/test.yaml)
[![CodeFactor](https://www.codefactor.io/repository/github/informaticsmatters/cookiecutter-ansible-kubernetes/badge)](https://www.codefactor.io/repository/github/informaticsmatters/cookiecutter-ansible-kubernetes)

A [cookiecutter] template repository to create projects that contain an
[Ansible] **playbook** (and a **role**) using its **k8s** module
to to deploy container images as a Kubernetes application (**Pod**).

Use it to quickly create a playbook to deploy a container image as a: -

- **Job**
- **CronJob**
- **Deployment**
- **StatefulSet**
- **DaemonSet**

With optional additional template objects to help you create: -

- **Persistent Volume Claims**
- **Config Maps**
- **Secrets**
- **Services**
- **Ingresses**

Guided cookie-cutter questions enable you to create a pre-formatted project
to deploy a container image to Kubernetes. You can also decide whether you want to get
started with a **PVC** (attached to the application container), an **Ingress**,
and an example **Secret** and **ConfigMap**.

The cookie-cutter wraps this up with a playbook and an associated **Role** with
pre-formatted variables defined in `defaults` and `vars` along with a series of
`tasks` to flexibly deploy the application and all its components from the
kubernetes `templates` that it creates. This is finished-off
with root-level `requirements.txt`, `site.yaml`, `inventory.yaml` and
`ansible.cfg` files so you can deploy the application *out-of-the-box*.

The *cut* project is ready to deploy to a Kubernetes cluster from the command-line -
you don't even need to provide a container image, you can use the default
**PySimple** image if you just want to experiment with deploying a web-based application
to Kubernetes.

>   This version of the cookie-cutter only supports Kubernetes up to version 1.24 as
    it still deals with **PodSecurityPolicies**. It'll be updated when we move beyond
    1.24 in our active deployments. 

Additionally, the generated project contains a `.gitignore`, `workflows`,
`.yamllint` and `build-requirements.txt` to perform CI/CD lint and ansible
checking of the project using GitHub Actions (once you commit the project to GitHub).

## Creating an application

>   Importantly **YOU DO NOT NEED TO CLONE THIS REPOSITORY** to use the cookie-cutter.
    The cookie-cutter will clone and use the repository for you.

Consider creating a virtual environment and then run the cookie-cutter
from a directory where you want your kubernetes-based Ansible project to be created.

    python -m venv ~/.venv/cookiecutter-ansible-kubernetes
    source ~/.venv/cookiecutter-ansible-kubernetes/bin/activate
    pip install --upgrade pip

    pip install cookiecutter==2.*

    cd ~/Code
    cookiecutter gh:informaticsmatters/cookiecutter-ansible-kubernetes

The resultant project is created in the current directory, in a directory
named after your chosen **project_name**.

## Deploying the application
You'll probably want to adjust the application's role or templates before you
deploy it but, for the very simplest applications, you might be ready to go
straight away if you've used the **PySimple** image.

Move to the project directory and install the requirements: -

    cd <project_name>
    pip install -r requirements.txt

To run the produced playbook you will need a suitable `KUBECONFIG` environment variable
for your Kubernetes cluster, one that allows you to create namespaces and deploy all of
the objects: -

    export KUBECONFIG=~/k8s-config/config-local

>   You can also provide a kubernetes host and API key with `K8S_AUTH_HOST` and
    `K8S_AUTH_API_KEY` environment variables.

Then run the `site.yaml` playbook in the project's directory...

    ansible-playbook site.yaml

## Un-deploying the application
Run the site playbook, setting your application's `state` variable to
`absent`. Depending on what you used for the cookiecutter **var_prefix**
this might be: -

    ansible-playbook site.yaml -e cc_state=absent

---

[ansible]: https://github.com/ansible/ansible
[cookiecutter]: https://cookiecutter.readthedocs.io
