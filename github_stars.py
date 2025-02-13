import httpx

from prefect import flow, task


@flow(log_prints=True)
def show_stars(github_repos: list[str]):
    """Shows number of stars that Github repos have"""
    for repo in github_repos:
        repo_stats = fetch_stats(repo)
        stars = get_stats(repo_stats)
        print(f"{repo}: {stars} stars")


@task
def fetch_stats(github_repo: str):
    """Fetch repo stats"""
    return httpx.get(f"https://api.github.com/repos/{github_repo}").json()


@task
def get_stats(repo_stats: dict):
    "Get number of stars from Github repo stats"
    return repo_stats['stargazers_count']


if __name__ == "__main__":
    show_stars([
        "PrefectHQ/prefect",
        "pydantic/pydantic",
        "huggingface/transformers",
    ])
