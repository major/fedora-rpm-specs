Name:           fityk
Version:        1.3.2
Release:        10%{?dist}
Summary:        Non-linear curve fitting and data analysis
License:        GPL-2.0-or-later
URL:            http://fityk.nieto.pl/

Source0:        https://github.com/wojdyr/%{name}/archive/v%{version}/%{name}-%{version}.tar.bz2
# patch to check for cmpfit dependency
Patch0:         cmpfit_config.patch

BuildRequires:  boost-devel
BuildRequires:  cmpfit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
#BuildRequires:  python-sphinx
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  wxGTK-devel
BuildRequires:  xylib-devel
BuildRequires:  zlib-devel

Requires:       gnuplot


%description
Fityk is a program for nonlinear curve-fitting of analytical
functions (especially peak-shaped) to data (usually experimental
data). It can also be used for visualization of x-y data only.


%package devel
Summary: Header files, libraries and development documentation for %{name}
Requires: %{name} = %{version}-%{release}


%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs that make
use of %{name}, you will need to install %{name}-devel.


%prep
%setup -q
%patch -P0 -p0

#mv {S:1} doc/
#tar xf {S:2}
#mv img doc/

# remove pre-built documentation
rm -fr doc/html

# change lua version in configure file
sed -i 's/AX_PROG_LUA(5.1, 5.4)/AX_PROG_LUA(5.1, 5.5)/' configure.ac

#unbundle cmpfit
rm -fr fityk/cmpfit
sed -i 's|#include "cmpfit/mpfit.h"|#include "mpfit.h"|' fityk/CMPfit.h
#sed -i 's/swig\/luarun.h \\/swig\/luarun.h/' fityk/Makefile.am
sed -i 's|cmpfit/mpfit.c cmpfit/mpfit.h|mpfit.h|' fityk/Makefile.am


%build
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags} -std=c++14" LDFLAGS="%{optflags} -lmpfit"
autoreconf -iv
%configure

# remove rpath
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

# Temporarily disable building documentation
# needs python-sphinx >=1.5

# build html documentation
#pushd doc
#make pdf
#popd


%install
make install DESTDIR=%{buildroot}
# get rid of libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

#rm -f $RPM_BUILD_ROOT%%{_libdir}/*.la

# SWIG bindings are not packaged, remove samples
rm -f %{buildroot}%{_datadir}/%{name}/samples/*.py*
rm -f %{buildroot}%{_datadir}/%{name}/samples/*.lua
rm -f %{buildroot}%{_datadir}/%{name}/samples/*.pl

#ln -s fityk.1.gz $RPM_BUILD_ROOT%%{_mandir}/man1/cfityk.1.gz

mkdir -p %{buildroot}%{_metainfodir}
cp -p %{buildroot}/usr/share/appdata/%{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml
rm -rf %{buildroot}/usr/share/appdata


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/fityk.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%doc NEWS
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/*
%{_libdir}/*.so.*
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{name}.appdata.xml


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/%{name}/samples/*.cc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3.2-8
- Rebuilt for proper patch macro syntax - patched by churchyard

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 10 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3.2-3
- Rebuild for cmpfit v1.5

* Wed Oct 19 2022 Scott Talbert <swt@techie.net> - 1.3.2-2
- Rebuild with wxWidgets 3.2

* Sun Aug 07 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3.2-1
- Update to v1.3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 1.3.1-25
- Force C++14 as this code is not C++17 ready

* Tue Aug 04 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3.1-24
- Increment max lua version (5.5) - FTBFS bug #1863560

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3.1-21
- Fix make command

* Tue Apr 21 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3.1-20
- Rebuilt

* Tue Apr 21 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3.1-19
- Rebuilt for cmpfit 1.4
- Remove patch for wx-config version check

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-16
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3.1-13
- Change source URL due to missing files in the "release" tarball
- Remove certain sample files that require SWIG bindings
- Add AppData file and check
- Spec file clean-up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Scott Talbert <swt@techie.net> - 1.3.1-11
- Update to build against merged compat-wxGTK3-gtk2-devel package

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-8
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-5
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-4
- Rebuilt for Boost 1.63

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.3.1-3
- Rebuild for readline 7.x

* Tue Dec 20 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-2
- Disable building docs temporarily (needs python-sphinx >=1.5)

* Tue Dec 20 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-7
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.3.0-6
- Rebuilt for Boost 1.59

* Tue Aug 04 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.0-5
- Built against GTK2 built wx widgets - BR: compat-wxGTK3-gtk2
- patch for wx-config version check
- removed lua version patch
- added icons and removed README and TODO

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.3.0-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0 - bugfix update

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.9-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 31 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.9-5
- Fix configure file for lua 5.3 building

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.2.9-4
- Rebuild for boost 1.57.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.2.9-3
- update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 05 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.9-1
- updated to latest upstream version
- built against patched cmpfit
- Added BuildRequires for cmpfit-devel

* Fri Feb 28 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.2.1-1
- updated to latest upstream version
- disabled using MPfit for now (removed bundling)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.9.8-6
- Rebuild for boost 1.54.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Marcin Wojdyr <wojdyr@gmail.com> - 0.9.8-1
- update to 0.9.8
- removed configure flag --with-samples
- removed minimal boost version
- updated URL

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 12 2010 Marcin Wojdyr <wojdyr@gmail.com> - 0.9.4-1
- update to 0.9.4
- update BuildRequires and files
- add configure flag --disable-xyconvert and remove -DNDEBUG
- symlink man page for cfityk

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.8.8-2
- rebuilt against wxGTK-2.8.11-2

* Tue Aug 18 2009 Marcin Wojdyr <wojdyr@gmail.com> - 0.8.8-1
- upstream license was changed from GPLv2 to GPLv2+
- install mime files and call update-mime-database
- use configure flag --with-samples to install samples
- update %%doc
- do not move program's icon from pixmaps/ to icons/
- add xylib-devel to BuildRequires
- add minimal wxGTK version
- remove not needed CXX and CC variables from configure and make
- drop obsolete changes to desktop file
- drop obsolete patch
- update to 0.8.8. Closes Red Hat Bugzilla bug #511758.
  Closes Red Hat Bugzilla bug #511307.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.8.1-14
- fix license tag

* Mon Apr 07 2008 Jesse Keating <jkeating@redhat.com> - 0.8.1-13
- Patch for GCC 4.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.1-11
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.8.1-10
- Rebuild for selinux ppc32 issue.

* Thu Jul 19 2007 John Pye <john@curioussymbols.com> 0.8.1-9
- First import to Fedora package management system

* Sun Jun 24 2007 John Pye <john.pye@anu.edu.au> 0.8.1-8
- Remove 'INSTALL'
- Remove 'tips.txt', kepts 'fityk_tips.txt'

* Sun Jun 24 2007 John Pye <john.pye@anu.edu.au> 0.8.1-7
- Taking suggestions from Mamoru Tasaka:
- Removing unneeded install steps
- Removing "LDFLAGS='-s'"; can't recall why it was there...
- Fixing timestamps with 'install -p'
- Remove mime-database update

* Sun Jun 24 2007 John Pye <john.pye@anu.edu.au> 0.8.1-6
- fixing for build on Mandrive 2006
- added missing dependencies following testing on openSUSE Build Service

* Mon May 07 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.8.1-5
- minor spec file cleanups (drop %%{vendor})
- fix up the included desktop file, get rid of the broken one
- get rid of rpath with libtool override

* Sun May 06 2007 John Pye <john.pye@anu.edu.au> 0.8.1-4
- Fixed file 02755 file permissions

* Wed May 02 2007 John Pye <john.pye@anu.edu.au> 0.8.1-3
- Separated -devel files into new package
- Added ldconfig lines
- Remove Makefiles from doc dirs.

* Tue May 01 2007 John Pye <john.pye@anu.edu.au> 0.8.1-2
- Corrected according to suggestions from Comrade Tom Callaway:
- makeinstall macro removed and replaced with 'make DESTDIR='
- _smp_mflags added
- removed .la file
- use of ccache is now conditional only
- removed runtime deps that will be autodetected
- removed unnecc buildtime deps

* Fri Apr 27 2007 John Pye <john.pye@anu.edu.au> 0.8.1-1
- Using .desktop file from the tarball
- Updating to new icon given in the tarball
- Fix _mandir
- Wildcard on .so.0.*
- Got rid of CVS file purge
- Install fityk_tips.txt

* Fri Apr 27 2007 John Pye <john.pye@anu.edu.au> 0.8.1-0
- 0.8.1
- Converted to Fedora

* Thu Jul 1 2004 Austin Acton <austin@mandrake.org> 0.4.2-1mdk
- 0.4.2

* Wed Jun 16 2004 Austin Acton <austin@mandrake.org> 0.4.1-1mdk
- 0.4.1
- configure 2.5
- new menu
