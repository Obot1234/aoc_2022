import json
import os
from pathlib import Path
from typing import TypeVar

import requests

from inputs.converter import Converter

T = TypeVar('T')


class DailyInput:
    aoc_path = Path(__file__).parent
    session_cookie_path = aoc_path.parent / "session_cookie.json"
    cache_path = aoc_path / "cache"

    def __init__(self, day: int, test=False):
        self.day = day
        self.filename = self.cache_path / (f"day{day}_test.txt" if test else f"day{day}.txt")

    def convert(self, converter: Converter[T]) -> T:
        return converter.convert(self.get())

    def get(self) -> [str]:
        if self.filename.exists():
            return self.__get_from_file().splitlines()
        else:
            return self.__get_from_web().splitlines()

    def __get_from_file(self) -> str:
        with open(self.filename, 'r') as file:
            res = file.read()
        return res

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
