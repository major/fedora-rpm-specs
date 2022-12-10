%global pypi_name certbot-dns-google

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Google Cloud DNS Authenticator plugin for Certbot

License:        Apache-2.0
URL:            https://pypi.python.org/pypi/certbot-dns-google
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
Source2:        https://dl.eff.org/certbot.pub

BuildArch:      noarch

BuildRequires:  python3-acme >= %{version}
BuildRequires:  python3-certbot >= %{version}
BuildRequires:  python3-devel
BuildRequires:  python3-google-api-client >= 1.5.5
BuildRequires:  python3-httplib2
BuildRequires:  python3-oauth2client >= 4.0
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools >= 41.6.0

# Used to verify OpenPGP signature
BuildRequires:  gnupg2

%description
This certbot plugin automates the process of completing an ACME
dns-01 challenge by creating, and subsequently removing, TXT
records using Google Cloud DNS.

%package -n python3-%{pypi_name}
Summary:        %{summary}

# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:       %{pypi_name} = %{version}-%{release}
%endif
# Recommend the CLI as that will be the interface most use
Recommends:     certbot
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This certbot plugin automates the process of completing an ACME
dns-01 challenge by creating, and subsequently removing, TXT
records using Google Cloud DNS.

This is the Python 3 version of the package.


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
%{python3_sitelib}/certbot_dns_google
%{python3_sitelib}/certbot_dns_google-%{version}*.egg-info

%changelog
* Thu Dec 08 2022 Nick Bebout <nb@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Wed Nov 09 2022 Nick Bebout <nb@fedoraproject.org> - 1.32.0-1
- Update to 1.32.0

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.30.0-1
- Update to 1.30.0 rhbz#2125052

* Wed Aug 10 2022 Jonathan Wright <jonathan@almalinux.org> - 1.29.0-2
- Update to 1.29.0 (#2104686)
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.27.0-2
- Rebuilt for Python 3.11

* Wed May 04 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.27.0-1
- Update to 1.27.0 (#2081526)

* Thu Apr 07 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0 (#2064925)

* Mon Mar 14 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.24.0-1
- Update to 1.24.0 (#2052134)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.22.0-1
- Update to 1.22.0 (#2020077)

* Tue Oct 05 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0 (#2010960)

* Fri Sep 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0 (#2002048)

* Wed Aug 04 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0 (#1966783)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.14.0-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0 (#1946811)

* Tue Mar 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0 (#1934812)

* Tue Feb 2 2021 Nick Bebout <nb@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0 (#1913026)

* Thu Dec  3 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#1904192)

* Thu Dec  3 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0 (#1903320)

* Thu Oct 08 2020 Nick Bebout <nb@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Tue Oct 06 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Aug 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#1866077)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1854591)

* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843209)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831922)

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809817)

* Sat Feb 29 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.2.0-1
- Update to 1.2.0 (#1791078)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769111)

* Wed Dec 04 2019 Eli Young <elyscape@gmail.com> - 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757585)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748619)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742585)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717685)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686192)

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673754)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669321)

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1627577)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600299)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591038)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588226)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574143)

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563906)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0

* Mon Feb 26 2018 Nick Bebout <nb@usi.edu> - 0.21.1-2
- Simplify deps, add python2- prefix where available

* Wed Feb 14 2018 Eli Young <elyscape@gmail.com> - 0.21.1-1
- Initial package (#1544555)
