%global nginx_modname vts
%global origname nginx-module-%{nginx_modname}

Name:           nginx-mod-vts
Version:        0.2.3
Release:        1%{?dist}
Summary:        Nginx virtual host traffic status module

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/vozlt/nginx-module-vts
Source0:        %{url}/archive/v%{version}/%{origname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  nginx-mod-devel


%description
%{summary}.

%prep
%autosetup -n %{origname}-%{version}


%build
%nginx_modconfigure
%nginx_modbuild


%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_vhost_traffic_status_module.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_vhost_traffic_status_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-vhost-traffic-status.conf
popd


%files
%license LICENSE
%doc README.md
%{nginx_moddir}/ngx_http_vhost_traffic_status_module.so
%{nginx_modconfdir}/mod-vhost-traffic-status.conf


%changelog
* Thu Jan 02 2025 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.2.3-1
- Update to 0.2.3 rhbz#2335121

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.2-11
- convert license to SPDX

* Mon Aug 26 2024 Felix Kaechele <felix@kaechele.ca> - 0.2.2-10
- Rebuild for nginx 1.26.2... again.

* Sat Aug 17 2024 Felix Kaechele <felix@kaechele.ca> - 0.2.2-9
- Rebuild for nginx 1.26.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Felix Kaechele <felix@kaechele.ca> - 0.2.2-7
- Rebuild for 1.26.1 again, last rebuild still pulled in 1.26.0

* Tue Jun 04 2024 Felix Kaechele <felix@kaechele.ca> - 0.2.2-6
- Rebuild for nginx 1.26.1

* Mon Apr 29 2024 Felix Kaechele <felix@kaechele.ca> - 0.2.2-5
- Rebuild for nginx 1.26.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 27 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.2.2-1
- Update to 0.2.2 rhbz#2210486

* Mon Apr 17 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.2.1-4
- Rebuild for nginx 1.24.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.2.1-2
- Rebuild for nginx 1.22.1

* Thu Sep 22 2022 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.2.1-1
- Bump to 0.2.1 rhbz#2124567

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.1.18-4
- Rebuild for nginx 1.22.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.1.18-2
- Rebuild for nginx 1.20.2

* Mon Aug 16 2021 Neal Gompa <ngompa@datto.com> - 0.1.18-1
- Initial packaging
