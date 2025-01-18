
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Summary: Base libraries for GGZ gaming zone
Name:    ggz-base-libs
Version: 0.99.5
Release: 40%{?dist}

# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL: http://www.ggzgamingzone.org/
#Source0: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/ggz-base-libs-snapshot-%{version}.tar.gz
Source0: http://mirrors.ibiblio.org/pub/mirrors/ggzgamingzone/ggz/snapshots/ggz-base-libs-snapshot-%{version}.tar.gz

# upstreamable patches, fix --with-tls=NSS
# https://bugs.ggzgamingzone.org/mantis/view.php?id=114
Patch50: ggz-base-libs-snapshot-0.99.5-tls_nss3.patch

Patch99: ggz-base-libs-0.99.5-fedora-c99.patch

Obsoletes: libggz < 1:0.99.5
Provides:  libggz = 1:%{version}-%{release}

Obsoletes: ggz-client-libs < 1:0.99.5
Provides:  ggz-client-libs = 1:%{version}-%{release}

Source1: ggz.modules
# see http://fedoraproject.org/wiki/PackagingDrafts/GGZ
Source2: macros.ggz

BuildRequires:  gcc
BuildRequires: expat-devel
BuildRequires: gettext
BuildRequires: libgcrypt-devel >= 1.4
BuildRequires: nss-devel
BuildRequires: pkgconfig
BuildRequires: make


%description
GGZ (which is a recursive acronym for GGZ Gaming Zone) develops libraries,
games and game-related applications for client-server online gaming. Player
rankings, game spectators, AI players and a chat bot are part of this effort.

%package devel
Summary: Development files for %{name}
Obsoletes: libggz-devel < 1:0.99.5
Obsoletes: ggz-client-libs-devel < 1:0.99.5
Provides: libggz-devel = 1:%{version}-%{release}
Provides: ggz-client-libs-devel = 1:%{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
# %{_sysconfdir}/rpm ownership
Requires: rpm
%description devel
%{summary}.


%prep
%setup -q -n %{name}-snapshot-%{version}

%patch -P50 -p1 -b .tls_nss3
%patch -P99 -p1

%if 0 
# some auto*/libtool love to quash rpaths
rm -f m4/libtool.m4 m4/lt*
#libtoolize -f --automake
#aclocal -Im4
autoreconf -i -f
%else
# avoid lib64 rpaths, quick-n-dirty
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif
%endif


%build
%configure \
  --disable-debug \
  --disable-static \
  --with-gcrypt \
  --with-tls=NSS

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# GGZCONFDIR stuff
install -D -m644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/ggz.modules
mkdir -p %{buildroot}%{_sysconfdir}/ggz.modules.d
# GGZDATADIR
mkdir -p %{buildroot}%{_datadir}/ggz
# GGZGAMEDIR
mkdir -p %{buildroot}%{_libdir}/ggz
# RPM macros
install -D -m644 -p %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.ggz

%find_lang ggzcore_snapshot-%{version}
%find_lang ggz-config
cat ggz*.lang >> all.lang

# unpackaged files
rm -f %{buildroot}%{_libdir}/lib*.la


%check
make check ||:


%ldconfig_scriptlets

%files -f all.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%verify(not size md5 mtime) %config(noreplace) %{_sysconfdir}/ggz.modules
%dir %{_sysconfdir}/ggz.modules.d
# GPLv2+
%{_bindir}/ggz-config
%dir %{_datadir}/ggz
%dir %{_libdir}/ggz
%{_libdir}/libggzmod.so.4*
%{_mandir}/man5/ggz.modules.5*
# LGPLv2+
%{_libdir}/libggz.so.2*
%{_libdir}/libggzcore.so.9*
%{_mandir}/man6/ggz*
%{_mandir}/man7/ggz*
%{_sysconfdir}/xdg/menus/applications-merged/ggz.merge.menu
%{_sysconfdir}/xdg/menus/ggz.menu
%{_datadir}/desktop-directories/ggz*.directory

%files devel
%{rpm_macros_dir}/macros.ggz
# GPLv2+
%{_includedir}/ggzmod.h
%{_libdir}/libggzmod.so
%{_libdir}/pkgconfig/ggzmod.pc
%{_mandir}/man3/ggzmod_h.3*
# LGPLv2+
%{_includedir}/ggz.h
%{_includedir}/ggz_*.h
%{_libdir}/libggz.so
%{_libdir}/pkgconfig/libggz.pc
%{_mandir}/man3/ggz*
%{_includedir}/ggzcore.h
%{_libdir}/libggzcore.so
%{_libdir}/pkgconfig/ggzcore.pc
%{_mandir}/man3/ggzcore_h.3*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 0.99.5-39
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar  2 2023 DJ Delorie <dj@redhat.com> - 0.99.5-34
- Port configure script to C99 (#2175046)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Tomáš Mráz <tmraz@redhat.com> - 0.99.5-15
- Rebuild for new libgcrypt

* Sat Feb 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.99.5-14
- -devel: use %%_rpmconfigdir/macros.d (where supported)
- .spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 18 2012 Rex Dieter <rdieter@fedoraproject.org> 0.99.5-10
- make %%check non-fatal

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 28 2010 Rex Dieter <rdieter@fedoraproject.org> 0.99.5-7
- --with-tls=NSS (#347021)
- %%check: make check

* Sat Dec 12 2009 Rex Dieter <rdieter@fedoraproject.org> 0.99.5-6
- Verify Check ( rpm -V ggz-client-libs ) (#487984)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 02 2009 Rex Dieter <rdieter@fedoraproject.org> 0.99.5-4
- own %%{_sysconfdir}/ggz.modules.d
- kill rpaths (again)

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> 0.99.5-3
- conflict with ggz-client-libs, include epoch in Obsoletes/Provides: 
  libggz ggz-client-libs (#491638)

* Tue Mar 10 2009 Rex Dieter <rdieter@fedoraproject.org> 0.99.5-2
- drop --with-tls (busted), fixes f11+ build

* Fri Feb 06 2009 Rex Dieter <rdieter@fedoraproject.org> 0.99.5-1
- ggz-base-libs-snapshot-0.99.5
- Obsoletes/Provides: libggz,ggz-client-libs

* Sun Aug 24 2008 Rex Dieter <rdieter@fedoraproject.org> 0.99.4-1
- ggz-client-libs-snapshot-0.99.4

* Sun Feb 17 2008 Rex Dieter <rdieter@fedoraproject.org> 0.0.14.1-1
- ggz 0.0.14.1

* Fri Feb 08 2008 Rex Dieter <rdieter@fedoraproject.org> 0.0.14-6
- include %%_sysconfdir/rpm/macros.ggz

* Wed Feb 06 2008 Rex Dieter <rdieter@fedoraproject.org> 0.0.14-5
- %%config(noreplace) %%_sysconfdir/ggz.modules (#431726)
- own %%_datadir/ggz, %%_libdir/ggz

* Sat Nov 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.0.14-4
- --disable-ggzwrap (for now, until multilib, licensing is sorted out)
- move ggz-config to main pkg (runtime management of ggz modules)
- clarify GPL vs. LGPL bits
- drop BR: automake libtool

* Fri Nov 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.0.14-3
- try (no)rpath trick #2: modify configure

* Thu Nov 08 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.0.14-2
- libtoolize to avoid rpaths
- -devel +%%defattr

* Thu Sep 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.0.14-1
- cleanup

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
