from src.priority_queue import BucketList


def test_heap():
    bucket_list = BucketList()
    bucket_list.add('travel world')
    bucket_list.add('write a book')
    bucket_list.add('save the world')

    assert bucket_list.n_items == 3
    assert bucket_list.get() == 'save the world'

    bucket_list.prioritize('travel world')

    bucket_list.print()
    # bucket_list.prioritize('save the world')
    assert bucket_list.get() == 'travel world'


def test_init_heap():
    bucket_list = BucketList(
        [
            'stuff to do',
            'more to do',
            'even more to do'
        ]
    )
    assert bucket_list.get() == 'even more to do'
    assert bucket_list.n_items == 3


# def test_validate():
#     bucket_list = BucketList()
#     assert (bucket_list.validate((0.1, 'Test this function')))
#     assert (not bucket_list.validate(('0.1', 'Test this function')))
#     assert (not bucket_list.validate(
#         [(0.1, 'This should fail'), (0.2, 'This should really fail')]
#     ))
