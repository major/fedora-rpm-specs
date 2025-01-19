Summary:      Advanced drum machine for GNU/Linux
Name:         hydrogen
Version:      1.2.3
Release:      4%{?dist}
URL:          http://www.hydrogen-music.org/
Source0:      https://github.com/hydrogen-music/%{name}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:      GPL-2.0-or-later

Patch0:       %{name}-cxxflags.patch

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: flac-devel 
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: ladspa-devel
BuildRequires: libsndfile-devel
BuildRequires: libarchive-devel
BuildRequires: liblo-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtxmlpatterns-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtsvg-devel
BuildRequires: cmake
BuildRequires: cppunit-devel
BuildRequires: make
BuildRequires: doxygen
BuildRequires: libappstream-glib

Requires:      hicolor-icon-theme

%description
Hydrogen is an advanced drum machine for GNU/Linux. It's main goal is to bring 
professional yet simple and intuitive pattern-based drum programming.

%package devel
Summary:    Hydrogen header files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
Requires:   %{name}%{_isa} = %{version}-%{release}
Obsoletes:  devel <= 0.9.7-9

%description devel
Header files for the hydrogen drum machine.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DWANT_DEBUG=OFF -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build

%install
%cmake_install

# install hydrogen.desktop properly.
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications   \
  --add-category X-Drumming                    \
  --add-category Midi                          \
  --add-category X-Jack                        \
  --add-category AudioVideoEditing             \
  --remove-mime-type text/xml                  \
  --delete-original                            \
  %{buildroot}%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop

# Move the icon to the proper place
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp %{buildroot}%{_datadir}/%{name}/data/img/gray/*.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# No need to package these (they will not be installed automatically in rc3?):
rm -f %{buildroot}%{_datadir}/%{name}/data/doc/{Makefile,README}* \
      %{buildroot}%{_datadir}/%{name}/data/doc/*.{docbook,po,pot}

# Validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.hydrogenmusic.Hydrogen.metainfo.xml

%files
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/hydrogen
%{_bindir}/h2*
%{_datadir}/hydrogen/
%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_libdir}/libhydrogen-core-1.2.*.so
%{_mandir}/man1/hydrogen.1*
%{_metainfodir}/org.hydrogenmusic.Hydrogen.metainfo.xml

%files devel
%{_includedir}/hydrogen/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.3-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 05 2024 Guido Aulisi <guido.aulisi@gmail.com> - 1.2.3-1
- Update to 1.2.3

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 17 2023 Florian Weimer <fweimer@redhat.com> - 1.1.1-5
- Backport upstream patch to fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 08 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 06 2021 Guido Aulisi <guido.aulisi@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 2020 Guido Aulisi <guido.aulisi@gmail.com> - 1.0.1-1
- Update to 1.0.1
- Use Qt5
- Drop unmaintained subpackage ladspa-wasp-plugins

* Tue Aug 04 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.7-15
- Fix FTBFS in Fedora rawhide/f33 (#1863864)
- Some spec cleanup

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Jan Beran <jaberan@redhat.com> - 0.9.7-11
- Avoid using compression format in manpage listing
- Use %%{_prefix} macro instead of hardcoded /usr

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Nils Philippsen <nils@tiptoe.de> - 0.9.7-9
- rebuild to fix GUI glitch
- use spaces for formatting
- rename 'devel' subpackage to 'hydrogen-devel' (d'oh)
- remove obsolete patches

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 0.9.7-6
- require gcc, gcc-c++ for building

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.7-1
- 0.9.7

* Wed Feb 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.9.5.1-13
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.5.1-11
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.9.5.1-8
- format-security patch

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-6
- Fix scons build once again

* Tue Feb 12 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.5.1-5
- Drop desktop vendor tag.

* Sun Jul 22 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-4
- Use pkg-config to detect cflags for liblrdf since raptor header file location changed

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-2
- Rebuilt for c++ ABI breakage

* Sun Feb 19 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5.1-1
- Update to 0.9.5.1. Drop upstreamed patch.

* Mon Jan 16 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5-3
- gcc-4.7 compile fixes

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 27 2011 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.5-1
- Update to 0.9.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 16 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.2-3
- Fix data directory. Fixes RHBZ#643622

* Wed Sep 29 2010 jkeating - 0.9.4.2-2
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.2-1
- Update to 0.9.4.2
- Drop all upstreamed patches

* Sat Apr 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4.1-1
- Update to 0.9.4.1
- Build the wasp plugins
- Fixes ladspa plugin path on 64bit systems
- Fixes crash RHBZ#570348

* Sat Feb 13 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-3
- Fix DSO linking RHBZ#564719

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-2
- Add patch against portmidi-200 on F13+. Fixes RHBZ#555488

* Tue Sep 15 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-1
- Update to 0.9.4

* Sat Aug 22 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.7.rc2
- Update to 0.9.4-rc2

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.6.rc1.1
- Update .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.5.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.4.rc1.1
- Rebuild against new lash build on F-12 due to the e2fsprogs split

* Tue Apr 14 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.3.rc1.1
- Update to 0.9.4-rc1-1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-0.2.790svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.9.4-0.1.790svn
- Update to 0.9.4-beta3 (uses scons and qt4)

* Fri Apr 04 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0.9.3-13
- QT3 changes by rdieter
- Fix build

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.3-12
- Autorebuild for GCC 4.3

* Thu Jan 03 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-11
- Previous change was not a good idea
- Adding missing includes to fix build with gcc-4.3

* Sun Oct 14 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-10
- Remove unneeded dependencies on desktop-file-utils

* Tue Oct 09 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-9
- Incorporate fixes from #190040, thanks to Hans de Goede
- Removed useless LIBDIR introduced in previous revision
- Fixed desktop file installation
- Call gtk-update-icon-cache only if it is present

* Sun Oct 07 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-8
- Remove -j from make to fix concurrency problems
- Handle libdir on 64bit platforms correctly
- Rename patches

* Sat Oct 06 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.9.3-7.1
- Fix desktop file
- Fix compatibility with new FLAC
- Fix linking for Build ID use

* Mon Mar 26 2007 Anthony Green <green@redhat.com> 0.9.3-7
- Improve Source0 link.
- Add %%post(un) scriptlets for MimeType update.
- Add update-desktop-database scriptlets.

* Sat Jul 22 2006 Anthony Green <green@redhat.com> 0.9.3-6
- Add hydrogen-null-sample.patch to fix crash.

* Sun Jul 02 2006 Anthony Green <green@redhat.com> 0.9.3-5
- Clean up BuildRequires.
- Configure with --disable-oss-support
- Don't run ldconfig (not needed)
- Remove post/postun scriptlets.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-4
- BuildRequire libxml2-devel.
- Remove explicit Requires for some runtime libraries.
- Set QTDIR via /etc/profile.d/qt.sh.
- Update desktop icons and icon cache in post and postun.
- Don't use __rm or __make macros.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-3
- Conditionally apply ardour-lib64-ladspa.patch.

* Sat May 13 2006 Anthony Green <green@redhat.com> 0.9.3-2
- Build fixes for x86_64.

* Wed Apr 26 2006 Anthony Green <green@redhat.com> 0.9.3-1
- Created.
