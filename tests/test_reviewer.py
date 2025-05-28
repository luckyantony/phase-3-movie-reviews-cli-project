from models.reviewers import Reviewer

def test_reviewer_creation():
    reviewer = Reviewer("Test User")
    assert reviewer.name == "Test User"
    assert reviewer.id is None

def test_reviewer_save():
    reviewer = Reviewer("Test Save")
    reviewer.save()
    assert reviewer.id is not None