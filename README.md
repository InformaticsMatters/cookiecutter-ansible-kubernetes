# cookiecutter-ansible-kubernetes
A [cookiecutter] template repository to create our style of AWX-compliant
repositories - repositories that contain a playbook (and a role) to deploy a
Kubernetes application.

Use this cookiecutter to quickly template new Kubernetes application projects
that you expect to deploy through AWX. The cookiecutter produces an Ansible
playbook and role with some preset variables defined in `defaults` and `vars`
with `tasks` to deploy the application and all its components from Ansible
`templates`.
        
Answer the cookiecutter questions to create pre-formatted templates
for the deployment of a container image application that can be a **CronJob**,
**Deployment**, **Job** or **StatefulSet**. You can also decide whether you
want a **PVC** (attached to the application) and an example **Secret** and
**ConfigMap** to get you started.

If it's a simple application it should be ready to add as a **Project** in AWX
and run once you commit the new project to Git.

Additionally, the generated project contains a `.travis.yml`
to perform lint and ansible checking of the project.

## Creating projects with the cookiecutter

???

---

[cookiecutter]: https://cookiecutter.readthedocs.io
