%global  basever 0.8.18

Name:    compiz-plugins-extra
Version: 0.8.18
Release: 14%{?dist}
Epoch:   1
Summary: Additional Compiz Fusion plugins for Compiz

# Automatically converted from old format: GPLv2+ and MIT - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:     https://gitlab.com/compiz/%{name}
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires: compiz-plugins-main-devel >= %{basever}
BuildRequires: compiz-bcop >= %{basever}
BuildRequires: gettext-devel
BuildRequires: perl(XML::Parser)
BuildRequires: mesa-libGLU-devel
BuildRequires: libXrender-devel
BuildRequires: libnotify-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: gtk2-devel
BuildRequires: automake
BuildRequires: make

Requires: compiz >= %{basever}
Requires: compiz-plugins-main%{?_isa} >= %{basever}
# https://gitlab.com/compiz/compiz-plugins-extra/-/issues/36
Patch0: compiz-plugins-extra-0.8.18-gcc-14-fix.patch

%description
The Compiz Fusion Project brings 3D desktop visual effects that improve
usability of the X Window System and provide increased productivity
though plugins and themes contributed by the community giving a
rich desktop experience.
This package contains additional plugins from the Compiz Fusion Project

%package devel
Summary: Development files for Compiz-Fusion
Requires: compiz-plugins-main-devel%{?_isa} >= %{basever}
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contain development files required for developing other plugins


%prep
%autosetup -p1 -n %{name}-v%{version}

%build
./autogen.sh
%configure

make %{?_smp_mflags} V=1

%install
%{make_install}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

%find_lang %{name}


%ldconfig_scriptlets


%files -f %{name}.lang
%doc COPYING AUTHORS NEWS
%{_libdir}/compiz/*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png
%{_datadir}/compiz/icons/hicolor/scalable/apps/*.svg

%files devel
%{_includedir}/compiz/
%{_libdir}/pkgconfig/compiz-*


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug  28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.8.18-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb  6 2024 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.18-10
- Fixed FTBFS with gcc-14
  Resolves: rhbz#2261043

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  9 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.18-1
- New version
  Related: rhbz#1891137

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr  2 2019 Jaroslav Škarvada <jskarvad@redhat.com> - 1:0.8.16-1
- New version
  Related: rhbz#1656467
- New URL

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.8.14-5
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-1
- update to 0.8.14 release
- Notification improvements.
- Fix a potential crash in animationaddon when restarting Compiz.
- Backport the Grid snap feature.
- Update catalan translation.
- drop usless macro %%global plugins from spec file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 12 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.1-1
- update to 0.8.12.1 release
- remove ExcludeArch: s390 s390x, they have libdrm now

* Sat Feb 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-1
- update to 0.8.12 release
- Add font family configuration in Group/Tab (Tabbar font), and
- Scale title filter plugins.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.9-1
- update to 0.8.9
- new upstream is at https://github.com/raveit65/compiz-plugins-extra
- remove upstreamed patches
- use libjpeg-turbo as build require
- remove old obsoletes for f15/16
- use modern make install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-15
- fix animation-addon plugin

* Wed Mar 18 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-14
- rebuild for f22

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 25 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-10
- fix build for aarch64
- add autoreconf command + necessary BR
- fix automake-1.13 build deprecations
- add BR gtk2-devel

* Sun Feb 10 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-9
- rework mate patch
- remove gconf usage
- switch to libnotify

* Sun Feb 10 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-8
- add compiz_primary-is-control.patch
- this will set all default configurations to pimary key
- fix (#909657)

* Sun Jan 13 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-7
- obsolete compiz-fusion-extra

* Sat Jan 12 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-6
- add ldconfig scriplets
- trailing whitespace from the Summary,Group,License and URL lines

* Sat Dec 22 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-5
- disable mateconf schemas
- remove rpm scriptlet
- remove mate subpackage
- remove copying part from mate patch

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-4
- build for fedora
- rename patch
- own include dir
- fix license information
- add basever

* Sat Sep 29 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-3
- add Epoch tag
- improve spec file

* Wed Sep 19 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.8-2
- add compiz-plugins-extra_mate.patch
- improve spec file

* Tue May 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.8-1
- build for mate

