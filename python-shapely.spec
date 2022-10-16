# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-shapely
Version:        1.8.5.post1
Release:        %autorelease
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

License:        BSD-3-Clause
URL:            https://github.com/shapely/shapely
Source0:        %{url}/archive/%{version}/shapely-%{version}.tar.gz

# Revert "BLD: avoid using latest setuptools for building 1.8.x (#1481)"
#
# This reverts commit f25c3ff57e7afcde8db7c35a7ec01c9195c4655e.
#
# The setuptools version was upper-bounded due to changes in editable
# installations, but these are not relevant for building distribution
# packages.
#
# See also https://github.com/shapely/shapely/pull/1481, where the version cap
# was discussed and added upstream.
Patch:          0001-Revert-BLD-avoid-using-latest-setuptools-for-buildin.patch

BuildRequires:  gcc
BuildRequires:  geos-devel

BuildRequires:  python3-devel

# Vendored upstream, but we remove the vendored copy:
BuildRequires:  python3dist(packaging)

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global _description %{expand:
Shapely is a package for creation, manipulation, and analysis of planar
geometry objects – designed especially for developers of cutting edge
geographic information systems. In a nutshell: Shapely lets you do PostGIS-ish
stuff outside the context of a database using idiomatic Python.

You can use this package with python-matplotlib and numpy. See README.rst for
more information!}

%description %_description


%pyproject_extras_subpkg -n python3-shapely vectorized


%package -n python3-shapely
Summary:        Manipulation and analysis of geometric objects in the Cartesian plane

%description -n python3-shapely %_description


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc %_description


%prep
%autosetup -n shapely-%{version} -p1

# Remove vendored python-packaging
rm -rvf _vendor
sed -r -i 's/_vendor\.//g' setup.py

# Currently, the GitHub tarball does not ship with pre-generated Cython C
# sources. We preventively check for them anyway, as they must be removed if
# they do appear.
find . -type f -name '*.c' -print -delete

# We don’t need the “oldest supported numpy” in the RPM build, and the
# metapackage in question (https://pypi.org/project/oldest-supported-numpy/) is
# not packaged. Just depend on numpy.
sed -r -i 's/oldest-supported-(numpy)/\1/' 'pyproject.toml'

# We can use requirements-dev.txt to get extra dependencies for the
# documentation, but we must loosen exact-version pins to allow newer versions,
# and we must drop the dependency on descartes.
#
# While python3dist(descartes) is needed for a complete documentation build, it
# no longer has an upstream; its tests started failing in Fedora
# (RHBZ#1907389); and it was retired after F34. See
# https://github.com/shapely/shapely/issues/1145. The documentation is still
# useful without it.
sed -r  \
    -e 's/==/>=/' \
    -e '/\bdescartes\b/d' \
    'requirements-dev.txt' | tee 'requirements-dev-filtered.txt'


%generate_buildrequires
# Extra “all” is currently “vectorized”+“test”.
%pyproject_buildrequires -x all requirements-dev-filtered.txt


%build
%pyproject_wheel

%if %{with doc_pdf}
# We can build documentation without the optional compiled vectorized
# extensions, but we use the “built” copy of the package instead since it easy
# enough to do so.
PYTHONPATH="%{pyproject_build_lib}" \
    %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files shapely


%check
# Ensure the “un-built” package is not imported. Otherwise compiled extensions
# cannot be tested.
mkdir empty
cd empty
ln -s ../tests/

%pytest


%files -n python3-shapely -f %{pyproject_files}
# pyproject-rpm-macros handles LICENSE.txt; verify with “rpm -qL -p …”
%exclude %{python3_sitearch}/shapely/examples/


%files doc
%license LICENSE.txt

%doc CHANGES.txt
%doc CITATION.txt
%doc CODE_OF_CONDUCT.md
%doc CREDITS.txt
%doc FAQ.rst
%doc GEOS-C-API.txt
%doc README.rst

%doc docs/design.rst

%if %{with doc_pdf}
%doc docs/_build/latex/Shapely.pdf
%endif

%doc shapely/examples/


%changelog
%autochangelog
