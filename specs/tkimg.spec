%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:		tkimg
Version:	1.4.16
Release:	4%{?dist}
Summary:	Image support library for Tk
# The core tkimg code is TCL
# tiff/ is libtiff
# gif/gif.c is HPND-Pbmplus AND URT-RLE
# compat/libjpeg is IJG AND HPND-Pbmplus
# compat/libpng is Libpng AND (BSD-4-Clause OR GPL-2.0-or-later) AND BSD-4-Clause AND MIT
# compat/libtiff is libtiff AND MIT
#   ... (yes, the SPDX MIT)
# compat/zlib is Zlib
#   ... the dotzlib stuff is BSL-1.0, but I know it's not used here.
License:	TCL AND libtiff AND HPND-Pbmplus AND URT-RLE AND IJG AND Libpng AND (BSD-4-Clause OR GPL-2.0-or-later) AND BSD-4-Clause AND MIT AND Zlib
# Try saying that three times fast.
URL:		http://sourceforge.net/projects/tkimg
Source0:	https://downloads.sourceforge.net/project/tkimg/tkimg/1.4/Img-%{version}-Source.tar.gz
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	tcl-devel tk-devel tcllib

# CVE-2023-6277
# https://gitlab.com/libtiff/libtiff/-/issues/614
# https://gitlab.com/libtiff/libtiff/-/merge_requests/545
Patch0:	tkimg-libtiff-CVE-2023-6277.patch

# tkimg builds its own bundled copies of the zlib, libjpeg, libpng,
# and libtiff libraries. From the README:
#  Note that you have to build these libraries to
#  support the named formats, even if your system already has shared
#  libraries for these formats. This is because the libraries here are
#  built such that they can be loaded as packages by the Tcl/Tk core,
#  making the handling of the various dependencies much easier. An
#  earlier version, 1.2.4, used a modified copy of Tcl's functions for
#  loading of shared libraries to load the support libraries at runtime.
#  These have been abandoned in favor of the new approach.

Provides: bundled(zlib) = 1.2.13
Provides: bundled(libjpeg) = 9e
Provides: bundled(libpng) = 1.6.39
Provides: bundled(libtiff) = 4.5.0
Requires: tcl(abi) = 8.6
Requires: tk >= 8.6

%description
This package contains a collection of image format handlers for the Tk
photo image type, and a new image type, pixmaps.

%package devel
Summary:	Libraries, includes, etc. used to develop an application with %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	tcl-devel tk-devel

%description devel
These are the header files needed to develop a %{name} application

%prep
%setup -q -n Img-%{version}
%patch -P 0 -p1 -b .CVE-2023-6277

%build
%configure --with-tcl=%{tcl_sitearch} --with-tk=%{_libdir} --libdir=%{tcl_sitearch} --disable-threads --enable-64bit

make %{?_smp_mflags}

%install
make %{?_smp_mflags} INSTALL_ROOT=%{buildroot} install

%files
%doc README
%{tcl_sitearch}/Img%{version}
%{_mandir}/mann/img*
%exclude %{tcl_sitearch}/Img%{version}/*.a

%files devel
%doc README
%{_includedir}/*
%{tcl_sitearch}/*.sh
%{tcl_sitearch}/Img%{version}/*.a

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan  5 2024 Tom Callaway <spot@fedoraproject.org> - 1.4.16-1
- update to 1.4.16
- apply upstream (libtiff) fix for CVE-2023-6277
- update license tag

* Fri Dec  8 2023 Florian Weimer <fweimer@redhat.com> - 1.4.14-5
- Backport part of an upstream patch to fix C compatibility issues

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar  7 2023 Tom Callaway <spot@fedoraproject.org> - 1.4.14-3
- apply upstream libtiff fix for CVE-2022-4645

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Tom Callaway <spot@fedoraproject.org> - 1.4.14-1
- update to 1.4.14
- use bundled zlib, libpng, libjpeg, libtiff

* Fri Nov 18 2022 Florian Weimer <fweimer@redhat.com> - 1.4-38
- Eliminate implicit int declarations

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
