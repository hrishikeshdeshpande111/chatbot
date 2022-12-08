from setuptools import find_packages
from setuptools import setup

setup(
    name="revChatGPT",
    version="0.0.32.1",
    license="GNU General Public License v2.0",
    author="Antonio Cheong",
    author_email="acheong@student.dalat.org",
    description="ChatGPT is a reverse engineering of OpenAI's ChatGPT API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/acheong08/ChatGPT",
    install_requires=[
        "requests",
        "httpx[http2]",
        "OpenAIAuth",
    ]
)

from revChatGPT.revChatGPT import Chatbot