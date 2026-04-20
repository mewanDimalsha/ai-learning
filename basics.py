import asyncio


async def fetch_response(question):
    print(f"Fetching answer for: {question}")
    await asyncio.sleep(1)  # simulates API wait
    return f"Answer to {question}"


async def main():
    question = "What is the capital of France?"
    question2 = "What is the capital of Germany?"
    answer = await asyncio.gather(fetch_response(question), fetch_response(question2))
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())
