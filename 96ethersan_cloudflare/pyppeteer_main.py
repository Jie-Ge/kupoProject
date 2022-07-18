import asyncio
from pyppeteer import launch, launcher
from lxml import etree


async def main():
    # 在导入 launch 之前 把 --enable-automation 禁用 防止监测webdriver
    launcher.DEFAULT_ARGS.remove("--enable-automation")
    browser = await launch(headless=False, args=['--disable-infobars'])  # 运行一个无头的浏览器,headless是否输出网页源码

    # 打开新的标签页
    page = await browser.newPage()

    # 设置视图大小
    await page.setViewport({'width': 1366, 'height': 768})

    # 设置UserAgent
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36')

    # 访问页面
    response = await page.goto('https://cn.etherscan.com/address/0x2b74cf42d87ad6ffcc46c29a07cff14149c18b84')

    await asyncio.sleep(100000)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())  # 异步