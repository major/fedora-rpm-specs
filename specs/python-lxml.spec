Name:           python-lxml
Version:        5.3.0
Release:        %autorelease
Summary:        XML processing library combining libxml2/libxslt with the ElementTree API

# The lxml project is licensed under BSD-3-Clause
# Some code is derived from ElementTree and cElementTree
# thus using the MIT-CMU elementtree license
# .xsl schematron files are under the MIT license
License:        BSD-3-Clause AND MIT-CMU AND MIT
URL:            https://github.com/lxml/lxml

# We use the get-lxml-source.sh script to generate the tarball
# without the isoschematron RNG validation file under a problematic license.
# See: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/154
Source0:        lxml-%{version}-no-isoschematron-rng.tar.gz
Source1:        get-lxml-source.sh

# Fix missing "//" in file URLs under Python 3.14
# https://bugs.launchpad.net/bugs/2085619
# https://bugzilla.redhat.com/2335830
Patch:          https://github.com/lxml/lxml/commit/9e95960cd6.patch

BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  python3-devel

# Some of the extras create a build dependency loop.
# - [cssselect] Requires cssselect BuildRequires lxml
# - [html5] Requires html5lib BuildRequires lxml
# - [htmlsoup] Requires beautifulsoup4 Requires lxml
# - [html_clean] Requires lxml-html-clean Requires lxml
# Hence we provide a bcond to disable the extras altogether.
# By default, the extras are disabled in RHEL, to avoid dependencies.
%bcond extras %{undefined rhel}

%global _description \
lxml is a Pythonic, mature binding for the libxml2 and libxslt libraries. It\
provides safe and convenient access to these libraries using the ElementTree It\
extends the ElementTree API significantly to offer support for XPath, RelaxNG,\
XML Schema, XSLT, C14N and much more.

%description %{_description}

%package -n     python3-lxml
Summary:        %{summary}
%if %{with extras}
Suggests:       python3-lxml+cssselect
Suggests:       python3-lxml+html5
Suggests:       python3-lxml+htmlsoup
Suggests:       python3-lxml+html_clean
%endif

%description -n python3-lxml %{_description}

Python 3 version.

%if %{with extras}
%pyproject_extras_subpkg -n python3-lxml cssselect html5 htmlsoup html_clean
%endif

%prep
%autosetup -n lxml-%{version} -p1
# Don't run html5lib tests --without extras
%{!?without_extras:rm src/lxml/html/tests/test_html5parser.py}

# Remove limit for version of Cython
sed -i "s/Cython.*/Cython/" requirements.txt
sed -i 's/"Cython.*",/"Cython",/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x source%{?with_extras:,cssselect,html5,htmlsoup,html_clean}

%build
# Remove pregenerated Cython C sources
# We need to do this after %%pyproject_buildrequires because setup.py errors
# without Cython and without the .c files.
find -type f -name '*.c' -print -delete >&2
export WITH_CYTHON=true
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lxml

%check
# The tests assume inplace build, so we copy the built library to source-dir.
# If not done that, Python can either import the tests or the extension modules, but not both.
cp -a build/lib.%{python3_platform}-*/* src/
# The options are: verbose, unit, functional
%{python3} test.py -vuf

%files -n python3-lxml -f %{pyproject_files}
%license doc/licenses/BSD.txt doc/licenses/elementtree.txt
%doc README.rst

%changelog
%autochangelog
