# Fedora spec file for mysql-connector-python
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

ExcludeArch: %{ix86}

# Tests only run on manual build --with tests
%global with_tests   %{?_with_tests:1}%{!?_with_tests:0}

# Build the X DevAPI C extension (_mysqlxpb) with system protobuf
%global with_mysqlxpb 1

Name:           mysql-connector-python
Version:        26.7.0
Release:        %autorelease
Summary:        MySQL Connector for Python 3
License:        GPL-2.0-only WITH Universal-FOSS-exception-1.0
URL:            https://dev.mysql.com/doc/connector-python/en/

# Original URL: https://dev.mysql.com/get/Downloads/Connector-python/%%{name}-%%{version}-src.tar.gz
# Fonts in mysqlx-connector-python/docs/ are under restrictive copyright
# (FontAwesome, Roboto Slab, Lato) and must be stripped before shipping.
# Use 'generate-modified-sources.sh' to create the font-free tarball.
Source0:        %{name}-%{version}-src-without-fonts.tar.gz

# Remove RPATH injection into C extensions — Fedora uses system library paths
Patch0:         %{name}-rpath.patch
# Fix sphinx conf.py version import for the split source layout
Patch1:         %{name}-docs-import.patch
# Guard removed ssl.PROTOCOL_TLSv1* constants with hasattr() (Python 3.15, PEP 644)
Patch2:         %{name}-python315-ssl.patch
# Adapt mysqlx C extension and protobuf bindings for system protobuf 6.x
Patch3:         %{name}-system-protobuf.patch
# Fix test_errors for Python 3.15 format-string message change; skip flaky test_shutdown
Patch4:         %{name}-test-fixes.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mysql-devel
BuildRequires:  python3-protobuf
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxcontrib-jquery

%if %{with_mysqlxpb}
BuildRequires:  protobuf-compiler >= 4.25.3
BuildRequires:  protobuf-devel >= 4.25.3
%endif

%if %{with_tests}
BuildRequires:  mysql-server
BuildRequires:  openssl
%endif

%generate_buildrequires
%pyproject_buildrequires -d mysql-connector-python
%pyproject_buildrequires -d mysqlx-connector-python

%global _description %{expand:
MySQL Connector/Python is implementing the MySQL Client/Server protocol
completely in Python. No MySQL libraries are needed, and no compilation
is necessary to run this Python DB API v2.0 compliant driver.

Documentation: https://dev.mysql.com/doc/connector-python/en/}

%description %_description

%package -n mysql-connector-python3
Summary:        MySQL Connector for Python 3
%{?python_provide:%python_provide python3-mysql-connector}

%description -n mysql-connector-python3 %_description


%prep
%autosetup -p1 -n %{name}-%{version}-src
chmod -x mysql-connector-python/examples/*py

%if %{with_tests}
# Regenerate expired SSL test certificates (upstream ships with 365-day validity)
bash mysql-connector-python/tests/data/ssl/generate.sh \
     mysql-connector-python/tests/data/ssl
%endif


%build
export MYSQL_CAPI=%{_prefix}
export LDFLAGS="$LDFLAGS -L%{_libdir}/mysql"

%if %{with_mysqlxpb}
export MYSQLXPB_PROTOBUF=%{_prefix}
export MYSQLXPB_PROTOBUF_INCLUDE_DIR=%{_includedir}
export MYSQLXPB_PROTOBUF_LIB_DIR=%{_libdir}
export MYSQLXPB_PROTOC="%{_bindir}/protoc"
export PROTOBUF_INCLUDE_DIR=%{_includedir}
export PROTOBUF_LIB_DIR=%{_libdir}
export PROTOC="%{_bindir}/protoc"
%endif

%pyproject_wheel -d mysql-connector-python
%pyproject_wheel -d mysqlx-connector-python

# Build man pages from the mysqlx sphinx docs
export CPY_BUILD_DIR=$PWD/mysqlx-connector-python/lib
pushd mysqlx-connector-python/docs/mysqlx
%python3 conf.py
make man BUILDDIR=%{_builddir}
popd


%install
%pyproject_install

# pyproject_install may place pure Python files in sitelib while
# C extensions go to sitearch; consolidate everything into sitearch
if [ "%{python3_sitelib}" != "%{python3_sitearch}" ] && \
   [ -d "%{buildroot}%{python3_sitelib}" ]; then
    cp -a %{buildroot}%{python3_sitelib}/* %{buildroot}%{python3_sitearch}/
    rm -r %{buildroot}%{python3_sitelib}
fi

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{_builddir}/man/mysqlxconnectorpythondevapireference.1 \
    %{buildroot}%{_mandir}/man1/%{name}3.1


%check
%py3_check_import mysql mysqlx
%if %{with_tests}
pushd mysql-connector-python
%python3 unittests.py --with-mysql=%{_prefix} --unix-socket=/tmp --verbosity=1
popd
%else
: test suite disabled, pass '--with tests' to enable
%endif


%files -n mysql-connector-python3
%doc CHANGES.txt README.rst README.txt CONTRIBUTING.md SECURITY.md
%doc mysql-connector-python/examples
%license LICENSE.txt
%{python3_sitearch}/mysql/
%{python3_sitearch}/mysqlx/
%{python3_sitearch}/_mysql_connector%{python3_ext_suffix}
%if %{with_mysqlxpb}
%{python3_sitearch}/_mysqlxpb%{python3_ext_suffix}
%endif
%{python3_sitearch}/mysql_connector_python-%{version}.dist-info/
%{python3_sitearch}/mysqlx_connector_python-%{version}.dist-info/
%{_mandir}/man1/%{name}3.1.*

%changelog
%autochangelog
