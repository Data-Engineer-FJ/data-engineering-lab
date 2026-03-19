import importlib
from concurrent.futures import ThreadPoolExecutor
from src.pipelines.dag import DAG


executed = set()


def run_task(layer, task):
    try:
        module_path = f"src.pipelines.{layer}.{task}"
        module = importlib.import_module(module_path)

        print(f"🚀 Running {layer}.{task}")

        if hasattr(module, "run"):
            module.run()

        executed.add(task)

    except Exception as e:
        print(f"❌ Error in {task}: {e}")


def can_run(task, dependencies):
    return all(dep in executed for dep in dependencies)


def run_layer(layer):
    print(f"\n🔷 Running {layer.upper()} layer with DAG...")

    tasks = DAG[layer]

    while len(executed.intersection(tasks.keys())) < len(tasks):

        ready_tasks = [
            task for task, deps in tasks.items()
            if task not in executed and can_run(task, deps)
        ]

        if not ready_tasks:
            raise Exception("❌ Deadlock detected in DAG")

        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(lambda t: run_task(layer, t), ready_tasks)


def run():
    print("🚀 Running DAG pipeline...")

    run_layer("silver")
    run_layer("gold")

    print("\n✅ DAG pipeline completed")


if __name__ == "__main__":
    run()