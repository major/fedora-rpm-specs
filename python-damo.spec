%bcond_without tests

# at least one test fails on Koji
# use --with all_tests on local builds to make sure test suite is still good
%bcond_with all_tests

%global srcname damo
%global _description %{expand:
damo is a user space tool for DAMON. Using this, you can monitor the data access
patterns of your system or workloads and make data access-aware memory
management optimizations.}

Name:           python-%{srcname}
Version:        2.1.9
Release:        %autorelease
Summary:        Data Access Monitoring Operator

License:        GPL-2.0-only
URL:            https://github.com/awslabs/damo
# PyPI source does not contain tests
# Source:         %%pypi_source
Source:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
# some tests assume 64-bit and fail on ix86
ExclusiveArch:  x86_64 aarch64 ppc64le s390x noarch

%description %{_description}


%package -n %{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pytest)
%endif

%description -n %{srcname} %{_description}


%prep
%autosetup -p 1 -n %{srcname}-%{version}


# from packaging/build.sh
for f in pyproject.toml setup.py; do
  cp -p packaging/$f .
done

mkdir -p src/damo
cp -p *.py src/damo/
# this should not get packaged!
rm src/damo/setup.py
cp -p damo src/damo/damo.py
# remove shebang from the newly copied damo.py
sed -i '1{\@^#!/usr/bin/env python@d}' src/damo/damo.py
touch -r damo src/damo/damo.py
touch -r damo src/damo/__init__.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pyproject_check_import
%if %{with tests}
%if %{with all_tests}
%pytest
%else
# get_damon_dir does not work on Koji
# "read failed (reading /sys/kernel/debug/damon/mk_contexts failed ([Errno 22] Invalid argument))"
%pytest -k "not test_files_content_to_kdamonds"
%endif
%endif


%files -n %{srcname} -f %{pyproject_files}
%license COPYING
%doc CONTRIBUTING README.md SECURITY.md USAGE.md release_note
%{_bindir}/%{srcname}


%changelog
%autochangelog
