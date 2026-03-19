import os
import importlib


def run():
    print("🥉 Bronze Layer (auto-discovery)")

    base_path = "src/pipelines/bronze"

    for file in sorted(os.listdir(base_path)):

        if file.endswith(".py") and file != "__init__.py":

            module_name = file.replace(".py", "")
            module_path = f"src.pipelines.bronze.{module_name}"

            print(f"🚀 Running {module_name}...")

            module = importlib.import_module(module_path)

            if hasattr(module, "run"):
                module.run()

    print("✅ Bronze completed")


if __name__ == "__main__":
    run()