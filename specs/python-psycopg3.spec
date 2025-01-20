%global package_name	psycopg
%global src_name		%{package_name}3

%global pool_version	3.2.2
%global pool_name		pool-%{pool_version}

%if 0%{?fedora}
%bcond_without			cython
%bcond_without			pypy
%bcond_without			tests
%else
# EL9 does not have pypy, and cython build failed
%bcond_with			cython
%bcond_with			pypy
# postgresql-test-rpm-macros built but not published in CRB
# https://kojihub.stream.centos.org/koji/buildinfo?buildID=59955
# requested in https://issues.redhat.com/browse/RHEL-32610
%bcond_with			tests
%endif

Name:		python-%{src_name}
Version:	3.2.1
Release:	4%{?dist}
Summary:	Psycopg 3 is a modern implementation of a PostgreSQL adapter for Python

License:	LGPL-3.0-only
URL:		https://www.psycopg.org/%{src_name}/
Source0:	https://github.com/%{package_name}/%{package_name}/archive/refs/tags/%{version}.tar.gz
Source1:	https://github.com/%{package_name}/%{package_name}/archive/refs/tags/%{pool_name}.tar.gz

%if %{without cython}
BuildArch:		noarch
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:	%{ix86}

BuildRequires:	python3-devel
BuildRequires:	libpq openssl
BuildRequires:	postgresql-static postgresql-server-devel
BuildRequires:	python3-pip python3-wheel python3-tomli
%if %{with pypy}
BuildRequires:	pypy
%endif

%if %{with tests}
# Required for running tests
BuildRequires:	postgresql-test-rpm-macros
BuildRequires:	python3-anyio python3-mypy pytest python3-pytest-cov python3-pytest-randomly
%endif

%if %{with cython}
# Required for Cython
BuildRequires:	cython gcc
%endif

# Runtime dependency
# https://github.com/psycopg/psycopg/blob/master/README.rst
Requires:		libpq

%description
Psycopg 3 is a PostgreSQL database adapter for the Python programming language.
Psycopg 3 presents a familiar interface for everyone who has used Psycopg 2 or
any other DB-API 2.0 database adapter, but allows to use more modern PostgreSQL
and Python features.

%package -n python3-%{src_name}

Summary:		%{Summary}
BuildArch:		noarch
Requires:		libpq

%description -n python3-%{src_name}
%{description}

%package -n python3-%{src_name}_pool
Summary:		Connection pooling for Psycopg 3
Requires:		python-%{src_name}
BuildArch:		noarch
Requires:		libpq

%description -n python3-%{src_name}_pool
This package contains the pooling functionality for Psycopg 3.

%if %{with cython}
%package -n python3-%{src_name}_c
Summary:		C extensions for Psycopg 3
Requires:		libpq

%description -n python3-%{src_name}_c
This package contains the C extensions for enhanced performance in Psycopg 3.
%endif

%prep
%autosetup -p1 -n %{package_name}-%{version}

# Remove old psycopg_pool folder
rm -rf psycopg_pool/*

# Unpack upstream psycopg_pool
tar -xzf %{SOURCE1} -C psycopg_pool/ --strip-components=2 %{package_name}-%{pool_name}/psycopg_pool/

%build
pushd psycopg
%pyproject_wheel
popd

pushd psycopg_pool
%pyproject_wheel
popd

%if %{with cython}
pushd psycopg_c
%pyproject_wheel
popd
%endif

%install
pushd psycopg
%pyproject_install
popd

pushd psycopg_pool
%pyproject_install
popd

%if %{with cython}
pushd psycopg_c
%pyproject_install
popd
%endif

%if %{with tests}
%check
export PGTESTS_LOCALE=C.UTF-8
%postgresql_tests_run

export PSYCOPG_TEST_DSN="host=$PGHOST port=$PGPORT dbname=${PGTESTS_DATABASES##*:} sslmode=disable"

# Remove tests that need to use internet or specific settings
%pytest tests/ -k "not (\
		test_typing or \
		test_module or \
		test_conninfo_attempts_async or \
		test_connection_async or \
		test_connection or \
		test_conninfo_attempts or \
		test_pool_async or \
		test_null_pool_async or \
		test_pool or \
		test_null_pool or \
		test_client_cursor_async or \
		test_cursor_async or \
		sched_async or \
		test_pipeline_async or \
		test_copy_async or \
		test_pipeline or \
		test_multirange or \
		test_datetime or \
		test_range or \
		test_string or \
		test_notify or \
		test_waiting\
)"
%endif


%files -n python3-%{src_name}
%{python3_sitelib}/psycopg/
%{python3_sitelib}/psycopg-%{version}.dist-info/
%license psycopg/LICENSE.txt
%doc psycopg/README.rst

%files -n python3-%{src_name}_pool
%{python3_sitelib}/psycopg_pool/
%{python3_sitelib}/psycopg_pool-%{pool_version}.dist-info/
%license psycopg_pool/LICENSE.txt
%doc psycopg_pool/README.rst

%if %{with cython}
%files -n python3-%{src_name}_c
%{python3_sitearch}/psycopg_c/
%{python3_sitearch}/psycopg_c-%{version}.dist-info/
%license psycopg_c/LICENSE.txt
%doc psycopg_c/README.rst
%endif

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jul 30 2024 Ondrej Sloup <osloup@redhat.com> - 3.2.1-3
- Added specific tests to skip (test_pipeline) as it fails on s390x (rhbz#2301198)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Ondrej Sloup <osloup@redhat.com> - 3.2.1-1
- Rebase to the latest upstream version (rhbz#2295550)
- Added specific tests to skip (test_pipeline, test_multirange, test_datetime, test_range, test_string, test_notify)

* Tue Jun 11 2024 Python Maint <python-maint@redhat.com> - 3.1.19-2
- Rebuilt for Python 3.13

* Mon Jun 10 2024 Ondrej Sloup <osloup@redhat.com> - 3.1.19-1
- Rebase to the latest upstream version

* Mon Jun 10 2024 Ondrej Sloup <osloup@redhat.com> - 3.1.18-6
- Correct Requires libpq everywhere (rhbz#2266555)

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 3.1.18-5
- Rebuilt for Python 3.13

* Wed Apr 17 2024 Michel Lind <salimma@fedoraproject.org> - 3.1.18-4
- Make Cython and PyPy conditional, and only enable on Fedora for now
- Disable tests on non-Fedora builds due to missing dependencies

* Wed Apr 03 2024 Ondrej Sloup <osloup@redhat.com> -  3.1.18-3
- Confirm libpq require for (rhbz#2266555)
- Fix architectures for specific subpackages (rhbz#2268354)

* Tue Apr 02 2024 Sandro Mani <manisandro@gmail.com> - 3.1.18-2
- Add Requires: libpq (#2266555)

* Wed Jan 31 2024 Ondrej Sloup <osloup@redhat.com> -  3.1.18-1
- Add Cython version of psycopg and psycopg_pool as subpackages
- Rebase to the latest upstream version (rhbz#2250316)
- Update license tag to the SPDX format (LGPL-3.0-only) 

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 27 2023 Ondrej Sloup <osloup@redhat.com> -  3.1.12-1
- Rebase to the latest upstream version (rhbz#2240358)

* Mon Aug 07 2023 Ondrej Sloup <osloup@redhat.com> -  3.1.10-1
- Rebase to the latest upstream version (rhbz#2229392)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 3.1.9-2
- Rebuilt for Python 3.12

* Fri May 05 2023 Ondrej Sloup <osloup@redhat.com> -  3.1.9-1
- Rebase to the latest upstream version (rhbz#2192620)
- Remove the version for anyio from setup.py

* Fri Jan 20 2023 Ondrej Sloup <osloup@redhat.com>  - 3.1.8-1
- Rebase to the latest upstream version (rhbz#2161450)

* Wed Dec 21 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 3.1.7-1
- Release bump rhbz#2155285
- Enable postgresql server for tests

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
