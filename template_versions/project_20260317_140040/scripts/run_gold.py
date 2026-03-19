import os
import importlib
from concurrent.futures import ThreadPoolExecutor


def run_module(module_name):
    try:
        module_path = f"src.pipelines.gold.{module_name}"
        module = importlib.import_module(module_path)

        print(f"🚀 Running {module_name}...")

        if hasattr(module, "run"):
            module.run()
        else:
            print(f"⚠️ {module_name} has no run()")

    except Exception as e:
        print(f"❌ Error in {module_name}: {e}")


def run():
    print("🥇 Gold Layer (parallel)")

    base_path = "src/pipelines/gold"

    modules = [
        f.replace(".py", "")
        for f in os.listdir(base_path)
        if f.endswith(".py") and f != "__init__.py"
    ]

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(run_module, sorted(modules))

    print("✅ Gold completed")


if __name__ == "__main__":
    run()