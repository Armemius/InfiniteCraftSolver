import random
import time
import requests
import cloudscraper
from loguru import logger
import os

initial_elements = ["💧 Water", "🔥 Fire", "🌬️ Wind", "🌍 Earth"]
elements = set(["Water", "Fire", "Wind", "Earth"])

used_combinations = set()


def gen_all_combinations(elements: list) -> set:
    """
    Generates all possible combinations of current elements.
    """
    if len(elements) == 0:
        return set()

    combinations = set()
    for i in range(len(elements)):
        for j in range(i, len(elements)):
            combinations.add((elements[i], elements[j]))

    logger.info(f"Generated {len(combinations)} possible combinations")

    return combinations


def get_result(first: str, second: str) -> str:
    """
    Returns the result of the operation on two elements.
    """

    url = "https://neal.fun/api/infinite-craft/pair"
    querystring = {"first": first, "second": second}

    user_agents = [
        "not-a-bot",
        "amogus",
        "totally-not-a-bot",
        "legitimate-bot",
        "privet-ot-detey-donbassa",
        "vodka_is_op",
    ]

    headers = {
        "Host": "neal.fun",
        "Accept": "*/*",
        "Referer": "https://neal.fun/infinite-craft/",
        "User-Agent": random.choice(user_agents),
    }

    scraper = cloudscraper.create_scraper()
    response = scraper.get(
        url, params=querystring, headers=headers, allow_redirects=True
    )
    response.raise_for_status()
    data = response.json()

    return data["result"], data["emoji"], data["isNew"]


def main():
    """
    Main function to run the script.
    """
    global elements, used_combinations

    logger.info("Starting Infinite Craft solver...")
    logger.info("Initial elements: " + ", ".join(initial_elements))

    if os.path.exists("elements.txt"):
        os.remove("elements.txt")
        logger.info("Removed old elements.txt")
    if os.path.exists("recipies.txt"):
        os.remove("recipies.txt")
        logger.info("Removed old recipies.txt")

    with open("elements.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(initial_elements) + "\n")
        logger.info("Created elements.txt with initial elements")

    iteration = 0
    while True:
        iteration += 1
        logger.info(f"Iteration {iteration} started.")
        combinations = gen_all_combinations(list(elements))
        new_combinations = combinations - used_combinations

        if not new_combinations:
            logger.info("No new combinations found.")
            break

        for first, second in new_combinations:
            while True:
                try:
                    result, emoji, is_new = get_result(first, second)
                    break
                except requests.exceptions.RequestException:
                    time.sleep(random.uniform(30, 60))  # Rate limit sucks
            if result and result != "Nothing":
                if result not in elements:
                    with open("elements.txt", "a", encoding="utf-8") as f:
                        f.write(f"{emoji} {result}\n")
                elements.add(result)
            if is_new:
                logger.info(f"Discovered new element: {result}")
            else:
                logger.info(
                    f"Processed new recipe: {first} + {second} = {result}"
                )
            used_combinations.add((first, second))
            used_combinations.add((second, first))
            with open("recipies.txt", "a") as f:
                f.write(f"{first} + {second} = {result}\n")
        logger.info(
            f"Iteration {iteration} "
            f"| Current elements: {len(elements)} "
            f"| Used combinations: {len(used_combinations)}"
        )


if __name__ == "__main__":
    main()
