# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.28

# Settings used for build from snapshots.
%{!?rel_build:%global commit 7ba7e03f4d5e2ecd3c77f9d9394521b7608ca05f}
%{!?rel_build:%global commit_date 20131212}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:          eom
Version:       %{branch}.0
%if 0%{?rel_build}
Release:       6%{?dist}
%else
Release:       0.22%{?git_rel}%{?dist}
%endif
Summary:       Eye of MATE image viewer
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ 
URL:           http://mate-desktop.org 

# for downloading the tarball use 'spectool -g -R eom.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires: desktop-file-utils
BuildRequires: exempi-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk3-devel
BuildRequires: ImageMagick-devel
BuildRequires: lcms2-devel
BuildRequires: libexif-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpeas1-devel
BuildRequires: librsvg2-devel
BuildRequires: libxml2-devel
BuildRequires: mate-common
BuildRequires: make
BuildRequires: mate-desktop-devel
BuildRequires: zlib-devel

#fix rhbz (#1008249)
Requires:      mate-desktop-libs
Requires:      libpeas-loader-python3

%description
The Eye of MATE (eom) is the official image viewer for the
MATE desktop. It can view single image files in a variety of formats, as
well as large image collections.
Eye of Mate is extensible through a plugin system.

%package devel
Summary:  Support for developing plugins for the eom image viewer
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for eom


%prep
%if 0%{?rel_build}
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

%if 0%{?rel_build}
#NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure \
   --with-x \
   --disable-schemas-compile \
   --enable-introspection=yes \
   --enable-thumbnailer \
   --without-gdk-pixbuf-thumbnailer
           
make %{?_smp_mflags} V=1

%install
%{make_install}

desktop-file-install                               \
  --delete-original                                \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
$RPM_BUILD_ROOT%{_datadir}/applications/eom.desktop

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_mandir}/man1/*
%{_bindir}/eom
%{_bindir}/eom-thumbnailer
%dir %{_libdir}/eom
%dir %{_libdir}/eom/plugins
%{_libdir}/eom/plugins/*
%{_libdir}/girepository-1.0/Eom-1.0.typelib
%{_datadir}/applications/eom.desktop
%{_datadir}/eom/
%{_datadir}/icons/hicolor/*
%{_datadir}/glib-2.0/schemas/org.mate.eom.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.eom.enums.xml
%{_datadir}/metainfo/eom.appdata.xml
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/eom-thumbnailer.thumbnailer

%files devel
%{_libdir}/pkgconfig/eom.pc
%dir %{_includedir}/eom-2.20
%dir %{_includedir}/eom-2.20/eom
%{_includedir}/eom-2.20/eom/*.h
%{_datadir}/gtk-doc/html/eom/
%{_datadir}/gir-1.0/*.gir


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-5
- another rebuild for unannounced so-name bump of image-magick !

* Mon Nov 11 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-4
- rebuild for unannounced so-name bump of image-magick !

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.28.0-3
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 22 2024 Wolfgang Ulbrich <fedora@raveit.de> - 1.28.0-1
- update to 1.28.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-3
- update spec file for using libpeas1
- fix building with libxml 2.12.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun May 07 2023 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.1-1
- update to 1.26.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Robert Scheck <robert@fedoraproject.org> - 1.26.0-9
- Fix building with ImageMagick 7 (#2159313)

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.26.0-8
- Rebuild for ImageMagick 7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Robert Scheck <robert@fedoraproject.org> - 1.26.0-6
- Require libpeas-loader-python3 also for RHEL 8 and 9

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-4
- let run autogen

* Mon Dec 06 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-3
- add some upstream patches
- use https://github.com/mate-desktop/eom/commit/cd3df0e
- use https://github.com/mate-desktop/eom/pull/319

* Fri Oct 15 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-2
- rebuild for ImageMagick soname bump

* Wed Aug 04 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- update to 1.26.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 23 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.2-1
- update to 1.24.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 16 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.1-1
- update to 1.24.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 15 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-2
- add upstream patches
- update authors in about
- fix pt and pt_BR locale translation issues

* Mon Feb 10 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.24.0-1
- update to 1.24.0

* Mon Feb 03 2020 Wolfgang Ulbrich <fedora@raveit.de> - 1.23.2-1
- update to 1.23.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.2-1
- update to 1.22.2

* Fri Sep 06 2019 Nikola Forró <nforro@redhat.com> - 1.22.1-3
- rebuilt for exempi 2.5.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.1-1
- update 1.22.1 release

* Mon Mar 04 2019 Wolfgang Ulbrich <fedora@raveit.de> - 1.22.0-1
- update to 1.22.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 15 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.2-1
- update to 1.20.2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.1-1
- update to 1.20.1 release

* Sun May 13 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-3
- Fix offset coordinates when transforming SVG images on HiDPI
- https://github.com/mate-desktop/eom/commit/530d7cb
- use libpeas-loader-python3 for all branches
- https://github.com/mate-desktop/eom/commit/c94e091

* Wed Apr 25 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-2
- Scale images correctly with HIDPI
- drop IconCache scriptlet

* Sat Feb 10 2018 Wolfgang Ulbrich <fedora@raveit.de> - 1.20.0-1
- update to 1.20 release
- drop desktop-database rpm scriptlet
- drop GSettings Schema rpm scriptlet
- switch to using autosetup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.1-1
- update to 1.19.1

* Wed Aug 09 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-4
- remove virtual provides

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.19.0-1
- update to 1.19.0 release

* Mon May 08 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.2-1
- update to 1.18.2

* Wed Apr 05 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.1-1
- update to 1.18.1

* Tue Mar 14 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Wed Feb 08 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.2-2
- use BR libpeas-loader-python only for fedora

* Mon Jan 09 2017 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.2-1
- update to 1.17.2
- add BR libpeas-loader-python
- fix running in wayland session

* Mon Dec 12 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.1-1
- update to 1.17.1 release

* Tue Dec 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update 1.17.0 release

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Wed Sep 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.1-1
- update to 1.15.1 release

* Thu Jun 09 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release
- switch to gtk+3

* Sat May 21 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.1-1
- update to 1.14.1 release

* Wed Apr 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.14.0-1
- update to 1.14.0 release

* Mon Feb 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.1-1
- update to 1.13.1 release

* Sun Feb 07 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.13.0-1
- update to 1.13.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.1-1
- update to 1.12.1 release
- fix gir compilation

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Thu Oct 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.0-1
- update to 1.11.0 release

* Thu Oct 08 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.5-1
- update to 1.10.5 release

* Tue Jul 14 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.3.1
- update to 1.10.3 release
- remove upstreamed patches

* Sat Jun 27 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-2
- fix rhbz (#1230244)

* Wed Jun 17 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-1
- update to 1.10.2 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1.2
- fix broken translations in gsettings key
- fix issue in finen and korean laguages
- fix build with --strict option
- fix a eom-critical warning

* Fri Jun 12 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1.1
- update to 1.10.1 release

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release
- fix glib-compile-schemas

* Sun Apr 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.90-1
- update to 1.9.90 release
- add BR cairo-gobject-devel
- disable introspection build temporarily

* Thu Jan 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release
- enable inrospection build

* Sun Oct 26 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- update to 1.9.0
- support gnome-software

* Tue Sep 30 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.1-1
- update to 1.8.1 release
- fix obsoletes/provides

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0.3
- fix obsoletes/provides for -devel subpackage

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Thu Feb 13 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-1
- update to 1.7.0
- add --with-x configure flag
- use -devel subpackage for release builds

* Wed Dec 18 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.0-0.1.git20131212.7ba7e03
- rename mate-image-viewer to eom
- use latest git snapshot
- make maintainers life easier and use better git snapshot usage, thanks to Björn Esser
- use --with-gnome --all-name for find locale

* Fri Dec 06 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0 from mate-desktop git

* Mon Sep 16 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-2
- add mate-desktop-libs runtime require, fix rhbz (#1008249)
- remove gsettings-desktop-schemas BR and runtime require
- add BR pkgconfig(zlib)
- cleanup BRs
- update descriptions
- use modern make install macro
- remove needless check for "*.a" files
- remove needless --with-gnome from find locale
- remove needless 'save space by linking identical images in translated docs'
- remove needless gsettings convert file
- fix rpm scriptlets
- add omf directory
- own directories
- add python-libdir patch

* Mon Jul 29 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.1-1
- Update to latest 1.6.1 stable release.

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.5.0-3
- rebuild due to "jpeg8-ABI" feature drop

* Tue Nov 06 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-2
- Fix scriptlet mistake

* Mon Nov 05 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- Initial build

