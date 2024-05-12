# Whenever you ask a new question, it will find the 10 most relevant pieces of training data and use it as part of the LLM prompt to generate the SQL.
# vn.ask(question="delete every customer with first name Tom")

from vanna.flask import VannaFlaskApp

from vanna_demo.train import train
from vanna_demo.my_vanna import vn

train()

app = VannaFlaskApp(vn)
app.run()