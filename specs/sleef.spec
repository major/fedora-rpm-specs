%bcond dft 1
%bcond quad 1
# Fedora packages should not ship static libraries unless absolutely required.
# Some software may really rely on the inline headers and accompanying static
# support library for exceptional performance requirements, but we will leave
# this feature disabled until someone asks for it.
%bcond static 0

# Adds a BuildRequires on tlfloat and enables more tests
%bcond tlfloat 1

Name:           sleef
Version:        3.9.0
%global tag %{version}
%global so_version 3
Release:        %autorelease
Summary:        Vectorized math library

# The entire source is BSL-1.0, except the following gencoef tool sources,
# which are CC-BY-4.0:
#   src/gencoef/dp.h
#   src/gencoef/gencoef.c
#   src/gencoef/ld.h
#   src/gencoef/qp.h
#   src/gencoef/simplexfr.c
#   src/gencoef/sp.h
# Since CC-BY-4.0 is allowed for content but not for code, these are removed
# before uploading the source to the lookaside cache.
License:        BSL-1.0
URL:            https://sleef.org
# This is a filtered version of:
#   https://github.com/shibatch/sleef/archive/%%{tag}/sleef-%%{tag}.tar.gz
# See the comment above License for why this is necessary. The archive is
# produced by using the script in Source1:
#   ./get_source.sh ${VERSION}
Source0:        sleef-%{tag}-filtered.tar.zst
Source1:        get_source.sh

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# On aarch64, since 3.9.0, we cannot link at least bin/tester3svenofma when LTO
# is enabled, due to confusion about SVE.
#
#   /builddir/build/BUILD/sleef-3.9.0-build/sleef-3.9.0/src/common/testerutil.c:
#   In function ‘memrand.constprop’:
#   /builddir/build/BUILD/sleef-3.9.0-build/sleef-3.9.0/src/common/testerutil.c:101:6:
#   error: this operation requires the SVE ISA extension
#     101 | void memrand(void *p, int size) {
#         |      ^
#   /builddir/build/BUILD/sleef-3.9.0-build/sleef-3.9.0/src/common/testerutil.c:101:6:
#   note: you can enable SVE using the command-line option ‘-march’, or by
#   using the ‘target’ attribute or pragma
#   /builddir/build/BUILD/sleef-3.9.0-build/sleef-3.9.0/src/common/testerutil.c:101:
#   confused by earlier errors, bailing out
#
# This might be an upstream bug, but it is hard to understand. Upstream
# provides their own LTO option, SLEEF_ENABLE_LTO, but for does not support it
# in combination with shared libraries.
#
# - We could still build the library with LTO and not test it
#   (-DSLEEF_BUILD_TESTS:BOOL=FALSE) on aarch64.
# - It’s not clear how we could disable LTO *only for the tests*.
# - We choose to disable LTO entirely on aarch64, because we really want to run
#   the tests. We hope that the performance impact is not significant. It
#   currently does not seem necessary to disable LTO on other architectures.
%ifarch %{arm64}
%global _lto_cflags %{nil}
%endif

BuildRequires:  cmake >= 3.4.3
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# For tests only:
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libcrypto)
%if %{with dft}
BuildRequires:  pkgconfig(fftw3)
%endif
%if %{with tlfloat}
BuildRequires:  pkgconfig(tlfloat)
%endif

# See https://sleef.org/additional.xhtml#gnuabi. The gnuabi version of the
# library only applies to these architectures.
%global gnuabi_arches %{ix86} %{x86_64} %{arm64}
# See https://github.com/shibatch/sleef/pull/283.
%if %{with static}
%global inline_enabled 1
%endif

%description
SLEEF stands for SIMD Library for Evaluating Elementary Functions. It
implements vectorized versions of all C99 real floating point math functions.
It can utilize SIMD instructions that are available on modern processors. SLEEF
is designed to efficiently perform computation with SIMD instructions by
reducing the use of conditional branches and scatter/gather memory access.

The library contains implementations of all C99 real FP math functions in
double precision and single precision. Different accuracy of the results can be
chosen for a subset of the elementary functions; for this subset there are
versions with up to 1 ULP error (which is the maximum error, not the average)
and even faster versions with a few ULPs of error. For non-finite inputs and
outputs, the functions return correct results as specified in the C99 standard.


%package devel
Summary:        Development files for sleef
Requires:       sleef%{?_isa} = %{version}-%{release}

%description devel
The sleef-devel package contains libraries and header files for
developing applications that use sleef.


%if 0%{?inline_enabled}
%package static
Summary:        Inline headers and static library for sleef
Requires:       sleef-devel%{?_isa} = %{version}-%{release}

%description static
The sleef-static package contains libraries and header files for
developing applications that use sleef.
%endif


%package doc
Summary:        Documentation for sleef
BuildArch:      noarch

%description doc
The sleef-doc package contains detailed API documentation for developing
applications that use sleef.


%ifarch %{gnuabi_arches}
%package gnuabi
Summary:        GNUABI version of sleef

%global gnuabi_enabled 1

%description gnuabi
The GNUABI version of the library (libsleefgnuabi.so) is built for x86 and
aarch64 architectures. This library provides an API compatible with libmvec in
glibc, and the API conforms to the x86 vector ABI, AArch64 vector ABI and Power
Vector ABI.


%package gnuabi-devel
Summary:        Development files for GNUABI version of sleef
Requires:       sleef-gnuabi%{?_isa} = %{version}-%{release}

%description gnuabi-devel
The sleef-gnuabi-devel package contains libraries for developing applications
that use the GNUABI version of sleef. Note that this package does not contain
any header files.
%endif


%if %{with dft}
%package dft
Summary:        Discrete Fourier Transform (DFT) library
Requires:       sleef%{?_isa} = %{version}-%{release}

%description dft
SLEEF includes subroutines for discrete Fourier transform(DFT). These
subroutines are fully vectorized, heavily unrolled, and parallelized in such a
way that modern SIMD instructions and multiple cores can be utilized for
efficient computation. It has an API similar to that of FFTW for easy
migration. The subroutines can utilize long vectors up to 2048 bits.


%package dft-devel
Summary:        Development files for sleef-dft
Requires:       sleef-dft%{?_isa} = %{version}-%{release}

%description dft-devel
The sleef-dft-devel package contains libraries and header files for
developing applications that use sleef-dft.
%endif


%if %{with quad}
%package quad
Summary:        Vectorized quad-precision math library

%description quad
An experimental quad-precision library


%package quad-devel
Summary:        Development files for sleef-quad
Requires:       sleef-quad%{?_isa} = %{version}-%{release}

%description quad-devel
The sleef-quad-devel package contains libraries and header files for
developing applications that use sleef-quad.
%endif


%prep
%autosetup -n sleef-%{tag} -p1
# Remove an unwanted hidden file from the docs
find docs/ -type f -name .nojekyll -print -delete


%conf
# -GNinja: This used to be required for parallel builds; it is still faster.
#
# -DENFORCE_TESTER3: The build should fail if we cannot build all tests.
# -DENFORCE_TESTER4: Likewise, except that tester4 requires tlfloat.
#
# -DBUILD_INLINE_HEADERS: Do not build the “inline” headers. This would provide
#   an arch-specific collection of sleefinline_*.h headers in _includedir, as
#   well as a static support library, libsleefinline.a, in _libdir. Both the
#   static library and the headers (which are basically a header-only library,
#   and would thus also be treated as a static library in the Fedora
#   guidelines) should be omitted unless something in Fedora absolutely
#   requires them.
#
# -DSLEEFDFT_ENABLE_STREAM: The author writes, “The recommended value for
#   SLEEFDFT_ENABLE_STREAM depends on the architecture, and it is only
#   recommended to be turned on on x86_64.”
#   https://github.com/shibatch/sleef/discussions/654#discussioncomment-12860550
%cmake \
    -GNinja \
    -DSLEEF_BUILD_DFT:BOOL=%{?with_dft:TRUE}%{?!with_dft:FALSE} \
    -DSLEEF_ENFORCE_DFT:BOOL=%{?with_dft:TRUE}%{?!with_dft:FALSE} \
%ifarch %{x86_64}
    -DSLEEFDFT_ENABLE_STREAM:BOOL=TRUE \
%else
    -DSLEEFDFT_ENABLE_STREAM:BOOL=FALSE \
%endif
    -DSLEEF_BUILD_GNUABI_LIBS:BOOL=%{?gnuabi_enabled:TRUE}%{?!gnuabi_enabled:FALSE} \
    -DSLEEF_BUILD_INLINE_HEADERS:BOOL=%{?inline_enabled:TRUE}%{?!inline_enabled:FALSE} \
    -DSLEEF_BUILD_QUAD:BOOL=%{?with_quad:TRUE}%{?!with_quad:FALSE} \
    -DSLEEF_BUILD_SHARED_LIBS:BOOL=TRUE \
    -DSLEEF_ENFORCE_TESTER3:BOOL=TRUE \
    -DSLEEF_ENFORCE_TESTER4:BOOL=%{?with_tlfloat:TRUE}%{?!with_tlfloat:FALSE} \
    -DSLEEF_ENABLE_TLFLOAT:BOOL=%{?with_tlfloat:TRUE}%{?!with_tlfloat:FALSE}


%build
%cmake_build


%install
%cmake_install


%check
# Logging CPU features is helpful for debugging, especially in COPR builds
# where the builder hardware information is not necessarily logged separately.
echo '==== Build host CPU features ===='
cat /proc/cpuinfo

skips='^($.'

%ifarch %{arm64}
# Some tests are specifically for SVE code. We can only run these tests on
# builder hardware that has the SVE extensions, which are not part of the
# aarch64 baseline.
if ! grep -E '[Ff](lags|eatures).*\bsve\b' /proc/cpuinfo >/dev/null
then
  skips="${skips}|gnuabi_compatibility_SVE(_masked)?|qiutsve"
fi
%endif
%ifarch %{power64}
# Some tests are specifically for VSX3 code. We can only run these tests on
# builder hardware that has the VSX3 extensions (POWER 9 or later), which are
# not part of the ppc64le baseline (POWER 8).
if grep -E -i '\bPOWER8\b' /proc/cpuinfo >/dev/null
then
  skips="${skips}|.*vsx3(nofma)?"
fi
%endif

skips="${skips})$"

%ctest --exclude-regex "${skips}" --extra-verbose


%files
%license LICENSE.txt
%{_libdir}/libsleef.so.%{so_version}{,.*}


%files devel
%{_includedir}/sleef.h
%{_libdir}/libsleef.so
%{_libdir}/pkgconfig/sleef.pc
%{_libdir}/cmake/sleef/


%if 0%{?inline_enabled}
%files static
%{_includedir}/sleefinline_*.h
%{_libdir}/libsleefinline.a
%endif


%files doc
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.adoc
%doc docs/


%ifarch %{gnuabi_arches}
%files gnuabi
%license LICENSE.txt
%{_libdir}/libsleefgnuabi.so.%{so_version}{,.*}


%files gnuabi-devel
%{_libdir}/libsleefgnuabi.so
%endif


%if %{with dft}
%files dft
%{_libdir}/libsleefdft.so.%{so_version}{,.*}


%files dft-devel
%{_includedir}/sleefdft.h
%{_libdir}/libsleefdft.so
%endif


%if %{with quad}
%files quad
%license LICENSE.txt
%{_libdir}/libsleefquad.so.%{so_version}{,.*}


%files quad-devel
%{_includedir}/sleefquad.h
%{_libdir}/libsleefquad.so
%endif


%changelog
%autochangelog
