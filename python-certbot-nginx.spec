%global pypi_name certbot-nginx

Name:       python-%{pypi_name}
Version:    2.1.0
Release:    1%{?dist}
Summary:    The nginx plugin for certbot

License:    Apache-2.0
URL:        https://pypi.python.org/pypi/certbot-nginx
Source0:        %{pypi_source}
Source1:        %{pypi_source}.asc
Source2:        https://dl.eff.org/certbot.pub

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Used to verify OpenPGP signature
BuildRequires:  gnupg2

%description
Plugin for certbot that allows for automatic configuration of ngnix


%package -n python3-%{pypi_name}
Summary:     The nginx plugin for certbot
# Provide the name users expect as a certbot plugin
%if 0%{?fedora}
Provides:      %{pypi_name} = %{version}-%{release}
%endif
# Recommend the CLI as that will be the interface most use
Recommends:    certbot >= %{version}

%description -n python3-%{pypi_name}
Plugin for certbot that allows for automatic configuration of nginx

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files certbot_nginx

%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%exclude %{python3_sitelib}/certbot_nginx/tests

%changelog
* Wed Dec 07 2022 Nick Bebout <nb@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Wed Nov 09 2022 Nick Bebout <nb@fedoraproject.org> - 1.32.0-1
- Update to 1.32.0

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.30.0-1
- Update to 1.30.0 rhbz#2125058

* Wed Aug 10 2022 Jonathan Wright <jonathan@almalinux.org> - 1.29.0-5
- Update to 1.29.0 (#2094627)
- Update license to SPDX format

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.27.0-3
- Rebuilt for pyparsing-3.0.9

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 1.27.0-2
- Rebuilt for Python 3.11

* Wed May 04 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.27.0-1
- Update to 1.27.0 (#2081535)

* Thu Apr 07 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.26.0-1
- Update to 1.26.0 (#2064933)

* Mon Mar 14 2022 Felix Schwarz <fschwarz@fedoraproject.org> - 1.24.0-1
- Update to 1.24.0 (#2052143)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 11 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.22.0-1
- Update to 1.22.0 (#2020085)

* Tue Oct 05 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0 (#2010969)

* Fri Sep 10 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0 (#2002056)

* Wed Aug 04 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0 (#1966774)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.14.0-2
- Rebuilt for Python 3.10

* Wed Apr 07 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0 (#1946821)

* Tue Mar 16 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0 (#1934848)

* Fri Feb 26 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.12.0-2
- lower pyparsing requirement to fix EPEL 8 (#1931256)

* Tue Feb 2 2021 Nick Bebout <nb@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan  5 2021 Felix Schwarz <fschwarz@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0 (#1913034)

* Thu Dec  3 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1 (#1904197)

* Wed Dec 02 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0 (#1903328)

* Thu Oct 08 2020 Nick Bebout <nb@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Tue Oct 06 2020 Nick Bebout <nb@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Sun Aug 16 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 (#1866076)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.6.0-1
- Update to 1.6.0 (#1854588)

* Sat Jun 06 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0 (#1843218)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-2
- Rebuilt for Python 3.9

* Sat May 09 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 (#1831930)

* Wed Mar 04 2020 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.3.0-1
- Update to 1.3.0 (#1809810)

* Fri Feb 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-2
- add missing build requirements

* Fri Feb 07 2020 Felix Schwarz <fschwarz@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 (#1791086)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Eli Young <elyscape@gmail.com> - 1.0.0-1
- Update to 1.0.0 (#1769120)

* Wed Dec 04 2019 Eli Young <elyscape@gmail.com> - 0.39.0-2
- Verify source OpenPGP signature

* Tue Oct 01 2019 Eli Young <elyscape@gmail.com> - 0.39.0-1
- Update to 0.39.0 (#1757588)

* Tue Sep 10 2019 Eli Young <elyscape@gmail.com> - 0.38.0-1
- Update to 0.38.0 (#1748627)

* Mon Aug 26 2019 Eli Young <elyscape@gmail.com> - 0.37.2-1
- Update to 0.37.2 (#1742593)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.36.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Eli Young <elyscape@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Fri Jun 21 2019 Eli Young <elyscape@gmail.com> - 0.35.1-1
- Update to 0.35.1 (#1717693)

* Tue May 28 2019 Eli Young <elyscape@gmail.com> - 0.34.2-1
- Update to 0.34.2 (#1686200)

* Fri Feb 08 2019 Eli Young <elyscape@gmail.com> - 0.31.0-1
- Update to 0.31.0 (#1673775)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Eli Young <elyscape@gmail.com> - 0.30.2-1
- Update to 0.30.2 (#1669329)

* Tue Dec 11 2018 Eli Young <elyscape@gmail.com> - 0.29.1-1
- Update to 0.29.1
- Remove Python 2 package in Fedora 30+ (#1654016)

* Wed Nov 14 2018 Eli Young <elyscape@gmail.com> - 0.28.0-1
- Update to 0.28.0

* Mon Sep 10 2018 Eli Young <elyscape@gmail.com> - 0.27.1-1
- Update to 0.27.1 (#1627585)

* Tue Jul 17 2018 Eli Young <elyscape@gmail.com> - 0.26.1-1
- Update to 0.26.1 (#1600304)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.25.1-2
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Eli Young <elyscape@gmail.com> - 0.25.1-1
- Update to 0.25.1 (#1591043)

* Tue Jun 12 2018 Eli Young <elyscape@gmail.com> - 0.25.0-2
- Add requirement on python-acme >= 0.25.0 (upstream #6096)

* Thu Jun 07 2018 Eli Young <elyscape@gmail.com> - 0.25.0-1
- Update to 0.25.0 (#1588231)

* Wed May 02 2018 Eli Young <elyscape@gmail.com> - 0.24.0-1
- Update to 0.24.0 (#1574150)

* Thu Apr 05 2018 Eli Young <elyscape@gmail.com> - 0.23.0-1
- Update to 0.23.0 (#1563911)

* Tue Mar 20 2018 Eli Young <elyscape@gmail.com> - 0.22.2-1
- Update to 0.22.2 (#1558283)

* Sat Mar 10 2018 Eli Young <elyscape@gmail.com> - 0.22.0-1
- Update to 0.22.0 (#1552956)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Eli Young <elyscape@gmail.com> - 0.21.1-1
- Update to 0.21.1 (#1535998)

* Wed Dec 20 2017 Eli Young <elyscape@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Fri Oct 06 2017 Eli Young <elyscape@gmail.com> - 0.19.0-1
- Update to 0.19.0 (bz#1499370)

* Fri Oct 06 2017 Eli Young <elyscape@gmail.com> - 0.18.2-2
- Fix provides (bz#1497315)

* Fri Sep 22 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.2-1
- Update to 0.18.2

* Mon Sep 11 2017 Nick Bebout <nb@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 17 2017 James Hogarth <james.hogarth@gmail.com> - 0.14.1-1
- Update to 0.14.1

* Fri May 12 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-1
- Update to 0.14.0
- Remove the tests directory from binary rpm

* Fri Apr 21 2017 James Hogarth <james.hogarth@gmail.com> - 0.13.0-1
- Initial packaging of the plugin
