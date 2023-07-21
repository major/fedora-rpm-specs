%{?python_enable_dependency_generator}
%global srcname fontdump
%global sum Dump the CSS and different formats of fonts for Google Fonts

Name:           %{srcname}
Version:        1.3.0
Release:        29%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/glasslion/fontdump
Source0:        %{pypi_source %{srcname}}

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-%{srcname}

%description
A command line tool to dump the CSS and different formats of fonts for Google
Fonts, so you can serve them on your local servers.

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:   python3-setuptools
BuildRequires:   python3dist(docopt)
BuildRequires:   python3dist(cssutils)
BuildRequires:   python3dist(requests)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
A command line tool to dump the CSS and different formats of fonts for Google
Fonts, so you can serve them on your local servers.

%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' fontdump/*.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%{_bindir}/%{srcname}

%files -n python3-%{srcname}
%doc PKG-INFO
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py3.*.egg-info

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.0-24
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Parag Nemade <pnemade AT redhat DOT com> - 1.3.0-21
- Add missing BR: python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-20
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-17
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-15
- Drop unneeded Requires

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Parag Nemade <pnemade AT redhat DOT com> - 1.3.0-13
- Resolves:rh#1631324: Remove python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-11
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Parag Nemade <pnemade AT redhat DOT com> - 1.3.0-8
- Add missing dependencies (rh#1458516)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 04 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.3.0-4
- Add python3 subpackage
- Follow new python and updated packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.3.0-1
- Update to new upstream 1.3.0 release

* Thu Oct 30 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.2.1-1
- Update to new upstream 1.2.1 release

* Thu Oct 30 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.2.0-2
- Add upstream LICENSE file (asked in review)
- Add Requires: python-setuptools (asked in review)

* Mon Sep 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.2.0-1
- Initial packaging

