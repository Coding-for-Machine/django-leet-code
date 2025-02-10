import docker

cliend = docker.from_env()

for i in cliend.containers.list():
    print(f"id:{i.id}--name: {i.name}--status: {i.status}")

for i in cliend.containers.list(all=True):
    print(f"id:{i.id}--name: {i.name}--status: {i.status}")

# contaner runs code
run_python = cliend.containers.run("python-app",
                      command="docker run python-app",
                      detach=True,
                      stderr=True,
                      stdout=True,
                      stdin_open=True
                      )



