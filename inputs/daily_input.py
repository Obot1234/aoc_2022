import os

import requests
from pathlib import Path
import json

from inputs.converter import Converter


class DailyInput:
    aoc_path = Path(__file__).parent
    session_cookie_path = aoc_path.parent / "session_cookie.json"
    cache_path = aoc_path / "cache"

    def __init__(self, day: int):
        self.day = day
        self.filename = self.cache_path / f"day{day}.txt"

    def convert(self, converter: Converter):
        return converter.convert(self.__get())

    def __get(self) -> [str]:
        if self.filename.exists():
            return self.__get_from_file().splitlines()
        else:
            return self.__get_from_web().splitlines()

    def __get_from_file(self) -> str:
        return open(self.filename, 'r').read()

    def __get_from_web(self) -> str:
        print("Cached file not found. Downloading input..")
        url = f"https://adventofcode.com/2022/day/{self.day}/input"
        with open(self.session_cookie_path, 'r') as file:
            session_cookie = json.load(file)
        r = requests.get(url, allow_redirects=True, cookies=session_cookie)
        if r.ok:
            if not self.cache_path.exists():
                os.makedirs(self.cache_path)
            with open(self.filename, 'w') as file:
                file.write(r.text)
            return r.text
        else:
            raise PermissionError(f"oh no something when wrong with downloading day {self.day}: {r}.")
