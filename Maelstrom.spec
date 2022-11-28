Name:			Maelstrom
Summary:		A space combat game
Version:		3.0.6
Release:		44%{?dist}
# See Maelstrom-Content-License.txt for details on the updated content licensing
License:		GPLv2+ and CC-BY
Source0:		http://www.libsdl.org/projects/Maelstrom/src/Maelstrom-%{version}.tar.gz
Source1:		maelstrom.png
Source2:		Maelstrom.desktop
Source3:		Maelstrom-Content-License.txt
Source4:		Maelstrom.appdata.xml
Patch0:			Maelstrom-3.0.6-setgid.patch
Patch1:			Maelstrom-3.0.6-gcc34.patch
Patch2:			Maelstrom-3.0.6-64bit.patch
Patch3:			Maelstrom-3.0.6-install.patch
Patch4:			Maelstrom-open.patch
Patch5:			Maelstrom-3.0.6-DESTDIR.patch
Patch6:                 Maelstrom-3.0.6-gcc5.patch
Patch7:                 Maelstrom-netd-c99.patch
URL:			http://www.libsdl.org/projects/Maelstrom/
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:		SDL_net-devel, desktop-file-utils, libtool
Requires(post):		coreutils
Requires(postun):	coreutils

%description
Maelstrom is a space combat game, originally ported from the Macintosh 
platform. Brave pilots get to dodge asteroids and fight off other ships 
at the same time.


%prep
%setup -q
%patch0 -p1 -b .setgid
%patch1 -p1 -b .gcc34
%patch2 -p1 -b .64bit
%patch3 -p1 -b .install
%patch4 -p1 -b .open
%patch5 -p1 -b .destdir
%patch6 -p1
%patch7 -p1
cp %{SOURCE3} .


%build
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-write-strings"
%configure
make %{?_smp_mflags}


%install
%make_install

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE2}

# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_bindir}/{Maelstrom-netd,macres,playwave,snd2wav}

mkdir -p -m 755 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

mkdir -p -m 755 %{buildroot}%{_localstatedir}/lib/games
mv %{buildroot}%{_datadir}/Maelstrom/*Scores %{buildroot}%{_localstatedir}/lib/games

mkdir -p -m 755 %{buildroot}%{_datadir}/appdata
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/appdata

find %{buildroot} -name "Makefile*" -exec rm -f {} \;

%files
%doc CREDITS README* Changelog Docs
%license Maelstrom-Content-License.txt COPYING*
%attr(2755,root,games) %{_bindir}/Maelstrom
%{_datadir}/Maelstrom
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/appdata/Maelstrom.appdata.xml
%config(noreplace) %attr(0664,root,games) %{_localstatedir}/lib/games/Maelstrom-Scores


%changelog
* Sat Nov 26 2022 Florian Weimer <fweimer@redhat.com> - 3.0.6-44
- Fixes for building in strict(er) C99 mode (#2148634)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.6-34
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb  2 2016 Hans de Goede <hdegoede@redhat.com> - 3.0.6-30
- Add Keywords to .desktop file
- Modernize spec and appdata
- Fix FTBFS

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 09 2014 Bill Nottingham <notting@redhat.com> - 3.0.6-26
- add appdata file

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.0.6-24
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Dec  6 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.0.6-19
- Revived and cleaned up, license issues resolved

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 11 2008 Bill Nottingham <notting@redhat.com> 3.0.6-16
- fix requirements for scriptlets (#475922)

* Thu Feb 14 2008 Bill Nottingham <notting@redhat.com> 3.0.6-15
- rebuild for gcc-4.3

* Wed Oct 10 2007 Bill Nottingham <notting@redhat.com> 3.0.6-14
- rebuild for buildid

* Fri Aug  3 2007 Bill Nottingham <notting@redhat.com>
- tweak license tag

* Mon Sep 11 2006 Bill Nottingham <notting@redhat.com> 3.0.6-13
- fix build

* Fri Jun  2 2006 Bill Nottingham <notting@redhat.com> 3.0.6-12
- more fixes from review (#189375)

* Tue May  9 2006 Bill Nottingham <notting@redhat.com> 3.0.6-11
- various fixes from review:
  - update the icon cache
  - move out of /usr/games
  - move scores to /var
  - rework setuid code
  - use desktop-file-install
  
* Mon Feb 13 2006 Bill Nottingham <notting@redhat.com> 3.0.6-10
- rebuild

* Thu May 26 2005 Bill Nottingham <notting@redhat.com>
- fix x86_64 build

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
- Add gcc34.patch

* Sun May 23 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- make some files again owned by root

* Tue Mar 23 2004 Bill Nottingham <notting@redhat.com> 3.0.6-3
- make score file %%config (#108386)
- move icon (#111583)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Sep 30 2003 Bill Nottingham <notting@redhat.com> 3.0.6-1
- tweak desktop file (#79668, #105792 <ville.skytta@iki.fi>)
- update to 3.0.6

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 18 2003 Bill Nottingham <notting@redhat.com> 3.0.5-8
- fix desktop (#81096)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 3.0.5-6
- remove unpackaged files from the buildroot

* Fri Aug 23 2002 Tim Powers <timp@redhat.com>
- bump release number and rebuild

* Thu Aug 22 2002 Preston Brown <pbrown@redhat.com>
- set maelstrom to setgid and access high score file safely (#70768)
- BuildReq on SDL_net-devel (#69105)

* Sat Aug 10 2002 Elliot Lee <sopwith@redhat.com>
- rebuilt with gcc-3.2 (we hope)

* Tue Jul 23 2002 Tim Powers <timp@redhat.com> 3.0.5-2
- build using gcc-3.2-0.1

* Mon Jun 24 2002 Bill Nottingham <notting@redhat.com> 3.0.5-1
- update to 3.0.5

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jan 25 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed Sep 12 2001 Tim Powers <timp@redhat.com>
- rebuild with new gcc and binutils

* Tue Jul 10 2001 Elliot Lee <sopwith@redhat.com>
- Rebuild to remove libXv/libXxf86dga deps

* Mon Jun 25 2001 Bill Nottingham <notting@redhat.com>
- add buildprereq (#44884)

* Tue Jun 12 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Mon May  7 2001 Bill Nottingham <notting@redhat.com>
- fix some prototypes in the network daemon
- rebuild against fixed SDL (#24119)

* Mon Apr 30 2001 Bill Nottingham <notting@redhat.com>
- use official tarball, fixes a minor /tmp issue (#38393)

* Fri Apr 27 2001 Bill Nottingham <notting@redhat.com>
- rebuild for C++ exception handling on ia64

* Mon Mar 12 2001 Bill Nottingham <notting@redhat.com>
- move desktop file to /etc/X11/applnk (#31492)

* Tue Feb 27 2001 Bill Nottingham <notting@redhat.com>
- fix Packager: tag

* Fri Dec  1 2000 Bill Nottingham <notting@redhat.com>
- Maelstrom is cool. Let's put it in the base distro.

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jul 05 2000 Tim Powers <timp@redhat.com>
- cleaned up spec file, shoudln't try to install files in the post or preun
  sections
- use %%configure and %%makeinstall
- use predefined RPM macros whenever possible
- don't use redundant defines at top of spec
- patched to buld with gcc-2.96

* Mon Apr 24 2000 Tim Powers <timp@redhat.com>
- rebuilt for 7.0

* Tue Feb 08 2000 Tim Powers <timp@redhat.com>
- strip binaries

* Fri Jan 28 2000 Tim Powers <timp@redhat.com>
- changed to valid group

* Wed Dec  8 1999 Bill Nottingham <notting@redhat.com>
- don't echo in %%pre/%%post, don't add desktop entries to $HOME

* Tue Sep 21 1999 Sam Lantinga <slouken@devolution.com>

- first attempt at a spec file

