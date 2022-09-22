Name:           libifp
Version:        1.0.0.2
Release:        34%{?dist}
Summary:        A general-purpose library-driver for iRiver's iFP portable audio players

License:        GPLv2
URL:            http://ifp-driver.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/ifp-driver/%{name}/%{version}-stable/%{name}-%{version}.tar.gz
Source1:        libifp.hotplug
Source2:        10-libifp.rules
# autoconf-2.69 breaks configure.in (likely configure.in is the broken part)
# Upstream is dead, so fix it here:
Patch0:         libifp-1.0.0.2-fix-broken-configure.in.diff
Patch1:         libifp-1.0.0.2-fix-broken-configure-again.diff

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  libusb-devel
BuildRequires:  systemd
BuildRequires: make

%description
libifp is a general-purpose library-driver for iRiver's iFP (flash-based)
portable audio players. The source code is pure C and is fairly portable.

Also included is a console app that uses the library.

%package        devel
Summary:        Headers and libraries for developing with libifp
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains headers and libraries for developing apps that use
libifp.

%prep
%autosetup

%build
autoreconf -fiv
%configure --with-libusb --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;
install -D -m 0755 %{SOURCE1} $RPM_BUILD_ROOT/sbin/libifp-hotplug
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_udevrulesdir}/10-libifp.rules

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/*
%{_libdir}/*.so.*
/sbin/*
%{_udevrulesdir}/*libifp.rules

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_mandir}/man3/*

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Conrad Meyer <cemeyer@uw.edu> - 1.0.0.2-20
- Move udev rules from /etc to /usr/lib (rh #1226691)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 28 2013 Conrad Meyer <cemeyer@uw.edu> - 1.0.0.2-16
- Update Source0 URL (sourceforge broke their download URLs again)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Apr 27 2013 Conrad Meyer <cemeyer@uw.edu> - 1.0.0.2-14
- Build with autoreconf -fiv because static copies of auto-generated scripts
  are fucking dumb
- Fix rh #925775
- add BR: autoconf, automake, libtool
- Patch configure.in which breaks with newer autotools

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0.2-7
- Autorebuild for GCC 4.3

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0.0.2-6
- rebuild for BuildID
- fix license tag

* Thu Jul 05 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0.0.2-5
- update udev rules to newer syntax (bug 246844)

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.0.0.2-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.0.0.2-3
- rebuild

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.0.2-2
- Rebuild for Fedora Extras 5

* Mon Aug 22 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.0.2-1
- Upstream update
- Disabled build of static libraries

* Thu Jul 14 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.0.1-2
- Modified for new udev

* Thu Jul  7 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net>
- Added Per Bjornsson's hotplug files

* Wed Jun 29 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 1.0.0.1-1
- Initial RPM release
