%global srcname persist-queue

Name:          python-%{srcname}
Version:       1.1.0
Release:       %autorelease
Summary:       A thread-safe disk based persistent queue in Python

License:       BSD-3-Clause
URL:           https://github.com/peter-wangxu/persist-queue
Source:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch

BuildRequires: python3-devel
# Without this I get errors like
#E   ModuleNotFoundError: No module named 'module_name'
BuildRequires: python3dist(aiofiles)
BuildRequires: python3dist(aiosqlite)
BuildRequires: python3dist(cbor2)
BuildRequires: python3dist(msgpack)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-asyncio)

%global _description %{expand:
persist-queue implements file-based and SQLite3-based persistent queues for
Python. It provides thread-safe, disk-based queue implementations that survive
process crashes and restarts.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l persistqueue
# Disabled due to missing dbutils and pymsql dependencies.
#%%pyproject_extras_subpkg -n python3-%%{srcname} extra
%pyproject_extras_subpkg -n python3-%{srcname} async

%check
# test_mysqlqueue.py requires dbutils, which is unavailable and only an extra requirement.
%pytest --ignore=persistqueue/tests/test_mysqlqueue.py 

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst docs/ASYNC_IMPLEMENTATION.md docs/async_api.md

%changelog
%autochangelog
