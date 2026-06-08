%global srcname zict

Name:           python-%{srcname}
Version:        3.0.0
Release:        %autorelease
Summary:        Mutable mapping tools

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source:         %pypi_source %{srcname}
# Fix hang in test_stress_different_keys_threadsafe.
Patch:          https://github.com/dask/zict/pull/108.patch

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-repeat)
BuildRequires:  python3dist(pytest-timeout)
# lmdb is broken with python 3.13:
# https://bugzilla.redhat.com/show_bug.cgi?id=2259530
# https://github.com/jnwatson/py-lmdb/issues/362
#BuildRequires:  python3dist(lmdb)
BuildRequires:  python3dist(psutil)

%global _description %{expand:
Zict builds abstract MutableMapping classes that consume and build on other
MutableMappings. They can be composed with each other to form intuitive
interfaces over complex storage systems policies.

Data can be stored in-memory, on disk, in archive files, etc., managed with
different policies like LRU, and transformed when arriving or departing the
dictionary.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p1
# drop LMDB bits till LMDB is buildable again
rm -f zict/lmdb.py
sed -i "/lmdb/d" zict/__init__.py
rm -f zict/tests/test_lmdb.py


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} -ra

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
