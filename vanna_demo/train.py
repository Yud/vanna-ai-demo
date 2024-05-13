# The information schema query may need some tweaking depending on your database. This is a good starting point.
# df_information_schema = vn.run_sql("SELECT * FROM INFORMATION_SCHEMA.COLUMNS")

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
# plan = vn.get_training_plan_generic(df_information_schema)
# plan

# If you like the plan, then uncomment this and run it to train
# vn.train(plan=plan)

from vanna_demo.my_vanna import vn
from vanna_demo.config import my_config

def get_ddl():
    ddl = None
    ddl_path = f"{my_config.root_dir}/db_data/schema.sql"

    with open(ddl_path, 'r') as file:
        ddl = file.read()

    return ddl

def get_documentation():
    return """
    There are 15 tables in the DVD Rental database:
    actor – stores actor data including first name and last name.
    film – stores film data such as title, release year, length, rating, etc.
    film_actor – stores the relationships between films and actors.
    category – stores film’s categories data.
    film_category- stores the relationships between films and categories.
    store – contains the store data including manager staff and address.
    inventory – stores inventory data.
    rental – stores rental data.
    payment – stores customer’s payments.
    staff – stores staff data.
    customer – stores customer data.
    address – stores address data for staff and customers
    city – stores city names.
    country – stores country names.
    """

def train():
    vn.train(ddl=get_ddl())
    vn.train(documentation=get_documentation())
