%global pypi_name kaitaistruct

%global desc Kaitai Struct is a declarative language used to describe various binary data\
structures, laid out in files or in memory: i.e. binary file formats, network\
stream packet formats, etc.\
\
It is similar to Python’s Construct 2.9 but it is language-agnostic. The format\
description is done in YAML-based .ksy format, which then can be compiled into\
a wide range of target languages.

Name: python-%{pypi_name}
Version: 0.10
Release: 2%{?dist}
Summary: A new way to develop parsers for binary structures
License: MIT
URL: https://kaitai.io
Source0: %{pypi_source}
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel

%description -n python3-%{pypi_name}
%{desc}

%prep
%setup -q -n %{pypi_name}-%{version}
rm -r %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}.cpython-%{python3_version_nodots}*.pyc

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Dominik Mierzejewski <dominik@greysector.net> 0.10-1
- update to 0.10 (#2105607)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Dominik Mierzejewski <dominik@greysector.net> 0.9-1
- update to 0.9 (#1888860)
- BuildRequire setuptools explicitly

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Dominik Mierzejewski <dominik@greysector.net> 0.8-2
- use pypi_source macro
- drop initial newline from description

* Fri Jan 04 2019 Dominik Mierzejewski <dominik@greysector.net> 0.8-1
- initial build
