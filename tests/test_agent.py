from agent import analyze_severity

def test_severity_detection():

    timeline = """
    Database outage detected
    Service unavailable
    Service restored
    """

    result = analyze_severity(timeline)

    assert result == "Critical"