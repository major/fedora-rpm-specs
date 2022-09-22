Name:           flam3
Version:        3.0.1
Release:        25%{?dist}
Summary:        Programs to generate and render cosmic recursive fractal flames

License:        GPLv2+
URL:            http://www.flam3.com/
Source0:        http://flam3.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         flam3-libpng15.patch

BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  chrpath
BuildRequires: make

%description
Flam3, or Fractal Flames, are algorithmically generated images and animations.
This is free software to render fractal flames as described on
http://flam3.com. Flam3-animate makes animations, and flam3-render makes still
images. Flam3-genome creates and manipulates genomes (parameter sets).


%package devel
Summary:        C headers to generate and render cosmic recursive fractal flames
Requires:       pkgconfig
Requires:       libxml2-devel
Requires:       libpng-devel
Requires:       libjpeg-devel
Requires:       flam3 = %{version}-%{release}

%description devel
Flam3, or Fractal Flames, are algorithmically generated images and animations.
This is free software to render fractal flames as described on
http://flam3.com. Flam3-animate makes animations, and flam3-render makes still
images. Flam3-genome creates and manipulates genomes (parameter sets). This
package contains a header file for C, a library, and a pkgconfig file.


%prep
%setup -qn %{name}-%{version}/src
%patch0 -p0 -b .libpng15


%build
%configure --prefix=%{_prefix} --includedir=%{_includedir}/%{name} --enable-shared
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm %{buildroot}/%{_libdir}/lib%{name}.la %{buildroot}/%{_libdir}/lib%{name}.a
chrpath --delete %{buildroot}%{_bindir}/flam3-*



%ldconfig_scriptlets


%files
%doc COPYING.txt README.txt
%{_bindir}/flam3-animate
%{_bindir}/flam3-convert
%{_bindir}/flam3-genome
%{_bindir}/flam3-render
%{_datadir}/flam3
%{_libdir}/libflam3.so.*
%{_mandir}/man1/flam3*

%files devel
%doc COPYING.txt README.txt
%{_includedir}/%{name}/
%{_libdir}/libflam3.so
%{_libdir}/pkgconfig/flam3.pc


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.0.1-6
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.0.1-5
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 26 2012 Bruno Wolff III <bruno@wolff.to> - 3.0.1-3
- Fix building with libpng 1.5

* Thu Jan 26 2012 Ian Weller <iweller@redhat.com> - 3.0.1-2
- Forgot to upload the new source

* Thu Jan 26 2012 Ian Weller <iweller@redhat.com> - 3.0.1-1
- Update to 3.0.1, hopefully it fixes libpng issues

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5.20101118svn35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.0-4.20101118svn35
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3.20101118svn35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Ian Weller <iweller@redhat.com> - 3.0-2.20101118svn35
- Update to svn r35, which fixes a couple of issues 3.0 had

* Mon Nov 15 2010 Ian Weller <iweller@redhat.com> - 3.0-1
- Update to 3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 18 2009 Ian Weller <ianweller@gmail.com> - 2.7.18-1
- Upstream update to 2.7.18:
    Added fuzz testing with zzuf to the regression tests.  'Strip'
    mode and genomes with the zoom parameter used now break into pieces
    properly.  insert_palette fixed (broken a few versions ago.)  fixed
    twintrian variation when small weights are used.  various rare
    segfaults and memory leaks fixed.  'palette_mode' attribute added to
    flame element for smoother palette interpolation in slow animations;
    possible values are 'step' and 'linear' ('step' mode is default and 
    matches previous behaviour.)  Release as 2.7.18.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 16 2008 Ian Weller <ianweller@gmail.com> 2.7.17-1
- Upstream updated:
    Add error checking on the numbers in the input genome.  Do
    not exit on read errors, fail gracefully. Changed sin/cos = tan in
    the tangent variation. Added polar to list of variations that use
    the inverted linear identity. Bugfix: temporal_filter_exp was not
    set properly in template. Apply interpolation attribute in
    templates. Add/publish datarootdir with pkg-config so the palette
    file is easy to find (for qosmic). Copyright by Spotworks LLC
    instead of Spot and Erik.  Add fuzz checks to the regression
    suite.  include LNX/OSX/WIN in the version string.  In
    flam3-genome animate command, added one to last flame time, so the
    end time is inclusive.  Release as 2.7.17.

* Thu Sep 11 2008 Ian Weller <ianweller@gmail.com> 2.7.16-1
- Upstream updated:
    Added 'clone_all' to flam3_genome to allow application of 
    template to all flames in a file at once, and 'animate' to write
    a full sequence of interpolations out.  'animate' is similar to 
    'sequence' except that no control point rotation is performed.  
    Fixed non-functional 'write_genome' env var for flam3_animate.  
    Two bugs associated with interpolating from a log interpolation_type
    to a non-log interpolation_type fixed (rotate angle reduction and 
    special inverted identity).  when using flam3_rotate in 'spin_inter'
    the interp type of the first genome is now used rather than the
    current genome's interp type.  Enforced upper and lower bounds for
    xform color and upper bound for interpolated colormap values
    as "smooth" interpolation led to values out of range.  If "smooth"
    interpolation is specified for all flames in a file, the first and
    second-to-last genome is switched to "linear" with a warning.
    spatial filters with non-box-filter window functions fixed.
    Release as 2.7.16.

* Wed Sep 03 2008 Ian Weller <ianweller@gmail.com> 2.7.15-1
- Upstream updated:
    Added new interpolation types 'old' and 'older', for use in 
    recreating old animations.  'linear' mode now does not rotate padded
    xforms (results in prettier symmetric singularities). switched to
    using a 'padding' flag instead of a 'just initialized' flag; padding 
    flag used for implementation of 'old' and 'older' types.  
    interpolation_space now deprecated, instead use interpolation_type. 
    flam3_align is now idempotent (multiple applications do not change
    the control points.)  Default number of temporal samples bumped to 
    1000.  Removed CVS headers from source code (now using SVN).
    Default interpolation mode now log. Removed 'move' and 'split' vars.
    changes to flam3-genome: sequence mode now returns linear 
    interpolation mode for all control points except first/last of edges 
    - these cps will use the original interpolation mode;  inter and 
    rotate modes will now return padded genomes for all control points,
    all with linear interpolation specified.  instead of centering 
    sometimes reframe by golden mean plus noise. Release as 2.7.15.

* Mon Aug 04 2008 Ian Weller <ianweller@gmail.com> 2.7.14-1
- Upstream updated:
    Add configuration option for atomic-ops.  bug fix: do not
    truncate floating point palettes.  new motion blur features: add
    temporal_filter_type, can be "box" (default) or "gaussian" or
    "exp".  Temporal_filter_width and temporal_filter_exp are parms to
    it.  'blur' env var no longer used.  Small bug fix: iteration
    count depends only on the size of the output image, not the padded
    image (the gutter).  When interpolating, only do -pi/pi adjustment
    for non-asymmetric cases.  Julian/juliascope variations use the
    alternate inverted identity for interpolation (reduces wedge
    effect).  Add python script for regression and consistency
    checking. Add svn revision number to version string (in the
    software not of the package). Release as 2.7.14.
- Remove patch for removing atomic ops for pre-GCC 4.3 packages

* Sat Jun 07 2008 Ian Weller <ianweller@gmail.com> 2.7.13-1
- Upstream updated

* Sun May 25 2008 Ian Weller <ianweller@gmail.com> 2.7.12-1
- Upstream updated

* Wed Apr 09 2008 Ian Weller <ianweller@gmail.com> 2.7.11-1
- Upstream updated

* Thu Mar 20 2008 Ian Weller <ianweller@gmail.com> 2.7.10-2
- Force rebuild due to odd quirk in Koji

* Thu Mar 20 2008 Ian Weller <ianweller@gmail.com> 2.7.10-1
- Upstream updated

* Sat Feb 09 2008 Ian Weller <ianweller@gmail.com> 2.7.9-1
- Upstream updated
- Upstream made changes based on our patches, so removed now redundant patches

* Fri Feb 01 2008 Ian Weller <ianweller@gmail.com> 2.7.8-4
- Made patch commands less confusing

* Tue Jan 29 2008 Ian Weller <ianweller@gmail.com> 2.7.8-3
- Removed config.h properly
- We now own datadir/flam3

* Mon Jan 28 2008 Ian Weller <ianweller@gmail.com> 2.7.8-2
- Added more missing headers -- they might be used by some program somewhere:
  private.h config.h img.h
- Fix atomic ops error on ppc and ppc64 with Patch1

* Sun Jan 27 2008 Ian Weller <ianweller@gmail.com> 2.7.8-1
- Updated to version 2.7.8
- Made sure that libflam3.la wasn't included, complying with review guidelines
  "Packages must NOT contain any .la libtool archives, these should be removed in the spec."

* Thu Jan 17 2008 Mamorut Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> 2.7.7-3
- Fix pkgconfig .pc file
- Install missing headers
- Move header files into %%{_includedir}/%%{name}
- Fix cflags to meet Fedora guidelines
- More Requires to -devel subpackage for static archive

* Wed Dec 19 2007 Ian Weller <ianweller@gmail.com> 2.7.7-2
- *-devel now includes *-static
- *-static no longer exists, but is provided by *-devel
- added version requirement to *-devel requires main

* Mon Dec 17 2007 Ian Weller <ianweller@gmail.com> 2.7.7-1
- Fixed spurious-executable-perm issue
- *-devel subpackage now requires *-static subpackage
- Subpackage now requires main package
- Update to version 2.7.7

* Sun Dec 16 2007 Ian Weller <ianweller@gmail.com> 2.7.6-2
- Dropped kernel from requires, as most people have one installed
- Created *-devel and *-static packages
- Removed redundant explicit requires
- Added COPYING.txt and README.txt documentation files

* Sun Dec 9 2007 Ian Weller <ianweller@gmail.com> 2.7.6-1
- First package build.
