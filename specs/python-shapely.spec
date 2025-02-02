Name:           python-shapely
Version:        2.0.7
Release:        %autorelease
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

# The entire source is BSD-3-Clause, except:
#   Unlicense: versioneer.py (not packaged) and the generated
#              shapely/_version.py
#   MIT: src/kvec.h
License:        BSD-3-Clause AND Unlicense AND MIT
URL:            https://github.com/shapely/shapely
Source:         %{pypi_source shapely}

BuildRequires:  tomcli
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

# We first shipped Shapley 2.0 in Fedora 39, so the migration paths from F38
# (which need to be present for three releases) can be dropped after F41.
%if %{defined fc40} || %{defined fc41}
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
%endif

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


%files -n python3-shapely -f %{pyproject_files}
%doc CHANGES.txt
%doc CITATION.cff
%doc CREDITS.txt
%doc README.rst


%changelog
%autochangelog
