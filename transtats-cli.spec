%{?python_enable_dependency_generator}
%global module tscli
%global name transtats-cli
%global name_with_underscore transtats_cli
%global sum Transtats command line interface to query transtats server
%global project transtats

Name:           %{name}
Version:        0.6.0
Release:        5%{?dist}
Summary:        %{sum}
License:        Apache-2.0
URL:            https://github.com/%{project}/%{name}
Source0:        https://github.com/%{project}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Transtats command line interface to query transtats server.

%package -n python3-%{name}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-click
BuildRequires: python3-requests
BuildRequires: python3-mock
BuildRequires: python3-six
BuildRequires: python3-tabulate
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Transtats command line interface to query transtats server.


%prep
%autosetup -n %{name}-%{version}
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install
rm -fr %{buildroot}%{python3_sitelib}/tests


%check
%{__python3} setup.py test

%files -n python3-%{name}
%doc README.md transtats.conf Changelog.rst
%license LICENSE
%{_bindir}/%{project}
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{name_with_underscore}-%{version}-py%{python3_version}.egg-info
%{_mandir}/man1/transtats.1.gz
%{_datadir}/bash-completion/completions/transtats.bash

%changelog
* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.6.0-5
- Rebuilt for Python 3.12

* Wed Mar 29 2023 Sundeep Anand <suanand@redhat.com> - 0.6.0-4
- update license tag to as per SPDX identifiers

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 01 2022 Parag Nemade <pnemade AT redhat DOT com> - 0.6.0-1
- Update to 0.6.0 version (#2103082)

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Parag Nemade <pnemade AT redhat DOT com> - 0.5.0-1
- Update to 0.5.0 version (#1981761)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 09 2020 Parag Nemade <pnemade AT redhat DOT com> - 0.4.0-1
- Update to 0.4.0 version
- Drop BR: python3-flake8

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.8

* Sat Aug 03 2019 Parag Nemade <pnemade@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0 version

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.0-3
- Enable python dependency generator

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-2
- Subpackage python2-transtats-cli has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 04 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.2.0-1
- Update to 0.2.0 version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-2
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Sundeep Anand <suanand AT redhat DOT com> - 0.1.2-1
- Update transtats-cli to version 0.1.2, update 

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Jan Beran <jberan@redhat.com> - 0.1.1-4
- Fix of python3-transtats-cli requires both Python 2 and Python 3 (rhbz#1531568)

* Wed Nov 15 2017 Sundeep Anand <suanand AT redhat DOT com> - 0.1.1-3
- Update transtats-cli to version 0.1.1, update endpoints

* Wed Oct 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.0-4
- Fix Python 3 dependency from python2-transtats-cli
Resolves: rhbz#1495860

* Wed Sep 13 2017 Sundeep Anand <suanand AT redhat DOT com> - 0.1.0-3
- Add man page to transtats-cli

* Tue Sep 12 2017 Sundeep Anand <suanand AT redhat DOT com> - 0.1.0-2
- Update Spec file for py2 and py3

* Thu Sep 07 2017 Sundeep Anand <suanand AT redhat DOT com> - 0.1.0-1
- Initial RPM Packaging
