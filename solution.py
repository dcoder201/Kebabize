def kebabize(st):
    #your code here
    st = ''.join(c for c in st if not c.isdigit())
    # insert hyphen before each capital letter
    st = ''.join(['-' + c.lower() if c.isupper() else c for c in st])
    # remove leading hyphen if it exists
    if st and st[0] == '-':
        st = st[1:]
    return st
  

  import codewars_test as test
from solution import kebabize

@test.describe("Basic tests")
def test_group():
    @test.it("Should work for basic tests")
    def test_case():
        test.assert_equals(kebabize('myCamelCasedString'), 'my-camel-cased-string')
        test.assert_equals(kebabize('myCamelHas3Humps'), 'my-camel-has-humps')
        test.assert_equals(kebabize('SOS'), 's-o-s')
        test.assert_equals(kebabize('42'), '')
        test.assert_equals(kebabize('CodeWars'), 'code-wars')
