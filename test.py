import asyncio
import subprocess

async def f():
    subprocess.Popen('curl -i http://localhost/index.html"', shell=True)

async def main():
    num = 7
    await asyncio.gather(*[f() for _ in range(num)])

if __name__ == '__main__':
    asyncio.run(main())