%global nginx_modname headers-more
%global origname %{nginx_modname}-nginx-module

Name:           nginx-mod-headers-more
Version:        0.39
Release:        6%{?dist}
Summary:        This module allows adding, setting, or clearing specified input/output headers

License:        BSD-2-Clause
URL:            https://github.com/openresty/headers-more-nginx-module
Source0:        %{url}/archive/v%{version}/%{origname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  nginx-mod-devel

%description
%{summary}.

This is an enhanced version of the standard headers module because it provides
more utilities like resetting or clearing "builtin headers" like Content-Type,
Content-Length, and Server.

%prep
%autosetup -n %{origname}-%{version}


%build
%nginx_modconfigure
%nginx_modbuild


%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_headers_more_filter_module.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_headers_more_filter_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-headers-more.conf
popd


%files
%doc README.markdown
%license LICENSE
%{nginx_moddir}/ngx_http_headers_more_filter_module.so
%{nginx_modconfdir}/mod-headers-more.conf


%changelog
* Wed Feb 04 2026 Felix Kaechele <felix@kaechele.ca> - 0.39-6
- Rebuild for 1.28.2

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Dec 26 2025 Felix Kaechele <felix@kaechele.ca> - 0.39-4
- Rebuild for 1.28.1

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Wed Jul 09 2025 Felix Kaechele <felix@kaechele.ca> - 0.39-2
- Rebuild for nginx 1.28.0

* Fri Jul 04 2025 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.39-1
- Update to 0.39 rhbz#2376275

* Fri Mar 28 2025 Carl George <carlwgeorge@fedoraproject.org> - 0.38-2
- Rebuild for nginx 1.26.3 rhbz#2355674

* Sat Jan 25 2025 Luboš Uhliarik <luhliari@redhat.com> - 0.38-1
- new version 0.38

* Fri Jan 24 2025 Luboš Uhliarik <luhliari@redhat.com> - 0.37-1
- Initial packaging
