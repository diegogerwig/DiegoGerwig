import requests

USER_ID = "1193081"  # Tu ID público de TryHackMe
API_URL = f"https://tryhackme.com/api/v2/badges/public-profile?userPublicId={USER_ID}"

def main():
    response = requests.get(API_URL)
    data = response.json()

    name = data["name"]
    rank = data["rank"]
    points = data["points"]

    badge = f"![TryHackMe](https://img.shields.io/badge/TryHackMe-{points}pts--{rank}-red?logo=tryhackme)"
    link = f"[{badge}](https://tryhackme.com/p/{name})"

    with open("README.md", "r") as f:
        lines = f.readlines()

    with open("README.md", "w") as f:
        for line in lines:
            if line.startswith("![TryHackMe]") or "tryhackme.com/p/" in line:
                continue
            f.write(line)
        f.write("\n" + link + "\n")

if __name__ == "__main__":
    main()
