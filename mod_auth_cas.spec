%{!?_httpd_apxs:       %{expand: %%global _httpd_apxs       %%{_sbindir}/apxs}}
%{!?_httpd_mmn:        %{expand: %%global _httpd_mmn        %%(cat %{_includedir}/httpd/.mmn || echo missing-httpd-devel)}}
%{!?_httpd_confdir:    %{expand: %%global _httpd_confdir    %%{_sysconfdir}/httpd/conf.d}}
# /etc/httpd/conf.d with httpd < 2.4 and defined as /etc/httpd/conf.modules.d with httpd >= 2.4
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
%{!?_httpd_moddir:    %{expand: %%global _httpd_moddir    %%{_libdir}/httpd/modules}}


Name:           mod_auth_cas
Version:        1.1
Release:        10%{?dist}
Summary:        Apache 2.2/2.4 compliant module that supports the CASv1 and CASv2 protocols

License:        APLv2
URL:            http://www.ja-sig.org/wiki/display/CASC/mod_auth_cas
Source0:        https://github.com/Jasig/%{name}/archive/v%{version}.tar.gz
Source1:        auth_cas_mod.conf
Source2:        auth_cas_httpd.conf

BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  httpd-devel
BuildRequires:  m4, readline-devel, autoconf, automake
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  pcre-devel

Requires:       httpd
Requires:       mod_ssl

%description
mod_auth_cas is an Apache 2.2 and 2.4 compliant module that supports the CASv1
and CASv2 protocols

%prep
%setup -q -n %{name}-1.1

%build
autoreconf -vif #BZ926155 - support aarch64
%configure --with-apxs=%{_httpd_apxs}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} LIBEXECDIR=%{_httpd_moddir}
echo "DEBUG: _httpd_modconfdir: %{_httpd_modconfdir}"
echo "DEBUG: _httpd_confdir: %{_httpd_modconfdir}"
%if "%{_httpd_modconfdir}" == "%{_httpd_confdir}"
# httpd <= 2.2.x
cat %{SOURCE1} %{SOURCE2} > auth_cas.conf
install -Dp -m 644 auth_cas.conf %{buildroot}%{_httpd_modconfdir}/auth_cas.conf
%else
# httpd >= 2.4.x
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-auth_cas.conf
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_httpd_confdir}/auth_cas.conf
%endif

mkdir -p %{buildroot}/var/cache/httpd/%{name}


%files
%doc README
%{_libdir}/httpd/modules/*.so
%config(noreplace) %{_httpd_confdir}/*.conf
%config(noreplace) %{_httpd_modconfdir}/*.conf

%defattr(-,apache,apache,-)
%dir /var/cache/httpd/%{name}

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-3
- Fix /var/cache/httpd/mod_auth_cas directory ownership (BZ#1368448)

* Fri Sep 02 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-2
- Fix EPEL6 conditionals for 1.1 update

* Thu Jun 16 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-1
- Update to latest stable upstream

* Wed May 11 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-0.2.rc3
- Update refs to apache versions
- Fix entry module conf in _httpd_modconfdir
- Add conf to _httpd_confdir
- Add cachedir

* Tue May 10 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-0.1.rc3
- Pull in latest RC from upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Adam Miller <maxamillion@fedoraproject.org> - 1.0.9.1-1
- Update to latest upstream.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-8
- BZ926155 - support aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Joe Orton <jorton@redhat.com> - 1.0.8.1-5
- update packaging (#803065)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 29 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-2
- Fixed svn export link, upstream changed canonical URL names.

* Wed Apr 28 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-1
- added requires of httpd
- fixed mixed use of macros
- updated to latest version

* Fri Aug 07 2009 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8-1
- First attempt to package mod_auth_cas for Fedora

