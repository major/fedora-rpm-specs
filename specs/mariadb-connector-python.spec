Name:           mariadb-connector-python
Version:        1.1.14
Release:        %autorelease
Summary:        MariaDB Connector for Python

# License breakdown
# LGPL-2.0-or-later - C source files and header files
# LGPL-2.1-or-later - source license file and readme
# CC-BY-3.0 - documentation/man pages
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND CC-BY-3.0
URL:            https://mariadb.com/docs/connectors/%{name}
Source0:        https://github.com/mariadb-corporation/%{name}/archive/refs/tags/v%{version}.tar.gz

# Patch disabling sphinx_markdown_builder, as it is only used to
# build md pages for the documentation. This builder is not a standalone
# package in Fedora and would require pip to install.
Patch0:         %{name}-disable-md-docs.patch

# Drop i686 support (https://fedoraproject.org/wiki/Changes/Noi686Repositories)
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  mariadb-connector-c-devel >= 3.3.1
# Required for man page generation
BuildRequires:  python3-sphinx
BuildRequires:  python3-myst-parser

# Provide python3-mariadb to match the importable module name,
# since our physical package name uses the upstream repository name.
%py_provides python3-mariadb

%generate_buildrequires
%pyproject_buildrequires

%description
MariaDB Connector/Python enables python programs to access MariaDB and MySQL
databases, using an API which is compliant with the Python DB API 2.0 (PEP-249).
It is written in C and uses MariaDB Connector/C client library for client server
communication.


%package test
Summary: Upstream integration test suite for MariaDB Connector for Python
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Requires:   python3-pytest

%py_provides python3-mariadb-test

%description test
Upstream integration test suite for MariaDB Connector/Python.
Requires a live MariaDB database connection and is executed via pytest.


%prep
%autosetup -p1
# Strip out the web-specific Marketo form macro to prevent Sphinx build warnings
sed -i '/% @marketo/d' docs/source/license.rst


%build
%pyproject_wheel

# Create a local build directory for documentation outputs
mkdir -p %{_builddir}/docs_out/

# Generate man pages
PYTHONPATH=$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots} \
sphinx-build -M man %{_builddir}/%{name}-%{version}/docs/source/ %{_builddir}/docs_out/


%install
%pyproject_install

# Install generated man pages into standard system locations
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 0644 %{_builddir}/docs_out/man/mariadbconnectorpython.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Install upstream test suite into python3_sitelib for the -test subpackage
mkdir -p %{buildroot}%{python3_sitelib}/%{name}/
cp -rp %{_builddir}/%{name}-%{version}/testing/test/ %{buildroot}%{python3_sitelib}/%{name}/

# Remove shebangs from test files as they are not meant to be run as standalone scripts
find %{buildroot}%{python3_sitelib}/%{name}/test/ -name "*.py" -exec sed -i '1{/^#!/d}' {} +

%check
# Ensure the module can be successfully imported in a clean environment. 
# The extensive upstream test suite requires a live database connection.
# The suite will be run in the CI pipeline.
%py3_check_import mariadb


%files 
%license LICENSE docs/source/license.rst
%doc docs/examples/basic01.py README.md
%{_mandir}/man1/%{name}.1*
%{python3_sitearch}/mariadb/
%{python3_sitearch}/mariadb-%{version}.dist-info/

%files test
%{python3_sitelib}/%{name}/

%changelog
%autochangelog
