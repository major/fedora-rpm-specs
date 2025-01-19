%undefine __cmake_in_source_build

Name: kxstitch
Summary: Program to create cross stitch patterns
Version: 2.2.0
Release: 7%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://userbase.kde.org/KXStitch
Source0: http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gettext-devel
BuildRequires:  gcc-c++
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  desktop-file-utils
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  extra-cmake-modules

%description
KXStitch can be used to create cross stitch patterns from scratch. It is also
possible to convert existing images to a cross stitch pattern or scan one with 
a Sane supported scanner.

%prep
%setup -q

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde || touch %{name}.lang

# move docs to Fedora standard directory
mkdir -p %{buildroot}/%{_docdir}/%{name}/
mv %{buildroot}/%{_datadir}/doc/HTML %{buildroot}/%{_docdir}/%{name}/
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/{128x128,16x16,256x256,48x48,64x64,scalable}/
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/22x22/apps/

%check
desktop-file-validate "%{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop"

%find_lang %{name} --with-kde

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_docdir}/%{name}/HTML/
%{_datadir}/%{name}/
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/*
%{_datadir}/icons/hicolor/22x22/actions/*
%{_datadir}/kxmlgui5/%{name}/
%{_datadir}/config.kcfg/%{name}.kcfg
%{_mandir}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.0-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 20 2023 Golo Fuchert <packages@golotop.de> - 2.2.0-1
- Update to 2.0.0, removed patches required for 2.1.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 2.1.1-9
- Rebuild for ImageMagick 7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-6
- rebuild for new ImageMagick

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 28 2019 Golo Fuchert <packages@golotop.de> - 2.1.1-2
- Not all files were uploaded correctly during last git session.

* Sun Aug 25 2019 Golo Fuchert <packages@golotop.de> - 2.1.1-1
- Update to 2.1.1, applying required patches that upstream is aware about.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 2.0.0-6
- Rebuild for new ImageMagick 6.9.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-3
- Remove obsolete scriptlets

* Tue Sep 05 2017 Adam Williamson <awilliam@redhat.com> - 2.0.0-2
- Rebuild for ImageMagick 6 reversion, drop ImageMagick 7 patch

* Mon Aug 28 2017 Michael Cronenworth <mike@cchtml.com> - 2.0.0-1
- Update to 2.0.0
- Rebuild for new ImageMagick

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Kevin Fenzi <kevin@scrye.com> - 1.2.0-9
- Rebuild for new ImageMagick

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 09 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.2.0-3
- Rebuild for ImageMagick.

* Wed Dec 03 2014 Golo Fuchert <packages@golotop.de> - 1.2.0-2
- removed differences between f21 and rawhide version of the spec file

* Mon Dec 01 2014 Golo Fuchert <packages@golotop.de> - 1.2.0-1
- Update to kde4 version

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.8.4.1-21
- update mime scriptlet
- fix icon scriptlets
- use %%find_lang for kde docs too
- omit locolor icons

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 27 2013 Golo Fuchert <packages@golotop.de> - 0.8.4.1-17
- Rebuilt for new ImageMagick
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 30 2013 Kevin Fenzi <kevin@scrye.com> - 0.8.4.1-15
- Rebuild for broken deps in rawhide

* Sun Mar 24 2013 Golo Fuchert <packages@golotop.de> - 0.8.4.1-14
- Rebuild for new ImageMagick

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.4.1-12
- Add libXi-devel dependency

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Tom Callaway <spot@fedoraproject.org> - 0.8.4.1-10
- rebuild for new ImageMagick

* Thu Mar 01 2012 Golo Fuchert <packages@golotop.de> - 0.8.4.1-9
- Rebuild for new libpng

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.8.4.1-7
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Nov 24 2010 Golo Fuchert <packages@golotop.de> - 0.8.4.1-5
- changed _defaultdocdir to _kde4_docdir
- instead of using sed on the faulty desktopfile, a new one is installed with a heredoc
- used name macro in the files list

* Mon Nov 08 2010 Golo Fuchert <packages@golotop.de> - 0.8.4.1-4
- Minor changes to summary and description

* Sat Nov 06 2010 Golo Fuchert <packages@golotop.de> - 0.8.4.1-3
- Made summary section more concise
- Dropped manual compression of manpage
- Removed BR qt3-devel, ImageMagick-devel, libjpeg-devel, kernel-headers
- Made the source URL compliant to the Packaging Guidelines
- Included updating of the GTK icon cache
- Made use of the SOURCE1 macro
- No inclusion of the upstream INSTALL instructions

* Wed Oct 27 2010 Golo Fuchert <packages@golotop.de> - 0.8.4.1-2
- Corrected the files section (folders were not owned correctly)

* Fri Oct 01 2010 Golo Fuchert <packages@golotop.de> - 0.8.4.1-1
- Initial packaging
