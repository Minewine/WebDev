import json
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

with open("config.json") as f:
    config = json.load(f)

env = Environment(loader=FileSystemLoader("template"))
template = env.get_template("index.html")

output = template.render(**config)
Path("dist").mkdir(exist_ok=True)
with open("dist/index.html", "w") as f:
    f.write(output)

print("Website built! Check dist/index.html")