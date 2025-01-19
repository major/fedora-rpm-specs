%if 0%{?fedora} >= 41
%ifarch %{ix86}
%bcond_with     php
%else
%bcond_without  php
%endif
%else
%bcond_without  php
%endif

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_prefix}/%{_lib}/tcl%{tcl_version}}

Name:		owfs
Version:	3.2p4
Release:	10%{?dist}
Summary:	1-Wire Virtual File System

# some parts licensed differently, see http://owfs.org/index.php?page=license
License:	GPL-2.0-only
URL:		http://www.owfs.org/
Source0:	https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	owserver.xml
# install into 'vendor' perl directories; not suitable for upstream
Patch0:		owfs-0001-install-into-vendor-perl-directories.patch
Patch1: owfs-configure-c99.patch

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%{?systemd_requires}
BuildRequires: make
BuildRequires:	systemd
BuildRequires:	autoconf automake libtool
BuildRequires:	perl-macros

%description
OWFS is a user-space virtual file-system providing access to 1-Wire networks.


%package libs
Summary: Core library providing base functions to other OWFS modules

Requires: libusb-compat-0.1
Requires: libftdi
BuildRequires: automake autoconf libtool
BuildRequires: libusb-compat-0.1-devel libusb1-devel

%description libs
%{name}-libs is a core library providing base functions to other OWFS modules.


%package capi
Summary: C-API to develop third-part applications which access 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description capi
%{name}-capi library on top of libow providing an easy API to develop third-party
applications to access to 1-Wire networks.


%package devel
Summary: Files for development of OWFS applications
Requires: %{name}-libs%{?_isa} = %{version}
Requires: %{name}-capi%{?_isa} = %{version}

%description devel
This package contains the libraries and header files that are needed for
developing OWFS applications.


%package ownet
Summary: C-API to develop third-part applications which access 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description ownet
%{name}-ownet library provides an easy API to develop third-party applications
to access to 1-Wire networks. It doesn't depend on owlib, and only supports
remote-server connections. This library doesn't include any 1-wire adapter
support, except server connections.


%package fs
Summary: Virtual file-system on top of %{name}-libs providing access to 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: fuse >= 1.0
Requires: %{name}-server
BuildRequires: fuse-devel >= 1.0

%description fs
%{name}-fs is a virtual file-system on top of %{name}-libs providing
access to 1-Wire networks.


%package httpd
Summary: HTTP daemon providing access to 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-server

%description httpd
%{name}-httpd is a HTTP daemon on top of %{name} providing
access to 1-Wire networks.


%package ftpd
Summary: FTP daemon providing access to 1-Wire networks
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-server

%description ftpd
%{name}-ftpd is a FTP daemon on top of %{name} providing access to 1-Wire networks.


%package server
Summary: Back-end server (daemon) for 1-wire control
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: firewalld-filesystem
Requires(pre): shadow-utils
BuildRequires: firewalld-filesystem
BuildRequires: libftdi-devel

%description server
%{name}-server is the back-end component of the OWFS 1-wire bus control system.
owserver arbitrates access to the bus from multiple client processes. The
physical bus is usually connected to a serial or USB port, and other processes
connect to owserver over network sockets (TCP port). Communication can be local
or over a network.


%package tap
Summary: Packet sniffer for the owserver protocol
Requires: tcl >= 8.1
Requires: %{name}-tcl%{?_isa} = %{version}-%{release}
BuildRequires: zlib-devel

%description tap
%{name}-tap is a packet sniffer for the owserver protocol


%package mon
Summary: Statistics and settings monitor for owserver
Requires: tcl >= 8.1
Requires: %{name}-tcl%{?_isa} = %{version}-%{release}

%description mon
%{name}-mon is a graphical monitor of owserver’s status


%if %{with php}
%package php
Summary: PHP interface for the 1-wire file-system
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Requires: php-cli >= 4.3.0
BuildRequires: swig
BuildRequires: php-devel >= 4.3.0

%description php
%{name}-php is a php interface for the 1-wire file-system
%endif


%package tcl
Summary: Tcl interface for the 1-wire file-system
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: tcl >= 8.1
BuildRequires: tcl-devel >= 8.1

%description tcl
%{name}-tcl is a Tcl interface for the 1-wire file-system


%package shell
License: MIT
Summary: Light weight shell access to owserver and the 1-wire file-system

%description shell
%{name}-shell is 5 small programs to easily access owserver (and thus
the 1-wire system) from shell scripts. owdir, owread, owwrite, owget
and owpresent.


%prep
%setup -q
# Perl dirs
%patch -P0 -p1
%patch -P1 -p1

sed -i -e 's/) Makefile.PL/& INSTALLDIRS=vendor/' \
	module/swig/perl5/Makefile.am \
	module/ownet/perl5/Makefile.am


%build
./bootstrap
%configure --disable-rpath \
%if %{without php}
  --disable-owphp \
%endif
  --disable-owperl

# deal with RPATH
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
# deal with unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool


make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# remove files that won't be packaged
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
rm -f %{buildroot}%{perl_archlib}/auto/OW/.packlist
rm -f %{buildroot}%{perl_archlib}/auto/OWNet/.packlist
rm -f %{buildroot}%{_libdir}/libow.la
rm -f %{buildroot}%{_libdir}/libowcapi.la
rm -f %{buildroot}%{_libdir}/libownet.la
rm -f %{buildroot}%{php_extdir}/libowphp.la
rm -f %{buildroot}%{tcl_sitearch}/ow.la

rm -f %{buildroot}/usr/local/lib64/perl5/auto/OWNet/.packlist

install -Dm 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/services/owserver.xml

%pre server
# TODO: migrate to systemd-sysusers when guidelines are ready
getent group ow >/dev/null || groupadd -r ow
getent passwd ow >/dev/null || \
    useradd -r -g ow -d /var/empty -s /sbin/nologin \
    -c "1-wire file-system (OWFS) utilities account" ow
exit 0


%post fs
%systemd_post owfs.service

%post httpd
%systemd_post owhttpd.service

%post ftpd
%systemd_post owftpd.service

%post server
%systemd_post owserver.service owserver.socket
%firewalld_reload


%preun fs
%systemd_preun owfs.service

%preun httpd
%systemd_preun owhttpd.service

%preun ftpd
%systemd_preun owftpd.service

%preun server
%systemd_preun owserver.service owserver.socket


%postun fs
%systemd_postun_with_restart owfs.service

%postun httpd
%systemd_postun_with_restart owhttpd.service

%postun ftpd
%systemd_postun_with_restart owftpd.service

%postun server
%systemd_postun_with_restart owserver.service owserver.socket
%firewalld_reload


%files libs
%doc NEWS ChangeLog AUTHORS
%license COPYING
%{_libdir}/libow-*.so*
%{_mandir}/man3/*.3.*
%{_mandir}/man5/owfs.5.*
%{_mandir}/man5/owfs.conf.5.*


%files devel
%{_includedir}/owfs_config.h
%{_includedir}/owcapi.h
%{_includedir}/ownetapi.h
%{_libdir}/libow.so
%{_libdir}/libowcapi.so
%{_libdir}/libownet.so
%{_libdir}/pkgconfig/owcapi.pc
%{_mandir}/man?/*


%files capi
%{_libdir}/libowcapi-*.so*
%{_mandir}/man1/*owcapi.1.*


%files ownet
%{_libdir}/libownet-*.so*
%{_mandir}/man1/*ownet*.1.*


%files fs
%{_bindir}/owfs
%{_mandir}/man1/owfs.1.*
%{_unitdir}/owfs.service

%files ftpd
%{_bindir}/owftpd
%{_mandir}/man1/owftpd.1.*
%{_unitdir}/owftpd.service


%files httpd
%{_bindir}/owhttpd
%{_mandir}/man1/owhttpd.1.*
%{_unitdir}/owhttpd.service


%files shell
%{_bindir}/owdir
%{_bindir}/owexist
%{_bindir}/owread
%{_bindir}/owwrite
%{_bindir}/owget
%{_bindir}/owpresent
%{_bindir}/owusbprobe
%{_mandir}/man1/owshell.1.*
%{_mandir}/man1/owdir.1.*
%{_mandir}/man1/owread.1.*
%{_mandir}/man1/owget.1.*
%{_mandir}/man1/owpresent.1.*
%{_mandir}/man1/owwrite.1.*


%files server
%{_bindir}/owserver
%{_bindir}/owexternal
%{_mandir}/man1/owserver.1.*
%{_unitdir}/owserver.service
%{_unitdir}/owserver.socket
%{_prefix}/lib/firewalld/services/owserver.xml


%files tap
%doc COPYING
%{_bindir}/owtap
%{_mandir}/man1/owtap.1.*


%files mon
%doc COPYING
%{_bindir}/owmon
%{_mandir}/man1/owmon.1.*


%if %{with php}
%files php
%dir %{php_extdir}
%{php_extdir}/libowphp.so*
%{_datarootdir}/php/OWNet/ownet.php
%endif


%files tcl
%dir %{tcl_sitearch}/owtcl-*
%{tcl_sitearch}/owtcl-*/*
%{_mandir}/mann/owtcl.n.*
%{_mandir}/mann/ow.n.*



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Remi Collet <remi@fedoraproject.org> - 3.2p4-9
- rebuild for https://fedoraproject.org/wiki/Changes/php84

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Remi Collet <remi@remirepo.net> - 3.2p4-7
- disable PHP extension on 32-bit
  https://fedoraproject.org/wiki/Changes/php_no_32_bit

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 17 2023 Florian Weimer <fweimer@redhat.com> - 3.2p4-3
- Port configure script to C99 (with extensions)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.2p4-1
- update to the most recent version
- remove patch for issue fixed upstream
- switch URL to GitHub (sources are the same, project have migrated)

* Sun Aug 21 2022 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.2p3-11.1
- adjust to new libusb* package names (fixes rhbz#2113568)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 28 2021 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.2p3-8
- remove old trigerun

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.2p3-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 29 2020 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.2p3-4
- fix GCC10 -fno-common issue (rhbz#1794368)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.2p3-1
- update to latest 3.2p3
- restore PHP subpackage

* Mon Nov 12 2018 Miro Hrončok <mhroncok@redhat.com> - 3.2p2-5
- Remove python2 subpackage (#1627428)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.2p2-3
- add patch to include sys/sysmacros.h for major() (rhbz#(rhbz#1554314))

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2p2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.2p2-1
- update to latest version
- modernize systemd Requires

* Fri Jan 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1p5-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1p5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1p5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.1p5-4
- Rebuild due to bug in RPM (RHBZ #1468476)

* Mon Jul 03 2017 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.1p5-3
- add libftdi to -libs deps (reported by Ruben Kerkhof)

* Thu Jun 29 2017 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.1p5-2
- bump version to latest 3.1p5
- rename owfs-python to python2-owfs in accordance with
  https://python-rpm-porting.readthedocs.io/en/latest/naming-scheme.html

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1p4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 15 2016 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.1p4-1
- bump to upstream 3.1p4 release: drop upstreamed & backported patches
- remove incomplete python3 fragments from .spec: p3 support does not work
  in upstream; pyownet is recommended as python binding

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1p0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 04 2016 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.1p0-7
- disable owphp - won't build with rawhide's php7

* Thu Apr 21 2016 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.1p0-6
- backport patches for Type=notify

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1p0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.1p0-4
- backported fix for w1 kernel interface (rhbz #1294589)

* Thu Jan 14 2016 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.1p0-3
- owfs (FUSE module) started to fork in the meantime – update
  unit to accomodate that (rhbz #1294589)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1p0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.1p0-1
- new upstream release

* Tue Feb 10 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.0p0-2
- make -devel require C-API files, that what people expect
  (spotted by Ruben Kerkhof)

* Wed Feb 04 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 3.0p0-1
- new upstream release

* Wed Jan 07 2015 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p8-2
- add firewalld service definition for owserver

* Tue Oct 21 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p8-1
- new upstream release
- dropped tmpfiles snippet - /run/owfs is now managed by RuntimeDirectory=

* Thu Oct 09 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p7-1
- new upstream release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9p5.20140721git6d00fb1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p5.20140721git6d00fb1-1
- package snapshot
- use upstream systemd units
- enable owserver's socket activation
- fixed hardcoded tcl_sitearch, patch by Jaroslav Škarvada <jskarvad@redhat.com>

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9p5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 2.9p5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Thu May 15 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p5-1
- latest upstream release

* Tue Mar 25 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p3-1
- new upstream release

* Sun Feb 23 2014 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p2-1
- new upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9p1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 09 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p1-4
- add BR: systemd

* Wed Jul 03 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p1-3
- include main COPYING in -tap and -mon

* Mon Jul 01 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p1-2
- deal with unused-direct-shlib-dependency

* Thu Jun 20 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p1-1
- update to 2.9p1, dropping merged patches
- remove perl-owfs bits from .spec, for now
- correct python _OW.so perms 0775 -> 0755

* Thu Jun 13 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p0-4
- furher fixes:
  - BR: python2-devel for -python; drop -devel req
  - add tcl dep for owmon and owtap

* Fri May 10 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p0-3
- use /run/owfs instead of /mnt/1wire
  (ref: https://lists.fedoraproject.org/pipermail/devel/2013-May/182420.html)

* Mon May 06 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p0-2
- fix issues:
  - add Require: python-devel to python subpackage
  - synchronise ldconfig requires with glibc provides

* Mon Mar 25 2013 Tomasz Torcz <ttorcz@fedoraproject.org> - 2.9p0-1
- initial package, based on work by Serg Oskin and Vadim Tkachenko
