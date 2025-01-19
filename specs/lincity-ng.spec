%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global commit d35c3bee434900deedd610b7b08a9bd8504e4c41
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210424
%global fonts font(dejavusans)

# For rpmdev-bumpspec
%global baserelease 36

Name:		lincity-ng
Version:	2.9
Release:	0.%{baserelease}.%{commitdate}git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Summary:	City Simulation Game
URL:		http://lincity-ng.berlios.de/
Source0:	https://github.com/lincity-ng/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# use PHYSFS_getLastErrorCode() and PHYSFS_getErrorByCode instead of deprecated
# PHYSFS_getLastError()
Patch0:		lincity-ng-PHYSFS-use-getErrorByCode.patch
# use PHYSFS_readBytes and PHYSFS_writeBytes instead of
# deprecated PHYSFS_read and PHYSFS_write
Patch1:		lincity-ng-PHYSFS-readwriteBytes.patch
# use PHYSFS_getPrefDir instead of
# deprecated PHYSFS_getUserDir
Patch2:		lincity-ng-PHYSFS-getPrefDir.patch
# use PHYSFS_stat instead of
# deprecated PHYSFS_isDirectory
Patch3:         lincity-ng-PHYSFS-stat.patch
# use PHYSFS_stat instead of
# deprecated PHYSFS_getLastModTime
Patch4:		lincity-ng-PHYSFS-remove-getLastModTime.patch
# use PHYSFS_mount instead of
# deprecated PHYSFS_addToSearchPath
Patch5:		lincity-ng-PHYSFS-remove-addToSearchPath.patch
Patch6: lincity-ng-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:	jam, physfs-devel, zlib-devel, libxml2-devel
BuildRequires:	SDL2-devel, SDL2_mixer-devel, SDL2_image-devel, SDL2_gfx-devel
BuildRequires:	SDL2_ttf-devel, desktop-file-utils
BuildRequires:	xorg-x11-proto-devel, libX11-devel, mesa-libGL-devel, mesa-libGLU-devel
BuildRequires:	autoconf, automake, libtool
BuildRequires:	fontconfig %{fonts} dejavu-sans-fonts
Requires:	%{name}-data = %{version}-%{release}

%description
LinCity-NG is a City Simulation Game. It is a polished and improved version
of the classic LinCity (http://www.floot.demon.co.uk/lincity.html) game with
a new iso-3D graphics engine and a completely redone and modern GUI.

%package data
Summary:	Data files needed to run lincity-ng
# data bits are dual licensed GPLv2+ or CC-BY-SA
License:	GPLv2+ or CC-BY-SA
Requires:	%{name} = %{version}-%{release}
Requires:	dejavu-sans-fonts
BuildArch: noarch

%description data
This package contains the data files (graphics, models, audio) necessary to
play Lincity-NG.

%prep
%autosetup -n %{name}-%{commit} -p 1
sed -i "s|CFLAGS += -O3 -g -Wall|CFLAGS += $RPM_OPT_FLAGS|" Jamrules
sed -i "s|CXXFLAGS += -O3 -g -Wall|CXXFLAGS += $RPM_OPT_FLAGS|" Jamrules
sed -i 's|lincity-ng.png|lincity-ng|g' lincity-ng.desktop

%build
./autogen.sh
touch CREDITS
%configure
jam

%install
DESTDIR=$RPM_BUILD_ROOT jam -sappdocdir=%{_pkgdocdir} install

# Make a symlink to system font, rather than include a copy of DejaVu Sans
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/sans.ttf
pushd $RPM_BUILD_ROOT
ln -f -s $(fc-match -f "%{file}" "sans") $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/sans.ttf
popd

desktop-file-install --delete-original		\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications	\
  --mode 0644					\
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

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
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
BugReportURL: https://code.google.com/p/lincity-ng/issues/detail?id=3&thanks=3&ts=1411587797
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">lincity-ng.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>LinCity-NG</summary>
  <description>
    <p>
      LinCity-NG is a game where you are the mayor of a small town and your goal
      is to make it prosper gerenciand building improvements and the resources of
      their city.
    </p>
    <p>
      Good game for Sim City fans.
    </p>
  </description>
  <url type="homepage">http://sourceforge.net/projects/lincity-ng.berlios/</url>
  <screenshots>
    <screenshot type="default">http://a.fsdn.com/con/app/proj/lincity-ng.berlios/screenshots/Lincity-ng-2.0.png</screenshot>
    <screenshot>http://a.fsdn.com/con/app/proj/lincity-ng.berlios/screenshots/NewSolar.png</screenshot>
    <screenshot>http://a.fsdn.com/con/app/proj/lincity-ng.berlios/screenshots/Height.png</screenshot>
  </screenshots>
</application>
EOF

%files
%doc %{_pkgdocdir}
%{_bindir}/lincity-ng
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*lincity-ng.desktop

%files data
%{_datadir}/lincity-ng/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.36.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9-0.35.20210424gitd35c3be
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.34.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.33.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.32.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 15 2023 Florian Weimer <fweimer@redhat.com> - 2.9-0.31.20210424gitd35c3be
- Fix incompatible-pointer-types bug in configure script

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.30.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.29.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.28.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.27.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.26.20210424gitd35c3be
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 20 2021 Neal Gompa <ngompa13@gmail.com> - 2.9-0.25.20210424gitd35c3be
- Bump to new snapshot for SDL2 port
- Refresh patch set

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.24.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.23.20160605git7f266b1
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.22.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Tom Callaway <spot@fedoraproject.org> - 2.9-0.21.20160605git7f266b1
- be smarter about how we make the dejavusans font symlink (bz1835504)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.20.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Tom Callaway <spot@fedoraproject.org> - 2.9-0.19.20160605git7f266b1
- apply fixes from upstream
- patch out all of the deprecated physfs calls

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.18.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.17.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.16.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.15.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Tom Callaway <spot@fedoraproject.org> - 2.9-0.14.20160605git7f266b1
- apply fixes from upstream, resolves issue where world len was 0.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.13.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.12.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-0.11.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.10.20160605git7f266b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-0.8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-0.7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.9-0.6.beta
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 2.9-0.5.beta
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Hans de Goede <hdegoede@redhat.com> - 2.9-0.3.beta
- Rebuild for new SDL_gfx

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9-0.2.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 30 2013 Tom Callaway <spot@fedoraproject.org> - 2.9-0.1.beta
- update to 2.9.beta

* Tue Dec  3 2013 Tom Callaway <spot@fedoraproject.org> - 2.0-14
- fix format-security issues

* Sat Nov  9 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.0-13
- Install docs to %%{_pkgdocdir} where available (#993856).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 2.0-11
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Tom Callaway <spot@fedoraproject.org> - 2.0-6
- rebuild for physfs2

* Tue Jul 26 2011 Bruno Wolff III <bruno@wolff.to> - 2.0-5
- Rebuild for SDL_gfx soname bump

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Dennis Gilmore <dennis@ausil.us> 2.0-2
- make data subpackage noarch

* Fri Jan 30 2009 Tom "spot" Callaway <tcallawa@redhat.com> 2.0-1
- 2.0 final

* Sat Jan 17 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.97-0.3.beta
- fix Requires: dejavu-sans-fonts

* Mon Jan 12 2009 Tom "spot" Callaway <tcallawa@redhat.com> 1.97-0.2.beta
- do not bundle font in data subpackage, use symlink and Requires: dejavu-fonts-sans

* Tue Dec 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.97-0.1.beta
- update to 1.97.beta

* Thu Sep 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.92-0.3.beta
- fix f9 crash (upstream bug #14544)

* Tue Sep 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.92-0.2.beta
- fix typo in spec file

* Tue Sep 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.92-0.1.beta
- update to 1.92.beta

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.91-0.2.beta
- Autorebuild for GCC 4.3

* Tue Feb 19 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.91-0.1.beta
- bump to 1.91.beta

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.1-2
- package no longer requires kdelibs, hooray!

* Thu Aug 23 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.1-1
- bump to 1.1.1 final
- license fix, GPLv2+
- rebuild in devel for ppc32

* Thu Aug  2 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.1-0.1.pre
- bump to 1.1.1pre 

* Mon Jul  9 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.0-1.1
- rebuild for new SDL_gfx in rawhide

* Wed Apr 11 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.1.0-1
- bump to 1.1.0

* Thu Sep 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.3-2
- rebuild for FC-6

* Wed Apr 19 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.3-1
- bump to 1.0.3

* Fri Mar 24 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.2-4
- -O3 optimization makes the code cry

* Tue Feb 28 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.2-3
- bump for FC-5

* Thu Jan  5 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.2-2
- FC5: BR: mesa-libGLU-devel

* Thu Jan  5 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.2-1
- bump to 1.0.2

* Wed Oct  5 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.1-3
- add Requires: kdelibs to resolve bz 169941

* Sun Sep 25 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.1-2
- split datadir/lincity-ng into its own package
- shorten main description

* Fri Aug 19 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.1-1
- initial package for Fedora Extras
