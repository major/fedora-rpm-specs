Summary: Music Player Daemon Library
Name: libmpd
Version: 11.8.17
Release: 28%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Url: http://gmpc.wikia.com/wiki/Gnome_Music_Player_Client
Source: http://download.sarine.nl/Programs/gmpc/11.8/libmpd-11.8.17.tar.gz
Patch0: libmpd-11.8.17-strndup.patch
Patch1: libmpd-c99.patch
BuildRequires:  gcc
BuildRequires: glib2-devel >= 2.16
BuildRequires: make

%package devel
Summary: Header files for developing programs with libmpd
Requires: %{name} = %{version}
Requires: pkgconfig

%description
libmpd is an abstraction around libmpdclient. It provides an easy and
reliable callback based interface to mpd.

%description devel
libmpd-devel is a sub-package which contains header files and static libraries
for developing program with libmpd.

%prep
%setup -q
%patch -P0 -p1 -b .strndup
%patch -P 1 -p1

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR="$RPM_BUILD_ROOT" install
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

%ldconfig_scriptlets

%files
%doc ChangeLog COPYING README
%{_libdir}/libmpd.so.1*

%files devel
%{_libdir}/libmpd.so
%{_libdir}/pkgconfig/libmpd.pc
%{_includedir}/libmpd-1.0

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 11.8.17-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 08 2024 Florian Weimer <fweimer@redhat.com> - 11.8.17-23
- Fix C compatibility issue (#2257240)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 11.8.17-6
- Fix build for http://fedoraproject.org/wiki/Changes/Harden_All_Packages

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Adrian Reber <adrian@lisas.de> - 11.8.17-1
- updated to 11.8.17

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 Adrian Reber <adrian@lisas.de> - 0.20.0-1
- updated to 0.20.0

* Wed Nov 25 2009 Adrian Reber <adrian@lisas.de> - 0.19.0-2
- updated to 0.19.0

* Mon Aug 03 2009 Adrian Reber <adrian@lisas.de> - 0.18.0-3
- added versioned BR for glib2-devel >= 2.16 (#514565)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 08 2009 Adrian Reber <adrian@lisas.de> - 0.18.0-1
- updated to 0.18.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 27 2008 Adrian Reber <adrian@lisas.de> - 0.16.1-1
- updated to 0.16.1

* Mon Feb 25 2008 Adrian Reber <adrian@lisas.de> - 0.15.0-3
- added patch to remove a few inline statements from
  functions which are actually not inline'd

* Fri Feb 15 2008 Adrian Reber <adrian@lisas.de> - 0.15.0-2
- rebuilt for gcc43

* Sun Dec 23 2007 Adrian Reber <adrian@lisas.de> - 0.15.0-1
- update to 0.15.0
- added BR glib2-devel

* Sun Nov 11 2007 Adrian Reber <adrian@lisas.de> - 0.14.0-1
- update to 0.14.0

* Sun Aug 26 2007 Adrian Reber <adrian@lisas.de> - 0.13.0-2
- rebuilt

* Sun Mar 25 2007 Adrian Reber <adrian@lisas.de> - 0.13.0-1
- update to 0.13.0

* Sat Nov 25 2006 Adrian Reber <adrian@lisas.de> - 0.12.0-3
- added requires pkgconfig to -devel package

* Sat Nov 25 2006 Adrian Reber <adrian@lisas.de> - 0.12.0-2
- small changes for FE submission

* Mon Mar 27 2006 Jan "Yenya" Kasprzak <kas@fi.muni.cz> 0.12.0-1
- initial build
