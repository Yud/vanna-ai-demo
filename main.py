from vanna.chromadb import ChromaDB_VectorStore
from vanna.google import GoogleGeminiChat

from vanna_demo.config import my_config

class MyVanna(ChromaDB_VectorStore, GoogleGeminiChat):
    def __init__(self, chroma_config=None):
        ChromaDB_VectorStore.__init__(self, config=chroma_config)
        GoogleGeminiChat.__init__(self, config={'api_key': my_config.gemini_api_key, 'model': my_config.gemini_api_key})

vn = MyVanna()
vn.connect_to_postgres(
    host=my_config.db_host,
    dbname=my_config.db_name,
    user=my_config.db_user,
    password=my_config.db_pass,
    port=my_config.db_port,
)

# The information schema query may need some tweaking depending on your database. This is a good starting point.
df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

# The following are methods for adding training data. Make sure you modify the examples to match your database.

# DDL statements are powerful because they specify table names, colume names, types, and potentially relationships
# vn.train(ddl="""
#     CREATE TABLE IF NOT EXISTS my-table (
#         id INT PRIMARY KEY,
#         name VARCHAR(100),
#         age INT
#     )
# """)

# Sometimes you may want to add documentation about your business terminology or definitions.
# vn.train(documentation="Our business defines OTIF score as the percentage of orders that are delivered on time and in full")

# You can also add SQL queries to your training data. This is useful if you have some queries already laying around. You can just copy and paste those from your editor to begin generating new SQL.
# vn.train(sql="SELECT * FROM my-table WHERE name = 'John Doe'")

# At any time you can inspect what training data the package is able to reference
# training_data = vn.get_training_data()
# training_data

# You can remove training data if there's obsolete/incorrect information. 
# vn.remove_training_data(id='1-ddl')


# This will break up the information schema into bite-sized chunks that can be referenced by the LLM
plan = vn.get_training_plan_generic(df_information_schema)
plan

# If you like the plan, then uncomment this and run it to train
# vn.train(plan=plan)

# Whenever you ask a new question, it will find the 10 most relevant pieces of training data and use it as part of the LLM prompt to generate the SQL.
vn.ask(question="delete every customer with first name Tom")
