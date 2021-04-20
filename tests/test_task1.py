from src.task1 import run


organizations = ["https://masterdel.ru/", "https://repetitors.info/"]


def test_one_page():
    page_url = organizations[0]
    [[url, phones]] = run([page_url])
    assert url == page_url
    assert phones == set(["84956608317", "88005057285", "88005057289"])
    for p in phones:
        assert len(p) == 11
        assert p[0] == "8"
        assert p.isdigit()


def test_few_pages():
    assert run(organizations) == [
        (
            "https://masterdel.ru/",
            set(["84956608317", "88005057285", "88005057289"]),
        ),
        (
            "https://repetitors.info/",
            set(["84955405676", "88005057283", "88005057284"]),
        ),
    ]
