# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-OWSLib
Version:        0.28.1
Release:        %autorelease
Summary:        Client library for OGC web services

License:        BSD-3-Clause
URL:            https://geopython.github.io/OWSLib
Source0:        https://github.com/geopython/OWSLib/archive/%{version}/OWSLib-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  pandoc
%endif

%global common_description %{expand:
OWSLib is a Python package for client programming with Open Geospatial
Consortium (OGC) web service (hence OWS) interface standards, and their related
content models.

Full documentation is available at http://geopython.github.io/OWSLib

OWSLib provides a common API for accessing service metadata and wrappers for
numerous OGC Web Service interfaces.}

%description %{common_description}


%package -n python3-OWSLib
Summary:        %{summary}

%py_provides python3-owslib

%description -n python3-OWSLib %{common_description}


%package doc
Summary:        Documentation and examples for OWSLib

%description doc
%{summary}.


%prep
%autosetup -n OWSLib-%{version}

# Don’t analyze/report test coverage
sed -r -i 's/[-]-cov[^[:blank:]]*[[:blank:]][^[[:blank:]]+//g' tox.ini
# Don’t generate linting/coverage dependencies.
#
# We don’t have python3dist(pandoc) packaged, and besides, we don’t actually
# need python3dist(pandoc)—only the pandoc command-line tool, which we have
# manually BR’d.
#
# Don’t generate twine dependency, which is just for the upstream maintainer
# uploading to PyPI.
sed -r -e '/^(flake8|pytest-cov|pandoc|coverage|coveralls|twine)\b/d' \
%if %{without doc_pdf}
    -e '/^(ipykernel|nbconvert|.*sphinx)/d' \
%endif
    requirements-dev.txt | tee requirements-dev-filtered.txt

# We don’t need shebangs in the examples. The pattern of selecting files
# before modifying them with sed keeps us from unnecessarily discarding the
# original mtimes on unmodified files.
find 'examples' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'
# Some of them, but not all of them, were executable.
chmod -v a-x examples/*.py

# Because at least one notebook requires Internet access, we must continue past
# notebook errors when building documentation.
echo 'nbsphinx_allow_errors = True' >> docs/conf.py


%generate_buildrequires
%pyproject_buildrequires requirements-dev-filtered.txt


%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex/en LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files owslib


%check
# Otherwise, pytest finds the package twice in the Python path and complains.
rm -rf owslib

# There is a convenient “online” mark for deselecting tests that require
# Internet access, but we still have to manually deselect doctests that try to
# make network requests.
k="${k-}${k+ and }not wms_geoserver_mass_gis.txt"
k="${k-}${k+ and }not wfs_MapServerWFSFeature.txt"
k="${k-}${k+ and }not wfs_MapServerWFSCapabilities.txt"
k="${k-}${k+ and }not wfs2_storedqueries.txt"
k="${k-}${k+ and }not wfs1_generic.txt"
k="${k-}${k+ and }not wcs_thredds.txt"
k="${k-}${k+ and }not test_wmts_example_informatievlaanderen"

# This is a trivial error where the representation of the expected TypeError
# has changed over time:
# Differences (unified diff with -expected +actual):
#     @@ -1,3 +1,6 @@
#      Traceback (most recent call last):
#     -...
#     -TypeError: get_namespace() ...
#     +  File "/usr/lib64/python3.10/doctest.py", line 1346, in __run
#     +    exec(compile(example.source, filename, "single",
#     +  File "<doctest namespaces.txt[15]>", line 1, in <module>
#     +    ns.get_namespace()
#     +TypeError: Namespaces.get_namespace() missing 1 required positional argument: 'key'
k="${k-}${k+ and }not namespaces.txt"

# Unknown problem—check if it is fixed in a later version:
k="${k-}${k+ and } not (TestOffline and test_wfs_110_remotemd_parse_all)"
k="${k-}${k+ and } not (TestOffline and test_wfs_110_remotemd_parse_single)"
k="${k-}${k+ and } not (TestOffline and test_wfs_200_remotemd_parse_all)"
k="${k-}${k+ and } not (TestOffline and test_wfs_200_remotemd_parse_single)"
k="${k-}${k+ and } not (TestOffline and test_wms_130_remotemd_parse_all)"
k="${k-}${k+ and } not (TestOffline and test_wms_130_remotemd_parse_single)"

%pytest -m 'not online' -k "${k-}"


%files -n python3-OWSLib -f %{pyproject_files}
# pyproject_files handles LICENSE; verify with “rpm -qL -p …”


%files doc
%license LICENSE
%doc AUTHORS.rst
%doc CHANGES.rst
%doc README.rst
%doc examples
%if %{with doc_pdf}
%doc docs/build/latex/en/OWSLib.pdf
%endif


%changelog
%autochangelog
