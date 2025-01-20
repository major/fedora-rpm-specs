Name:		pfstools
Version:	2.2.0
Release:	18%{?dist}
Summary:	Programs for handling high-dynamic range images

License:	GPL-2.0-or-later
URL:		http://pfstools.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0:		pfstools-freeglut.patch
# From https://sourceforge.net/p/pfstools/bugs/54
Patch1:		0001-Prefer-upstream-CMake-Config-Mode-files-for-OpenEXR.patch
# From openSUSE
Patch2:		pfstools-ImageMagick7.patch

BuildRequires:  make
BuildRequires:	cmake
BuildRequires:	libtiff-devel
BuildRequires:	cmake(OpenEXR)
BuildRequires:	octave-devel
BuildRequires:	libGL-devel
BuildRequires:	ImageMagick-devel
BuildRequires:	freeglut-devel
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	perl-generators
BuildRequires:	pkgconfig(Qt5)
BuildRequires:	libXi-devel
BuildRequires:	netpbm-devel
BuildRequires:	texlive-latex
BuildRequires:	gsl-devel
BuildRequires:	fftw-devel
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description
pfstools is a set of command line programs for reading,
writing, manipulating and viewing high-dynamic range (HDR) images and
video frames. All programs in the package exchange data using unix
pipes and a simple generic HDR image format (pfs). The concept of the
pfstools is similar to netpbm package for low-dynamic range images.


%package -n pfscalibration
Summary:	Scripts and programs for photometric calibration
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	perl-interpreter
Requires:	dcraw
Requires:	jhead

%description -n pfscalibration
PFScalibration package provides an implementation of the Robertson et al. 2003
method for the photometric calibration of cameras, Mitsunaga and Nayar's
algorithm "Radiometric Self Calibration", and for the recovery of high dynamic
range (HDR) images from the set of low dynamic range (LDR) exposures.


%package -n pfstmo
Summary:	PFS tone mapping operators
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description -n pfstmo
The pfstmo package contains the implementation of state-of-the-art tone
mapping operators. The motivation here is to provide an implementation of
tone mapping operators suitable for convenient processing of both static
images and animations.


%package libs
Summary:	Libraries for HDR processing
License:	LGPLv2+

%description libs
The pfstools-libs package contains a runtime library of functions for
handling HDR graphics files.


%package qt
Summary:	Qt-based viewer for HDR files
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description qt
The pfstools-qt package contains viewer programs based on Qt5 for
viewing HDR graphics files.


%package glview
Summary:	GL-based viewer for HDR files
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description glview
The pfstools-glview package contains viewer programs based on OpenGL for
viewing HDR graphics files.


%package exr
Summary:	EXR file import for PFS tools
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description exr
The pfstools-exr package contains input and output filters for EXR files
to and from the HDR graphics file format used in pfstools.


%package imgmagick
Summary:	ImageMagick file import for PFS tools
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description imgmagick
The pfstools-exr package contains input and output filters based in
ImageMagick to and from the HDR graphics file format used in pfstools.


%package octave
Summary:	Octave interaction with PFS tools
Requires:	octave(api) = %{octave_api}

%description octave
The pfstools-octave package contains programs to process red, green and blue
channels or luminance channels in pfs stream using Octave.


%package devel
Summary:	Files for development with PFS tools
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The netpbm-devel package contains the header files and link libraries,
etc., for developing programs which can handle HDR graphics files.


%prep
%autosetup -p1

%build
%{?el7:export CXXFLAGS="%{optflags} -std=gnu++11"}
%if 0%{?fedora} >= 33
export CXXFLAGS="%{optflags} -std=gnu++11"
%endif
%{cmake} -DBUILD_SHARED_LIBS=ON -DLIB_DIR=%{_lib} -DWITH_OpenCV=OFF
# Not parallel build safe
%global _smp_build_ncpus 1
%{cmake_build}

%install
%{cmake_install}

# XXX Nuke unpackaged files
{ cd ${RPM_BUILD_ROOT}
  rm -f .%{_libdir}/libpfs-1.2.la
  rm -f .%{_mandir}/man1/pfsinjpeghdr.1
  rm -f .%{_mandir}/man1/pfsoutjpeghdr.1
}



%ldconfig_scriptlets libs


%files
%doc README
%{_bindir}/pfsabsolute
%{_bindir}/pfscat
%{_bindir}/pfsclamp
%{_bindir}/pfscut
%{_bindir}/pfsextractchannels
%{_bindir}/pfsdisplayfunction
%{_bindir}/pfsflip
%{_bindir}/pfsgamma
%{_bindir}/pfsin
%{_bindir}/pfsindcraw
%{_bindir}/pfsinpfm
%{_bindir}/pfsinppm
%{_bindir}/pfsinrgbe
%{_bindir}/pfsintiff
%{_bindir}/pfsinyuv
%{_bindir}/pfsout
%{_bindir}/pfsouthdrhtml
%{_bindir}/pfsoutpfm
%{_bindir}/pfsoutppm
%{_bindir}/pfsoutrgbe
%{_bindir}/pfsouttiff
%{_bindir}/pfsoutyuv
%{_bindir}/pfspad
%{_bindir}/pfspanoramic
%{_bindir}/pfsrotate
%{_bindir}/pfssize
%{_bindir}/pfstag
%{_bindir}/pfscolortransform
%{_bindir}/pfsretime
%{_bindir}/pfs_automerge
%{_bindir}/pfs_split_exposures.py
%{_datadir}/pfstools/hdrhtml_c_b2.csv
%{_datadir}/pfstools/hdrhtml_c_b3.csv
%{_datadir}/pfstools/hdrhtml_c_b4.csv
%{_datadir}/pfstools/hdrhtml_c_b5.csv
%{_datadir}/pfstools/hdrhtml_default_templ/
%{_datadir}/pfstools/hdrhtml_hdrlabs_templ/
%{_datadir}/pfstools/hdrhtml_t_b2.csv
%{_datadir}/pfstools/hdrhtml_t_b3.csv
%{_datadir}/pfstools/hdrhtml_t_b4.csv
%{_datadir}/pfstools/hdrhtml_t_b5.csv
%{_mandir}/man1/pfsabsolute.1.gz
%{_mandir}/man1/pfscat.1.gz
%{_mandir}/man1/pfsclamp.1.gz
%{_mandir}/man1/pfscut.1.gz
%{_mandir}/man1/pfsdisplayfunction.1.gz
%{_mandir}/man1/pfsextractchannels.1.gz
%{_mandir}/man1/pfsflip.1.gz
%{_mandir}/man1/pfsgamma.1.gz
%{_mandir}/man1/pfsin.1.gz
%{_mandir}/man1/pfsindcraw.1.gz
%{_mandir}/man1/pfsinpfm.1.gz
%{_mandir}/man1/pfsinppm.1.gz
%{_mandir}/man1/pfsinrgbe.1.gz
%{_mandir}/man1/pfsintiff.1.gz
%{_mandir}/man1/pfsinyuv.1.gz
%{_mandir}/man1/pfsout.1.gz
%{_mandir}/man1/pfsouthdrhtml.1.gz
%{_mandir}/man1/pfsoutpfm.1.gz
%{_mandir}/man1/pfsoutppm.1.gz
%{_mandir}/man1/pfsoutrgbe.1.gz
%{_mandir}/man1/pfsouttiff.1.gz
%{_mandir}/man1/pfsoutyuv.1.gz
%{_mandir}/man1/pfspad.1.gz
%{_mandir}/man1/pfspanoramic.1.gz
%{_mandir}/man1/pfsrotate.1.gz
%{_mandir}/man1/pfssize.1.gz
%{_mandir}/man1/pfstag.1.gz
%{_mandir}/man1/pfscolortransform.1.gz
%{_mandir}/man1/pfsretime.1.gz
%{_mandir}/man1/pfs_automerge.1.gz
%doc

%files -n pfscalibration
%{_bindir}/dcraw2hdrgen
%{_bindir}/jpeg2hdrgen
%{_bindir}/pfshdrcalibrate
%{_bindir}/pfsinhdrgen
%{_bindir}/pfsinme
%{_bindir}/pfsplotresponse
%{_mandir}/man1/dcraw2hdrgen.1.gz
%{_mandir}/man1/jpeg2hdrgen.1.gz
%{_mandir}/man1/pfshdrcalibrate.1.gz
%{_mandir}/man1/pfsinhdrgen.1.gz
%{_mandir}/man1/pfsinme.1.gz
%{_mandir}/man1/pfsplotresponse.1.gz

%files -n pfstmo
%{_bindir}/pfstmo_reinhard05
%{_bindir}/pfstmo_pattanaik00
%{_bindir}/pfstmo_mantiuk06
%{_bindir}/pfstmo_fattal02
%{_bindir}/pfstmo_drago03
%{_bindir}/pfstmo_reinhard02
%{_bindir}/pfstmo_durand02
%{_bindir}/pfstmo_mantiuk08
%{_bindir}/pfstmo_ferradans11
%{_bindir}/pfstmo_mai11
%{_mandir}/man1/pfstmo_reinhard05.1.gz
%{_mandir}/man1/pfstmo_pattanaik00.1.gz
%{_mandir}/man1/pfstmo_mantiuk06.1.gz
%{_mandir}/man1/pfstmo_fattal02.1.gz
%{_mandir}/man1/pfstmo_drago03.1.gz
%{_mandir}/man1/pfstmo_reinhard02.1.gz
%{_mandir}/man1/pfstmo_durand02.1.gz
%{_mandir}/man1/pfstmo_mantiuk08.1.gz
%{_mandir}/man1/pfstmo_ferradans11.1.gz
%{_mandir}/man1/pfstmo_mai11.1.gz

%files libs
%{_libdir}/libpfs.so.2.0.0
%{_libdir}/libpfs.so.2

%files qt
%{_bindir}/pfsv
%{_bindir}/pfsview
%{_mandir}/man1/pfsview.1.gz

%files glview
%{_bindir}/pfsglview
%{_mandir}/man1/pfsglview.1.gz

%files exr
%{_bindir}/pfsinexr
%{_bindir}/pfsoutexr
%{_mandir}/man1/pfsinexr.1.gz
%{_mandir}/man1/pfsoutexr.1.gz

%files imgmagick
%{_bindir}/pfsinimgmagick
%{_bindir}/pfsoutimgmagick
%{_mandir}/man1/pfsinimgmagick.1.gz
%{_mandir}/man1/pfsoutimgmagick.1.gz

%files octave
%{_bindir}/pfsoctavelum
%{_bindir}/pfsoctavergb
%{_bindir}/pfsstat
%{_libdir}/octave/*/site/oct/*/pfstools
%{_datadir}/octave/*/site/m/pfstools
%{_mandir}/man1/pfsoctavelum.1.gz
%{_mandir}/man1/pfsoctavergb.1.gz
%{_mandir}/man1/pfsstat.1.gz

%files devel
#%doc doc/pfs_format_spec.pdf
%{_libdir}/libpfs.so
%{_libdir}/pkgconfig/pfs.pc
%{_includedir}/pfs

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 14 2024 Orion Poplawski <orion@nwra.com> - 2.2.0-17
- Rebuild for octave 9.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.2.0-15
- Rebuilt for openexr 3.2.4

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 08 2023 Orion Poplawski <orion@nwra.com> - 2.2.0-11
- Rebuild with octave 8.1.0

* Fri Mar 31 2023 Tomas Smetana <tsmetana@redhat.com> - 2.2.0-10
- Use SPDX tag for license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Neal Gompa <ngompa@fedoraproject.org> - 2.2.0-8
- Rebuild for ImageMagick 7

* Sun Dec 04 2022 Neal Gompa <ngompa@fedoraproject.org> - 2.2.0-7
- Add patches for upgraded dependency compatibility
  + Add patch for ImageMagick 7 compatibility
  + Add patch for OpenEXR 3+ compatibility

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-6
- Rebuild for gsl-2.7.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Orion Poplawski <orion@nwra.com> - 2.2.0-4
- Rebuild for octave 7.1

* Thu May 12 2022 Orion Poplawski <orion@nwra.com> - 2.2.0-3
- Use current cmake macros (Fix FTBFS)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 20 2021 Tomas Smetana <tsmetana@redhat.com> - 2.2.0-1
- Rebase to upstream 2.2.0 verison, drop upstreamed patches

* Wed Aug 11 2021 Orion Poplawski <orion@nwra.com> - 2.1.0-20
- Rebuild for octave 6.3.0

* Sun Aug 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-19
- Move to openexr2 compat package.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-16
- rebuild against New OpenEXR again

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-15
- Rebuild for OpenEXR 2.5.3.

* Tue Aug 18 2020 Jeff Law <law@redhat.com> - 2.1.0-14
- Force C++11 as this code is not C++17 ready

* Thu Aug 06 2020 Tomas Smetana <tsmetana@redhat.com> - 2.1.0-13
- Fix #1865214: Update spec for new cmake

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.1.0-9
- Rebuilt for new freeglut

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 2.1.0-8
- Rebuilt for GSL 2.6.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Orion Poplawski <orion@nwra.com> - 2.1.0-6
- Rebuild for octave 5.1

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 2.1.0-5
- Rebuild for OpenEXR 2.3.0.

* Wed Feb 13 2019 Tomas Smetana <tsmetana@redhat.com> - 2.1.0-4
- Bump release

* Wed Feb 13 2019 Tomas Smetana <tsmetana@redhat.com> - 2.1.0-3
- Rebuild (FTBFS with new cmake)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-1
- Update to 2.1.0
- Switch to Qt5
- Rebuild for octave 4.4

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 2.0.6-9
- Rebuild for ImageMagick 6.9.10

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 08 2017 Tomas Smetana <tsmetana@redhat.com> - 2.0.6-6
- Rebuild for new ImageMagick

* Tue Aug 29 2017 Tomas Smetana <tsmetana@redhat.com> - 2.0.6-5
- Rebuild for new ImageMagick

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Kevin Fenzi <kevin@scrye.com> - 2.0.6-3
- Rebuild for new ImageMagick

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2.0.6-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Tomas Smetana <tsmetana@redhat.com> - 2.0.6-1
- New upstream bugfix-only release

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 2.0.5-4
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 07 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.5-2
- Rebuild for octave 4.2

* Wed Jun 08 2016 Tomas Smetana <tsmetana@redhat.com> - 2.0.5-1
- Update to new upstream version, drop upstreamed patches

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.4-3
- Rebuild for gsl 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Tomas Smetana <tsmetana@redhat.com> - 2.0.4-1
- Update to new upstream version
- pfscalibration and pfstools are now part of pfstools

* Tue Jul 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.5-23
- Rebuild for octave 4.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.5-21
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 10 2015 Tomas Smetana <tsmetana@redhat.com> 1.8.5-20
- rebuild for the new ImageMagick and gcc-5

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1.8.5-19
- rebuild(openexr), s|qt-devel|qt4-devel|, tighten subpkg deps (via %%{?_isa})

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-16
- Rebuild for the ImageMagick

* Sat Dec 28 2013 Kevin Fenzi <kevin@scrye.com> - 1.8.5-15
- Rebuild to fix broken deps

* Fri Dec 06 2013 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-14
- Patch for the #1037243 (-Werror=format-security) non-bug

* Thu Nov 28 2013 Rex Dieter <rdieter@fedoraproject.org> 1.8.5-13
- rebuild (openexr)

* Fri Oct 11 2013 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-12
- Another rebuild for ImageMagick

* Fri Sep 13 2013 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-11
- Rebuild for new ImageMagick

* Tue Aug 27 2013 Orion Poplawski <orion@cora.nwra.com> - 1.8.5-10
- Rebuild for gdal 1.10.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-8
- fix #926324: add autoreconf -if to support aarch64

* Wed Mar 20 2013 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-7
- rebuild for new ImageMagick

* Mon Mar 11 2013 Rex Dieter <rdieter@fedoraproject.org> - 1.8.5-6
- rebuild (OpenEXR)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-3
- rebuild for new libtiff

* Fri Mar 02 2012 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-2
- rebuild for new ImageMagick

* Thu Feb 16 2012 Tomas Smetana <tsmetana@redhat.com> - 1.8.5-1
- New upstream version

* Wed Jan 18 2012 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.8.3-5
- Rebuild against octave 3.6.0.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 16 2011 Jindrich Novy <jnovy@redhat.com> - 1.8.3-3
- rebuild against new libnetpbm

* Thu Aug 18 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.8.3-2
- Add dependecy on octave(api) in -octave.
- Rebuild for octave 3.4.2.

* Tue May 10 2011 Orion Poplawski <orion@cora.nwra.com> - 1.8.3-1
- Update to upstream release 1.8.3
- pfsview now uses qt4
- Rebuild for octave 3.4.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.8.1-3
- Rebuilt for gcc bug 634757

* Mon Sep 20 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 1.8.1-2
- rebuild for new ImageMagick

* Sun Oct 25 2009 Ulrich Drepper <drepper@redhat.com> - 1.8.1-1
- Update to upstream release 1.8.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  9 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.7.0-7
- Patch to generate useful debuginfo subpackage (#499912).
- Disable autotools dependency tracking during build for cleaner build logs
  and possible slight build speedup.

* Sun May 10 2009 Ulrich Drepper <drepper@redhat.com> - 1.7.0-6
- fix up spec file.  Remove unnecessary code.
- fix comparison of strings

* Mon Mar 23 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.7.0-5
- Add patch to fix building with GCC 4.4

* Wed Feb 25 2009 Ulrich Drepper <drepper@redhat.com> - 1.7.0-4
- recompile for hdf5 ABI change

* Wed Feb 4 2009 Ulrich Drepper <drepper@redhat.com> - 1.7.0-3
- add missing directories to spec file

* Mon Jan 5 2009 Ulrich Drepper <drepper@redhat.com> - 1.7.0-2
- Fix BuildRequires

* Fri Jan 2 2009 Ulrich Drepper <drepper@redhat.com> - 1.7.0-1
- update to most recent upstream release
  - new subpackage pfstools-gdal for GIS data handling
  - new program pfsdisplayfunction

* Fri Jan 2 2009 Ulrich Drepper <drepper@redhat.com> - 1.6.5-5
- add automake BuildRequires

* Wed Nov 5 2008 Ulrich Drepper <drepper@redhat.com> - 1.6.5-4
- ship more doc files

* Sun Oct 12 2008 Ulrich Drepper <drepper@redhat.com> - 1.6.5-3
- .spec file cleanups
- install Octave files without execution permission

* Wed Sep 03 2008 Manuel Wolfshant <wolfy@fedoraproject.org> - 1.6.5-2
- fix missing BR, Source URL, double inclusion of several files
- preserve timestamps

* Tue Aug 19 2008 Ulrich Drepper <drepper@redhat.com> - 1.6.5-1
- Initial package.
