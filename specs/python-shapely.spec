# Break a circular dependency on pyproj introduced by running doctests.
%bcond bootstrap 0
%bcond doctests %{without bootstrap}
# Enables more tests, but could sometimes be broken on new Pythons
%bcond matplotlib 1

Name:           python-shapely
Version:        2.2.0
Release:        %autorelease
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

# The entire source is BSD-3-Clause, except:
#   Unlicense: versioneer.py (not packaged) and the generated
#              shapely/_version.py
#   MIT: src/kvec.h
License:        BSD-3-Clause AND Unlicense AND MIT
URL:            https://github.com/shapely/shapely
Source:         %{pypi_source shapely}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildSystem:    pyproject
BuildOption(install): --assert-license shapely
BuildOption(generate_buildrequires): --pyproject-dependencies
BuildOption(generate_buildrequires): --dependency-groups build
BuildOption(generate_buildrequires): --dependency-groups tests
BuildOption(build): -Ccompile-args=-j%{?_smp_build_ncpus}
BuildOption(build): -Ccompile-args=--verbose
BuildOption(check): --exclude 'shapely.tests*'
%if %{without matplotlib}
BuildOption(check): --exclude shapely.plotting
%endif

BuildRequires:  gcc
BuildRequires:  geos-devel

%if %{with matplotlib}
# Enables shapely/tests/test_plotting.py
BuildRequires:  %{py3_dist matplotlib}
%endif
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


%prep -a
# Currently, the PyPI sdist does not ship with pre-generated Cython C sources.
# We preventively check for them anyway, as they must be removed if they do
# appear. Note that C sources in src/shapely/lib/ are not generated.
rm --verbose --force src/shapely/*.c

%if %{without doctests}
%pyproject_patch_dependency scipy-doctest:ignore
%endif
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
%pyproject_patch_dependency pytest-cov:ignore


%check -a
%pytest -rs --verbose '%{buildroot}%{python3_sitearch}/shapely'

%if %{with doctests}
%if 0%{?fedora} > 44
# Several doctest failures with GEOS 3.15.0
# https://github.com/shapely/shapely/issues/2527
dtk="${dtk-}${dtk+ and }not shapely._coverage.coverage_clean"
dtk="${dtk-}${dtk+ and }not shapely.constructive.make_valid"
dtk="${dtk-}${dtk+ and }not shapely.constructive.voronoi_polygons"
dtk="${dtk-}${dtk+ and }not shapely.set_operations.difference"
dtk="${dtk-}${dtk+ and }not shapely.set_operations.intersection"
dtk="${dtk-}${dtk+ and }not shapely.set_operations.symmetric_difference"
dtk="${dtk-}${dtk+ and }not shapely.set_operations.union"
dtk="${dtk-}${dtk+ and }not shapely.set_operations.union_all"
%endif

%pytest --doctest-modules --doctest-only-doctests=true \
    '%{buildroot}%{python3_sitearch}/shapely' \
    --ignore='%{buildroot}%{python3_sitearch}/shapely/tests' \
    -k="${dtk-}" --verbose
%endif


%files -n python3-shapely -f %{pyproject_files}
%doc CHANGES.txt
%doc CITATION.cff
%doc CREDITS.txt
%doc README.rst


%changelog
%autochangelog
