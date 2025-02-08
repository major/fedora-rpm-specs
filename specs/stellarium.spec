Name:           stellarium
Version:        24.4
Release:        4%{?dist}
Summary:        Photo-realistic nightsky renderer

License:        GPL-2.0-or-later
URL:            http://www.stellarium.org
Source0:        https://github.com/Stellarium/stellarium/archive/v%{version}/stellarium-%{version}.tar.gz

# Disabled due to lconvert segfaulting on armv7hl
# https://bugzilla.redhat.com/show_bug.cgi?id=1884681
%if 0%{?fedora} > 32
ExcludeArch:    armv7hl
%endif

BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtlocation-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtcharts-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  gettext-devel
BuildRequires:  boost-devel
BuildRequires:  glib2-devel
BuildRequires:  perl-podlators
BuildRequires:  libappstream-glib
BuildRequires:  CalcMySky-devel >= 0.2.1
%if 0%{?fedora} && 0%{?fedora} < 38
BuildRequires:  libindi-devel
%endif
BuildRequires:  QXlsx-devel
BuildRequires:  libnova-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  exiv2-devel
BuildRequires:  NLopt-devel

Requires:       %{name}-data = %{version}-%{release}

%description
Stellarium is a real-time 3D photo-realistic nightsky renderer. It can
generate images of the sky as seen through the Earth's atmosphere with
more than one hundred thousand stars from the Hipparcos Catalogue,
constellations, planets, major satellites and nebulas.


%package        data
Summary:        Data files for Stellarium
BuildArch:      noarch

%description    data
Data files for the stellarium package.


%prep
%setup -q

%build
# Kill USE_PLUGIN_TELESCOPECONTROL support due to libindi 2 incompatibility
%{cmake} -DCMAKE_BUILD_TYPE=Release -DQT6_LIBS=%{_libdir}/qt6 -DCPM_USE_LOCAL_PACKAGES=yes -DENABLE_SHOWMYSKY=yes \
%if 0%{?fedora} >= 38
   -DUSE_PLUGIN_TELESCOPECONTROL=no \
%endif
   %{nil}
%cmake_build

%install
%cmake_install

#Fix appdata
sed -i /url/d $RPM_BUILD_ROOT%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml

# Fix mimetype icon: https://github.com/Stellarium/stellarium/pull/3011
sed -i -e 's/<icon/<generic-icon/' $RPM_BUILD_ROOT%{_datadir}/mime/packages/stellarium.xml

# Remove unwanted files
rm -f $RPM_BUILD_ROOT%{_datadir}/stellarium/data/*.ttf
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/stellarium.xpm
rm -f $RPM_BUILD_ROOT%{_datadir}/stellarium/data/stellarium.ico

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.stellarium.Stellarium.desktop

%files
%license COPYING
%doc ChangeLog CREDITS.md README.md
%{_bindir}/stellarium
%{_datadir}/applications/org.stellarium.Stellarium.desktop
%{_datadir}/icons/hicolor/*/apps/stellarium.png
%{_datadir}/metainfo/org.stellarium.Stellarium.appdata.xml
%{_mandir}/man1/stellarium.1*
%{_datadir}/mime/packages/stellarium.xml

%files data
%license COPYING
%{_datadir}/stellarium

%changelog
* Thu Feb 06 2025 Björn Esser <besser82@fedoraproject.org> - 24.4-4
- Rebuild (NLopt)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jan 11 2025 Mattia Verga <mattia.verga@proton.me> - 24.4-2
- Rebuilt for libnova v0.16

* Sun Dec 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.4-1
- 24.4

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 24.3-2
- Rebuild (qt6)

* Tue Sep 24 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.3-1
- 24.3

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 30 2024 Robert-André Mauchin <zebob.m@gmail.com> - 24.2-2
- Rebuilt for exiv2 0.28.2

* Mon Jun 24 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.2-1
- 24.2

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 24.1-3
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 24.1-2
- Rebuild (qt6)

* Tue Mar 26 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.1-1
- 24.1

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 23.4-3
- Rebuild (qt6)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.4-1
- 23.4

* Wed Dec 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.3-1
- 23.3

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 23.2-7
- Rebuild (qt6)

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 23.2-6
- Rebuild (qt6)

* Thu Oct 05 2023 Jan Grulich <jgrulich@redhat.com> - 23.2-5
- Rebuild (qt6)

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 23.2-3
- Rebuild for qtbase private API version change

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 23.2-2
- Rebuild for qtbase private API version change

* Wed Jul 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.2-1
- 23.2

* Mon May 29 2023 Jan Grulich <jgrulich@redhat.com> - 23.1-2
- Rebuild (qt6)

* Mon Mar 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.1-1
- 23.1

* Mon Mar 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2-9
- Patches for CVE-2023-28371

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.2-8
- Kill TELESCOPECONTROL support on F38 due to libindi 2 incompatibility

* Thu Mar  2 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2-7
- F-39: kill USE_PLUGIN_TELESCOPECONTROL support due to libindi 2 incompatibility

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2-6
- migrated to SPDX license

* Sun Feb 26 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2-5
- libindi rebuild.

* Mon Jan 23 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2-4
- Fix mimetype icon.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2-2
- QXlsx rebuild

* Tue Jan 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2-1
- 1.2

* Wed Nov 30 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.1-3
- QT6 rebuild.

* Mon Nov 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.1-2
- QT6 rebuild.

* Tue Nov 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.1-1
- 1.1

* Mon Oct 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.0-2
- Enable showmysky

* Mon Oct 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.0-1
- 1.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 09 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.22.2-1
- 0.22.2

* Mon Apr 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.22.1-1
- 0.22.1

* Tue Apr 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.22.0-1
- 0.22.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.21.3-1
- 0.21.3

* Mon Sep 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.21.2-1
- 0.21.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.21.1-1
- 0.21.1

* Mon Mar 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.21.0-1
- 0.21.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Kalev Lember <klember@redhat.com> - 0.20.4-1
- Update to 0.20.4

* Tue Oct 20 2020 Kalev Lember <klember@redhat.com> - 0.20.3-2
- ExcludeArch armv7hl on F33+ due to lconvert segfaulting (#1884681)

* Sun Sep 27 2020 Kalev Lember <klember@redhat.com> - 0.20.3-1
- Update to 0.20.3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Kalev Lember <klember@redhat.com> - 0.20.2-1
- Update to 0.20.2

* Mon Apr 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.20.1-1
- 0.20.1

* Mon Mar 30 2020 Kalev Lember <klember@redhat.com> - 0.20.0-1
- 0.20.0
- Drop old, unused buildrequires

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 22 2019 Kalev Lember <klember@redhat.com> - 0.19.3-1
- 0.19.3
- Don't replace upstream screenshots in appdata
- Use desktop-file-validate rather than desktop-file-install
- Validate appdata

* Sun Sep 29 2019 Kalev Lember <klember@redhat.com> - 0.19.2-1
- 0.19.2

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.1-1
- 0.19.1

* Mon Mar 25 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.19.0-1
- 0.19.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 fedora-toolbox <otaylor@redhat.com> - 0.18.3-2
- Handle both compressed and uncompressed manual pages

* Wed Dec 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.18.3-1
- 0.18.3

* Wed Aug 15 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.18.2-1
- 0.18.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.18.1-1
- 0.18.1

* Mon Mar 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.18.0-1
- 0.18.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.17.0-2
- Fix lunar eclipse crash.

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.17.0-1
- 0.17.0

* Mon Sep 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.16.1-1
- 0.16.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.16.0-1
- 0.16.0.

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Mar 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.15.2-1
- 0.15.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 27 2016 Jon Ciesla <limburgher@gmail.com> - 0.15.1-1
- 0.15.1.

* Mon Aug 01 2016 Jon Ciesla <limburgher@gmail.com> - 0.15.0-1
- 0.15.0.

* Sun May 22 2016 Jon Ciesla <limburgher@gmail.com> - 0.14.3-1
- 0.14.3.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Jon Ciesla <limburgher@gmail.com> - 0.14.1-2
- BR fix.

* Wed Dec  2 2015 Jochen Schmitt <Jochen herr-schmitt de> - 0.14.1-1
- New minor upstream update release

* Mon Nov 02 2015 Jon Ciesla <limburgher@gmail.com> - 0.14.0-1
- Latest upstream, BZ 1274980.
- Changelog date fix.
- Qt 5.5 patch upstreamed.

* Thu Oct 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.13.3-5
- Fix build with Qt 5.5

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.13.3-3
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May  3 2015 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.3-1
- Ne upstream release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.13.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 30 2015 Richard Hughes <rhughes@redhat.com> - 0.13.2-3
- Use better AppData screenshots

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.13.2-2
- Rebuild for boost 1.57.0

* Thu Jan 22 2015 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.2-1
- New monor bug-fixing release from upstream

* Tue Oct 21 2014 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.1-1
- New upstream release
- Remove ms-no-bitfields patch

* Wed Sep 24 2014 Dan Horák <dan[at]danny.cz> - 0.13.0-3
- fix build on non-x86 arches, patch taken from Debian

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Jochen Schmitt <Jochen herr-schmitt de> - 0.13.0-1
- New upstream release
- Add AppData support
- Exclude armv7hl due an unsupported compiler option

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.12.4-2
- Rebuild for boost 1.55.0

* Sun Sep 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.4-1
- New upstream release

* Sun Sep 15 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.3-1
- New upstream release
- Remove subpackage with obsoltete program documentation
- Correcting the project home page

* Sun Aug  4 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.2-1
- New upstream release
- Add phonon-devel as a BR

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.12.1-2
- Rebuild for boost 1.54.0
- Add patch from upstream to solve a issue with pod2man

* Mon Apr 22 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.1-1
- New upstream release

* Tue Feb 12 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.0-4
- Use upstream stellarium.desktop file

* Tue Feb 12 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.0-3
- Remove opengl-games-utils wrapper (#910402)
- Make BR to perl-podlators conditional

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.12.0-2
- Drop desktop vendor tag.

* Sun Feb  3 2013 Jochen Schmitt <Jochen herr-schmitt de> - 0.12.0-1
- New upstream release
- Clean up SPEC file
- Add perl-podlators as a BR to access pod2man

* Mon Aug 27 2012 Jochen Schmitt <JOchen her-schmitt de> - 0.11.4a-1
- New upstream release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  8 2012 Jochen Schmitt <s4504kr@omega.in.herr-schmitt.de> - 0.11.3-2
- Remove duplicate desktop file

* Mon Jun  4 2012 Jochen Schmitt <Jochen herr-schmitt de> 0.11.3-1
- New upstream release

* Tue Mar 13 2012 Jochen Schmitt <Jochen herr-schmitt de> 0.11.2-1
- New upstream release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-3
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.11.1-1
- New upstream release

* Tue Jul  5 2011 Jochen Schmitt <Jochen herr-schmitt de> 0.11.0-1
- New upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec  6 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.6-1
- New upstream release

* Thu Jun  3 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.5-1
- Nrw upstream release

* Sun Mar 14 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.4-4
- Set StartupNotify=true in desktop file

* Wed Feb 24 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.4-3
- Remove font files

* Tue Feb 23 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.4-2
- Fix uploaded sources

* Tue Feb 23 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.4-1
- New upstream release

* Sun Jan 31 2010 Jochen Schmitt <Jochen herr-schmitt de> 0.10.3-1
- New upstream release (#559929)

* Wed Nov 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.10.2-7
- Rebuild for Qt 4.6.0 RC1 in F13 (was built against Beta 1 with unstable ABI)

* Sun Nov  1 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-6
- Remove symlink to font files

* Thu Sep 24 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-5
- Updated program documentation (#525302)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  2 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-3
- Rebuild for new boost release

* Tue Mar 24 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-2
- Changed desktop file (#491922)

* Thu Mar 12 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.2-1
- New upstream release

* Thu Mar  5 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.1-4
- Support noarch subpackates

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  8 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.1-2
- New upstream release

* Sun Jan 18 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.0-3
- Change Req. to fonts pakcage because fonts package renaming (#480474)

* Sun Jan  4 2009 Jochen Schmitt <Jochen herr-schmitt de> 0.10.0-2
- Create symlinks to DejaVu fonts (#477460)

* Wed Sep 24 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.10.0-1
- New upstream release

* Sat Sep  6 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.9.1-7
- fix license tag

*  Mon Feb 11 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.9.1-6
- Fix gcc-4.3 related issues

* Tue Jan 22 2008 Jochen Schmitt <Jochen herr-schmitt de> 0.9.1-1
- New upstream release

* Tue Oct 23 2007 Will Woods <wwoods@redhat.com> 0.9.0-6
- Fix opengl-game-wrapper.sh usage

* Wed Sep 26 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-5
- Add usage of opengl-game-wrapper (BZ #304851)

* Thu Aug  9 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-4
- Rebuild

* Tue Aug  7 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-3
- Solve weakday displaying issue (#250621)

* Wed Jun 27 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-2
- Change category of the desktop entry (#241440)

* Tue Jun 12 2007 Jochen Schmitt <Jochen herr-schmitt de> 0.9.0-1
- New upstream release

* Sun Dec 17 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.2-5
- Resize icon to 32x32

* Tue Nov 14 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.2-3
- Try to fix AMD64 problem (#210525)

* Thu Oct 19 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.2-2
- Fix segfault on x64 systems (#210525)

* Tue Oct 10 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.2-1
- New upstream release

* Tue Jul  4 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.1-1
- New upstream release
- Fix demaged PDF (#197301)

* Wed May 31 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.0-4
- Update user guide
- change dl.sf.net to prdownloads.sf.net

* Sun May  7 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.8.0-3
- New upstream release

* Tue Feb 14 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-7
- Add stellarium user guide as doc subpackage
- Add gcc41 patch from Diego Petteno

* Mon Feb 13 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-4
- Add SDL_mixer-devel as BuildRequires:

* Sun Feb 12 2006 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-3
- Rebuilt for FC5

* Mon Oct 10 2005 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-2
- use of %%find_lang

* Sun Oct  9 2005 Jochen Schmitt <Jochen herr-schmitt de> 0.7.1-1
- New upstream release

* Thu Aug 11 2005 Jochen Schmitt <Jochen herr-schmitt de> 0.6.2-6
- Add %%{?dist} to release.

* Wed Aug 10 2005 Jochen Schmitt <Jochen herr-schmitt de> 0.6.2-5
- Fix build for GCC4.

* Thu Apr 14 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.6.2-4
- Fix build for GCC4.
- Fix desktop icon installation.

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Jan 23 2005 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.2-2
- Fixed broken patch.

* Sun Jan 16 2005 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.2-0.fdr.1
- Updated to 0.6.2.

* Sun Oct 17 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.1-0.fdr.1
- Updated to 0.6.1.

* Sat Aug 21 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.0-0.fdr.2
- Patched to honour optflags.
- Added nvidia specific patch.

* Sat Jul 17 2004 Marius L. Jøhndal <mariuslj at ifi.uio.no> - 0:0.6.0-0.fdr.1
- Initial RPM release.
