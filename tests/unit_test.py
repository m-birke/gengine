from gengine import GenGine


def my_gen(_inp):
    yield from range(10)


def my_add(inp):
    return inp + 2


def my_mul(inp):
    for i in range(3):
        yield inp * i


def my_filter(inp):
    if inp % 2 == 0:
        return None

    return inp


g = GenGine([my_gen, my_add, my_mul, my_filter])

out = list(g.run(1))

assert out == [3, 5, 7, 9, 11]
