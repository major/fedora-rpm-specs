%bcond levmar %{defined fedora}

Name:           teem
Version:        1.11.0
%global so_version 1
Release:        %autorelease -b 13
Summary:        Libraries for processing and visualizing scientific raster data

# The entire source is LGPL-2.1-or-later WITH Simple-Library-Usage-exception,
# except files noted at the License fields of certain subpackages.
#
# See https://gitlab.com/fedora/legal/fedora-license-data/-/issues/658,
# https://github.com/spdx/license-list-xml/issues/2745.
License:        LGPL-2.1-or-later WITH Simple-Library-Usage-exception
# Additionally, the following are removed in %%prep to assert that they do not
# contribute to the built package:
#
# Zlib:
#   arch/win32/include/zlib.h
# MIT:
#   python/ctypes/Nrrd.py
#   python/ctypes/pullDemo.py
#   python/ctypes/teem-gen.py
#   python/ctypes/teem.py
SourceLicense:  %{license} AND BSD-3-Clause AND MIT AND Zlib
URL:            https://teem.sourceforge.net
Source0:        https://downloads.sourceforge.net/project/teem/teem/%{version}/teem-%{version}-src.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

Source1:        gprobe.1
Source2:        ilk.1
Source3:        miter.1
Source4:        mrender.1
Source5:        nrrdSanity.1
Source6:        overrgb.1
Source7:        puller.1
Source8:        tend.1
Source9:        unu.1
Source10:       vprobe.1

Source800:      tend-about.1
Source801:      tend-grads.1
Source802:      tend-epireg.1
Source803:      tend-bmat.1
Source804:      tend-estim.1
Source805:      tend-sim.1
Source806:      tend-mfit.1
Source807:      tend-mconv.1
Source808:      tend-msim.1
Source809:      tend-make.1
Source810:      tend-avg.1
Source811:      tend-helix.1
Source812:      tend-sten.1
Source813:      tend-glyph.1
Source814:      tend-ellipse.1
Source815:      tend-anplot.1
Source816:      tend-anvol.1
Source817:      tend-anscale.1
Source818:      tend-anhist.1
Source819:      tend-triple.1
Source820:      tend-tconv.1
Source821:      tend-point.1
Source822:      tend-slice.1
Source823:      tend-norm.1
Source824:      tend-fiber.1
Source825:      tend-eval.1
Source826:      tend-evalpow.1
Source827:      tend-evalclamp.1
Source828:      tend-evaladd.1
Source829:      tend-evalmult.1
Source830:      tend-log.1
Source831:      tend-exp.1
Source832:      tend-evec.1
Source833:      tend-evecrgb.1
Source834:      tend-evq.1
Source835:      tend-unmf.1
Source836:      tend-expand.1
Source837:      tend-shrink.1
Source838:      tend-bfit.1
Source839:      tend-satin.1

Source900:      unu-about.1
Source901:      unu-env.1
Source902:      unu-i2w.1
Source903:      unu-w2i.1
Source904:      unu-make.1
Source905:      unu-head.1
Source906:      unu-data.1
Source907:      unu-convert.1
Source908:      unu-resample.1
Source909:      unu-fft.1
Source910:      unu-cmedian.1
Source911:      unu-dist.1
Source912:      unu-minmax.1
Source913:      unu-cksum.1
Source914:      unu-diff.1
Source915:      unu-quantize.1
Source916:      unu-unquantize.1
Source917:      unu-project.1
Source918:      unu-slice.1
Source919:      unu-sselect.1
Source920:      unu-dice.1
Source921:      unu-splice.1
Source922:      unu-join.1
Source923:      unu-crop.1
Source924:      unu-acrop.1
Source925:      unu-inset.1
Source926:      unu-pad.1
Source927:      unu-reshape.1
Source928:      unu-permute.1
Source929:      unu-swap.1
Source930:      unu-shuffle.1
Source931:      unu-flip.1
Source932:      unu-unorient.1
Source933:      unu-axinfo.1
Source934:      unu-axinsert.1
Source935:      unu-axsplit.1
Source936:      unu-axdelete.1
Source937:      unu-axmerge.1
Source938:      unu-tile.1
Source939:      unu-untile.1
Source940:      unu-histo.1
Source941:      unu-dhisto.1
Source942:      unu-jhisto.1
Source943:      unu-histax.1
Source944:      unu-heq.1
Source945:      unu-gamma.1
Source946:      unu-1op.1
Source947:      unu-2op.1
Source948:      unu-3op.1
Source949:      unu-affine.1
Source950:      unu-lut.1
Source951:      unu-mlut.1
Source952:      unu-subst.1
Source953:      unu-rmap.1
Source954:      unu-mrmap.1
Source955:      unu-imap.1
Source956:      unu-lut2.1
Source957:      unu-ccfind.1
Source958:      unu-ccadj.1
Source959:      unu-ccmerge.1
Source960:      unu-ccsettle.1
Source961:      unu-save.1

# This is the combination of an older patch to fix library install paths to
# suit FHS standards for Fedora, and some adjustments for compatibility with
# CMake 4. This is downstream-only for now because upstream development has
# progressed so far since the last stable release (in 2012!) that
# CMakeLists.txt now looks quite different. However, a new release is planned,
# and we should re-evaluate what might need to be upstreamed when that happens.
Patch:          teem-1.11.0-cmake.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  bzip2-devel
BuildRequires:  fftw-devel
%if %{with levmar}
BuildRequires:  levmar-devel
%endif

%global common_description %{expand:
What Is Teem?

Teem is a coordinated group of libraries for representing, processing, and
visualizing scientific raster data. Teem includes command-line tools that
permit the library functions to be quickly applied to files and streams,
without having to write any code. The most important and useful libraries in
Teem are:

  • Nrrd (and the unu command-line tool on top of it) supports a range of
    operations for transforming N-dimensional raster data (resample, crop,
    slice, project, histogram, etc.), as well as the NRRD file format for
    storing arrays and their meta-information.
  • Gage: fast convolution-based measurements at arbitrary point locations in
    volume datasets (scalar, vector, tensor, etc.)
  • Mite: a multi-threaded ray-casting volume render with transfer functions
    based on any quantity Gage can measure
  • Ten: for estimating, processing, and visualizing diffusion tensor fields,
    including fiber tractography methods.

Strengths of Teem

  • Teem works: Its purpose is to enable research in visualization and image
    processing, and research is enabled when simple things are simple to do.
    Teem’s functionality and its ease of use have allowed it to become a
    component of larger research software projects, such as SCIRun and 3D
    Slicer.
  • Teem is light-weight: The libraries are written with an eye towards
    minimizing the annoyance of getting data in an out, by using the simplest
    possible constructs for the job, and by supporting combinations of
    operations that arise in common practice.
  • Teem is coherent: There is a consistent logic to how information is
    represented, and uniformity in the APIs across libraries.
  • Teem is portable: All the code is written in plain ANSI C, so it compiles
    everywhere, including Windows, using either CMake or GNU Make. A Dashboard
    is used to monitor compiler errors and warnings.
  • Teem is growing: Some Teem libraries were created years ago and have
    remained stable, but new libraries and new functionality are continually
    being added.
  • Teem is open source: Anyone can use it, and contributions are welcome. Teem
    is licensed under the GNU Lesser General Public License, plus exceptions
    which facilitate linking Teem into binary-only applications.}

%description %{common_description}

The teem package contains the command-line tools included with Teem.


%package libs
Summary:        Libraries for teem

%description libs %{common_description}

The teem-libs package contains libraries that may be required at runtime by
applications that use Teem.


%package devel
Summary:        Development files for teem

Requires:       teem-libs%{?_isa} = %{version}-%{release}

%description devel %{common_description}

The teem-devel package contains libraries and header files for developing
applications that use Teem.


%package examples
Summary:        Examples for developing with for teem
# The entire contents of this subpackage are
# LGPL-2.1-or-later WITH Simple-Library-Usage-exception, except:
#
# Zlib:
#   UseTeemCMakeDemo/sanity.c
# BSD-3-Clause:
#   Examples/sanity/sanity.c
License:        %{shrink:
    LGPL-2.1-or-later WITH Simple-Library-Usage-exception AND
    Zlib AND
    BSD-3-Clause
    }
BuildArch:      noarch

%description examples %{common_description}

The teem-examples package contains examples for developing applications that
use Teem.


%prep
%autosetup -n teem-%{version}-src -p1

# Remove files that, while they have acceptable licenses, we want to assert do
# not contribute to the built RPMs:
#   - Not applicable to this platform
rm -rvf arch/win32
#   - Nothing here appears suitable for packaging:
rm -rvf python


%conf
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DTeem_USE_LIB_INSTALL_SUBDIR=ON \
    -DTeem_FFTW3=ON \
    -DTeem_LEVMAR=%{?with_levmar:ON}%{?!with_levmar:OFF}


%build
%cmake_build


%install
%cmake_install

install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -p -m 0644 \
    %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
    %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} \
    %{SOURCE800} %{SOURCE801} %{SOURCE802} %{SOURCE803} %{SOURCE804} \
    %{SOURCE805} %{SOURCE806} %{SOURCE807} %{SOURCE808} %{SOURCE809} \
    %{SOURCE810} %{SOURCE811} %{SOURCE812} %{SOURCE813} %{SOURCE814} \
    %{SOURCE815} %{SOURCE816} %{SOURCE817} %{SOURCE818} %{SOURCE819} \
    %{SOURCE820} %{SOURCE821} %{SOURCE822} %{SOURCE823} %{SOURCE824} \
    %{SOURCE825} %{SOURCE826} %{SOURCE827} %{SOURCE828} %{SOURCE829} \
    %{SOURCE830} %{SOURCE831} %{SOURCE832} %{SOURCE833} %{SOURCE834} \
    %{SOURCE835} %{SOURCE836} %{SOURCE837} %{SOURCE838} %{SOURCE839} \
    %{SOURCE900} %{SOURCE901} %{SOURCE902} %{SOURCE903} %{SOURCE904} \
    %{SOURCE905} %{SOURCE906} %{SOURCE907} %{SOURCE908} %{SOURCE909} \
    %{SOURCE910} %{SOURCE911} %{SOURCE912} %{SOURCE913} %{SOURCE914} \
    %{SOURCE915} %{SOURCE916} %{SOURCE917} %{SOURCE918} %{SOURCE919} \
    %{SOURCE920} %{SOURCE921} %{SOURCE922} %{SOURCE923} %{SOURCE924} \
    %{SOURCE925} %{SOURCE926} %{SOURCE927} %{SOURCE928} %{SOURCE929} \
    %{SOURCE930} %{SOURCE931} %{SOURCE932} %{SOURCE933} %{SOURCE934} \
    %{SOURCE935} %{SOURCE936} %{SOURCE937} %{SOURCE938} %{SOURCE939} \
    %{SOURCE940} %{SOURCE941} %{SOURCE942} %{SOURCE943} %{SOURCE944} \
    %{SOURCE945} %{SOURCE946} %{SOURCE947} %{SOURCE948} %{SOURCE949} \
    %{SOURCE950} %{SOURCE951} %{SOURCE952} %{SOURCE953} %{SOURCE954} \
    %{SOURCE955} %{SOURCE956} %{SOURCE957} %{SOURCE958} %{SOURCE959} \
    %{SOURCE960} %{SOURCE961}


%check
# Tests probeSS_ctmr04 and probeSS_ctmr10 have overly-strict rounding
# requirements; they fail on certain architectures, and the details may differ
# in e.g. EPEL branches. We find it best to skip them unconditionally.
%global ctest_excludes --exclude-regex '^(probeSS_ctmr(04|10))$'

# Tests are not parallel-safe
%global _smp_mflags -j1
%ctest %{?ctest_excludes}


%files
%doc README.txt
%{_bindir}/gprobe
%{_bindir}/ilk
%{_bindir}/miter
%{_bindir}/mrender
%{_bindir}/nrrdSanity
%{_bindir}/overrgb
%{_bindir}/puller
%{_bindir}/tend
%{_bindir}/unu
%{_bindir}/vprobe

%{_mandir}/man1/gprobe.1*
%{_mandir}/man1/ilk.1*
%{_mandir}/man1/miter.1*
%{_mandir}/man1/mrender.1*
%{_mandir}/man1/nrrdSanity.1*
%{_mandir}/man1/overrgb.1*
%{_mandir}/man1/puller.1*
%{_mandir}/man1/tend.1*
%{_mandir}/man1/tend-*.1*
%{_mandir}/man1/unu.1*
%{_mandir}/man1/unu-*.1*
%{_mandir}/man1/vprobe.1*


%files libs
%license LICENSE.txt
%{_libdir}/libteem.so.%{so_version}{,.*}


%files devel
%{_includedir}/teem/
%{_libdir}/libteem.so
%{_libdir}/cmake/Teem-%{version}/


%files examples
%license LICENSE.txt
%doc Examples
%doc UseTeemCMakeDemo


%changelog
%autochangelog
