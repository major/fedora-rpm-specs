# Break a circular dependency on pyproj introduced by running doctests.
%bcond bootstrap 0
%bcond doctests %{without bootstrap}

Name:           python-shapely
Version:        2.1.1
Release:        %autorelease
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

# The entire source is BSD-3-Clause, except:
#   Unlicense: versioneer.py (not packaged) and the generated
#              shapely/_version.py
#   MIT: src/kvec.h
License:        BSD-3-Clause AND Unlicense AND MIT
URL:            https://github.com/shapely/shapely
Source:         %{pypi_source shapely}

# TST: update frechet_distance densify test for latest GEOS main
# (densify>0.001)
# https://github.com/shapely/shapely/pull/2311
Patch:          %{url}/pull/2311.patch
# TST: update test_coverage_union_overlapping_inputs for upstream GEOS change
# https://github.com/shapely/shapely/pull/2318
Patch:          %{url}/pull/2318.patch

BuildRequires:  tomcli
BuildRequires:  gcc
BuildRequires:  geos-devel

BuildRequires:  python3-devel
%if %{with doctests}
BuildRequires:  %{py3_dist pyproj}
%endif

%global _description %{expand:
Shapely is a package for creation, manipulation, and analysis of planar
geometry objects – designed especially for developers of cutting edge
geographic information systems. In a nutshell: Shapely lets you do PostGIS-ish
stuff outside the context of a database using idiomatic Python.

You can use this package with python-matplotlib and numpy. See README.rst for
more information!}

%description %_description


%package -n python3-shapely
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

# The file src/kvec.h comes from klib
# (https://github.com/attractivechaos/klib), which is intended to be used as a
# collection of mostly-independent “copylib” components.
Provides:       bundled(klib-kvec) = 0.1.0

%description -n python3-shapely %_description


%prep
%autosetup -n shapely-%{version} -p1

# Currently, the PyPI sdist does not ship with pre-generated Cython C sources.
# We preventively check for them anyway, as they must be removed if they do
# appear. Note that C sources in src/ are not generated.
find shapely -type f -name '*.c' -print -delete

# Patch out coverage analysis from the “test” extra.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.test pytest-cov

%if %{without doctests}
tomcli set pyproject.toml lists delitem \
    project.optional-dependencies.test scipy-doctest
%endif


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l shapely


%check
# Ensure the “un-built” package is not imported. Otherwise compiled extensions
# cannot be tested.
mkdir empty
cd empty
ln -s ../shapely/tests/

%pytest -v

%if %{with doctests}
# TODO: Why does this fail? We cannot reproduce it in a git checkout.
#
# The expected and actual results do at least describe equivalent circles, so
# the library is not giving the wrong answer.
#
# ___________ [doctest] shapely.constructive.maximum_inscribed_circle ____________
# 1473 **kwargs
# 1474     For other keyword-only arguments, see the
# 1475     `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.
# 1476
# 1477 Examples
# 1478 --------
# 1479 >>> import shapely
# 1480 >>> from shapely import Polygon
# 1481 >>> poly = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
# 1482 >>> shapely.maximum_inscribed_circle(poly)
# Expected:
#     <LINESTRING (5 5, 0 5)>
# Got:
#     <LINESTRING (5 5, 10 5)>
#
# /[…]/shapely/constructive.py:1482: DocTestFailure
dtk="${dtk-}${dtk+ and }not shapely.constructive.maximum_inscribed_circle"

%pytest --doctest-modules --doctest-only-doctests=true \
    '%{buildroot}%{python3_sitearch}/shapely' \
    --ignore='%{buildroot}%{python3_sitearch}/shapely/tests' \
    -k="${dtk-}" -v
%endif


%files -n python3-shapely -f %{pyproject_files}
%doc CHANGES.txt
%doc CITATION.cff
%doc CREDITS.txt
%doc README.rst


%changelog
%autochangelog
