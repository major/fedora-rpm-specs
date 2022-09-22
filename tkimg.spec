%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:		tkimg
Version:	1.4
Release:	37%{?dist}
Summary:	Image support library for Tk
License:	BSD
URL:		http://sourceforge.net/projects/tkimg
Source0:	https://downloads.sourceforge.net/project/tkimg/tkimg/1.4/%{name}%{version}.tar.bz2
Patch0:		tkimg-zlib.patch
Patch1:		tkimg-jpg.patch
Patch2:		tkimg-libpng.patch
Patch3:		tkimg-libtiff.patch
Patch4:		tkimg-libpng15.patch
Patch5:		tkimg-libtiff4.patch
# gzgetc is now defined as a macro in zlib, which causes tkimg to ftbfs
# because it wants to define all of its functions internally to map to the 
# tcl/tk bits. The simple fix is to use the abstraction function "gzgetc_"
# which avoids the problem. See: https://bugzilla.redhat.com/show_bug.cgi?id=844462
Patch6:		tkimg-zlib127-gzgetc_fix.patch
# changes in libpng16
Patch7:		tkimg-libpng16.patch
Patch8:		tkimg-libpng-deprecated.patch
# gcc10 has -fno-common by default
Patch9:		tkimg-gcc10.patch

# A request to allow building with system libraries has been submitted
# https://sourceforge.net/tracker/index.php?func=detail&aid=2292032&group_id=52039&atid=465495
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	tcl-devel tk-devel tcllib
BuildRequires:	zlib-devel >= 1.2.7
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.6
BuildRequires:	libtiff-devel >= 4.0

Requires: tcl(abi) = 8.6
Requires: tk >= 8.6

%description
This package contains a collection of image format handlers for the Tk
photo image type, and a new image type, pixmaps.
The provided format handlers include bmp, gif, ico, jpeg, pcx, png,
ppm, ps, sgi, sun, tga, tiff, xbm, and xpm.

%package devel
Summary:	Libraries, includes, etc. used to develop an application with %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	tcl-devel tk-devel
Requires:	libjpeg-devel zlib-devel
Requires:	libtiff-devel
Requires:	libpng-devel

%description devel
These are the header files needed to develop a %{name} application

%prep
%setup -q -n %{name}%{version}
%patch0 -p1 -b .zlib
rm -rf compat/zlib
%patch1 -p1 -b .jpeg
rm -rf compat/libjpeg
%patch2 -p1 -b .libpng
rm -rf compat/libpng
%patch3 -p1 -b .libtiff
rm -rf compat/libtiff
%patch4 -p1 -b .png15
%patch5 -p1 -b .tiff4
%patch6 -p1 -b .gzgetc_fix
%patch7 -p1 -b .png16
%patch8 -p1 -b .deprecated
%patch9 -p1 -b .gcc10

%build
%configure --with-tcl=%{tcl_sitearch} --with-tk=%{_libdir} --libdir=%{tcl_sitearch} --disable-threads --enable-64bit

make %{?_smp_mflags}

%install
make %{?_smp_mflags} INSTALL_ROOT=%{buildroot} install

# Fixing some permissions
find %{buildroot}/%{tcl_sitearch} -name "*.sh" |xargs chmod 644
find %{buildroot}/%{tcl_sitearch} -name "*.tcl" |xargs chmod 644
find %{buildroot}/%{tcl_sitearch} -name "*.a" |xargs chmod 644
find %{buildroot}/%{tcl_sitearch} -name "*.so" |xargs chmod 755

# Make library links
mv %{buildroot}/%{tcl_sitearch}/*.sh %{buildroot}/%{_libdir}
for tcllibs in %{buildroot}/%{tcl_sitearch}/Img1.4/*tcl*.so; do
btcllibs=`basename $tcllibs`
ln -s tcl%{tcl_version}/Img1.4/$btcllibs %{buildroot}/%{_libdir}/$btcllibs
done

%ldconfig_scriptlets

%files
%doc README
%{_libdir}/*.so
%{tcl_sitearch}/Img1.4
%{_mandir}/mann/img*
%exclude %{tcl_sitearch}/Img1.4/*.a

%files devel
%doc README
%{_includedir}/*
%{_libdir}/*.sh
%{tcl_sitearch}/Img1.4/*.a

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Tom Callaway <spot@fedoraproject.org> - 1.4-32
- fix FTBFS

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Callaway <spot@fedoraproject.org> - 1.4-22
- modernize spec file

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Tom Callaway <spot@fedoraproject.org> - 1.4-20
- add missing libpng16 bits

* Mon Nov  3 2014 Tom Callaway <spot@fedoraproject.org> - 1.4-19
- add Requires: tk
- remove deprecated libpng api bit

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun  3 2014 Tom Callaway <spot@fedoraproject.org> - 1.4-16
- fix build against libpng 1.6

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.4-12
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 1.4-11
- rebuild against new libjpeg

* Tue Jul 31 2012 Tom Callaway <spot@fedoraproject.org> - 1.4-10
- fix for newer zlib (1.2.7+)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Tom Callaway <spot@fedoraproject.org> 1.4-8
- enable support for libtiff 4.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Tom Callaway <spot@fedoraproject.org> 1.4-6
- enable support for libpng 1.5

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.4-5
- Rebuild for new libpng

* Mon Aug  1 2011 Tom Callaway <spot@fedoraproject.org> - 1.4-4
- Unbundled libpng and libtiff

* Sun Feb 20 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4-3
- Unbundled zlib and libjpeg

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Sergio Pascual <sergiopr at fedoraproject.org> - tkimg-1.4-1
- Upstream releases 1.4

* Thu Oct 07 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4-0.9.20100906svn
- EVR bump. Upload source tarball

* Thu Oct 07 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4-0.8.20100906svn
- New upstream source

* Sat Feb 06 2010 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4-0.7.20091129svn
- Patch to obey mandir configure option

* Tue Dec 01 2009 Sergio Pascual <sergiopr at fedoraproject.org> - 1.4-0.6.20091129svn
- New upstream source, version 228 from trunk
- Provides man pages
- Passing tests for sgi format
- Fixes bz #542356

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-0.5.20081115svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-0.4.20081115svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Sergio Pascual <sergiopr at fedoraproject.org>  1.4-0.3.20081115svn
- Adding libXft-devel to build requires

* Tue Jan 20 2009 Sergio Pascual <sergiopr at fedoraproject.org>  1.4-0.2.20081115svn
- Reverting patches to fix bz #468357

* Sat Nov 15 2008 Sergio Pascual <sergiopr at fedoraproject.org>  1.4-0.1.20081115svn
- New upstream source, version 173 from trunk, release 1.4
- Relative links in libdir
- Removed ignored disable-static option in configure
- Patches simplified and separated by library

* Thu Jul 03 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3-0.12.200805005svn
- more syslibs fixes (note: this code is held together with spit and chewing gum)

* Thu Jul 03 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3-0.11.200805005svn
- fix configure to use --with-tcl=%%{tcl_sitearch}

* Mon May 05 2008 Sergio Pascual <sergiopr at fedoraproject.org> - 1.3-0.10.20080505svn
- New upstream source
- Including fooConfig.sh files in -devel 
- Making symlinks of shared libraries in libdir
- Removing file in ld.so.conf.d
- Fixing bug #444872

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-0.9.20071018svn
- Autorebuild for GCC 4.3

* Fri Jan 04 2008 Sergio Pascual <sergiopr at fedoraproject.org> 1.3-0.8.20071018svn
- Following PackagingDrafts/Tcl

* Thu Jan 03 2008 Sergio Pascual <sergiopr at fedoraproject.org> 1.3-0.7.20071018svn
- Rebuilt for tcl 8.5

* Mon Dec 24 2007 Sergio Pascual <sergiopr at fedoraproject.org> 1.3-0.6.20071018svn
- Static 'stub' library included in devel subpackage
- Rebuild to fix bug #426683

* Sat Nov 08 2007 Sergio Pascual <sergiopr at fedoraproject.org> 1.3-0.5.20071018svn
- Build patch simplified

* Mon Oct 29 2007 Sergio Pascual <sergiopr at fedoraproject.org> 1.3-0.4.20071018svn
- Giving instructions to duplicate my checkout

* Sun Oct 28 2007 Sergio Pascual <sergiopr at fedoraproject.org> 1.3-0.3.20071018svn
- Using dist tag

* Tue Oct 24 2007 Sergio Pascual <sergiopr at fedoraproject.org>  1.3-0.2.20071018svn
- Using external libraries

* Fri Mar 30 2007 Sergio Pascual <sergiopr at fedoraproject.org>  1.3-0.1.20071018svn
- Initial spec file
