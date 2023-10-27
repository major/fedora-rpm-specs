%global srcname cachetools

Name:           python-%{srcname}
Version:        5.3.2
Release:        1%{?dist}
Summary:        Extensible memoizing collections and decorators

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description\
This module provides various memoizing collections and decorators,\
including a variant of the Python 3 Standard Library @lru_cache\
function decorator.\
\
This module provides multiple cache implementations based on different\
cache algorithms, as well as decorators for easily memoizing function\
and method calls.\


%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/GCPGM34ZGEOVUHSBGZTRYR5XKHTIJ3T7/
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc CHANGELOG.rst PKG-INFO README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Wed Oct 25 2023 John Eckersberg <jeckersb@redhat.com> - 5.3.2-1
- New upstream release 5.3.2 (rhbz#2245953)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.3.1-3
- Rebuilt for Python 3.12

* Thu Jun 08 2023 Jan Friesse <jfriesse@redhat.com> - 5.3.1-2
- migrated to SPDX license

* Tue May 30 2023 John Eckersberg <jeckersb@redhat.com> - 5.3.1-1
- New upstream release 5.3.1 (rhbz#2210490)

* Mon Jan 23 2023 John Eckersberg <jeckersb@redhat.com> - 5.3.0-1
- New upstream release 5.3.0 (rhbz#2163023)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  9 2023 John Eckersberg <jeckersb@redhat.com> - 5.2.1-1
- New upstream release 5.2.1 (rhbz#2159140)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.2.0-2
- Rebuilt for Python 3.11

* Tue May 31 2022 John Eckersberg <jeckersb@redhat.com> - 5.2.0-1
- New upstream release 5.2.0 (rhbz#2091436)

* Mon May 16 2022 John Eckersberg <jeckersb@redhat.com> - 5.1.0-1
- New upstream release 5.1.0 (rhbz#2086346)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan  5 2022 John Eckersberg <jeckersb@redhat.com> - 5.0.0-1
- New upstream release 5.0.0 (rhbz#2034731)

* Thu Sep 30 2021 John Eckersberg <jeckersb@redhat.com> - 4.2.4-1
- New upstream release 4.2.4 (rhbz#2009321)

* Wed Sep 29 2021 John Eckersberg <jeckersb@redhat.com> - 4.2.3-1
- New upstream release 4.2.3 (rhbz#2009071)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.2.2-2
- Rebuilt for Python 3.10

* Wed Apr 28 2021 John Eckersberg <jeckersb@redhat.com> - 4.2.2-1
- New upstream release 4.2.2 (rhbz#1954318)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 John Eckersberg <jeckersb@redhat.com> - 4.2.1-1
- New upstream release 4.2.1

* Fri Dec 11 2020 John Eckersberg <jeckersb@redhat.com> - 4.2.0-1
- New upstream release 4.2.0 (rhbz#1906619)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 John Eckersberg <jeckersb@redhat.com> - 4.1.1-1
- New upstream release 4.1.1 (rhbz#1851765)

* Tue Jun 23 2020 John Eckersberg <jeckersb@redhat.com> - 4.1.0-3
- Add explicit BuildRequires on python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.9

* Wed Apr  8 2020 John Eckersberg <eck@redhat.com> - 4.1.0-1
- New upstream release 4.1.0 (rhbz#1822156)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 John Eckersberg <eck@redhat.com> - 4.0.0-1
- New upstream release 4.0.0 (rhbz#1783791)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 John Eckersberg <eck@redhat.com> - 3.1.1-1
- New upstream release 3.1.1 (rhbz#1713496)

* Mon Feb  4 2019 John Eckersberg <eck@redhat.com> - 3.1.0-3
- Remove python2 subpackage (rhbz#1671973)
- Modernize spec from latest packaging guidelines

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 John Eckersberg <eck@redhat.com> - 3.1.0-1
- New upstream release 3.1.0 (rhbz#1670584)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 John Eckersberg <eck@redhat.com> - 2.1.0-1
- New upstream release 2.1.0 (rhbz#1577555)

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Lumír Balhar <lbalhar@redhat.com> - 2.0.1-3
- Fix directory ownership

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0.1-2
- Python 2 binary package renamed to python2-cachetools
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Sat Aug 12 2017 John Eckersberg <eck@redhat.com> - 2.0.1-1
- New upstream release 2.0.1 (rhbz#1480818)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 John Eckersberg <eck@redhat.com> - 2.0.0-3
- Use python_version macros for egg-info files

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuild for Python 3.6

* Tue Oct  4 2016 John Eckersberg <eck@redhat.com> - 2.0.0-1
- New upstream release 2.0.0 (rhbz#1381392)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr  3 2016 John Eckersberg <eck@redhat.com> - 1.1.6-1
- New upstream release 1.1.6 (rhbz#1323394)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 26 2015 John Eckersberg <eck@redhat.com> - 1.1.5-1
- New upstream release 1.1.5 (rhbz#1275112)

* Sun Oct 25 2015 John Eckersberg <eck@redhat.com> - 1.1.4-1
- New upstream release 1.1.4 (rhbz#1275015)

* Wed Sep 16 2015 John Eckersberg <eck@redhat.com> - 1.1.3-1
- New upstream release 1.1.3 (rhbz#1263484)

* Tue Sep  8 2015 John Eckersberg <eck@redhat.com> - 1.1.1-1
- New upstream release 1.1.1 (rhbz#1260808)

* Tue Sep  1 2015 John Eckersberg <eck@redhat.com> - 1.1.0-1
- New upstream release 1.1.0 (rhbz#1258091)

* Tue Jul 21 2015 John Eckersberg <eck@redhat.com> - 1.0.3-1
- New upstream release 1.0.3

* Mon Jul 20 2015 John Eckersberg <eck@redhat.com> - 1.0.2-2
- Remove egg-info in %%setup
- Install license via %%license instead of %%doc
- Don't rm -rf $RPM_BUILD_ROOT at the beginning of %%install
- Removed defines for __python2, python2_sitelib, and python2_sitearch
- Be more explicit in %%files

* Fri Jun 19 2015 John Eckersberg <eck@redhat.com> - 1.0.2-1
- Initial package
