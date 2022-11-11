%global pypi_name certbot-apache

Name:       python-%{pypi_name}
Version:    1.32.0
Release:    1%{?dist}
Summary:    The apache plugin for certbot

License:    Apache-2.0
URL:        https://pypi.python.org/pypi/certbot-apache
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
Source2:        https://dl.eff.org/certbot.pub

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires: python3-acme >= %{version}
BuildRequires: python3-augeas
BuildRequires: python3-certbot >= %{version}
BuildRequires: python3-pytest
BuildRequires: python3-setuptools >= 41.6.0

# Used to verify OpenPGP signature
BuildRequires:  gnupg2

%description
Plugin for certbot that allows for automatic configuration of apache

%package -n python3-%{pypi_name}
Summary:     The apache plugin for certbot

# Provide the name users expect as a certbot plugin
%if 0%{?fedora} || (0%{?rhel} && 0%{?rhel} >= 8)
Provides:      %{pypi_name} = %{version}-%{release}
%endif

Requires:      mod_ssl
# Recommend the CLI as that will be the interface most use
Recommends:    certbot >= %{version}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Plugin for certbot that allows for automatic configuration of apache

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%check
%{__python3} -m pytest


%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/certbot_apache
%{python3_sitelib}/certbot_apache-%{version}*.egg-info

%changelog
* Wed Nov 09 2022 Nick Bebout <nb@fedoraproject.org> - 1.32.0-1
- Update to 1.32.0

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.30.0-1
- Update to 1.30.0 rhbz#2125046

* Wed Aug 10 2022 Jonathan Wright <jonathan@almalinux.org> - 1.29.0-1
- Update to 1.29.0 (#2094616)
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.27.0-2
- Rebuilt for Python 3.11

* Wed May 04 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.27.0-1
- Update to 1.27.0 (#2081520)

* Thu Apr 07 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0 (#2064916)

* Mon Mar 14 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.24.0-1
- Update to 1.24.0 (#2052126)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.22.0-1
- Update to 1.22.0 (#2020070)

* Tue Oct 05 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0 (#2010953)

* Fri Sep 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0 (#2002041)

* Wed Aug 04 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0 (#1966770)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.14.0-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0 (#1946805)

* Tue Mar 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0 (#1934811)

* Tue Feb 2 2021 Nick Bebout <nb@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0 (#1913018)

* Thu Dec  3 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#1904184)

* Wed Dec 02 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0 (#1903311)

* Thu Oct 08 2020 Nick Bebout <nb@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Tue Oct 06 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Aug 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#1866069)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1854617)

* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843202)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831915)

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809791)

* Sun Mar 01 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-2
- remove runtime dependencies on mock, pytest

* Thu Feb 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (#1791074)

* Sun Feb 02 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.0-2
- add missing sources

* Sat Feb 01 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0 (#1791074)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769106)

* Wed Dec 04 2019 Eli Young <elyscape@gmail.com> - 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757576)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748614)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742578)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717678)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686185) (#1706298) (#1701018)

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673770)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669314)

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1627570)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600293)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591032)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588220)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-2
- Remove unnecessary patch

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574151)

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563900)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2 (#1558281)

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0 (#1552954)

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.21.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Eli Young <elyscape@gmail.com> - 0.21.1-1
- Update to 0.21.1 (#1535996)

* Wed Dec 20 2017 Eli Young <elyscape@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Fri Oct 06 2017 Eli Young <elyscape@gmail.com> - 0.19.0-1
- Update to 0.19.0 (bz#1499369)

* Fri Oct 6 2017 Eli Young <elyscape@gmail.com> - 0.18.2-2
- Fix condition on provides for Fedora pre-26 - bz#1497314

* Mon Oct 2 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-2
- Fix provides - bz#1497314

* Fri Sep 22 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2

* Sun Sep 10 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Fri May 12 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.0-1
- Update to 0.14.0

* Wed Apr 19 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-1
- update to 0.13.0
* Fri Mar 03 2017 James Hogarth <james.hogarth@gmail.com> - 0.12.0-1
- update to 0.12.0
- add python3 compatibility
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Sat Feb 04 2017 James Hogarth <james.hogarth@gmail.com> - 0.11.1-1
- Upgrade to 0.11.1
- Add requires on mod_ssl bz#1367943
* Fri Oct 14 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3
* Thu Oct 13 2016 Nick Bebout <nb@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Sun Jun 19 2016 James Hogarth <james.hogarth@gmail.com> - 0.8.1-2
- Spec bug on el7 requires - bz#1347997
* Wed Jun 15 2016 Nick Bebout <nb@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
* Tue Jun 07 2016 James Hogarth <james.hogarth@gmail.com> - 0.8.0-2
- Move recommends to correct subpackage
- change to require python-augeas as python2-augeas not provided in F23
- change the python-devel BR as per review
* Fri Jun 03 2016 james <james.hogarth@gmail.com> - 0.8.0-1
- update to upstream 0.8.0 release
* Tue May 31 2016 James Hogarth <james.hogarth@gmail.com> - 0.7.0-1
- Update to 0.7.0 release
* Thu May 26 2016 James Hogarth <james.hogarth@gmail.com> - 0.6.0-2
- Ensure python2-* provide is present as per python guidelines
* Thu May 26 2016 James Hogarth <james.hogarth@gmail.com> - 0.6.0-1
- Initial packaging of the plugin
