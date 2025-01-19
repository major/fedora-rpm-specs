# Don't build the debugging utils by default.
%bcond_with utils

Name:		mISDN
Version:	2.0.22
Release:	16%{?dist}
Summary:	Userspace part of Modular ISDN stack

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://www.misdn.org/
Source0:	https://github.com/ISDN4Linux/mISDNuser/archive/v2.0.22.tar.gz
Source1:        mISDN.rules

Patch0:         mISDNuser-2.0.22-error.patch
Patch1:         %{name}-gcc11.patch
Requires(pre): shadow-utils

BuildRequires: make
BuildRequires: automake libtool autoconf
BuildRequires: flex

%{?ldconfig:Requires(post): %ldconfig}

%package devel
Summary:	Development files Modular ISDN stack
Requires:	mISDN = %{version}-%{release}

%package utils
Summary:	Debugging utilities for Modular ISDN stack

BuildRequires:  gcc
%description
mISDN (modular ISDN) is intended to be the new ISDN stack for the
Linux 2.6 kernel, from the maintainer of the existing isdn4linux
code. This package contains the userspace libraries required to
interface directly to mISDN.

%description devel
mISDN (modular ISDN) is intended to be the new ISDN stack for the
Linux 2.6 kernel, from the maintainer of the existing isdn4linux
code. This package contains the development files for userspace
libraries required to interface to mISDN, needed for compiling
applications which use mISDN directly such as OpenPBX.

%description utils
mISDN (modular ISDN) is intended to be the new ISDN stack for the
Linux 2.6 kernel, from the maintainer of the existing isdn4linux
code. This package contains test utilities for mISDN.

%prep
%setup -q -n mISDNuser-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
aclocal
libtoolize --force --automake --copy
automake --add-missing --copy
autoconf

%configure
make CFLAGS="$RPM_OPT_FLAGS"

%install
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d
install -m0644 %SOURCE1 $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d/mISDN.rules
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/udev/rules.d/45-misdn.rules

%post 
%{?ldconfig}
getent group misdn >/dev/null || groupadd -r misdn -g 31
getent passwd misdn >/dev/null || \
    useradd -r -g misdn -d / -s /sbin/nologin -u 31 \
    -c "Modular ISDN" misdn
exit 0


%ldconfig_postun

%files 
%_libdir/*.so.*
%doc COPYING.LIB LICENSE
%config(noreplace) %{_sysconfdir}/udev/rules.d/mISDN.rules
%exclude %{_sysconfdir}/misdnlogger.conf
%exclude %_bindir/*
%exclude %_sbindir/*

%files devel
%_includedir/mISDN
%_libdir/*.so
%exclude %_libdir/*.a
%exclude %_libdir/*.la

%if 0%{?with_utils}
%files utils
%config(noreplace) %{_sysconfdir}/misdnlogger.conf
%_bindir/*
%_sbindir/*
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.22-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 07 2020 Jeff Law <law@redhat.com> - 2.0.22-5
- Avoid array-bounds diagnostic from gcc-11

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 03 2020 Than Ngo <than@redhat.com> - 2.0.22-3
- Fix FTBFS

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Than Ngo <than@redhat.com> - 2.0.22-1
- update to 2.0.22

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 13 2015 Adam Jackson <ajax@redhat.com> 1.1.5-14
- Fix build with -Werror=format-security

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Jon Ciesla <limburgher@gmail.com> -1.1.5-9
- Migrate from fedora-usermgmt to guideline scriptlets.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.5-2
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> 1.1.5-1
- Update to 1.1.5

* Wed May 30 2007 David Woodhouse <dwmw2@infradead.org> 1.1.3-1
- Update to 1.1.3

* Fri Feb 23 2007 David Woodhouse <dwmw2@infradead.org> 1.1.0-1
- Update to 1.1.0

* Sat Dec 16 2006 David Woodhouse <dwmw2@infradead.org> 1.0.3-1
- Update to 1.0.3

* Tue Oct 17 2006 David Woodhouse <dwmw2@infradead.org> 0-1.cvs20061010
- Initial import
