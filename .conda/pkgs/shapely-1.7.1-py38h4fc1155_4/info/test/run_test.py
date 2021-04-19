#  tests for shapely-1.7.1-py38h4fc1155_4 (this is a generated file);
print('===== testing package: shapely-1.7.1-py38h4fc1155_4 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---
import platform
import py

implementation = platform.python_implementation()
print('implementation: {}'.format(implementation))

# SvgTestCase.test_collection is failing due to GEOS 3.9 different coordinate order
# (it's fixed on master so can be removed again with Shapely 1.8)
pytest_args = ['tests', '-k', 'not test_collection']

if implementation != 'PyPy':
    from shapely import speedups
    import shapely.speedups._speedups
    import shapely.vectorized
    import shapely.vectorized._vectorized

    assert speedups.available;

    speedups.enable()
    pytest_args.append('--with-speedups')

py.test.cmdline.main(pytest_args)

from shapely.geometry import LineString

ls = LineString([(0, 0), (10, 0)])
# On OSX causes an abort trap, due to https://github.com/Toblerity/Shapely/issues/177
r = ls.wkt
area = ls.buffer(10).area

# Check if we can import lgeos.
# https://github.com/conda-forge/shapely-feedstock/issues/17
from shapely.geos import lgeos
#  --- run_test.py (end) ---

print('===== shapely-1.7.1-py38h4fc1155_4 OK =====');
print("import: 'shapely'")
import shapely

print("import: 'shapely.geometry'")
import shapely.geometry

print("import: 'shapely.algorithms'")
import shapely.algorithms

print("import: 'shapely.examples'")
import shapely.examples

print("import: 'shapely.geos'")
import shapely.geos

