Summary: Image Blending with Multiresolution Splines
Name: enblend
Version: 4.2
Release: 32%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://downloads.sourceforge.net/enblend/enblend-enfuse-%{version}.tar.gz
Patch0: enblend-limits.patch
URL: http://enblend.sourceforge.net/
BuildRequires:  gcc-c++
BuildRequires: libtiff-devel boost-devel lcms2-devel plotutils-devel
BuildRequires: freeglut-devel glew-devel libjpeg-devel libpng-devel OpenEXR-devel
BuildRequires: libXmu-devel libXi-devel
BuildRequires: vigra-devel >= 1.9.0
BuildRequires: gsl-devel

# commenting-out 'hevea' disables pdf documentation
#BuildRequires: hevea
BuildRequires: gnuplot graphviz tidy help2man ImageMagick librsvg2-tools texinfo texinfo-tex
BuildRequires: tex(amsmath.sty) tex(bold-extra.sty) tex(color.sty) tex(enumitem.sty) tex(fixltx2e.sty)
BuildRequires: tex(footnote.sty) tex(graphicx.sty) tex(hyperref.sty) tex(hyphenat.sty) tex(ifpdf.sty)
BuildRequires: tex(index.sty) tex(latexsym.sty) tex(listings.sty) tex(microtype.sty) tex(nag.sty)
BuildRequires: tex(ragged2e.sty) tex(shorttoc.sty) tex(suffix.sty) tex(trivfloat.sty) tex(url.sty) tex(xstring.sty)
BuildRequires: texlive-floatrow texlive-comment texlive-epstopdf-bin texlive-latex-fonts texlive-thumbpdf texlive-texloganalyser
BuildRequires: perl-Readonly
BuildRequires: perl(English) perl(Sys::Hostname) perl(File::Basename) perl(Getopt::Long) perl(IO::File)
BuildRequires: make

%description
Enblend is a tool for compositing images, given a set of images that overlap in
some irregular way, Enblend overlays them in such a way that the seam between
the images is invisible, or at least very difficult to see.  Enfuse combines
multiple images of the same subject into a single image with good exposure and
good focus.  Enblend and Enfuse do not line up the images for you, use a tool
like Hugin to do that.

%package doc
Summary: Usage Documentation for enblend and enfuse
License: GFDL

%description doc
PDF usage documentation for the enblend and enfuse command line tools

%prep
%setup -q -n enblend-enfuse-%{version}
%patch -P0 -p1

%build
export CPPFLAGS="-std=gnu++14 -I/usr/include/gperftools"
%configure --with-boost-filesystem --with-tcmalloc --enable-opencl --enable-openmp
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING NEWS README

%{_bindir}/enblend
%{_bindir}/enfuse
%{_mandir}/man1/*

%files doc
%doc COPYING
#doc COPYING doc/enblend.pdf doc/enfuse.pdf
#{_docdir}/enblend-enfuse/examples/enfuse/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.2-31
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 4.2-29
- Rebuilt for openexr 3.2.4

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2-24
- Rebuild for gsl-2.7.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Jeff Law <law@fedoraproject.org> - 4.2-19
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-18
- Fix mass rebuild failure by adding core perl modules to BuildRequires. patch to #include <limits>

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 4.2-15
- Rebuilt for GSL 2.6.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Bruno Postle <bruno@postle.net> - 4.2-13
- enblend-doc package no longer contains pdf documentation

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 4.2-10
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Filipe Rosset <rosset.filipe@gmail.com> - 4.2-8
- rebuilt for new libgsl

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Filipe Rosset <rosset.filipe@gmail.com> - 4.2-5
- Spec cleanup, fixes rhbz#1462365 and rhbz#1423526

* Tue Feb 28 2017 Bruno Postle <bruno@postle.net> - 4.2-4
- Rebuilt after mass rebuild failure due to broken vigra

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 28 2016 Bruno Postle <bruno@postle.net> - 4.2-2
- rebuild for new vigra

* Wed Apr 13 2016 Bruno Postle <bruno@postle.net> - 4.2-1
- upstream stable release

* Wed Mar 02 2016 Bruno Postle <bruno@postle.net> - 4.1.4-6
- rebuilt for new libgsl

* Mon Feb 15 2016 Bruno Postle <bruno@postle.net> - 4.1.4-5
- patch for gcc6 backported from upstream hg

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Jonathan Wakely <jwakely@redhat.com> - 4.1.4-3
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 4.1.4-2
- Rebuild for glew 1.13

* Sat Oct 03 2015 Bruno Postle <bruno@postle.net> - 4.1.4-1
- stable bugfix release

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 4.1.3-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 4.1.3-6
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.1.3-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 4.1.3-3
- Rebuild for boost 1.57.0

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 4.1.3-2
- rebuild (openexr)

* Wed Oct 22 2014 Bruno Postle <bruno@postle.net> - 4.1.3-1
- stable bugfix release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 4.1.2-5
- rebuild for boost 1.55.0

* Mon Dec 30 2013 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-4
- rebuild (vigra)

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.1.2-3
- rebuild (openexr)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 4.1.2-2
- rebuilt for GLEW 1.10

* Mon Oct 07 2013 Bruno Postle - 4.1.2-1
- stable release

* Sat Sep 14 2013 Bruno Wolff III <bruno@wolff.to> - 4.1.1-6
- Rebuild for ilmbase related soname bumps

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 4.1.1-4
- Rebuild for boost 1.54.0

* Mon Mar 11 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.1.1-3
- avoid/fix pitfalls associated with texinfo-5.x (#919935)

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.1.1-2
- rebuild (OpenEXR)

* Fri Feb 15 2013 Bruno Postle - 4.1.1-1
- stable release

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.1-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 4.1-2
- Rebuild for Boost-1.53.0

* Sun Jan 20 2013 Bruno Postle <bruno@postle.net> - 4.1-1
- Upstream release
- No longer provides bundled(vigra)
- New enblend-doc sub package containing pdf documentation

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 4.0-17
- rebuild due to "jpeg8-ABI" feature drop

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 4.0-16
- Rebuild for glew 1.9.0

* Tue Nov 13 2012 Dan Horák <dan[at]danny.cz> - 4.0-15
- fix FTBFS due new boost

* Wed Aug 01 2012 Adam Jackson <ajax@redhat.com> - 4.0-14
- -Rebuild for new glew

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-12
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Bruno Postle <bruno@postle.net> - 4.0-10
- patch to build with new libpng

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 4.0-9
- Rebuild for new libpng

* Mon Jun 20 2011 ajax@redhat.com - 4.0-8
- Rebuild for new glew soname

* Fri Jun 17 2011 Bruno Postle <bruno@postle.net> - 4.0-7
- workaround vigra bug where arithmetic coded JPEG is always created with libjpeg-turbo

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 04 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 4.0-5
- rebuild for new boost

* Sat Feb 06 2010 Bruno Postle <bruno@postle.net> - 4.0-4
- add missing texinfo buildrequires

* Fri Feb 05 2010 Bruno Postle <bruno@postle.net> - 4.0-3
- Fixes for push to fedora

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Wed Oct 08 2008 Bruno Postle <bruno@postle.net> - 3.2-2
- don't package /usr/share/info/dir

* Tue Sep 23 2008 Bruno Postle <bruno@postle.net> - 3.2-1
- upstream release

* Thu Jun 5 2008 Bruno Postle <bruno@postle.net> - 3.1-0.5.20080529cvs
- Add OpenEXR-devel build dependency

* Thu May 1 2008 Bruno Postle <bruno@postle.net> - 3.1-0.4.20080529cvs
- CVS snapshot with GCC 4.3 upstream fix

* Mon Apr 7 2008 Jef Spaleta <jspaleta AT fedoraproject Dot org> - 3.1-0.3.20080216cvs
- Patching for GCC 4.3

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1-0.2.20080216cvs
- Autorebuild for GCC 4.3

* Sat Feb 16 2008 Bruno Postle <bruno@postle.net> 3.1-0.1.20090216cvs
  - CVS snapshot, 3.1 beta, tarball name change

* Mon Jan 21 2008 Bruno Postle <bruno@postle.net> 3.1-0.1.20090106cvs
  - CVS snapshot, 3.1 beta, switch to fedora cvs naming

* Sun Jan 06 2008 Bruno Postle <bruno@postle.net> 3.1-0cvs20090106
  - CVS snapshot, 3.1 beta

* Mon Aug 20 2007 Bruno Postle <bruno@postle.net> 3.0-6
  - glew is now in fedora, remove build-without-glew patch
  - update licence tag, GPL -> GPLv2+

* Tue Mar 20 2007 Bruno Postle <bruno@postle.net> 3.0-4
  - patch to build without glew library

* Sun Jan 28 2007 Bruno Postle <bruno@postle.net>
  - 3.0 release

* Tue Dec 13 2005 Bruno Postle <bruno@postle.net>
  - 2.5 release

* Tue Dec 06 2005 Bruno Postle <bruno@postle.net>
  - 2.4 release

* Mon Apr 18 2005 Bruno Postle <bruno@postle.net>
  - 2.3 release

* Mon Nov 15 2004 Bruno Postle <bruno@postle.net>
  - 2.1 release

* Mon Oct 18 2004 Bruno Postle <bruno@postle.net>
  - 2.0 release

* Wed Oct 13 2004 Bruno Postle <bruno@postle.net>
  - new build for fedora fc2

* Tue Jun 22 2004 Bruno Postle <bruno@postle.net>
  - found tarball of enblend-1.3 and updated to that

* Tue Jun 22 2004 Bruno Postle <bruno@postle.net>
  - added patch for reading nona multi-layer tiff files

* Tue Apr 27 2004 Bruno Postle <bruno@postle.net>
  - update to latest version

* Sat Apr 03 2004 Bruno Postle <bruno@postle.net>
  - update to latest version

* Tue Mar 09 2004 Bruno Postle <bruno@postle.net>
  - initial RPM

 
