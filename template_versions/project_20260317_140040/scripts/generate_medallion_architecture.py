from diagrams import Diagram, Cluster
from diagrams.programming.language import Python
from diagrams.onprem.analytics import Spark
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.analytics import Metabase

graph_attr = {
    "fontsize": "24",
    "bgcolor": "white",
    "pad": "1.2",
    "ranksep": "2",
    "nodesep": "1.6",
}

node_attr = {
    "fontsize": "16",
}

cluster_attr = {
    "fontsize": "18",
    "pad": "20"
}

with Diagram(
    "Medallion Data Architecture",
    filename="docs/diagrams/medallion_architecture",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr
):

    source = Python("Data Sources")

    processing = Spark(
        "Processing Engine\n(PySpark)"
    )

    with Cluster(
        "Data Lake\n(Medallion Architecture)",
        graph_attr=cluster_attr
    ):

        bronze = Python(
            "Bronze Layer\nRaw Data"
        )

        silver = Python(
            "Silver Layer\nClean & Standardized"
        )

        gold = Python(
            "Gold Layer\nBusiness Aggregations"
        )

        bronze >> silver >> gold

    warehouse = PostgreSQL("Data Warehouse")

    bi = Metabase("BI / Analytics")

    source >> processing >> bronze
    gold >> warehouse >> bi