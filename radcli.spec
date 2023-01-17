Summary: RADIUS protocol client library
Name: radcli
Version: 1.3.0
Release: 6%{?dist}

#Breakdown of licenses. Under MIT license:
# lib/avpair.c, lib/buildreq.c, lib/clientid.c, lib/config.c, lib/dict.c,
# lib/env.c, lib/ip_util.c, lib/log.c, lib/sendserver.c, lib/util.c,
# src/local.c, src/radacct.c, src/radexample.c, src/radius.c, src/radlogin.c,
# src/radstatus.c, include/messages.h, include/pathnames.h, lib/options.h
# Under BSD license: lib/util.c, src/radiusclient.c, lib/rc-md5.c, lib/tls.c,
# lib/tls.h

License: BSD and MIT
URL: http://radcli.github.io/radcli/

%{expand:%(echo "%%global myversion %{version}" | \
  sed 's/\./_/g')}

Source0: https://github.com/radcli/radcli/releases/download/%{name}_%{myversion}/%{name}-%{version}.tar.gz
Patch0: radcli-autoconf.c99.patch

BuildRequires: libtool, automake, autoconf
#BuildRequires: gettext-devel
BuildRequires: make
BuildRequires:  gcc
BuildRequires: nettle-devel >= 2.7.1
BuildRequires: gnutls-devel

%description
The radcli library is a library for writing RADIUS Clients. The library's
approach is to allow writing RADIUS-aware application in less than 50 lines
of C code. It was based originally on freeradius-client and is source compatible
with it.

%package devel
Summary: Development files for radcli
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing applications
that use %{name}.

%package compat-devel
Summary: Development files for compatibility with radiusclient-ng and freeradius-client
Requires: %{name}-devel = %{version}-%{release}
# We provide compatible headers with it
Conflicts: freeradius-client-devel, radiusclient-ng-devel

%description compat-devel
This package contains the compatibility headers and libraries for freeradius-client
and radiusclient-ng.

%prep
%autosetup -p1
rm -f lib/md5.c
sed -i -e 's|sys_lib_dlsearch_path_spec="[^"]\+|& %{_libdir}|g' configure

%build
autoreconf -fvi
%configure --disable-static --disable-rpath --with-nettle --with-tls --enable-legacy-compat
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_libdir}/*.la

# these should be removed once the utils subpackage is on

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p %{buildroot}%{_datadir}/%{name}/dictionary %{buildroot}%{_sysconfdir}/%{name}/dictionary

%ldconfig_scriptlets

%files
%doc README.md NEWS
%license COPYRIGHT

%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/radiusclient.conf
%config(noreplace) %{_sysconfdir}/%{name}/radiusclient-tls.conf
%config(noreplace) %{_sysconfdir}/%{name}/servers
%config(noreplace) %{_sysconfdir}/%{name}/servers-tls
%config(noreplace) %{_sysconfdir}/%{name}/dictionary

%{_libdir}/libradcli.so.*

%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dictionary
%{_datadir}/%{name}/dictionary.roaringpenguin
%{_datadir}/%{name}/dictionary.microsoft
%{_datadir}/%{name}/dictionary.ascend
%{_datadir}/%{name}/dictionary.compat
%{_datadir}/%{name}/dictionary.merit
%{_datadir}/%{name}/dictionary.sip

%files devel

%dir %{_includedir}/%{name}
%{_includedir}/%{name}
%{_includedir}/%{name}/radcli.h
%{_includedir}/%{name}/version.h
%{_libdir}/libradcli.so
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*.pc

%files compat-devel

%{_includedir}/freeradius-client.h
%{_includedir}/radiusclient-ng.h
%{_libdir}/libfreeradius-client.so
%{_libdir}/libradiusclient-ng.so

%changelog
* Sat Jan 14 2023 Peter Fordham <peter.fordham@gmail.com> - 1.3.0-6
- Add missing return type to main in configure.ac and enable autoreconf.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.3.0-1
- New upstream release

* Fri Sep 11 2020 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.12-1
- New upstream release

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.11-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.10-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.9-1
- New upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.8-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan  2 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.7-2
- Use gnutls' random functions to avoid depending on getentropy entirely (#1409291)

* Mon Dec 19 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.7-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.5-1
- Added TCP support

* Thu Nov 26 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.3-2
- Fixed overflow in rc_ipaddr_local()

* Wed Sep  2 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.3-1
- Updated to 1.2.3

* Fri Aug 21 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.2-1
- Updated to 1.2.2

* Mon Jun 15 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.2.1-1
- Initial package
