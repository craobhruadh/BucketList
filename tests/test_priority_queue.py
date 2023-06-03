from src.priority_queue import BucketList, BucketItem


def test_BucketItem():
    item_1 = BucketItem(item="travel the world")
    item_2 = BucketItem(item="clean my apartment", priority=2)
    assert item_1.item == "travel the world"
    assert item_2.item == "clean my apartment"
    assert item_1.priority == 1
    assert item_2.priority == 2


def test_heap():
    bucket_list = BucketList()
    bucket_list.add("travel world")
    bucket_list.add("write a book")
    bucket_list.add("save the world")

    assert bucket_list.n_items == 3
    assert bucket_list.get() == "save the world"

    bucket_list.prioritize("travel world")
    bucket_list.print()
    # bucket_list.prioritize('save the world')
    assert bucket_list.get() == "travel world"


def test_init_heap():
    bucket_list = BucketList(["stuff to do", "more to do", "even more to do"])
    assert bucket_list.get() == "even more to do"
    assert bucket_list.n_items == 3
