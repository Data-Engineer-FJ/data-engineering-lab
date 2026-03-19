from diagrams import Diagram
from diagrams.programming.language import Python
from diagrams.onprem.workflow import Airflow
from diagrams.onprem.analytics import Spark
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.analytics import Metabase

with Diagram(
    "Data Platform Architecture",
    filename="docs/diagrams/data_platform_architecture",
    show=False,
    direction="LR"
):

    source = Python("Data Sources")

    ingestion = Python("Ingestion Scripts")
    airflow = Airflow("Airflow Scheduler")

    processing = Spark("Processing Engine\n(PySpark)")

    bronze = Python("Bronze Layer\nRaw Data")
    silver = Python("Silver Layer\nClean Data")
    gold = Python("Gold Layer\nBusiness Data")

    warehouse = PostgreSQL("Data Warehouse")

    bi = Metabase("BI / Analytics")

    source >> ingestion >> airflow >> processing
    processing >> bronze >> silver >> gold
    gold >> warehouse >> bi