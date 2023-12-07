%bcond_without  tests

Name:           python-immutables
Version:        0.20
Release:        %autorelease
Summary:        Immutable Collections
# The entire source code is Apache-2.0, except pythoncapi_compat.h, which is
# 0BSD. While this file is unbundled, it is a header-only library; its entire
# contents are compiled into the binary RPM, and packaging guidelines treat it
# as a static library. Its license therefore contributes to the license of the
# binary RPM. See discussion in
# https://src.fedoraproject.org/rpms/python-immutables/pull-request/2, and the
# (Rust-specific but relevant) policy
# https://docs.fedoraproject.org/en-US/legal/license-field/#_rust_packages.
License:        Apache-2.0 AND 0BSD
URL:            https://github.com/MagicStack/immutables
Source:         %{pypi_source immutables}

BuildRequires:  gcc

%global common_description %{expand:
An immutable mapping type for Python.

The underlying datastructure is a Hash Array Mapped Trie (HAMT) used in
Clojure, Scala, Haskell, and other functional languages. This implementation is
used in CPython 3.7 in the contextvars module (see PEP 550 and PEP 567 for more
details).

Immutable mappings based on HAMT have O(log N) performance for both set() and
get() operations, which is essentially O(1) for relatively small mappings.}


%description %{common_description}


%package -n python3-immutables
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  pythoncapi-compat-static

%description -n python3-immutables %{common_description}


%prep
%autosetup -n immutables-%{version} -p 1

# don't install source files
sed -e '/include_package_data=/ s/True/False/' -i setup.py

# delete mypy tests to avoid that dependency
rm tests/conftest.py tests/test_mypy.py

# remove bundled pythoncapi-compat
rm -vf immutables/pythoncapi_compat.h


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files immutables


%check
%if %{with tests}
%pytest --verbose
%else
%pyproject_check_import
%endif


%files -n python3-immutables -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
