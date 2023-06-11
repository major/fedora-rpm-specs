%global nginx_modname vts
%global origname nginx-module-%{nginx_modname}

Name:           nginx-mod-vts
Version:        0.2.2
Release:        1%{?dist}
Summary:        Nginx virtual host traffic status module

License:        BSD
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
