%global  basever 0.8.16

Name:           emerald
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Version:        0.8.18
Release:        12%{?dist}
Epoch:          1
Summary:        Themeable window decorator and compositing manager for Compiz
URL:            https://gitlab.com/compiz/%{name}
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

Requires:       compiz >= %{basever}

# fix rhbz (#1291897)
Obsoletes: compiz-xfce < %{epoch}:%{version}-%{release}
Obsoletes: compiz-lxde < %{epoch}:%{version}-%{release}
%if 0%{?fedora} < 24
Provides:  compiz-xfce = %{epoch}:%{version}-%{release}
Provides:  compiz-lxde = %{epoch}:%{version}-%{release}
%endif

BuildRequires:  compiz-devel >= %{basever}
BuildRequires:  libwnck3-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  gettext-devel
BuildRequires:  libXres-devel
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires: make


%description
Emerald is themeable window decorator and compositing
manager for Compiz.

%package devel
Summary: Development files for emerald
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: pkgconfig

%description devel
The emerald-devel package provides development files
for emerald, the themeable window decorator for Compiz.


%prep
%setup -q -n %{name}-v%{version}

%build
./autogen.sh
%configure \
    --with-gtk=3.0 \
    --disable-mime-update

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1


%install
%{make_install}

find %{buildroot} -type f -name "*.a" -o -name "*.la" | xargs rm -f

rm -f %{buildroot}%{_datadir}/applications/compiz-*-emerald.desktop
rm -f %{buildroot}%{_datadir}/applications/emerald-decorator.desktop
rm -f %{buildroot}%{_bindir}/compiz-*-emerald

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/emerald-theme-manager.desktop


%ldconfig_scriptlets


%files -f %{name}.lang
%doc COPYING NEWS
%{_bindir}/*
%dir %{_libdir}/emerald
%dir %{_libdir}/emerald/engines
%{_libdir}/emerald/engines/*.so
%{_libdir}/libemeraldengine.so.*
%{_datadir}/applications/emerald-theme-manager.desktop
%dir %{_datadir}/emerald
%dir %{_datadir}/emerald/theme
%{_datadir}/emerald/theme/*
%{_datadir}/emerald/settings.ini
%{_datadir}/mime-info/emerald.mime
%{_datadir}/mime/packages/emerald.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/*.1.*

%files devel
%{_includedir}/emerald/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libemeraldengine.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.8.18-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.18-4
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

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:0.8.14-5
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-2
- fixes rhbz (#1448809, #1399783, #1406234)

* Thu Apr 20 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1:0.8.14-1
- update to 0.8.14 release
- Fix wrong border extents.
- Fix oversized buttons.
- Fix crash when special characters are displayed in titlebar.
- Fix various GTK+ problems.
- Respect GTK+ double-click speed.
- Allow configurable middle-click titlebar actions.
- Update Catalan and French translations.
- remove ExcludeArch for s390 s390x, libdrm is available there
- modernize spec file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Apr 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.4-1
- update to 0.8.12.4 release
- build with gtk+3

* Wed Mar 16 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.2-1
- 0.8.12.2 release
- fix memleaks

* Thu Mar 03 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12.1-1
- update to 0.8.12.1 release

* Sun Feb 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-2
- fix https://github.com/raveit65/emerald/issues/1

* Sat Feb 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.12-1
- update to 0.8.12 release
- Fix resize glitches on some GPU's.
- Fix wrong size of button tooltips when hovering from one to another.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.9-3
- remove start scripts

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.9-2
- fix rhbz (#1291897)

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.9-1
- update to 0.8.9
- new upstream is at https://github.com/raveit65/emerald
- remove upstreamed patches
- add scriptlets and adjust file section for emerald start scripts
- use modern make install macro

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-13
- rebuild for f22

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 1:0.8.8-12
- fix icon scriptlet, update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 25 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-8
- fix build for aarch64
- re-work mate.patch again
- add libtool BR for autoreconf
- fix automake-1.13 build deprecations
- re-work DSO.patch

* Wed Feb 13 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-7
- rework mate-patch

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 26 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-5
- fix license information
- fix rpm scriptlets
- add icon cache rpm scriptlet
- rename DSO patch

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1:0.8.8-4
- build for fedora
- review package
- fix unused-direct-shlib-dependency
- add basever
- add Epoch tag

* Mon Oct 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.8-3
- add patches from Jasmine Hassan jasmine.aura@gmail.com

* Wed Sep 19 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.8-2
- improve spec file
- add desktop-file-validate for emerald-theme-manager.desktop

* Tue May 15 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.8.8-1
- build for mate

* Sun Nov 14 2010 Leigh Scott <leigh123linux@googlemail.com> - 0.8.4-7
- apply more upstream gtk deprecated fixes

