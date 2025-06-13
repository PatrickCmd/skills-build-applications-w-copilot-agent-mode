import pytest
import pymongo

@pytest.fixture(scope='session', autouse=True)
def setup_test_db():
    # Use a separate test database
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    test_db = client["octofit_test_db"]
    # Clean up before and after tests
    for collection in ["users", "teams", "activity", "leaderboard", "workouts"]:
        test_db[collection].delete_many({})
    yield test_db
    for collection in ["users", "teams", "activity", "leaderboard", "workouts"]:
        test_db[collection].delete_many({})

@pytest.fixture(autouse=True)
def patch_db(monkeypatch, setup_test_db):
    # Patch the db used in the app to point to the test db
    import octofit_app.views
    monkeypatch.setattr(octofit_app.views, 'db', setup_test_db)
