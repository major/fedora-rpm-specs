%global nginx_modname headers-more
%global origname %{nginx_modname}-nginx-module

Name:           nginx-mod-headers-more
Version:        0.38
Release:        1%{?dist}
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
* Sat Jan 25 2025 Luboš Uhliarik <luhliari@redhat.com> - 0.38-1
- new version 0.38

* Fri Jan 24 2025 Luboš Uhliarik <luhliari@redhat.com> - 0.37-1
- Initial packaging
