import requests
import json

GITHUB_USER = "tjnolan319"
GITHUB_TOKEN = None  # Optional: paste your GitHub token here

HEADERS = {
    "Accept": "application/vnd.github.mercy-preview+json"
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"

def get_repos(user):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_topics(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/topics"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get("names", [])

def build_network_data(repos):
    nodes = set()
    links = {}

    for repo in repos:
        full_name = repo["full_name"]
        topics = get_topics(full_name)
        for tag in topics:
            nodes.add(tag)
        for i in range(len(topics)):
            for j in range(i + 1, len(topics)):
                pair = tuple(sorted((topics[i], topics[j])))
                links[pair] = links.get(pair, 0) + 1

    node_list = [{"id": tag} for tag in sorted(nodes)]
    link_list = [
        {"source": a, "target": b, "weight": w}
        for (a, b), w in links.items()
    ]
    return {"nodes": node_list, "links": link_list}

def main():
    repos = get_repos(GITHUB_USER)
    print(f"Found {len(repos)} repositories.")
    network_data = build_network_data(repos)
    with open("tag_network.json", "w") as f:
        json.dump(network_data, f, indent=2)
    print("Saved tag network to tag_network.json")

if __name__ == "__main__":
    main()

