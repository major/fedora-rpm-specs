# Module Magic Number
%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}
# State directory
%{!?_httpd_statedir: %global _httpd_statedir %{_localstatedir}/lib/httpd}

Name:           mod_md
Version:        2.6.7
Release:        %autorelease
Summary:        Certificate provisioning using ACME for the Apache HTTP Server
License:        Apache-2.0
URL:            https://icing.github.io/mod_md/
Source0:        https://github.com/icing/mod_md/releases/download/v%{version}/mod_md-%{version}.tar.gz
Patch1:         mod_md-2.0.8-state_dir.patch
BuildRequires:  make, gcc
BuildRequires:  pkgconfig, httpd-devel >= 2.4.41, openssl-devel >= 1.1.0, jansson-devel, libcurl-devel, xmlto
Requires:       httpd-mmn = %{_httpd_mmn}, mod_ssl >= 1:2.4.41
Conflicts:      httpd < 2.4.39-7
Epoch:          1

%description
This module manages common properties of domains for one or more
virtual hosts. Specifically it can use the ACME protocol to automate
certificate provisioning.  Certificates will be configured for managed
domains and their virtual hosts automatically, including at renewal.

%prep
%autosetup -p1

%build
%configure --with-apxs=%{_httpd_apxs}
# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build V=1

%check
%make_build check

%install
%make_install
rm -rf %{buildroot}/etc/httpd/share/doc/

# remove links and rename SO files
rm -f %{buildroot}%{_httpd_moddir}/mod_md.so
mv %{buildroot}%{_httpd_moddir}/mod_md.so.0.0.0 %{buildroot}%{_httpd_moddir}/mod_md.so

# create configuration and state directory
mkdir -p %{buildroot}%{_httpd_modconfdir} %{buildroot}%{_httpd_statedir}/md
echo "LoadModule md_module modules/mod_md.so" > %{buildroot}%{_httpd_modconfdir}/01-md.conf

%files
%doc README.md ChangeLog AUTHORS
%license LICENSE
%config(noreplace) %{_httpd_modconfdir}/01-md.conf
%{_httpd_moddir}/mod_md.so
%{_bindir}/a2md
%{_mandir}/man1/*
%dir %{_httpd_statedir}/md

%changelog
%autochangelog
