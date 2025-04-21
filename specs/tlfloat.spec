# Build and run exhaustive tests for 16-bit and 32-bit arguments? This is far
# too slow to do on every build, and perhaps too slow to ever do in koji, but
# it is still useful to be able to do it on demand.
#
# On relatively fast x86_64 hardware with 16 cores, we find that
# test_exhaustive_bf16 takes less than two minutes, test_exhaustive_bf16_mpfr
# takes about two and a quarter hours, and test_exhaustive32 takes about five
# hours. We have not checked other architectures.
%bcond exhaustive 0

Name:           tlfloat
Version:        1.15.0
%global so_version 1
Release:        %autorelease
Summary:        C++ template library for floating point operations

# The entire source is BSL-1.0, except that CODE_OF_CONDUCT.md (which is not
# included in binary RPMs) is CC-BY-SA-4.0.
License:        BSL-1.0
SourceLicense:  %{license} AND CC-BY-SA-4.0
URL:            https://github.com/shibatch/tlfloat
Source:         %{url}/archive/v%{version}/tlfloat-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
# Our choice vs. makefiles; faster, with no disadvantages
BuildRequires:  ninja-build

# Architectures with libquadmath from gcc.spec, line 69:
# %%{ix86} x86_64 ia64 ppc64le
#
# - We choose not to support ix86
# - Nobody is likely to ever attempt to build this on ia64
# - On ppc64le, compilation fails in src/tester/test_arith.cpp because
#   libquadmath does not define fpclassifyq; the easiest solution is just to do
#   without libquadmath. We just lose a few tests.
%ifarch %{x86_64}
BuildRequires:  libquadmath-devel
%endif
BuildRequires:  mpfr-devel

%description
This library implements C++ classes with which half, single, double, quadruple
and octuple precision IEEE 754 floating point numbers can be operated.

Internally, these classes are implemented as class templates on top of
arbitrary-precision integer class templates so that the templates are expanded
as arbitrary precision floating-point operations by just changing the template
parameters, rather than implementing each floating-point operation for each
precision. The arbitrary-precision integer class templates are also included in
this library.


%package devel
Summary:        Development files for TLFloat
Requires:       tlfloat%{?_isa} = %{version}-%{release}

%description devel
The tlfloat-devel package contains libraries and header files for
developing applications that use TLFloat.


%prep
%autosetup -p1


%conf
# BUILD_UTILS: These utilities (genmathcoef,  mkrpitab) are intended for
#   library maintainers, and are not installed, so we do not build them.
%cmake \
    -GNinja \
%if %{with exhaustive}
    -DBUILD_EXHAUSTIVE_TESTING:BOOL=TRUE \
    -DENABLE_EXHAUSTIVE_TESTING:BOOL=TRUE \
%endif
    -DBUILD_UTILS:BOOL=FALSE


%build
%cmake_build


%install
%cmake_install


%check
# Do not set a timeout at all for exhaustive tests.
%ctest %{?with_exhaustive:--timeout 0}


%files
%license LICENSE.txt
%doc README.adoc
%{_libdir}/libtlfloat.so.%{so_version}{,.*}



%files devel
%{_includedir}/tlfloat/
%{_libdir}/libtlfloat.so
%{_libdir}/pkgconfig/tlfloat.pc


%changelog
%autochangelog
