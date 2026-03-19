from graphviz import Digraph
from src.pipelines.dag import DAG


def run():
    dot = Digraph(comment="Pipeline DAG")
    dot.attr(rankdir="LR")

    colors = {
        "silver": "lightblue",
        "gold": "gold"
    }

    for layer, tasks in DAG.items():

        for task, deps in tasks.items():

            node = f"{layer}.{task}"

            dot.node(node, node, style="filled", fillcolor=colors[layer])

            for dep in deps:
                dot.edge(f"silver.{dep}", node)

    output = "docs/diagrams/dag_pipeline"
    dot.render(output, format="png", cleanup=True)

    print(f"✅ Diagram generated: {output}.png")


if __name__ == "__main__":
    run()