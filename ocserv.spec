Version:	1.1.7
Release: 1%{?dist}
%global _hardened_build 1

%if 0%{?fedora} || 0%{?rhel} >= 7
%define use_systemd 1
%define have_gpgv2 1
%else
%define use_systemd 0
%define have_gpgv2 0
%endif

%if 0%{?fedora} >= 28 || 0%{?rhel} > 7
%define use_libwrap 0
%define use_geoip 0
%else
%define use_libwrap 1
%define use_geoip 1
%endif

%define use_local_protobuf 0

Name:		ocserv
Summary:	OpenConnect SSL VPN server

# For a breakdown of the licensing, see PACKAGE-LICENSING 
# To simplify licenses LGPLv2+ files have been promoted to GPLv2+.
License:	GPLv2+ and BSD and MIT and CC0
URL:		http://www.infradead.org/ocserv/
Source0:	ftp://ftp.infradead.org/pub/ocserv/%{name}-%{version}.tar.xz
Source1:	ftp://ftp.infradead.org/pub/ocserv/%{name}-%{version}.tar.xz.sig
Source2:	gpgkey-1F42418905D8206AA754CCDC29EE58B996865171.gpg
Source3:	ocserv.conf
Source4:	ocserv.service
Source5:	ocserv-pamd.conf
Source6:	PACKAGE-LICENSING
Source8:	ocserv-genkey
Source9:	ocserv-script
Source10:	gpgkey-56EE7FA9E8173B19FE86268D763712747F343FA7.gpg
Source11:	ocserv.init

# Taken from upstream:
# http://git.infradead.org/ocserv.git/commitdiff/7d70006a2dbddf783213f1856374bacc74217e09

BuildRequires: make
BuildRequires:	gcc
%if 0%{?rhel} && 0%{?rhel} <= 6
BuildRequires:	gnutls30-devel
%else
BuildRequires:	gnutls-devel
%endif
BuildRequires:	pam-devel
BuildRequires:	iproute
BuildRequires:	openconnect
BuildRequires:  gnutls-utils

%if (0%{?use_local_protobuf} == 0)
BuildRequires:	protobuf-c-devel
%endif

BuildRequires:	libnl3-devel
BuildRequires:	krb5-devel
BuildRequires:	libtasn1-devel
BuildRequires:	gperf
BuildRequires:	libtalloc-devel
BuildRequires:	libev-devel
BuildRequires:	http-parser-devel

%if %{use_libwrap}
BuildRequires:	tcp_wrappers-devel
%endif
BuildRequires:	automake, autoconf
BuildRequires:	radcli-devel
BuildRequires:	lz4-devel
BuildRequires:	readline-devel
%if %{use_geoip}
BuildRequires:	GeoIP-devel
%else
BuildRequires:	libmaxminddb-devel
%endif

%if %{use_systemd}
BuildRequires:	systemd
BuildRequires:	systemd-devel
BuildRequires:	liboath-devel
BuildRequires:	uid_wrapper
# Disable socket_wrapper on certain architectures because it
# introduces new syscalls that the worker cannot handle.
%ifnarch aarch64 %{ix86} %{arm}
BuildRequires:	socket_wrapper
%endif
BuildRequires:	gnupg2

%if 0%{?rhel} && 0%{?rhel} >= 7
%ifarch x86_64 %{ix86}
BuildRequires:	libseccomp-devel
%endif
%else
%ifarch x86_64 %{ix86} %{arm} aarch64
BuildRequires:	libseccomp-devel
%endif
%endif

%endif

# no rubygem in epel7
%if 0%{?fedora}
BuildRequires:	rubygem-ronn-ng
%endif

Recommends:		gnutls-utils
Recommends:		iproute
Recommends:		pam
Requires(pre):		shadow-utils
%if %{use_systemd}
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
%endif

#gnulib is bundled. See https://fedorahosted.org/fpc/ticket/174
Provides:		bundled(gnulib)
#CCAN is bundled. See https://fedorahosted.org/fpc/ticket/364
Provides:		bundled(bobjenkins-hash) bundled(ccan-container_of) 
Provides:		bundled(ccan-htable) bundled(ccan-list)
Provides:		bundled(ccan-check_type) bundled(ccan-build_assert)

%description
OpenConnect server (ocserv) is an SSL VPN server. Its purpose is to be a 
secure, small, fast and configurable VPN server. It implements the OpenConnect 
SSL VPN protocol, and has also (currently experimental) compatibility with 
clients using the AnyConnect SSL VPN protocol. The OpenConnect VPN protocol 
uses the standard IETF security protocols such as TLS 1.2, and Datagram TLS 
to provide the secure VPN service. 

%prep
%if %{have_gpgv2}
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0} || gpgv2 --keyring %{SOURCE10} %{SOURCE1} %{SOURCE0}
%endif

%autosetup -p1

rm -f src/http-parser/http_parser.c src/http-parser/http_parser.h
%if (0%{?use_local_protobuf} == 0)
rm -rf src/protobuf/protobuf-c/
touch src/*.proto
%endif
rm -rf src/ccan/talloc
sed -i 's|/etc/ocserv.conf|/etc/ocserv/ocserv.conf|g' src/config.c
sed -i 's/run-as-group = nogroup/run-as-group = nobody/g' tests/data/*.config
# GPLv3 in headers is a gnulib bug: 
# http://lists.gnu.org/archive/html/bug-gnulib/2013-11/msg00062.html
sed -i 's/either version 3 of the License/either version 2 of the License/g' build-aux/snippet/*

%if 0%{?rhel} && 0%{?rhel} <= 6
echo "int main() { return 77; }" > tests/valid-hostname.c
%endif

%build

%if 0%{?rhel} && 0%{?rhel} <= 6
export PKG_CONFIG_LIBDIR="%{_libdir}/gnutls30/pkgconfig:%{_libdir}/pkgconfig"
export LIBGNUTLS_CFLAGS="-I/usr/include/gnutls30"
export LIBGNUTLS_LIBS="-L%{_libdir}/gnutls30/ -lgnutls"
export CFLAGS="$CFLAGS -I/usr/include/libev -I/usr/include/gnutls30"
sed -i 's/AM_PROG_AR//g' configure.ac
autoreconf -fvi
%endif

%configure \
        --without-pcl-lib \
%if %{use_systemd}
	--enable-systemd \
%else
	--disable-systemd \
%endif
%if %{use_local_protobuf}
	--without-protobuf \
%endif
%if %{use_libwrap}
	--with-libwrap
%else
	--without-libwrap
%endif

make %{?_smp_mflags}

%pre
getent group ocserv &>/dev/null || groupadd -r ocserv
getent passwd ocserv &>/dev/null || \
	/usr/sbin/useradd -r -g ocserv -s /sbin/nologin -c ocserv \
		-d %{_localstatedir}/lib/ocserv ocserv
mkdir -p %{_sysconfdir}/pki/ocserv/public
mkdir -p -m 700 %{_sysconfdir}/pki/ocserv/private
mkdir -p %{_sysconfdir}/pki/ocserv/cacerts

%check
make check %{?_smp_mflags} VERBOSE=1

%if %{use_systemd}
%post
%systemd_post ocserv.service

%preun
%systemd_preun ocserv.service

%postun
%systemd_postun ocserv.service
%endif

%install
rm -rf %{buildroot}
cp -a %{SOURCE6} PACKAGE-LICENSING
mkdir -p %{buildroot}/%{_sysconfdir}/pam.d/
mkdir -p %{buildroot}/%{_sysconfdir}/ocserv/
install -p -m 644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/pam.d/ocserv
install -p -m 644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/ocserv/
mkdir -p %{buildroot}%{_localstatedir}/lib/ocserv/
install -p -m 644 doc/profile.xml %{buildroot}%{_localstatedir}/lib/ocserv/
mkdir -p %{buildroot}/%{_sbindir}
install -p -m 755 %{SOURCE8} %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE9} %{buildroot}/%{_bindir}

%if 0%{?rhel} && 0%{?rhel} <= 7
sed -i 's|expiration_days=-1|expiration_days=9999|' %{buildroot}/%{_sbindir}/ocserv-genkey
sed -i 's|tls-priorities = "@SYSTEM"|tls-priorities = "NORMAL:%SERVER_PRECEDENCE:%COMPAT:-VERS-SSL3.0"|' %{buildroot}/%{_sysconfdir}/ocserv/ocserv.conf
%if 0%{?rhel} <= 6
sed -i 's|isolate-workers = true|isolate-workers = false|' %{buildroot}/%{_sysconfdir}/ocserv/ocserv.conf
%endif
%endif

%if %{use_systemd}
mkdir -p %{buildroot}/%{_unitdir}
install -p -m 644 %{SOURCE4} %{buildroot}/%{_unitdir}
%else
mkdir -p %{buildroot}/%{_initrddir}
install -D -m 0755 %{SOURCE11} %{buildroot}/%{_initrddir}/%{name}
%endif

%make_install

%files
%defattr(-,root,root,-)

%dir %{_localstatedir}/lib/ocserv
%dir %{_sysconfdir}/ocserv

%config(noreplace) %{_sysconfdir}/ocserv/ocserv.conf
%config(noreplace) %{_sysconfdir}/pam.d/ocserv
%config(noreplace) %{_localstatedir}/lib/ocserv/profile.xml

%doc AUTHORS ChangeLog NEWS COPYING COPYING README.md PACKAGE-LICENSING
%doc src/ccan/licenses/CC0 src/ccan/licenses/LGPL-2.1 src/ccan/licenses/BSD-MIT

%{_mandir}/man8/ocserv.8*
%{_mandir}/man8/occtl.8*
%{_mandir}/man8/ocpasswd.8*

%{_bindir}/ocpasswd
%{_bindir}/occtl
%{_bindir}/ocserv-fw
%{_bindir}/ocserv-script
%{_sbindir}/ocserv
%{_sbindir}/ocserv-worker
%{_sbindir}/ocserv-genkey
%{_localstatedir}/lib/ocserv/profile.xml
%if %{use_systemd}
%{_unitdir}/ocserv.service
%else
%{_initrddir}/%{name}
%endif

%changelog
* Sun May 07 2023 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.7-1
- Updated to 1.1.7

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 17 2022 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.6-1
- Updated to 1.1.6

* Thu Feb 10 2022 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.4-3
- Update seccomp rules to allow the futex syscall
- Workaround incompatible API change in GnuTLS 3.7.3.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.4-1
- Update to upstream 1.1.4 release

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 1.1.3-4
- Rebuilt for protobuf 3.19.0

* Tue Oct 26 2021 Adrian Reber <adrian@lisas.de> - 1.1.3-3
- Rebuilt for protobuf 3.18.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun  2 2021 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.3-1
- Updated to latest release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 08:31:24 CET 2021 Adrian Reber <adrian@lisas.de> - 1.1.2-2
- Rebuilt for protobuf 3.14

* Sun Dec  6 2020 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.2-1
- Update to upstream 1.1.2 release

* Mon Nov 23 2020 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.1.1-5
- Rebuilt for ronn successor

* Wed Nov 11 2020 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.1.1-4
- Rebuilt for radcli 1.3.0

* Thu Oct 29 2020 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.1-3
- Rebuild without pcllib dependency
- Enhanced seccomp filters for tests to run in all architectures

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.1.1-2
- Rebuilt for protobuf 3.13

* Mon Sep 21 2020 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.1-1
- Update to upstream 1.1.1 release
- Set default priorities to NORMAL as using @SYSTEM is no longer necessary
  to follow crypto policies.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Adrian Reber <adrian@lisas.de> - 1.1.0-2
- Rebuilt for protobuf 3.12

* Tue Jun 16 2020 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.1.0-1
- Update to upstream 1.1.0 release (introduces ocserv-worker)

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Rebuild for http-parser 2.9.4

* Thu Apr 09 2020 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.0.1-1
- Update to upstream 1.0.1 release

* Fri Mar 20 2020 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 1.0.0-1
- Update to upstream 1.0.0 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 Nikos Mavrogiannopoulos <n.mavrogiannopoulos@gmail.com> - 0.12.6-1
- Update to upstream 0.12.6 release

* Wed Oct 16 2019 Nikos Mavrogiannopoulos <nmav@gnutls.org> - 0.12.5-1
- Update to upstream 0.12.5 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Nikos Mavrogiannopoulos <nmav@gnutls.org> - 0.12.4-1
- Update to upstream 0.12.4 release

* Tue Mar 12 2019 Nikos Mavrogiannopoulos <nmav@gnutls.org> - 0.12.3-1
- Update to upstream 0.12.3 release

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.2-4
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.12.2-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Thu Jan 10 2019 Nikos Mavrogiannopoulos <nmav@gnutls.org> - 0.12.2-1
- Update to upstream 0.12.2 release

* Tue Jul 24 2018 Nikos Mavrogiannopoulos <nmav@gnutls.org> - 0.12.1-3
- Added gcc as build-dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 12 2018 Nikos Mavrogiannopoulos <nmav@gnutls.org> - 0.12.1-1
- Update to upstream 0.12.1 release

* Mon Apr 23 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.12.0-1
- Update to upstream 0.12.0 release

* Thu Apr 12 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.11-2
- Update to upstream 0.11.11 release
- include crypt.h to use crypt()

* Mon Mar 05 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.11-1
- Update to upstream 0.11.11 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.11.10-2
- Rebuilt for switch to libxcrypt

* Mon Jan 08 2018 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.10-1
- Update to upstream 0.11.10 release

* Tue Nov 21 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.9-3
- Update to upstream 0.11.9 release

* Thu Nov 16 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.9-2
- Do not enable libwrap

* Tue Oct 10 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.9-1
- Update to upstream 0.11.9 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.8-1
- Update to upstream 0.11.8 release

* Mon Feb 13 2017 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.7-1
- Update to upstream 0.11.7 release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.11.6-3
- Rebuild for readline 7.x

* Tue Nov 15 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.6-2
- Removed gpgkeys from sources

* Tue Nov 15 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.6-1
- New upstream release

* Wed Sep 14 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.4-3
- Added getrandom to the list of allowed syscalls (#1375851)

* Thu Sep  8 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.4-2
- Rebuild to address http-parser breakage (#1374081)

* Fri Aug  5 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.4-1
- New upstream release

* Thu Jun 16 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.3-1
- New upstream release

* Tue Apr 26 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.2-1
- New upstream release
- Added automatic verification of signature during build

* Mon Mar 21 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.1-1
- new upstream release

* Fri Feb 19 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.11.0-1
- new upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.11-1
- new upstream release

* Mon Nov 30 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.10-1
- new upstream release

* Thu Oct  8 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.9-1
- new upstream release (#1269479)

* Thu Sep 17 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.8-2
- compile ocserv using radcli

* Mon Sep  7 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.8-1
- new upstream release (#1260327)

* Fri Aug  7 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.7-1
- new upstream release (#1251305)

* Thu Jul  9 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.6-2
- corrected JSON output

* Thu Jul  2 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.6-1
- new upstream release (#1238499)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.5-1
- new upstream release (#1215326)

* Mon Apr 27 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.4-1
- new upstream release

* Mon Mar 30 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.2-1
- new upstream release

* Mon Mar 16 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.1-1
- new upstream release

* Wed Mar 11 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.10.0-1
- new upstream release

* Wed Feb 18 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.9.2-1
- new upstream release
- enabled lz4 compression

* Mon Feb 16 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.1-2
- aarch64 (and ARMv7) now has seccomp support

* Mon Feb 16 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.9.1-1
- new upstream release

* Thu Jan 29 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.9.0-2
- only enable seccomp in x86-64. It seems to be broken in x86:
  http://sourceforge.net/p/libseccomp/mailman/message/33275762/

* Thu Jan 22 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.9.0-1
- new upstream release

* Fri Jan  9 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.9-4
- enable PIE

* Tue Jan  6 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.9-3
- Comply with system-wide crypto policies (#1179332)

* Mon Jan  5 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.9-2
- ocserv.service: depend on network-online.target (#1178760)
- enable seccomp (on platforms it is available)

* Thu Dec 11 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.9-1
- New upstream release

* Wed Nov 26 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.8-1
- New upstream release

* Mon Oct 27 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.7-1
- New upstream release

* Tue Sep 09 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.4-2
- Ship a default ocserv-script, which will put connecting clients
  into the internal firewall zone.

* Thu Aug 28 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.4-1
- New upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 08 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.2-3
- Rebuilt

* Tue Aug 05 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.2-2
- Rebuilt for new protobuf-c

* Mon Jul 28 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.2-1
- New upstream release

* Mon Jun 30 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.1-1
- New upstream release

* Fri Jun 06 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.0-2
- Generate certificates and private keys before the first run
- Corrected chroot path

* Mon Jun 02 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.0-1
- New upstream release

* Mon May 26 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.8.0pre0-1
- New upstream release

* Fri May 09 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.3.5-1
- New upstream release

* Fri May 02 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.3.4-1
- New upstream release

* Thu Apr 10 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.3.3-1
- New upstream release

* Fri Mar 14 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.3.2-1
- New upstream release

* Mon Feb 17 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.3.1-2
- new upstream release

* Wed Jan 29 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.3.0-2
- Generated certificates no longer carry an expiration date.

* Mon Jan 27 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.3.0-1
- Updated to latest upstream version (0.3.0).
- Certificates and private keys are auto-generated.

* Mon Dec 16 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.3-1
- Updated to latest upstream version (0.2.3).
- Corrected the chroot directory in config file.

* Fri Dec  6 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.1-6
- Added exception for the bundling of CCAN components.

* Wed Nov 13 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.1-5
- Updated the way PACKAGE-LICENSING is handled.

* Tue Nov 12 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.1-4
- Replaced gnulib's GPLv3+ license with GPLv2+. According to 
  http://lists.gnu.org/archive/html/bug-gnulib/2013-11/msg00062.html
  it was a gnulib bug.
- Reduced the number of applicable licenses by upgrading LGPLv2+ 
  components to GPLv2+.
- Added PACKAGE-LICENSING.

* Mon Nov 11 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.1-3
- Updated spec to add http-parser and pcllib as dependencies.
- Bundled library files are removed.
- Updated license information.

* Fri Nov  8 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.1-2
- Updated spec to account improvements suggested by Alec Leamas.

* Thu Nov  7 2013 Nikos Mavrogiannopoulos <nmav@redhat.com> - 0.2.1-1
- Initial version of the package
