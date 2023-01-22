%bcond_without tests

%global pypi_name datrie

%global _description %{expand:
The library implements the Trie data structure. The trie variable is a
dict-like object that can have Unicode keys of certain ranges and Python
objects as values.

In addition to implementing the mapping interface, the library tries to
facilitate finding the items for a given prefix, and vice versa, finding the
items whose keys are prefixes of a given string. As a common special case,
finding the longest-prefix item is also supported.}

Name:           python-%{pypi_name}
Version:        0.8.2
Release:        8%{?dist}
Summary:        Super-fast, efficiently stored Trie for Python

License:        LGPLv2
URL:            https://github.com/pytries/%{pypi_name}
Source0:        %{pypi_source}
# Patch to correctly decode on big/little endian systems
# https://github.com/pytries/datrie/issues/38
Patch0:			0001-BUG-Decode-string-based-on-byteorder-of-system.patch

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  gcc-c++
BuildRequires:  libdatrie
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist setuptools}

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-runner}
BuildRequires:  %{py3_dist hypothesis}
%endif

%py_provides python3-%{pypi_name}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

# use system's libdatrie
sed -i -e 's/..\/libdatrie\///g' src/cdatrie.pxd

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING

%{python3_sitearch}/datrie.cpython-*.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.2-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 21 2020 Aniket Pradhan <major AT fedoraproject DOT org> - 0.8.2-1
- Initial build
