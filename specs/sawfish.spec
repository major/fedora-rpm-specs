Name:           sawfish
Version:        1.13.0
Release:        10%{?dist}
Summary:        An extensible window manager for the X Window System
License:        GPL-2.0-or-later AND Artistic-2.0
# GPLv2+ is for Sawfish
# Artistic 2.0 is for sounds
URL:            http://sawfish.wikia.com/
Source0:        http://download.tuxfamily.org/%{name}/%{name}_%{version}.tar.bz2
Patch0:         bool.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gtk2-devel
BuildRequires:  libXft-devel
BuildRequires:  libXtst-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  gettext
BuildRequires:  kde-filesystem
BuildRequires:  desktop-file-utils
BuildRequires:  librep-devel >= 0.92.3
BuildRequires:  rep-gtk-devel >= 0.90.7
BuildRequires:  gdk-pixbuf2-xlib-devel
Requires:       control-center-filesystem
Requires:       hicolor-icon-theme
Requires:       kde-filesystem
Requires:       librep >= 0.92.3
Requires:       rep-gtk >= 0.90.7

%define rep_execdir %(pkg-config librep --variable=repcommonexecdir)


%description
Sawfish is an extensible window manager which uses a Lisp-based
scripting language.  All window decorations are configurable and the
basic idea is to have as much user-interface policy as possible
controlled through the Lisp language.  Configuration can be
accomplished by writing Lisp code in a personal .sawfishrc file, or
using a GTK+ interface.  Sawfish is mostly GNOME compliant


%package devel
Summary:        Development files for Sawfish
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig


%description devel
Include files for Sawfish development.


%prep
%autosetup -p1 -n %{name}_%{version}


%build
./autogen.sh --nocfg
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
gzip -9nf %{buildroot}%{_infodir}/sawfish*
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot}%{_libdir} -name \*.a -exec rm '{}' \;
find %{buildroot}%{_libdir} -name \*.la -exec rm '{}' \;
# Fix main.jl (sawfish-config) for rpmlint
sed -i -e '/^\#!/,/^!\#/d' %{buildroot}%{_datadir}/sawfish/lisp/sawfish/cfg/main.jl

rm %{buildroot}%{_datadir}/xsessions/sawfish-kde4.desktop
rm -rf %{buildroot}%{_datadir}/ksmserver
rm -rf %{buildroot}%{_datadir}/kde4

desktop-file-validate %{buildroot}%{_datadir}/applications/sawfish.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/sawfish-config.desktop
desktop-file-validate %{buildroot}%{_datadir}/gnome/wm-properties/sawfish-wm.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish-kde5.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish-lumina.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish-mate.desktop
desktop-file-validate %{buildroot}%{_datadir}/xsessions/sawfish-xfce.desktop

%files -f %{name}.lang
%license COPYING COPYING.SOUNDS
%doc README README.IMPORTANT doc/*
%{_bindir}/*
%{rep_execdir}/sawfish
%{_libdir}/sawfish
%{_datadir}/sawfish
%{_datadir}/applications/sawfish.desktop
%{_datadir}/applications/sawfish-config.desktop
%{_datadir}/gnome/wm-properties/sawfish-wm.desktop
%{_datadir}/xsessions/sawfish.desktop
%{_datadir}/xsessions/sawfish-kde5.desktop
%{_datadir}/xsessions/sawfish-lumina.desktop
%{_datadir}/xsessions/sawfish-mate.desktop
%{_datadir}/xsessions/sawfish-xfce.desktop
%{_datadir}/icons/hicolor/32x32/apps/sawfish-config.png
%{_mandir}/man1/sawfish*.gz
%{_infodir}/sawfish*


%files devel
%{_includedir}/sawfish
%{_libdir}/pkgconfig/sawfish.pc

# Note about rpmlint warning:
# W: devel-file-in-non-devel-package /usr/bin/sawfish-config
# This is sawfish GUI configurator, not devel config script.


%changelog
* Mon Jan 27 2025 Kim B. Heino <b@bbbs.net> - 1.13.0-10
- Fix build on Fedora 42
- Resolves: rhbz#2341322

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  7 2024 Miroslav Suchý <msuchy@redhat.com> - 1.13.0-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 13 2024 Kim B. Heino <b@bbbs.net> - 1.13.0-6
- Drop KDE4, fixes rhbz#2261678

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 19 2022 Kim B. Heino <b@bbbs.net> - 1.13.0-1
- Upgrade to 1.13.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb  2 2020 Kim B. Heino <b@bbbs.net> - 1.12.90-9
- Fix compile with new gcc

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.12.90-5
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.12.90-2
- Rebuilt for switch to libxcrypt

* Thu Aug 31 2017 Kim B. Heino <b@bbbs.net> - 1.12.90-1
- Upgrade to 1.12.90

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 13 2016 Kim B. Heino <b@bbbs.net> - 1.12.0-1
- Upgrade to 1.12.0

* Fri Aug  5 2016 Kim B. Heino <b@bbbs.net> - 1.11.91-1
- Upgrade to 1.11.91

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Kim B. Heino <b@bbbs.net> - 1.11.90-1
- Update to 1.11.90

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Richard Hughes <richard@hughsie.com> - 1.11-2
- Rebuilt for gdk-pixbuf2-xlib split

* Tue Nov  4 2014 Kim B. Heino <b@bbbs.net> - 1.11-1
- Update to 1.11

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Kim B. Heino <b@bbbs.net> - 1.10-1
- Update to 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 12 2013 Kim B. Heino <b@bbbs.net> - 1.9.91-1
- Update to 1.9.91

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Kim B. Heino <b@bbbs.net> - 1.9.90-1
- Update to 1.9.90

* Sun Nov 11 2012 Kim B. Heino <b@bbbs.net> - 1.9.1-1
- Update to 1.9.1

* Mon Aug 27 2012 Adam Jackson <ajax@redhat.com> 1.9.0-3
- sawfish-1.9.0-no-pangox.patch: Adapt to pangox removal

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Kim B. Heino <b@bbbs.net> - 1.9.0-1
- Update to 1.9.0
- Cleanup spec file

* Mon Mar 26 2012 Kim B. Heino <b@bbbs.net> - 1.8.92-1
- Update to 1.8.92

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  2 2011 Kim B. Heino <b@bbbs.net> - 1.8.91-2
- Rebuild

* Sun Oct  9 2011 Kim B. Heino <b@bbbs.net> - 1.8.91-1
- Update to 1.8.91

* Mon Aug 22 2011 Kim B. Heino <b@bbbs.net> - 1.8.90-1
- Update to 1.8.90

* Sat Jul 30 2011 Kim B. Heino <b@bbbs.net> - 1.8.1-2
- Rebuild for new librep

* Mon May  2 2011 Kim B. Heino <b@bbbs.net> - 1.8.1-1
- Update to 1.8.1

* Fri Apr 15 2011 Kim B. Heino <b@bbbs.net> - 1.8.0-2
- Updated spec file

* Thu Mar 31 2011 Kim B. Heino <b@bbbs.net> - 1.8.0-1
- Update to 1.8.0

* Sat Sep 25 2010 Kim B. Heino <b@bbbs.net> - 1.7.0-1
- fix url, icons, misc fixes

* Sun Jan 10 2010 Kim B. Heino <b@bbbs.net> - 1.6.2-1
- fix devel package, fix rpmlint warnings

* Sat Sep 05 2009 Kim B. Heino <b@bbbs.net>
- add dist-tag, update files list

* Fri Jan 18 2008 Christopher Bratusek <zanghar@freenet.de>
- several fixups

* Mon Jun 12 2000 John Harper <john@dcs.warwick.ac.uk>
- merged differences from RH spec file

* Mon Apr 24 2000 John Harper <john@dcs.warwick.ac.uk>
- s/sawmill/sawfish/

* Fri Sep 17 1999 John Harper <john@dcs.warwick.ac.uk>
- don't patch the Makefile

* Tue Sep 14 1999 Aron Griffis <agriffis@bigfoot.com>
- 0.6 spec file update: added buildroot
