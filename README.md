# StackState Agent Integrations

This repository contains the Agent Integrations (also known as checks) that StackState
officially develops and supports. The [StackState Agent][1] packages are equipped with all the Integrations from this
repository.

# Development

## CI image
The CI image is built from .gitlab-scripts/image.

## Local setup

To work on packages in this directory you can run the following:

- source .gitlab-scripts/setup_env.sh

From this point on the stsdev script is in scope and commands can be ran.

If changes are made to the stsdev, you can use .gitlab-scripts/load_deps.sh

[1]: https://github.com/StackVista/stackstate-agent
