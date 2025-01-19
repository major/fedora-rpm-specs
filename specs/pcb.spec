# Features in Fedora/Free Electronic Lab

%global         pcbver    4.2.0

Name:           pcb
Version:        %{pcbver}
Release:        18%{?dist}

Summary:        An interactive printed circuit board editor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pcb.geda-project.org/index.html

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  perl-generators
BuildRequires:  tcl, tk, bison, flex, gawk, ImageMagick, gtk2-devel, gd-devel, fontconfig-devel
BuildRequires:  cups, tetex-latex, libICE-devel, desktop-file-utils, intltool, gettext-devel
BuildRequires:  dbus-devel
BuildRequires:  mesa-libGLU-devel gtkglext-devel
# Testsuite
# 2011-11-29 Disabling testsuite as rawhide has a broken libgmp.so.3
# BuildRequires:  gerbv geda-gaf

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Requires:       m4
Requires:       electronics-menu

Source0:        http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{pcbver}.tar.gz

# sent upstream
#Patch0:         0001-Fix-the-AppData-and-update-to-the-latest-spec-versio.patch

# Upstream http://git.geda-project.org/pcb/commit/?id=9dea9f5a3801d612f78c738fe7efccefa5745000
Patch1:		pcb-fedora-c99.patch

%description
PCB is an interactive printed circuit board editor.
PCB includes a rats nest feature, design rule checking, and can provide
industry standard RS-274-X (Gerber), NC drill, and centroid data (X-Y data)
output for use in the board fabrication and assembly process. PCB offers
high end features such as an auto-router and trace optimizer which can
tremendously reduce layout time.

%package doc
Summary:         Documentation for PCB, an interactive printed circuit board editor
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description doc
This package contains the documentation of PCB, an interactive printed circuit
board editor.


%prep
%setup -q -n %{name}-%{pcbver}

%{__sed} -i \
   's|examplesdir = $(pkgdatadir)/examples|examplesdir = @docdir@/examples|' \
   example/libraries/Makefile.*

%{__sed} -i \
   's|tutdir = $(pkgdatadir)/tutorial|tutdir = @docdir@/tutorial|' \
   tutorial/Makefile.*

#%%patch0 -p1 -b fix-appdata-file
%patch -P1 -p1 -b fedora-c99
touch aclocal.m4 Makefile.in

%build
export WISH=%{_bindir}/wish

# Fixes failed build on EPEL-5
%if 0%{?rhel}
export CFLAGS=`echo %optflags | sed "s/-D_FORTIFY_SOURCE=2 // g" -`
%endif


# Bug 472618 : disable-update-desktop-database
# Bug 544657 : --enable-dbus
%configure \
    --enable-dbus \
    --enable-toporouter \
    --disable-update-mime-database \
    --disable-update-desktop-database \
    --docdir=%{_pkgdocdir}

%{__make} %{?_smp_mflags}
pushd doc
%{__make} -t pcb.pdf pcb.info pcb.html
popd


%install
%{__make} DESTDIR=%{buildroot} INSTALL="%{_bindir}/install -p" install

# in /usr/share/pcb/newlib/ folder, sockets is an empty folder

desktop-file-install --vendor ""               \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original                          \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

#
# Additional Examples
#
set +x
dest=%{buildroot}%{_pkgdocdir}/examples
for d in thermal pad puller ; do
   echo -n -e "... Fixing path of $d  \t"
   mkdir -p $dest/$d
   mv $dest/../$d.* $dest/$d
   install -pm 0644 doc/$d.{pcb,pdf} $dest/$d
   sed -i "s|$d.png|examples/$d/$d.png|" $dest/../%{name}.html
   echo "done"
done
set -x

## --- pcb supports for acpcircuits
# http://www.apcircuits.com/resources/links/pcb_unix.html
unzip tools/apctools.zip
install -p -m 755 apc*.pl  %{buildroot}%{_datadir}/%{name}/tools

# Removes duplicates
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/apctools.zip

## ---

# Old versions of PCB don't support auto-route, pcb2ncap convert
# pcb format to ncap format used for mucspcb to auto-route the circuit.
# In newer versions of PCB, auto-route is included and pcb2ncap and mucspcb
# are no more needed.
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/pcb2ncap.tgz

chmod 755 %{buildroot}%{_datadir}/%{name}/tools/{PCB2HPGL,tgo2pcb.tcl,Merge*}

# remove unnecessary file
%{__rm} -f %{buildroot}%{_datadir}/%{name}/tools/gerbertotk.c

%{__rm} -rf %{buildroot}%{_datadir}/info/dir

mv %{buildroot}%{_pkgdocdir}/refcard.pdf %{buildroot}%{_pkgdocdir}/pcb-reference-card.pdf

# remove duplicates
%{__rm} -f %{buildroot}%{_bindir}/Merge*

# L#854396 0.20110918 needlessly installs gts static library & header file
%{__rm} -f %{buildroot}%{_libdir}/libgts.a %{buildroot}%{_includedir}/gts.h

# locale's
%find_lang %{name}


# Documentation sub-package
%files doc
%{_infodir}/%{name}*
%doc %{_pkgdocdir}/


# Main package
%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
#%%doc README_FILES/CHANGES README_FILES/Whats_new_in_2.0 README_FILES/Tools

%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/pcb.xml
#%%{_datadir}/mimelnk/application/x-*.desktop
%{_datadir}/gEDA/scheme/gnet-pcbfwd.scm



%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2.0-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb  3 2023 DJ Delorie <dj@redhat.com> - 4.2.0-12
- Fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 25 2020 Jeff Law <law@redhat.com> - 4.2.0-5
- Touch pcb.pdf pcb.info pcb.html after the main build is complete so
  that they don't need rebuilding if %configure changes any configure files

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 4.2.0-2
- Remove obsolete requirements for %%post/%%preun scriptlets

* Mon Feb 04 2019 Alain Vigne <alain DOT vigne DOT 14 AT gmail DOT com> - 4.2.0-1
- New upstream release - 4.2.0
- Change license from GPLv2 to GPLv2+, as more and more files are "(at your option) any later version"
- Add a license file in %%files
- Remove "rm -rf %%{buildroot}" at the beginning of %%install.
- Re-arrange documentation split between main and doc sub-packages

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Alain Vigne <alain DOT vigne DOT 14 AT gmail DOT com> - 4.1.3-1
- New upstream release - 4.1.3

* Mon Sep 17 2018 Alain Vigne <alain DOT vigne DOT 14 AT gmail DOT com> - 4.1.2-1
- New upstream release - 4.1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20140316-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20140316-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.20140316-15
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20140316-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20140316-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.20140316-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Sandro Mani <manisandro@gmail.com> - 0.20140316-11
- Rebuild (libwebp)

* Fri Jul 22 2016 Tom Callaway <spot@fedoraproject.org> - 0.20140316-10
- Rebuild to drop libvpx dep

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.20140316-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec  1 2015 Tom Callaway <spot@fedoraproject.org> - 0.20140316-8
- rebuild for libvpx 1.5.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20140316-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr  6 2015 Tom Callaway <spot@fedoraproject.org> - 0.20140316-6
- rebuild for libvpx 1.4.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.20140316-5
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20140316-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20140316-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Richard Hughes <richard@hughsie.com> - 0.20140316-2
- Fix the AppData file.

* Thu May 22 2014 Richard Hughes <richard@hughsie.com> - 0.20140316-1
- Update to 20140316
- Install the AppData file.

* Tue Sep 10 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.20110918-12
- Reflect docdir changes (RHBZ#994022).
- Fix bogus %%changelog entry.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110918-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.20110918-10
- Perl 5.18 rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 0.20110918-9
- rebuild for new GD 2.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110918-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.20110918-7
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.20110918-6
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110918-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110918-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20110918-3
- Temporary removed geda-gaf from BR

* Sun Nov 27 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20110918-2
- Bug fix L#882712 Route styles are not properly loaded after nm conversion
- Bug fix L#699307 Panning problem when mouse button is released on scrollbar (sf-2923335)
- Bug fix L#891041 png export broken for tilted, square pads

* Sat Nov 12 2011 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20110918-1
- New upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100929-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Oct 2 2010 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20100929-1
- New upstream release

* Sun Dec 6 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20091103-2
- Enable build for dbus support
- improved reference card

* Sat Nov 7 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20091103-1
- New upstream release

* Tue Sep 8 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20081128-4
- Fixes for PCB EL-5 build.

* Sat Nov 29 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20081128-1
- new upstream release
- restructuring docs, tutorials and examples
- Fixed Bug 472618 -  Must not include /usr/share/applications/mimeinfo.cache

* Sat Feb 09 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20080202-2
- added gettext-devel as BR
- treat locales properly

* Sat Feb 02 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20080202-1
- fixed docdir
- new upstream release
- treat locales properly

* Thu Jun 21 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20070208-2
- fixed docdir

* Fri Feb 09 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20070208-1
- New upstream release - 20070208

* Sun Feb 04 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-9
- fixed presence in gnome menu

* Sun Dec 24 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-8
- Removed duplicates

* Fri Dec 22 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-7
- Fixed info files and added to the pcb package #219406
- Fixed man pages (with patch0 to suit fedora packaging of pcb
- Added refcard.pdf in pcb binary package
- Removed duplicated MergePCBPS and Merge_dimPCBPS from pcb binary package
- pcb supports for acpcircuits included

* Fri Sep 15 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-6
- Fixed ownership of %%{_datadir}/%%{name}/ #206405

* Fri Sep 01 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-5
- release for devel

* Fri Sep 01 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-4
- Added m4 as requires: to fix the error msg:
-       can't find default font-symbol-file 'default_font'

* Fri Aug 25 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-3
- release for devel

* Fri Aug 25 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-2
- release for FC5 and minor fixes

* Fri Aug 25 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060822-1
- updated to 20060822's snapshot

* Wed Jul 12 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060422-4
- pcbver corrected in pcb.desktop

* Sun Jul 09 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 0.20060422-3
- fixed the icon of pcb

* Sun Jul 09 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060422-2
- fixed E: pcb info-dir-file /usr/share/info/dir
- added /sbin/install-info as requires for %%post and %%preun
- added icon and treated GTK+ icon cache as required

* Thu Jul 06 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.20060422-1
- New upstream release 20060422
- Minor fixes to work under mock

* Wed Apr 19 2006 <pjones@redhat.com> - 0.20060414-1
- Let there be pcb packaging.

