%global srcname ijson

Name:           python-%{srcname}
Version:        3.1.4
Release:        6%{?dist}
Summary:        Iterative JSON parser

License:        BSD
URL:            https://github.com/ICRAR/ijson
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

Recommends:     yajl
Recommends:     python3dist(cffi)

BuildRequires:  python3dist(setuptools)

%global _description %{expand:
Iterative JSON parser with standard Python iterator interfaces.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

# Test dependencies
BuildRequires:  python3dist(cffi)
BuildRequires:  yajl
BuildRequires:  yajl-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

# Disable tests for unsupported configurations.
sed -i "s/\['python', 'yajl', 'yajl2', 'yajl2_cffi', 'yajl2_c']/\['python', 'yajl2', 'yajl2_cffi']/" test/test_base.py

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:$PWD %{python3} -m unittest discover

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.4-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Kai A. Hiller <V02460@gmail.com> - 3.1.4-1
- Initial package.
