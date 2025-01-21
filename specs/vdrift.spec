%global commit 5ae309f1048c863f4745cd50c8cd81f98340b1d4
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: vdrift
Version:  20141020
Release:  33.git%{shortcommit}%{?dist}
Summary: Driving/drift racing simulation

License: GPL-3.0-or-later
URL: http://vdrift.net
Source0: https://github.com/VDrift/vdrift/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1: vdrift.desktop
Source2: vdrift.png
# Data
# svn checkout https://svn.code.sf.net/p/vdrift/code/ vdrift-code
# mv vdrift-code/vdrift-data data
# tar cvfJ vdrift-data-20210211.tar.xz data
Source3: vdrift-data-20210211.tar.xz

Patch1: vdrift-20071226-paths.patch
Patch4:	vdrift-20090215-joepack-includes.patch
BuildRequires: mesa-libGL-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: SDL_gfx-devel
BuildRequires: python3-scons
BuildRequires: libvorbis-devel
BuildRequires: desktop-file-utils
BuildRequires: glew-devel
BuildRequires: boost-devel
BuildRequires: asio-devel
BuildRequires: bullet-devel
BuildRequires: libarchive-devel
BuildRequires: libcurl-devel
BuildRequires: python3-devel
BuildRequires: gcc-c++
BuildRequires: subversion

Requires: vdrift-data = %{version}

%description
VDrift is a cross-platform, open source driving simulation made with drift 
racing in mind. It's powered by the excellent Vamos physics engine. It is
released under the GNU General Public License (GPL) v2. It is currently
available for Linux, FreeBSD, Mac OS X and Windows (Cygwin).

%package data
Summary: Driving/drift racing simulation data
Requires: vdrift = %{version}
BuildArch: noarch

%description data
VDrift is a cross-platform, open source driving simulation made with drift 
racing in mind. It's powered by the excellent Vamos physics engine. It is
released under the GNU General Public License (GPL) v2. It is currently
available for Linux, FreeBSD, Mac OS X and Windows (Cygwin).

These are the data files.

%prep

%setup -qn vdrift-%{commit} -a 3
# unbundling
rm -rf bullet

%ifarch ppc ppc64
sed -i 's/linuxx86/linuxppc/' src/SConscript
%endif

%patch -P 1 -p0
%patch -P 4 -p0
%py3_shebang_fix .

/bin/chmod -x src/main.cpp
/bin/chmod -x src/game.cpp


%build
scons %{?_smp_mflags}

%install
# As described in the README scons install is broken so DIY
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}
install -m 755 build/vdrift %{buildroot}%{_bindir}
cp -pr data %{buildroot}%{_datadir}/vdrift
rm `find %{buildroot}%{_datadir}/vdrift -name "SConscript*"`

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install           \
  --dir %{buildroot}%{_datadir}/applications \
 %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Luya Tshimbalanga <luya@fedoraproject.org> -->
<!--
BugReportURL: https://github.com/VDrift/vdrift/issues/122
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">vdrift.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Drifting oriented racing simulation</summary>
  <description>
    <p>
      VDrift is a racing simulation oriented to drifting.
    </p>
    <p>
      It features over 45 tracks based on famous real-world circuits and 45 cars
      based on real-world vehicles.
    </p>
  </description>
  <url type="homepage">http://vdrift.net</url>
  <screenshots>
    <screenshot type="default"><!--screenshot url here--></screenshot>
    <screenshot><!--screenshot url here--></screenshot>
    <screenshot><!--screenshot url here--></screenshot>
  </screenshots>
</application>
EOF

%files
%license LICENSE
%doc README.md
%{_bindir}/vdrift
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/vdrift.desktop
%{_datadir}/icons/hicolor/32x32/apps/vdrift.png

%files data
%{_datadir}/vdrift

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-33.git5ae309f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-32.git5ae309f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-31.git5ae309f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-30.git5ae309f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 20141020-29.git5ae309f
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-28.git5ae309f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-27.git5ae309f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-26.git5ae309f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-25.git5ae309f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 11 2021 Tom Callaway <spot@fedoraproject.org> - 20141020-24.git5ae309f
- update code to latest git
- update data from latest svn

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 2014-1020-21
- Change build options to fix crash.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 20141020-18
- Fix FTBFS.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 20171020-15
- Fix shebang.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 20141020-12
- Remove obsolete scriptlets

* Mon Dec 18 2017 Rich Mattes <richmattes@gmail.com> - 20141020-11
- Rebuild for bullet-2.87
- Force scons to run with python 2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 20141020-6
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20141020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 20141020-4
- Rebuilt for Boost 1.60

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141020-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 20141020-2
- rebuild for Boost 1.58

* Sun Jun 28 2015 Jon Ciesla <limburgher@gmail.com> - 20141020-1
- Latest upstream.
- Fixed changelog dates.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120722-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 20120722-15
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 20120722-14
- Add an AppData file for the software center

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 20120722-13
- Rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120722-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 20120722-11
- Rebuild for new SDL_gfx

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120722-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 20120722-9
- Rebuild for boost 1.55.0

* Sun Feb 09 2014 Rich Mattes <richmattes@gmail.com> - 20120722-8
- Rebuild for bullet-2.82

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 20120722-7
- rebuilt for GLEW 1.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120722-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 20120722-5
- Rebuild for boost 1.54.0

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 20120722-4
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Thu Jan 17 2013 Tomas Bzatek <tbzatek@redhat.com> - 20120722-3
- Rebuilt for new libarchive

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 20120722-2
- Rebuild for glew 1.9.0

* Wed Oct 24 2012 Jon Ciesla <limburgher@gmail.com> - 20120722-1
- Latest upstream.

* Sat Oct 13 2012 Rich Mattes <richmattes@gmail.com> - 20111022-8
- Rebuild for new bullet
- Add fix for build error with new bullet

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 20111022-7
- Rebuild for new glew

* Thu Jul 26 2012 Jon Ciesla <limburgher@gmail.com> - 20111022-6
- Rebuilt for boost 1.50.

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111022-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Rich Mattes <richmattes@gmail.com> - 20111022-4
- Rebuild for bullet 2.80

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111022-3
- Rebuilt for c++ ABI breakage

* Thu Jan 26 2012 Tomas Bzatek <tbzatek@redhat.com> - 20111022-2
- Rebuilt for new libarchive

* Wed Jan 18 2012 Jon Ciesla <limburgher@gmail.com> - 20111022-1
- New upstream.
- License changed to GPLv3+.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100630-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Jon Ciesla <limburgher@gmail.com> - 20100630-7
- Bump and rebuild for new bullet..

* Fri Jul 15 2011 Jon Ciesla <limb@jcomserv.net> - 20100630-6
- Bump and rebuild for new SDL.

* Mon Jun 20 2011 ajax@redhat.com - 20100630-5
- Rebuild for new glew soname

* Thu May 12 2011 Jon Ciesla <limb@jcomserv.net> - 20100630-4
- Rebuild for new bullet.

* Sat Feb 19 2011 Thomas Spura <tomspur@fedoraproject.org> - 20100630-3
- unbundle bullet (#621623)
- remove unneeded BR

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100630-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 28 2010 Jon Ciesla <limb@jcomserv.net> - 20100630-1
- New upstream.

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 20090615-4
- FTBFS fix, BZ 599767.

* Thu Aug 06 2009 Jon Ciesla <limb@jcomserv.net> - 20090615-3
- Path fix, BZ 515908.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090615-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Jon Ciesla <limb@jcomserv.net> - 20090615-1
- Update to 2009-06-15.
- Split data into noarch subpackage, BZ 508079.

* Thu Feb 19 2009 Jon Ciesla <limb@jcomserv.net> - 20090215-1
- Update to 2009-02-15.
- Includes patch.

* Mon Nov 24 2008 Jon Ciesla <limb@jcomserv.net> - 20080805-3
- Cleaned up summary.

* Tue Oct 21 2008 Hans de Goede <hdegoede@redhat.com> - 20080805-2
- Actually install the data now that its merged into the main package

* Tue Aug 12 2008 Jon Ciesla <limb@jcomserv.net> - 20080805-1
- Update to new upstream.
- Dropped gcc4.3 and jamfile patches, applied upstream.
- Merged and obsolete/provided -data package, following upstream.
- Added glew-devel BR.

* Fri Feb 15 2008 Jon Ciesla <limb@jcomserv.net> - 20071226-3
- Multiple fixes for the review.

* Thu Feb 14 2008 Jon Ciesla <limb@jcomserv.net> - 20071226-2
- Multiple package fixes.

* Tue Feb 12 2008 Jon Ciesla <limb@jcomserv.net> - 20071226-1
- Updated to current release.

* Wed Apr 18 2007 Jon Ciesla <limb@jcomserv.net> - 20070323-4
- Added patch to fix mouse driving from thelusiv@gmail.com.

* Mon Apr 16 2007 Jon Ciesla <limb@jcomserv.net> - 20070323-3
- Corrected patch to allow build without minimal data.
- Added release=1 to scons options.
- Passing compiler flags to scons.
- Turned off translations.

* Mon Apr 02 2007 Jon Ciesla <limb@jcomserv.net> - 20070323-2
- Split out minimal data.

* Thu Mar 29 2007 Jon Ciesla <limb@jcomserv.net> - 20070323-1
- Initial packaging
