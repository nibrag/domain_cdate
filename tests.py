import asyncio
from domain_cdate import creation_date

domains = [
    'vk.ru',
    'msc.su',
    'кремль.рф',
    'nic.xn--d1acj3b',
    'nic.XN--80ASWG'
]
# todo: add more domains for tests


def test_domains():
    loop = asyncio.get_event_loop()
    tasks = []

    for domain in domains:
        fut = asyncio.async(creation_date(domain, loop=loop))
        tasks.append(fut)

    try:
        results = loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))

        for r in results:
            assert not isinstance(r, Exception)
    finally:
        loop.close()
