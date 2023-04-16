%global origname nginx-module-modsecurity

Name:           nginx-mod-modsecurity
Version:        1.0.3
Release:        %autorelease
Summary:        ModSecurity v3 nginx connector

License:        Apache-2.0
URL:            https://github.com/SpiderLabs/ModSecurity-nginx
Source0:        %{url}/archive/v%{version}/%{origname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/SpiderLabs/ModSecurity/v3/master/modsecurity.conf-recommended
Source2:        https://raw.githubusercontent.com/SpiderLabs/ModSecurity/v3/master/unicode.mapping
Source3:        nginx.conf.modsecurity


BuildRequires:  gcc
BuildRequires:  libmodsecurity-devel
BuildRequires:  nginx-mod-devel
Requires:       nginx-filesystem

%description
The ModSecurity-nginx connector is the connection point between nginx and
libmodsecurity (ModSecurity v3). Said another way, this project provides a
communication channel between nginx and libmodsecurity. This connector is
required to use LibModSecurity with nginx.

The ModSecurity-nginx connector takes the form of an nginx module. The module
simply serves as a layer of communication between nginx and ModSecurity

%prep
%autosetup -n ModSecurity-nginx-%{version}

%build
%nginx_modconfigure
%nginx_modbuild

%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_modsecurity_module.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
echo 'load_module "%{nginx_moddir}/ngx_http_modsecurity_module.so";' \
    > %{buildroot}%{nginx_modconfdir}/mod-modsecurity.conf
popd
install -dm 0755 %{buildroot}%{_sysconfdir}/nginx/conf.d/
install -pm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/nginx/modsecurity.conf
install -pm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/nginx/unicode.mapping
install -pm 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/nginx/nginx.conf.modsecurity

%files
%license LICENSE
%doc README.md
%{nginx_moddir}/ngx_http_modsecurity_module.so
%{nginx_modconfdir}/mod-modsecurity.conf
%config(noreplace) %{_sysconfdir}/nginx/modsecurity.conf
%{_sysconfdir}/nginx/nginx.conf.modsecurity
%{_sysconfdir}/nginx/unicode.mapping

%changelog
%autochangelog
