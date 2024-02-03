%bcond tests 1

%global _description %{expand:
The library implements the Trie data structure. The trie variable is a
dict-like object that can have Unicode keys of certain ranges and Python
objects as values.

In addition to implementing the mapping interface, the library tries to
facilitate finding the items for a given prefix, and vice versa, finding the
items whose keys are prefixes of a given string. As a common special case,
finding the longest-prefix item is also supported.}

Name:           python-datrie
Version:        0.8.2
Release:        %autorelease
Summary:        Super-fast, efficiently stored Trie for Python

License:        LGPL-2.1-or-later
URL:            https://github.com/pytries/datrie
Source:         %{pypi_source datrie}
# BUGFIX: Decode string based on byteorder of system
# https://github.com/pytries/datrie/pull/85
#
# Fixes:
#
# UnicodeDecodeError: 'utf32' codec can't decode bytes in position 0-3: code
# point not in range(0x110000)
# https://github.com/pytries/datrie/issues/38
Patch:          %{url}/pull/85.patch
# Fix AlphaMap definition in cdatrie.pxd
# Fixes failure to compile on GCC with -Werror=incompatible-pointer-types.
# https://github.com/pytries/datrie/pull/99
#
# Fixes:
#
# python-datrie: FTBFS in Fedora rawhide/f40
# https://bugzilla.redhat.com/show_bug.cgi?id=2261554
Patch:          %{url}/pull/99.patch

BuildRequires:  python3-devel

BuildRequires:  gcc-c++
BuildRequires:  libdatrie

%description %_description

%package -n python3-datrie
Summary:        %{summary}

%description -n python3-datrie %_description

%prep
%autosetup -p1 -n datrie-%{version}

# use system's libdatrie
sed -r -i -e 's@\.\./libdatrie/@@g' src/cdatrie.pxd

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l datrie

%check
%if %{with tests}
%tox
%endif

%files -n python3-datrie -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
