class SimpleInterface(interface.Interface):

    def do_something():
        pass

    def do_some_other_thing():
        pass

@interface.implements(SimpleInterface)
@attr.s(frozen=True)
class SimpleOriginal:

    def do_something(self):
        return 5

    def do_some_other_thing(self):
        return 10

@interface.implements(SimpleInterface)
@attr.s(frozen=True, auto_attribs=True)
class SimpleWrapper:

    original: SimpleInterface

    def do_some_other_thing(self):
        return self.original.do_some_other_thing() + 1

class TestSimpleInterface(unittest.TestCase):

    def test_pass_through(self):
        orig = SimpleOriginal()
        wrapper = SimpleWrapper()
        assert_that(wrapper.do_something(), equals(5))
