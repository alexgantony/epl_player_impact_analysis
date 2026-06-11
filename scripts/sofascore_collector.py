import json

from playwright.sync_api import sync_playwright

from config.paths import RAW_DATA_DIR

url_params = {
    "summary": {"group": "summary", "order": "rating"},
    "attack": {"group": "attack", "order": "goals"},
    "defence": {"group": "defence", "order": "tackles"},
    "passing": {"group": "passing", "order": "bigChancesCreated"},
    "goalkeeper": {"group": "goalkeeper", "filters": "position.in.G", "order": "saves"},
}


def generate_url(config, offset=0):
    if config["group"] != "goalkeeper":
        sofascore_url = f"https://www.sofascore.com/api/v1/unique-tournament/17/season/76986/statistics?limit=20&order=-{config['order']}&offset={offset}&accumulation=total&group={config['group']}"
    else:
        sofascore_url = f"https://www.sofascore.com/api/v1/unique-tournament/17/season/76986/statistics?limit=20&order=-{config['order']}&offset={offset}&accumulation=total&group={config['group']}&filters={config['filters']}"

    return sofascore_url


def fetch_data(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto(url)

        page_content = page.text_content(selector="pre")
        browser.close()

    return page_content


def save_data(name, data):
    if not RAW_DATA_DIR.is_dir():
        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(RAW_DATA_DIR / f"{name}.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data))


for name, config in url_params.items():
    url = generate_url(config)
    data = fetch_data(url)

    assert data is not None
    first_page_data = json.loads(data)
    pages = first_page_data["pages"]
    iter_num = pages * len(first_page_data["results"])
    player_list = first_page_data["results"]

    for offset in range(20, iter_num + 1, 20):
        url = generate_url(config, offset)
        current_page_data = fetch_data(url)

        data_json = json.loads(current_page_data)
        new_players = data_json["results"]

        player_list.extend(new_players)
        print(f"New Players added from page: {offset / 20} in file: {name}")

    print(len(player_list))
    save_data(name, first_page_data)
