from founder_link import FounderLink, MVP

def test_host_mvp():
    founder_link = FounderLink("test_mvp")
    mvp = MVP("test_mvp", "https://test-mvp.com", False)
    founder_link.host_mvp(mvp)
    assert founder_link.get_mvp_url("test_mvp") == "https://test-mvp.com"

def test_deploy_mvp():
    founder_link = FounderLink("test_mvp")
    mvp = MVP("test_mvp", "https://test-mvp.com", False)
    founder_link.host_mvp(mvp)
    assert founder_link.deploy_mvp("test_mvp") == "https://test-mvp.com"

def test_update_mvp():
    founder_link = FounderLink("test_mvp")
    mvp = MVP("test_mvp", "https://test-mvp.com", False)
    founder_link.host_mvp(mvp)
    assert founder_link.update_mvp("test_mvp") == "https://test-mvp.com"
    assert founder_link.mvps["test_mvp"].updated

def test_get_mvp_url():
    founder_link = FounderLink("test_mvp")
    mvp = MVP("test_mvp", "https://test-mvp.com", False)
    founder_link.host_mvp(mvp)
    assert founder_link.get_mvp_url("test_mvp") == "https://test-mvp.com"
