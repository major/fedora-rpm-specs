Name:           python-shapely
Version:        2.0.2
Release:        %autorelease
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

# The entire source is BSD-3-Clause, except:
#   Unlicense: versioneer.py (not packaged) and the generated
#              shapely/_version.py
#   MIT: src/kvec.h
License:        BSD-3-Clause AND Unlicense AND MIT
URL:            https://github.com/shapely/shapely
Source:         %{pypi_source shapely}

# Adjust tests for docstring indent stripping in Python 3.13
# https://github.com/shapely/shapely/pull/1938
#
# Fixes:
#
# Test failure on Python 3.13 because it strips indents from docstrings
# https://github.com/shapely/shapely/issues/1937
#
# Rebased on 2.0.2.
Patch:          shapely-2.0.2-pr-1938.patch

BuildRequires:  gcc
BuildRequires:  geos-devel

BuildRequires:  python3-devel

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

# The [vectorized] extra has gone away in Shapely 2.0. We Provide the name of
# the old vectorized extra metapackage since vectorized implementations are
# always compiled in the base package, but we do not attempt to Provide
# python3dist(shapely[vectorized]) etc.
%py_provides python3-shapely+vectorized
Obsoletes:      python3-shapely+vectorized < 2.0.0-1

# We used to build PDF documentation in a separate subpackage. The PyPI sdist
# lacks necessary files, like docs/conf.py, but the GitHub archive lacks the
# proper released shapely/_version.py, so if we use it, we need to create a tag
# in a local git repository to get the right version number in the dist-info
# metadata. We find that the PDF documentation is not worth all that hassle!
Obsoletes:      python-shapely-doc < 2.0.0-1

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

# We don’t need the “oldest supported numpy” in the RPM build, and the
# metapackage in question (https://pypi.org/project/oldest-supported-numpy/) is
# not packaged. Just depend on numpy.
#
# Patch out coverage analysis from the “test” extra.
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i \
    -e 's/oldest-supported-(numpy)/\1/' \
    -e 's/^([[:blank:]]+)("pytest-cov")/\1# \2/' \
    pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files shapely


%check
# Ensure the “un-built” package is not imported. Otherwise compiled extensions
# cannot be tested.
mkdir empty
cd empty
ln -s ../shapely/tests/

%pytest -v


%files -n python3-shapely -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE.txt; verify with “rpm -qL -p …”
%doc CHANGES.txt
%doc CITATION.cff
%doc CREDITS.txt
%doc README.rst


%changelog
%autochangelog
