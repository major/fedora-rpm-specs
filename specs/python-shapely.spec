# Break a circular dependency on pyproj introduced by running doctests.
%bcond bootstrap 0
%bcond doctests %{without bootstrap}
# Enables more tests, but could sometimes be broken on new Pythons
%bcond matplotlib 1

Name:           python-shapely
Version:        2.1.2
Release:        %autorelease
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

# The entire source is BSD-3-Clause, except:
#   Unlicense: versioneer.py (not packaged) and the generated
#              shapely/_version.py
#   MIT: src/kvec.h
License:        BSD-3-Clause AND Unlicense AND MIT
URL:            https://github.com/shapely/shapely
Source:         %{pypi_source shapely}

BuildSystem:            pyproject
BuildOption(install):   -l shapely
BuildOption(generate_buildrequires): -x test

BuildRequires:  tomcli
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


%check
# Ensure the “un-built” package is not imported. Otherwise compiled extensions
# cannot be tested.
mkdir empty
cd empty
ln -s ../shapely/tests/

%pyproject_check_import -e 'shapely.tests*' %{?!with_matplotlib:-e shapely.plotting}
%pytest -rs -v

%if %{with doctests}
# Doctest shapely.constructive.maximum_inscribed_circle fails
# https://github.com/shapely/shapely/issues/2391
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
