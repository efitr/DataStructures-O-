
class Node(object):
    def __init__(self, data):


    def __repr__(self):
        return 'Node({!r})'.format(self.data)

class LinkedList(object):
    def __init__(self, items=None):

    def __str__(self):
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        return 'LinkedList({!r})'.format(self.items())

    def items(self):

        return items

    def is_empty(self):
        return self.head is None

    def length(self):


    
    def append(self, item):



    def prepend(self, item):

        

    def find(self, quality):


    def delete(self, item):
        
            


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print(ll.head)

    print('\nTesting append: ')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r}'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('lenght: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()