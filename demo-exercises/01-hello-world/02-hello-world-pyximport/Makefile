all:
	python setup.py build_ext --inplace --force

test: all
	python test_hello_world.py

clean:
	-rm -rf build cython_hello_world.{c,so}
