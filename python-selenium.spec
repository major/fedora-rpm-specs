%global upstream_name selenium

Name:          python-%{upstream_name}
Version:       3.14.0
Release:       10%{?dist}
Summary:       Python bindings for Selenium
License:       ASL 2.0
URL:           http://docs.seleniumhq.org/
Source0:       https://files.pythonhosted.org/packages/source/s/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildArch:     noarch

Patch1:        selenium-use-without-bundled-libs.patch

%description
The selenium package is used automate web browser interaction from Python.

Several browsers/drivers are supported (Firefox, Chrome, Internet Explorer,
PhantomJS), as well as the Remote protocol.


%package -n python3-%{upstream_name}
Summary:       Python bindings for Selenium
%{?python_provide:%python_provide python3-%{upstream_name}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires:      python3-rdflib
BuildArch:     noarch

%description -n python3-%{upstream_name}
The selenium package is used automate web browser interaction from Python.

Several browsers/drivers are supported (Firefox, Chrome, Internet Explorer,
PhantomJS), as well as the Remote protocol.

%prep
%setup -qn %{upstream_name}-%{version}
rm -r %{upstream_name}.egg-info

find . -type f -name "*.py" -exec sed -i '1{/^#!/d;}' {} \;

%patch1 -p2

%build
%py3_build

%install
%py3_install
rm -f %{buildroot}%{python3_sitelib}/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so
rm -f %{buildroot}%{python3_sitelib}/selenium/webdriver/firefox/x86/x_ignore_nofocus.so

%files -n python3-%{upstream_name}
%{python3_sitelib}/%{upstream_name}*
%doc README.rst

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.14.0-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 3.14.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 3.14.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Matthias Runge <mrunge@redhat.com> - 3.14.0-1
- update to 3.14 (rhbz#1595006)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-4
- Remove python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 3.12.0-2
- Rebuilt for Python 3.7

* Wed May 09 2018 Matthias Runge <mrunge@redhat.com> - 3.12.0-1
- update to 3.12.0 (rhbz#1431116)

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.7.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 3.7.0-2
- Update conditionals

* Mon Nov 27 2017 Lumír Balhar <lbalhar@redhat.com> - 3.7.0-1
- New upstream version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.53.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.53.6-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.53.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Matthias Runge <mrunge@redhat.com> - 2.53.6-1
- upstream version 2.53.6

* Wed Jun 15 2016 Matthias Runge <mrunge@redhat.com> - 2.53.5-1
- upstream version 2.53.5

* Fri Jun 10 2016 Matthias Runge <mrunge@redhat.com> - 2.53.4-1
- upstream version 2.53.4

* Wed May 18 2016 Matthias Runge <mrunge@redhat.com> - 2.53.2-1
- update to 2.53.2

* Fri Feb 12 2016 Matthias Runge <mrunge@redhat.com> - 2.52.0-1
- update to 2.52.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.49.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Matthias Runge <mrunge@redhat.com> - 2.49.0-1
- update to 2.49.0 (rhbz#1298407)
- spec cleanup, add py2 subpackage

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 2.48.0-2
- Rebuilt for Python3.5 rebuild

* Wed Oct 14 2015 Dhiru Kholia <dhiru@openwall.com> - 2.48.0-1
- update to 2.48.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 02 2015 Matthias Runge <mrunge@redhat.com> - 2.45.0-1
- update to 2.45.0 to fix compat issues with Firefox 36 (rhbz#1196922)

* Mon Feb 23 2015 Matthias Runge <mrunge@redhat.com> - 2.44.0-1
- update to 2.44.0

* Mon Oct 20 2014 Matthias Runge <mrunge@redhat.com> - 2.43.0-1
- update to 2.43.0
- correct deps for py3 version (rhbz#1116470)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Matthias Runge <mrunge@redhat.com> - 2.42.1-1
- rebuilt for python3.4 feature
- update to 2.42.1
- minor specs cleanup

* Fri Apr 04 2014 Dhiru Kholia <dhiru@openwall.com> - 2.41.0-1
- update to new upstream version

* Thu Feb 27 2014 Dhiru Kholia <dhiru@openwall.com> - 2.40.0-2
- fixed shebangs (BZ #1070125)

* Wed Feb 26 2014 Dhiru Kholia <dhiru@openwall.com> - 2.40.0-1
- initial version
