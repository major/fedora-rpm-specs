%global package_name	psycopg
%global src_name	%{package_name}3
%global _description %{expand:
Psycopg 3 is a PostgreSQL database adapter for the Python programming language.
Psycopg 3 presents a familiar interface for everyone who has used Psycopg 2 or
any other DB-API 2.0 database adapter, but allows to use more modern PostgreSQL
and Python features.}

Name:		python-%{src_name}
Version:	3.0.16
Release:	2%{?dist}
Summary:	Psycopg 3 is a modern implementation of a PostgreSQL adapter for Python

License:	LGPLv3
URL:		https://www.psycopg.org/%{src_name}/
Source0:	https://github.com/%{package_name}/%{package_name}/archive/refs/tags/%{version}.tar.gz

# Patch remove packages not availible in Fedora (pproxy)
# and removes specific version and code coverage
# Remove specific version to ensure build on
# Fedora 35 (pytest, pytest-randomly) + toml
Patch0: python-psycopg3-3.0.16-setup.patch
Patch1: python-psycopg3-3.0.16-toml.patch

BuildRequires:	python3-devel

# Required for running tests
BuildRequires:	libpq

BuildArch:	noarch

%description %_description

%package -n python3-%{src_name}
Requires:	libpq
Summary:	%{SUMMARY}

%description -n python3-%{src_name} %_description

%prep
%autosetup -p3 -n %{package_name}-%{version}/%{package_name}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{package_name}

# Prepare the test folder for pytest
pushd ../tests/

# Remove failing tests
# The DNS package is not installed and therefore the test 
# will not run. This is intented as there is no network in mock
rm test_typing.py test_module.py
# Remove all files in pool/ folder except the fix_pool.py.
# The pool/fix_pool.py is in conftest.py as plugin
find pool/ ! -name 'fix_pool.py' -type f -exec rm -f {} +

popd

%check

%if 0%{?fedora} > 36
    # Launchs tests with correctly set pytest-asyncio which
    # corrects the breaking change caused by the version
    %pytest ../tests/ --asyncio-mode=auto
%else
    # Python 36 and lower do not have the version which breaks 
    # the process available yet
    %pytest ../tests/
%endif


%files -n python3-%{src_name} -f %{pyproject_files}
%doc ../README.rst
%license LICENSE.txt


%changelog
* Fri Oct 14 2022 Ondrej Sloup <osloup@redhat.com> - 3.0.16-2
- Release bump

* Thu Aug 04 2022 Ondrej Sloup <osloup@redhat.com> - 3.0.16-1
- Rebase to the latest upstream version
- Create patch files instead of sed
- Fix release numbering

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.11-3
- Rebuilt for Python 3.11

* Fri May 13 2022 Ondrej Sloup <osloup@redhat.com> - 3.0.11-2
- Add support for Fedora 35 and 36
- Remove spaces at the end of the file
- Pray that Friday 13 will not break anything

* Thu Apr 28 2022 Ondrej Sloup <osloup@redhat.com> - 3.0.11-1
- Create package from git source (#2079251)