%global pypi_name tinydb
%global author msiemens
%global pypi_hash 78f24df0fec08f0fb92fc4b4758adcab780660caa8c3f94c2e175eb7e2ba

Name:           python-%{pypi_name}
Version:        4.7.1
Release:        3%{?dist}
Summary:        TinyDB is a tiny, document oriented database

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/32/ed/%{pypi_hash}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pyyaml
BuildRequires:  python%{python3_pkgversion}-pytest-runner
BuildRequires:  python%{python3_pkgversion}-pytest-cov

%description
TinyDB is a lightweight document oriented database optimized for your happiness


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
TinyDB is a lightweight document oriented database optimized for your happiness

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}/%{python3_sitelib}/tests

%check
%py3_check_import %{pypi_name}

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.7.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 16 2023 Sundeep Anand <suanand@redhat.com> - 4.7.1-1
- Update to latest version 4.7.1 (rhbz#2160948)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.7.0-2
- Rebuilt for Python 3.11

* Mon Feb 21 2022 Sundeep Anand <suanand@redhat.com> - 4.7.0-1
- Update to latest version 4.7.0 (rhbz#2041565)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Sundeep Anand <suanand@redhat.com> - 4.5.2-1
- Update to latest version 4.5.2 (rhbz#1983279)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 28 2021 Sundeep Anand <suanand@redhat.com> - 4.5.0-1
- Update to latest version 4.5.0 (rhbz#1976497)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.4.0-2
- Rebuilt for Python 3.10

* Fri Feb 12 2021 Sundeep Anand <suanand@redhat.com> - 4.4.0-1
- Update to latest version 4.4.0 (rhbz#1927906)

* Wed Nov 18 2020 Sundeep Anand <suanand@redhat.com> - 4.3.0-1
- Update to latest version 4.3.0 (rhbz#1897837)

* Sun Oct  4 2020 Sundeep Anand <suanand@redhat.com> - 4.2.0-1
- Update to latest version 4.2.0 (rhbz#1884924)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Sundeep Anand <suanand@redhat.com> - 4.1.1-1
- Update to latest version 4.1.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.15.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Sundeep Anand <suanand@redhat.com> - 3.15.2-1
- Update to latest version 3.15.2 (bz1784964)

* Wed Oct 30 2019 Sundeep Anand <suanand@redhat.com> - 3.15.1-1
- Update to latest version 3.15.1

* Mon Oct 14 2019 Sundeep Anand <suanand@redhat.com> - 3.15.0-1
- Update to latest version 3.15.0

* Mon Sep 16 2019 Sundeep Anand <suanand@redhat.com> - 3.14.2-1
- Update to latest version 3.14.2

* Mon Mar 25 2019 Sundeep Anand <suanand@redhat.com> - 3.13.0-1
- Update to latest version 3.13.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.10.0-2
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Jul 23 2018 Sundeep Anand <suanand@redhat.com> - 3.10.0-1
- Update to latest version 3.10.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.9.0-2
- Rebuilt for Python 3.7


* Wed Apr 25 2018 Sundeep Anand <suanand@redhat.com> - 3.9.0-1
- Update to latest version

* Wed Mar 28 2018 Sundeep Anand <suanand@redhat.com> - 3.8.1-1
- Update to latest version

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.8.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Sundeep Anand <suanand@redhat.com> - 3.7.0-1
- Update to latest version

* Mon Oct 23 2017 Sundeep Anand <suanand@redhat.com> - 3.6.0-1
- Update to latest version

* Tue Sep 05 2017 Sundeep Anand <suanand@redhat.com> - 3.5.0-1
- Update to latest version

* Thu Aug 24 2017 Sundeep Anand <suanand@redhat.com> - 3.4.1-1
- Update to latest version

* Thu Jun 08 2017 Sundeep Anand <suanand@redhat.com> - 3.3.0-1
- Update to latest version

* Wed Apr 26 2017 Sundeep Anand <suanand@redhat.com> - 3.2.3-1
- Update to latest version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.2.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jul 05 2016 Sundeep Anand <suanand@redhat.com> - 3.2.1-1
- Update to latest version

* Mon Jun 20 2016 Sundeep Anand <suanand@redhat.com> - 3.2.0-1
- Update to latest version

* Wed Feb 10 2016 Sundeep Anand <suanand@redhat.com> - 3.1.2-3
- EPEL specific changes

* Tue Feb 09 2016 Sundeep Anand <suanand@redhat.com> - 3.1.2-2
- Include docs directory.

* Tue Feb 02 2016 Sundeep Anand <suanand@redhat.com> - 3.1.2-1
- Initial RPM Package.

