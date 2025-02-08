%global shortname naxsi

Name:           nginx-mod-naxsi
Version:        1.6
Release:        9%{?dist}
Summary:        nginx web application firewall module
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only

URL:            https://github.com/wargio/naxsi
Source0:        %{url}/archive/%{version}/%{shortname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  nginx-mod-devel
BuildRequires:  pkgconfig(libinjection)

%description
naxsi is an nginx module that provides score based Web Application Firewall
(WAF) abilities in a highly granular fashion.

%prep
%autosetup -n %{shortname}-%{version} -p1

%build
pushd naxsi_src
%nginx_modconfigure
%nginx_modbuild
popd

%install
pushd naxsi_src/%{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm0755 ngx_http_naxsi_module.so %{buildroot}%{nginx_moddir}
popd

install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_naxsi_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-naxsi-web-app-firewall.conf

install -dm 0755 %{buildroot}%{_datadir}/nginx/naxsi
install -m0755 naxsi_rules/naxsi_core.rules %{buildroot}%{_datadir}/nginx/naxsi/


%files
%license LICENSE
%doc README.md
%doc naxsi_rules/
%{nginx_moddir}/ngx_http_naxsi_module.so
%{nginx_modconfdir}/mod-naxsi-web-app-firewall.conf
%{_datadir}/nginx/naxsi/


%changelog
* Thu Feb 06 2025 Felix Kaechele <felix@kaechele.ca> - 1.6-9
- Rebuild for nginx 1.26.3

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 26 2024 Felix Kaechele <felix@kaechele.ca> - 1.6-7
- Rebuild for nginx 1.26.2... again.

* Sat Aug 17 2024 Felix Kaechele <felix@kaechele.ca> - 1.6-6
- Rebuild for nginx 1.26.2

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Felix Kaechele <felix@kaechele.ca> - 1.6-3
- Rebuild for 1.26.1 again, last rebuild still pulled in 1.26.0

* Tue Jun 04 2024 Felix Kaechele <felix@kaechele.ca> - 1.6-2
- Rebuild for nginx 1.26.1

* Mon Apr 29 2024 Felix Kaechele <felix@kaechele.ca> - 1.6-1
- Update to 1.6

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 25 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.5-1
- Update to 1.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.4-1
- Rebase to 1.4 from the maintained fork

* Mon Apr 17 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.3-8
- Rebuild for nginx 1.24.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.3-6
- Rebuild for nginx 1.22.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.3-4
- Backport fix for nginx built with PCRE2
- Rebuild for nginx 1.22.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.3-2
- Rebuild for nginx 1.20.2

* Mon Aug 16 2021 Neal Gompa <ngompa@datto.com> - 1.3-1
- Initial packaging
