all:
	python setup.py build_ext -if
	python test_levenshtein.py

clean:
	-rm -rf build *.so build *.pyc levenshtein_cython.c levenshtein_solution.c
