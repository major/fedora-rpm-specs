Name: sheepdog
Summary: The Sheepdog distributed storage system for KVM/QEMU
Version: 1.0.1
Release: 24%{?dist}
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License: GPL-2.0-only AND GPL-2.0-or-later
URL: http://sheepdog.github.io/sheepdog
Source0: https://github.com/sheepdog/sheepdog/archive/v1.0.1.tar.gz
Source1: sheepdog.service
Source2: sheepdog.timer
Source3: sheepdog

Patch0: sha1-extern.patch

%{?systemd_requires}

# Build bits
BuildRequires: make
BuildRequires: autoconf automake libtool systemd
BuildRequires: corosync corosynclib corosynclib-devel
BuildRequires: userspace-rcu-devel

# For sheepfs
BuildRequires: fuse-devel

%ifarch x86_64
BuildRequires: yasm
%endif

# corosync not available on these architectures
%if 0%{?rhel} >= 6
Excludearch: aarch64
Excludearch: ppc 
Excludearch: ppc64
Excludearch: ppc64le
%endif

%description
This package contains the Sheepdog server and the "dog" command line tool,
which offer a distributed object storage system for KVM.

%package devel
Summary: Header files for the Sheepdog distributed storage system
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License: GPL-2.0-only AND GPL-2.0-or-later
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files for libsheepdog.

%package libs
Summary: Libraries for the Sheepdog distributed storage system
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License: GPL-2.0-only AND GPL-2.0-or-later

%description libs
This package contains the libsheepdog shared library.

%prep
%setup -q
%patch -P0 -p1

%build
./autogen.sh

# TODO: add LTTng-ust support
%{configure} \
  --without-initddir \
  --without-systemdsystemunitdir \
  --disable-static

make %{_smp_mflags} V=1

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/libsheepdog.la
rm -f %{buildroot}/%{_libdir}/libsheepdog.a

mkdir -p %{buildroot}/%{_unitdir}
cp -a %{SOURCE1} %{buildroot}/%{_unitdir}/
cp -a %{SOURCE2} %{buildroot}/%{_unitdir}/

mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
cp -a %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig

%post
%systemd_post sheepdog.timer

%preun
%systemd_preun sheepdog.timer

%postun
%systemd_postun_with_restart sheepdog.timer

%files
%doc COPYING README
%{_bindir}/dog
%{_sbindir}/sheep
%{_sbindir}/sheepfs
%{_sbindir}/shepherd
%{_sysconfdir}/bash_completion.d/dog

%{_unitdir}/sheepdog.service
%{_unitdir}/sheepdog.timer
%config %{_sysconfdir}/sysconfig/sheepdog

%dir %{_localstatedir}/lib/sheepdog
%{_mandir}/man8/sheep.8*
%{_mandir}/man8/dog.8*
%{_mandir}/man8/sheepfs.8*

%files devel
%dir %{_includedir}/sheepdog
%{_includedir}/sheepdog/internal.h
%{_includedir}/sheepdog/list.h
%{_includedir}/sheepdog/sheepdog.h
%{_includedir}/sheepdog/sheepdog_proto.h
%{_includedir}/sheepdog/util.h

%files libs
%{_libdir}/libsheepdog.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.1-23
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.1-15
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Paolo Bonzini <pbonzini@redhat.com> - 1.0.1-12
- New patch sha1-extern.patch to fix FTBFS
- Delete obsolete patches

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Kevin Fenzi <kevin@scrye.com> - 1.0.1-7
- Rebuild for new corosync. Fixes bug #1559672

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Paolo Bonzini <pbonzini@redhat.com> - 1.0.1-2
- Introduce sheepdog.timer
- For EPEL7, disable on aarch64

* Mon Jan 09 2017 Paolo Bonzini <pbonzini@redhat.com> - 1.0.1-1
- Update to 1.0.1 (Resolves: #1396430)
- /usr/bin/collie is now /usr/bin/dog
- Added /usr/sbin/sheepfs and /usr/sbin/shepherd
- Revamped systemd spec file, added /etc/sysconfig/sheepdog

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 0.3.0-9
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.3.0-6
- Drop empty %%postun script.
- Drop INSTALL from docs.
- Fix bogus date in %%changelog.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 16 2012 Fabio M. Di Nitto <fdinitto@redhat.com> - 0.3.0-2
- Rebuild against new corosync (soname change).
- Add patch to fix build against new corosync headers.

* Thu Jan 12 2012 David Nalley <david@gnsa.us> - 0.3.0-1
- updating to 0.3.0

* Thu Nov 24 2011 David Nalley <david@gnsa.us> - 0.2.4-2
- adding systemd support

* Thu Nov 24 2011 David Nalley <david@gnsa.us> - 0.2.4-1
- updating to 0.2.4

* Sat Jun 04 2011 David Nalley <david@gnsa.us> - 0.2.3-2
- excluding ppc and ppc64 arch for el6

* Sat May 21 2011 David Nalley <david@gnsa.us> - 0.2.3-1
- updating to 0.2.3 to track upstream.

* Fri May 20 2011 David Nalley <david@gnsa.us> - 0.2.2-2
- removed -n from setup
- hardcoded version number. 
- changed lic from gpl to gplv2
- added INSTALL to doc
- added proper handling of initscripts

* Fri May 20 2011 Autotools generated version <nobody@nowhere.org> - 0.2.2-1
- Autotools generated version

