%bcond_without tests

%global pypi_name editdistance-s
%global modname editdistance_s

%global _description %{expand:
Fast implementation of the edit distance (Levenshtein distance).

This library simply implements Levenshtein distance with C++ and Cython.

The algorithm used in this library is proposed by Heikki Hyyrö,
"Explaining and extending the bit-parallel approximate string matching
algorithm of Myers", (2001).}

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        8%{?dist}
Summary:        Fast implementation of the Levenshtein distance

License:        MIT
URL:            https://github.com/asottile/%{pypi_name}
Source0:        https://github.com/asottile/%{pypi_name}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist Cython}
BuildRequires:  %{py3_dist cffi}
BuildRequires:  gcc-c++

%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
# compile the source file "bycython.cpp" manually. setup.py does not do that itself.
cythonize --inplace %{pypi_name}/bycython.pyx
%py3_build

%install
%py3_install

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python3_sitearch}
pytest-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE

%{python3_sitearch}/%{modname}.py
%{python3_sitearch}/__pycache__/%{modname}*
%{python3_sitearch}/_editdistance_s.abi3.so*
%{python3_sitearch}/%{modname}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.0-8
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.0.0-1
- Initial build
