# Module Magic Number
%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2> /dev/null || echo 0-0)}

Summary:        Module for the Apache web server to query MaxMind DB files
Name:           mod_maxminddb
Version:        1.2.0
Release:        10%{?dist}
License:        Apache-2.0
URL:            https://maxmind.github.io/mod_maxminddb/
Source0:        https://github.com/maxmind/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        10-maxminddb.conf
Source2:        maxminddb.conf
BuildRequires:  gcc
BuildRequires:  httpd-devel >= 2.2.0
BuildRequires:  libmaxminddb-devel
Requires:       httpd-mmn = %{_httpd_mmn}

%description
The mod_maxminddb allows to query MaxMind DB files from the Apache web
server using the libmaxminddb library. The MaxMind DB files are provided
as free GeoLite2 databases as well as commercial GeoIP2 databases.

%prep
%setup -q

%build
%{_httpd_apxs} -lmaxminddb -c src/%{name}.c  # Avoid faulty upstream Makefile

%install
install -D -p -m 0755 src/.libs/%{name}.so $RPM_BUILD_ROOT%{_httpd_moddir}/%{name}.so
install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-maxminddb.conf
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_httpd_confdir}/maxminddb.conf

%files
%license LICENSE
%doc Changes.md README.md
%config(noreplace) %{_httpd_modconfdir}/10-maxminddb.conf
%config(noreplace) %{_httpd_confdir}/maxminddb.conf
%{_httpd_moddir}/%{name}.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Robert Scheck <robert@fedoraproject.org> 1.2.0-9
- Adjust module default configuration (thanks to Marcel Evenson)

* Wed Sep 04 2024 Robert Scheck <robert@fedoraproject.org> 1.2.0-8
- Remove dependencies on outdated geolite2-{country,city} RPMs

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Nov 28 2021 Robert Scheck <robert@fedoraproject.org> 1.2.0-1
- Upgrade to 1.2.0 (#2027078)
- Initial spec file for Fedora and Red Hat Enterprise Linux
