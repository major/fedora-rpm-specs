Summary:	Render a planetary image into an X window
Name:		xplanet
Version:	1.3.1
Release:	24%{?dist}

# src/ParseGeom.c.	... under review https://gitlab.com/fedora/legal/fedora-license-data/-/issues/502
# src/ParseGeom.h	... the same review
# src/getopt.c	LGPL-2.1-or-later
# src/getopt1.c	LGPL-2.1-or-later
# src/libdisplay/DesktopPicture.m	(unused)
# src/libdisplay/vroot.h	HPND
# src/libimage/bmp.c	GPL-2.0-or-later
# xplanet/fonts/README	GPL-3.0-or-later
# xplanet/images/README	not copyrighted
# xplanet/rgb.txt	.... the same review
#
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		https://gitweb.gentoo.org/repo/gentoo.git/plain/x11-misc/xplanet/files/xplanet-1.3.1-giflib.patch
URL:		http://%{name}.sourceforge.net

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	expat-devel
BuildRequires:	glib2-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXt-devel
BuildRequires:	libjpeg-devel
BuildRequires:	giflib-devel
BuildRequires:	libtiff-devel
BuildRequires:	netpbm-devel
BuildRequires:	pango-devel
Requires:	gnu-free-mono-fonts

%description
Xplanet is similar to Xearth, where an image of the earth is rendered
into an X window.  Azimuthal, Mercator, Mollweide, orthographic, or
rectangular projections can be displayed as well as a window with a
globe the user can rotate interactively.  The other terrestrial
planets may also be displayed. The Xplanet home page has links to
locations with map files.


%prep
%setup -q
%patch -P0 -p1 -b .gif

%if 0%{?fedora} >= 24
LANG=C grep -rl "inFile\.getline" . | \
	xargs sed -i.c++11 \
		-e '\@inFile\.getline@s|\(inFile\.getline[ \t]*\)\((.*)\)[ \t]*!= NULL|static_cast<bool> (\1\2)|' \
		-e '\@inFile\.getline@s|\(inFile\.getline[ \t]*\)\((.*)\)[ \t]*== NULL|(!(static_cast<bool> (\1\2)))|'
%endif

%build
%configure
make %{?_smp_mflags} -k

%install
CPPROG="cp -p" make DESTDIR=%{buildroot} install

ln -sf ../fonts/gnu-free/FreeMonoBold.ttf \
	%{buildroot}%{_datadir}/%{name}/FreeMonoBold.ttf

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/xplanet

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-23
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-10
- Remove pango workaround, fixed in pango-1.43.0-3

* Mon Feb  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-9
- Add gobject-2.0 to linker flag explicitly for now

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 11 2018 Sandro Mani <manisandro@gmail.com> - 1.3.1-7
- Rebuild (giflib)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.1-1
- 1.3.1

* Sat Feb  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-13
- Fix for C++11 wrt no implicit conversion from std::basic_istream
  to void ptr

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0-10
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 17 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.0-7
- Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.3.0-4.1
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.3.0-3.1
- rebuild against new libjpeg

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May  7 2012 Mamoru Tasaka <mtasaka@fedoraproject.org>
- F-18: rebuild against new libtiff

* Fri Mar 30 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.3.0-1
- 1.3.0

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for c++ ABI breakage

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.2.2-3
- F-17: rebuild against gcc47

* Wed Nov  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.2.2-2
- Rebuild

* Fri Feb 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.2.2-1
- 1.2.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-2
- F-12: Mass rebuild

* Thu Apr 23 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.1-1
- 1.2.1

* Wed Mar 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-7
- GNU FreeFont naming change

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-6
- F-11: Mass rebuild

* Thu Feb  5 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-5
- Patch to compile with g++44

* Sun Dec 21 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-4
- Remove xplanet private ttf file, use system one

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Fri Jan  4 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-3
- Some misc fixes for g++43

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-2.1.dist.2
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-2.1.dist.1
- License update

* Mon Oct  2 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-2.1
- rebuild against newest gcc(-4.1.1-27 or -28)

* Fri Sep 22 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-2
- bump release

* Sat Sep 16 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-1
- 1.2.0
- Keep timestamps

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0.1-7
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun May 11 2003 Juha Ylitalo <jylitalo@iki.fi> - 0:1.0.1-0.fdr.5
- added %%defattr so that we wouldn't get big list of user temp1 does not exist.
- added XFree86-devel into BuildRequires, since fedora build seems to lack
  dependencies to libX11 and libXext (from XFree86-libs)

* Thu May 01 2003 Juha Ylitalo <jylitalo@iki.fi> - 0:1.0.1-0.fdr.4
- appearantly removing INSTALL from %%files section was all that was needed...

* Thu May 01 2003 Juha Ylitalo <jylitalo@iki.fi> - 0:1.0.1-0.fdr.2
- fixed Group in SPEC file (to Amusements/Graphics)
- added AUTHORS, NEWS, README.config and TODO into %%files %%doc list.
- removed INSTALL from %%files
- and other minor changes based on bugzilla.fedora.us #109.

* Tue Apr 29 2003 Juha Ylitalo <jylitalo@iki.fi> - 0:1.0.1-0.fdr.1
- fixed release to match Fedora guidelines.
- ./configure to %%configure and bunch of other find-replace operations.
- added missing BuildRequires.

* Tue Apr 01 2003 Juha Ylitalo <jylitalo@iki.fi> - 0:1.0.1-1.fdr.1
- upgrade from 0.94 to 1.0.1
- fedora related changed to Hari Nair <hari@alumni.caltech.edu>'s original spec
- added patch to make my 0xf6 etc. finnish characters to show in markers.
