# yGenius Brain

[![](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

What is this: https://medium.com/@marcoworms/ygenius-chat-with-yearn-efa17d3f0ec8  
Frontend Source: https://github.com/yearn/ygenius-webui

![image](https://user-images.githubusercontent.com/7863230/219803104-9612160e-8a1b-42b1-9af5-12fccf77232d.png)

## Configuration

- copy `.env.sample` to `.env` and set environment variables (only `OPENAI_API_KEY` is mandatory)
- copy `index.json` model file to the current dir or generate a new one

## Run

Install docker and docker-compose and run:
`docker-compose up -d`

## Development

Whenever making changes to the code base, you need to rebuild a new docker image:
`docker-compose build`

## Usage

`curl "http://localhost:5001/ask?history=&query=what%20is%20yearn%20%3F"`

Output:

```
  Yearn is a decentralized finance (DeFi) platform that provides users with access
  to a range of financial services, including yield farming, liquidity pools, and
  automated portfolio management. Yearn is built on the Ethereum blockchain and is
  designed to make it easier for users to maximize their returns on their investments.
```
