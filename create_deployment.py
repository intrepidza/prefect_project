from prefect import flow

# SOURCE_REPO = "https://github.com/prefecthq/demos.git"
SOURCE_REPO = "https://github.com/intrepidza/prefect_project.git"

if __name__ == '__main__':
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="my_workflow.py:show_stars",
    ).deploy(
        name="my-first-deployment",
        parameters={
            "github_repos": [
                "PrefectHQ/prefect",
                "pydantic/pydantic",
                "huggingface/transformers",
            ]
        },
        work_pool_name = "my-work-pool",
        cron = "0 * * * *",
    )
