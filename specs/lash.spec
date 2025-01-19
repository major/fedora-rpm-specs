Summary:      LASH Audio Session Handler
Name:         lash
Version:      0.5.4
Release:      56%{?dist}
License:      GPL-2.0-or-later
URL:          http://www.nongnu.org/lash/
Source0:      http://download.savannah.gnu.org/releases/lash/lash-%{version}.tar.gz
Source1:      %{name}-panel.desktop
Patch0:       lash-0.5.3-no-static-lib.patch
# Fix DSO-linking failure
# Upstream bugtracker is closed for some reason. Sent via email:
Patch1:       lash-linking.patch
# Fix build against gcc-4.7
Patch2:       lash-gcc47.patch
# Modernize texi2html arguments for texi2html-5.0
Patch3:       lash-Modernize-texi2html-arguments.patch

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gtk2-devel 
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libxml2-devel
BuildRequires: readline-devel
BuildRequires: swig
BuildRequires: texi2html
BuildRequires: chrpath
BuildRequires: libuuid-devel
BuildRequires: make

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}


%description
LASH is a session management system for JACK and ALSA audio applications on
GNU/Linux. It allows you to save and restore audio sessions consisting of
multiple interconneced applications, restoring program state (i.e. loaded
patches) and the connections between them.

%package devel
Summary:      Development files for LASH
Requires:     %{name}-libs%{?_isa} = %{version}-%{release}
Requires:     alsa-lib-devel
Requires:     jack-audio-connection-kit-devel
Requires:     libuuid-devel

%description devel
Development files for the LASH library.

%package        libs
Summary:        Shared libraries for using %{name}

%description    libs
The %{name}-libs package contains lash shared libraries.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1 -b .linking
%patch -P2 -p1 -b .gcc47
%patch -P3 -p1 -b .texi2html

# Hack to build against newer swig
%if 0%{?rhel} && 0%{?rhel} <= 7
sed -i 's|1.3.31|2.0.0|g' configure*
%else
sed -i 's|1.3.31|4.0.0|g' configure*
%endif

%build
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" %configure --disable-static --disable-serv-inst
%make_build


%install
mkdir -p %{buildroot}%{_sysconfdir}
%make_install
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/liblash.la

# Move icons to the right place
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/96x96/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/lash/icons/lash_16px.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_24px.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_48px.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_96px.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/lash.svg

# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/lash_control
chrpath --delete %{buildroot}%{_bindir}/lash_simple_client
chrpath --delete %{buildroot}%{_bindir}/lashd
chrpath --delete %{buildroot}%{_bindir}/lash_synth
chrpath --delete %{buildroot}%{_bindir}/lash_panel
chrpath --delete %{buildroot}%{_bindir}/lash_save_button

# Move the dtd file to our Fedora Friendly place
mkdir -p %{buildroot}%{_datadir}/xml/lash/dtds
mv %{buildroot}%{_datadir}/lash/dtds/lash-project-1.0.dtd %{buildroot}%{_datadir}/xml/lash/dtds

# This directory is empty!
rm -rf %{buildroot}%{_datadir}/lash

# install the desktop entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                         \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Work around the newer texi2html which is behaving somehow else
if [ ! -d docs/lash-manual-html-split/lash-manual/ ]; then
  mkdir -p docs/lash-manual-html-split/lash-manual/
  cp -p docs/lash-manual-html-split/*.html docs/lash-manual-html-split/lash-manual/
fi

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog NEWS README docs/lash-manual-html-split/lash-manual icons/lash.xcf
%license COPYING
%{_bindir}/lash*
%{_datadir}/icons/hicolor/16x16/apps/lash.png
%{_datadir}/icons/hicolor/24x24/apps/lash.png
%{_datadir}/icons/hicolor/48x48/apps/lash.png
%{_datadir}/icons/hicolor/96x96/apps/lash.png
%{_datadir}/icons/hicolor/scalable/apps/lash.svg
%{_datadir}/xml/lash
%{_datadir}/applications/lash-panel.desktop

%files devel
%{_libdir}/liblash.so
%{_includedir}/lash-1.0
%{_libdir}/pkgconfig/lash*

%files libs
%{_libdir}/liblash.so.1
%{_libdir}/liblash.so.1.*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.5.4-51
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.5.4-49
- Revert to jack-audio-connection-kit

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 08 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.5.4-47
- Move to pipewire-jack-connection-kit

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Tom Stellard <tstellar@redhat.com> - 0.5.4-42
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Anthony Green <green@redhat.com> - 0.5.4-40
- Remove python2 bits

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.4-38
- Fixing FTBFS caused by the swig upgrade 3.0.12 -> 4.0.0 (#1707392)

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.4-37
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.4-33
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.4-32
- Python 2 binary package renamed to python2-lash
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Tue Aug 15 2017 Pete Walter <pwalter@fedoraproject.org> - 0.5.4-31
- Split out shared libraries to lash-libs subpackage

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.5.4-27
- Rebuild for readline 7.x

* Tue Oct 04 2016 Pete Walter <pwalter@fedoraproject.org> - 0.5.4-26
- Fix the build on EPEL 7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-25
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.5.4-23
- Modernize texi2html arguments

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 23 2014 Jaromir Capik <jcapik@redhat.com> - 0.5.4-19
- Fixing FTBFS caused by the swig upgrade 2.0.12 -> 3.0.0 (#1090111)
- Fixing rpath removal (libtool regenerated during the make phase -> sed didn't work)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.4-18
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247

* Sun Jul 22 2012 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.4-17
- Fix build against gcc-4.7

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.5.4-14
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 23 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.4-12
- Hack to build against newer swig

* Fri Jul 23 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.4-11
- More DSO-linking fixes

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0.5.4-10
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Feb 10 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.5.4-9
- Fix DSO-linking failure

* Wed Aug 05 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.5.4-8
- Update .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.5.4-6
- Build against libuuid on F-12 (e2fsprogs got split up)

* Sat Jun 13 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.5.4-5
- Re-enable python package
- Some macro consistency cleanup
- Update scriptlets according to new guidelines
- Make the .desktop file nicer
- Update description
- Remove rpath
- Clear some rpmlints

* Sun Mar 22 2009 Robert Scheck <robert@fedoraproject.org> - 0.5.4-4
- Work around the newer texi2html which is behaving somehow else

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 28 2008 Anthony Green <green@redhat.com> 0.5.4-2
- Force build with _GNU_SOURCE, not _POSIX_SOURCE..

* Thu Feb 28 2008 Anthony Green <green@redhat.com> 0.5.4-1
- Upgrade to 0.5.4.  Force build with _POSIX_SOURCE.

* Mon Oct 08 2007 Anthony Green <green@redhat.com> 0.5.3-3
- Disable pylash until we can figure out how to install it properly.

* Mon Oct 08 2007 Anthony Green <green@redhat.com> 0.5.3-2
- Fixed python installation for 64-bit systems.

* Sun Oct 07 2007 Anthony Green <green@redhat.com> 0.5.3-1
- Upgrade sources.
- Don't install info files (no longer built).
- Add python package.

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.5.1-15
- Rebuild for selinux ppc32 issue.

* Fri Jun 22 2007 Florian La Roche <laroche@redhat.com> 0.5.1-14
- info files are gzipped, add info dir entry

* Thu Feb 01 2007 Anthony Green <green@redhat.com> 0.5.1-11
- Rebuild to drop libtermcap dependency as per bugzilla #226761.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 0.5.1-10
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 Anthony Green <green@redhat.com> 0.5.1-9
- Update -texi-dir patch.

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 0.5.1-8
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com> 0.5.1-7.1
- Rebuild.

* Mon Sep  4 2006 Anthony Green <green@redhat.com> 0.5.1-7
- The devel package must Require pkgconfig.

* Fri Jul 14 2006 Anthony Green <green@redhat.com> 0.5.1-6
- The devel package must Require e2fsprogs-devel.

* Mon Jun 26 2006 Anthony Green <green@redhat.com> 0.5.1-5
- Use || : is %%post(un) scripts.

* Mon Jun 26 2006 Anthony Green <green@redhat.com> 0.5.1-4
- Fix files reference to %%{_datadir}/xml/lash.
- Don't use update-desktop-database.
- Use %%{version} in Source0.

* Mon Jun 19 2006 Anthony Green <green@redhat.com> 0.5.1-3
- Fix changelog entries.
- Move pkgconfig file to devel package.
- Run ldconfig is post and postun.
- Clean up BuildRequires.
- Fix docs install.
- Move icons to correct directory.
- Move dtds to correct directory.
- Don't install INSTALL or TODO.
- Install desktop file.

* Tue May 30 2006 Anthony Green <green@redhat.com> 0.5.1-2
- Fix URL.
- Add lash-0.5.1-service.patch.
- Fix some BuildRequires.
- The devel package Requires things now.
- Use %%{_infodir}.
- Delete the texinfo dir file.
- Add -texi-dir patch.
- Install info files properly.
- Add Fernando Lopez-Lazcano's -service.patch.
- Delete .la file after installation.
- Configure with --disable-serv-inst.

* Tue Apr 18 2006 Anthony Green <green@redhat.com> 0.5.1-1
- Build for Fedora Extras.

* Mon May 30 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- remove references to deprecated function jack_set_server_dir in
  jack (patch4), fc4 test build, no release bump yet
* Sun Dec 19 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- spec file cleanup
* Thu May 20 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- aded tetex buildrequires
* Sat May  8 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added buildrequires
- add patch to not add service to /etc/services
* Tue Feb 24 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-2
- added patch (thanks to Guenter Geiger) to not require a service number
  entry in /etc/services
* Fri Nov 14 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-1
- spec file tweaks
* Thu Nov  6 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.4.0-1
- updated to 0.4.0
- patched to build under gcc2.96 (patch1)
* Wed Feb 12 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.3.0-1
- updated to 0.3.0
- added 7.2 workaround for gtk2 configuration problem
* Mon Jan 13 2003  Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2-1
- Initial build.
