%global _x11fontdir %{_datadir}/X11/fonts
%global legacydir %{_x11fontdir}/dockapp

Name:           libdockapp
Version:        0.7.3
Release:        13%{?dist}
Summary:        DockApp Development Standard Library

License:        MIT
URL:            https://www.dockapps.net/libdockapp
Source0:        https://www.dockapps.net/download/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libXpm-devel libXext-devel libX11-devel

%description
LibDockApp is a library that provides a framework for developing dockapps. 
It provides functions and structures to define and display command-line 
options, create a dockable icon, handle events, etc.

The goal of the library is to provide a simple, yet clean interface and 
standardize the ways in which dockapps are developed. A dockapp developed 
using libDockApp will automatically behave well under most window 
managers, and especially well under Window Maker.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       libXpm-devel
Requires:       libX11-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        fonts
Summary:        Fonts provided with %{name}
Requires:       mkfontdir
BuildRequires:  xorg-x11-font-utils mkfontdir
BuildRequires:  fontconfig
BuildRequires: make

%description fonts
Bitmap X fonts provided with libdockapp.


%prep
%autosetup
find . -depth -type d -name CVS -exec rm -rf {} ';'

%build
%configure --disable-static --without-examples --disable-rpath
%make_build


%install
%make_install XFONTDIR=%{builddir}%{_x11fontdir}
rm %{buildroot}%{_libdir}/libdockapp.la

rm -rf __examples_dist
cp -a examples __examples_dist
rm __examples_dist/Makefile*

install -m 0755 -d %{buildroot}%{_sysconfdir}/X11/fontpath.d
install -m 0755 -d %{buildroot}%{legacydir}
ln -sf %{legacydir} %{buildroot}%{_sysconfdir}/X11/fontpath.d

%files
%doc AUTHORS BUGS COPYING NEWS README
%{_libdir}/libdockapp.so.3
%{_libdir}/libdockapp.so.3.*

%files devel
%doc __examples_dist/*
%{_includedir}/libdockapp
%{_libdir}/libdockapp.so
%{_libdir}/pkgconfig/dockapp.pc

%files fonts
%{legacydir}
%{_sysconfdir}/X11/fontpath.d/dockapp
%{_x11fontdir}/misc/fonts.dir
%{_x11fontdir}/misc/luxel-ascii-06x09.pcf.gz
%{_x11fontdir}/misc/seg7-ascii-05x07.pcf.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 04 2021 Peter Hutterer <peter.hutterer@redhat.com> 0.7.3-4
- BuildRequire mkfontdir in addition to xorg-x11-font-utils (#1933542)
- Require only mkfontdir, not xorg-x11-font-utils (#1933542)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Jani Juhani Sinervo <jani@sinervo.fi> - 0.7.3-1
- Update to 0.7.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon May  5 2008 Patrice Dumas <pertusus@free.fr> 0.6.2-1
- update to 0.6.2

* Sat Feb  2 2008 Patrice Dumas <pertusus@free.fr> 0.6.1-6
- more portable stdincl patch

* Thu Dec 27 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-5
- minor cleanups

* Sun Sep 30 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-4
- new fontpath.d configuraton mechanism, change by ajax, Adam Jackson

* Thu May 24 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-3
- fix libtool bug on ppc64

* Wed Jan 10 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-2
- don't ship the empty fonts.alias

* Fri Jan  5 2007 Patrice Dumas <pertusus@free.fr> 0.6.1-1
- Initial release
