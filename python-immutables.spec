%global srcname immutables

%bcond_without  tests

%global common_description %{expand:
An immutable mapping type for Python.

The underlying datastructure is a Hash Array Mapped Trie (HAMT) used in
Clojure, Scala, Haskell, and other functional languages. This implementation is
used in CPython 3.7 in the contextvars module (see PEP 550 and PEP 567 for more
details).

Immutable mappings based on HAMT have O(log N) performance for both set() and
get() operations, which is essentially O(1) for relatively small mappings.}


Name:           python-%{srcname}
Version:        0.18
Release:        3%{?dist}
Summary:        Immutable Collections
# The entire source code is ASL 2.0 except pythoncapi_compat.h which is 0BSD.
License:        ASL 2.0 and 0BSD
URL:            https://github.com/MagicStack/immutables
Source:         %pypi_source
BuildRequires:  gcc


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}

# don't install source files
sed -e '/include_package_data=/ s/True/False/' -i setup.py

# delete mypy tests to avoid that dependency
rm tests/conftest.py tests/test_mypy.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%if %{with tests}
%pytest --verbose
%else
%pyproject_check_import
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.18-2
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Carl George <carl@george.computer> - 0.18-1
- Latest upstream, resolves: rhbz#2092222
- Convert to pyproject macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.15-3
- Rebuilt for Python 3.10

* Wed Apr 21 2021 Carl George <carl@george.computer> - 0.15-2
- Include missing upstream license
- Disable package data in setup.py to avoid installing source files

* Wed Apr 21 2021 Carl George <carl@george.computer> - 0.15-1
- Initial package rhbz#1951868
