%global commit  0488c77f69669584324b70460614a382224b4883
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20210819
%global gh_name ModSecurity-apache


Name: mod_security3
Version: 0.0.9
Release: 0.%{commit_date}git%{shortcommit}.1%{?dist}.3
Summary: ModSecurity v3 Apache Connector

License: ASL 2.0
URL: https://github.com/SpiderLabs/ModSecurity-apache
Source0: https://github.com/SpiderLabs/%{gh_name}/archive/%{commit}/%{gh_name}-%{shortcommit}.tar.gz
Source1: mod_security3.conf
Source2: 10-mod_security3.conf

BuildRequires: httpd-devel
BuildRequires: libmodsecurity-devel
BuildRequires: git-core

BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(geoip)
BuildRequires: pkgconfig(yajl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libpcre)


# Minimal buildroot
BuildRequires: make
BuildRequires: gcc

# Required for pre-release
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

#Requires: libmodsecurity
Requires: httpd
Requires: httpd-mmn = %{_httpd_mmn}

# NOTE: Upstream still consdier mod_security3 as Non-production ready

# Needed to install core rules (mod_security_crs)
# Since mod_security3 will be able to replace mod_security2
#Provides: mod_security

%description
The ModSecurity-apache connector is the connection point between
Apache and libmodsecurity (ModSecurity v3). Said another way, this
project provides a communication channel between Apache and libmodsecurity.
This connector is required to use LibModSecurity with Apache.

%prep
%autosetup -S git -n %{gh_name}-%{commit}

%build
# Temp for prelease
./autogen.sh
%configure
%make_build


%install
mkdir -p %{buildroot}%{_httpd_confdir}
mkdir -p %{buildroot}%{_libdir}/httpd/modules
install -m 700 -d %{buildroot}%{_localstatedir}/lib/%{name}

install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/activated_rules
install -d %{buildroot}%{_sysconfdir}/httpd/modsecurity.d/local_rules

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# 2.4-style
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_httpd_modconfdir}/10-mod_security3.conf
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_httpd_confdir}/mod_security3.conf
%else
# 2.2-style
install -d -m0755 %{buildroot}%{_httpd_confdir}
cat %{SOURCE2} %{SOURCE1} > %{buildroot}%{_httpd_confdir}/mod_security3.conf
%endif
install -m 755 src/.libs/mod_security3.so %{buildroot}%{_httpd_moddir}


%files
%doc README.md
%license LICENSE
%{_httpd_moddir}/mod_security3.so
%config(noreplace) %{_httpd_confdir}/*.conf

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
    %config(noreplace) %{_httpd_modconfdir}/*.conf
%endif
%dir %{_sysconfdir}/httpd/modsecurity.d
%dir %{_sysconfdir}/httpd/modsecurity.d/activated_rules
%dir %{_sysconfdir}/httpd/modsecurity.d/local_rules
%attr(770,apache,root) %dir %{_localstatedir}/lib/%{name}

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-0.20210819git0488c77.1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-0.20210819git0488c77.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-0.20210819git0488c77.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 11 2021 Othman Madjoudj <athmane@fedoraproject.org> - 0.0.9-0.20210819git
- Update to latest release
- Remove upstreamed patch

* Mon Oct 30 2017 Othman Madjoudj <athmane@fedoraproject.org> - 0.1.1-0.20170821git4e8854c.1
- Update BR

* Sun Oct 29 2017 Othman Madjoudj <athmane@fedoraproject.org> - 0.1.1-0.20170821git4e8854c
- Initial spec

