Name:           xautolock
Version:        2.2
Release:        38%{?dist}
Summary:        Launches a program when your X session has been idle

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://freshmeat.net/projects/xautolock/
Source0:        http://www.ibiblio.org/pub/Linux/X11/screensavers/%{name}-%{version}.tgz
Patch0:         xautolock-2.2-XSS-fix.patch
# All of Debian's patches look pretty sane, so let's swipe 'em
# All by Roland Stigge, except 14 by Aurelien Jarno
Patch1:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/10-fix-memory-corruption.patch
Patch2:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/11-fix-no-dpms.patch
Patch3:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/12-fix-manpage.patch
Patch4:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/13-fix-hppa-build.patch
Patch5:         https://sources.debian.org/data/main/x/xautolock/1:2.2-5.1/debian/patches/14-do-not-use-union-wait-type.patch

# See RHBZ#956271. Local change; worth upstreaming?
Patch100:       xautolock-longer-times.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  libXScrnSaver-devel

%description
A program that launches a given program when
your X session has been idle for a given time.


%prep
%autosetup -p1
xmkmf


%build
make %{?_smp_mflags} CDEBUGFLAGS="%{optflags}" CC="%{__cc}"


%install
make install install.man DESTDIR=%{buildroot} INSTALL="install -p"


%files
%doc Changelog License Readme Todo
%{_bindir}/xautolock
%{_mandir}/man1/xautolock.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2-37
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.2-23
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")
- Swipe all of Debian's patches - fix a build fail and other bugs

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Ben Boeckel <mathstuf@gmail.com> - 2.2-13
- Make maximum lock and kill times 24 hours (RHBZ#956271).

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 06 2008 Ian Weller <ianweller@gmail.com> 2.2-6
- Fix build section from FTFBS (bug 464962)

* Mon Mar 17 2008 Thomas Woerner <twoerner@redhat.com> 2.2-5
- honor XScreenSaver disabled state

* Sun Feb 03 2008 Ian Weller <ianweller@gmail.com> 2.2-4
- Fixed dates in changelog (2007 -> 2008)
- Fixed grouping
- Tightened up files list

* Sat Feb 02 2008 Ian Weller <ianweller@gmail.com> 2.2-3
- Fixed timestamp of Source0
- Removed redundant installation

* Sat Feb 02 2008 Ian Weller <ianweller@gmail.com> 2.2-2
- Shortened summary
- Fixed make flags
- Fixed installation of man page

* Sun Jan 27 2008 Ian Weller <ianweller@gmail.com> 2.2-1
- First package build.
