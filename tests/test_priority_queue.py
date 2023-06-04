from src.priority_queue import BucketItem, BucketList


def test_BucketItem():
    item_1 = BucketItem(item="travel the world")
    item_2 = BucketItem(item="clean my apartment", priority=False)
    assert item_1.item == "travel the world"
    assert item_2.item == "clean my apartment"
    assert item_1.priority
    assert not item_2.priority


def test_heap():
    bucket_list = BucketList()
    bucket_list.add("travel world")
    bucket_list.add("write a book")
    bucket_list.add("save the world")

    assert bucket_list.size == 3
    assert bucket_list.get() == "travel world"

    bucket_list.add("put out fire", prioritize=True)
    assert bucket_list.get() == "put out fire"

    bucket_list.add("save the world", prioritize=True)
    assert bucket_list.get() == "save the world"
    assert bucket_list.size == 4

    # do it again to make sure it doesn't add to the queue
    bucket_list.add("save the world", prioritize=True)
    assert bucket_list.get() == "save the world"
    assert bucket_list.size == 4


def test_init_heap():
    bucket_list = BucketList(["stuff to do", "more to do", "even more to do"])
    assert bucket_list.get() == "stuff to do"
    assert bucket_list.size == 3


def test_remove():
    bucket_list = BucketList(
        ["travel world", "write a book", "save the world", "put out fire"]
    )

    bucket_list.remove("save the world")
    assert bucket_list.size == 3
    assert bucket_list.get() == "travel world"

    bucket_list.remove("travel world")
    assert bucket_list.size == 2
    assert bucket_list.get() == "write a book"

    assert not bucket_list.remove("flap arms")


def test_prioritize():
    bucket_list = BucketList(
        ["travel world", "write a book", "save the world", "put out fire", "sleep"]
    )
    bucket_list.prioritize("save the world")
    assert bucket_list.get() == "save the world"
    bucket_list.prioritize("buy a doughnut")
    assert bucket_list.get() == "buy a doughnut"


def test_serialization():
    bucket_list = BucketList(
        ["travel world", "write a book", "save the world", "put out fire", "sleep"]
    )
    bucket_list.to_file("debug.csv")
    new_bucket_list = BucketList.from_file("debug.csv")
    assert new_bucket_list.size == 5
    assert new_bucket_list.get() == "travel world"
