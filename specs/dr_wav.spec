%bcond ctest 1

Name:           dr_wav
Version:        0.14.6
Epoch:          1
Release:        %autorelease
Summary:        WAV audio loader and writer

URL:            https://github.com/mackron/dr_libs
# See LICENSE. Note also that external/fs/ is a copy of
# https://github.com/mackron/fs, with the same (Unlicense OR MIT-0) license
# terms. We don’t treat it as a bundled dependency because it is used only for
# testing and does not contribute to the contents of the binary RPMs.
License:        Unlicense OR MIT-0
Source:         %{url}/archive/wav-%{version}/dr_libs-wav-%{version}.tar.gz

# dr_wav: Fix an endian error with s24 conversion.
# https://github.com/mackron/dr_libs/commit/3a3e120a7d9d802b8e7d91f3a9ab83a628cb70d4
Patch:          %{url}/commit/3a3e120a7d9d802b8e7d91f3a9ab83a628cb70d4.patch
# dr_wav: Fix an endian error with Wave64 containers.
# https://github.com/mackron/dr_libs/commit/0901cdc54e719e2175827cb60b78fe725e581fe2
Patch:          %{url}/commit/0901cdc54e719e2175827cb60b78fe725e581fe2.patch
# Fixes:
#
# dr_wav: Discrepancies with libsndfile with certain 24 or 32 bit files on
# big-endian hosts
# https://github.com/mackron/dr_libs/issues/362

BuildSystem:    cmake
BuildOption(conf): -DDR_LIBS_BUILD_TESTS:BOOL=%{with ctest}
BuildOption(conf): -DDR_LIBS_NO_FLAC:BOOL=ON
BuildOption(conf): -DDR_LIBS_NO_MP3:BOOL=ON

BuildRequires:  gcc-c++

%if %{with ctest}
# The build system needs to find all test dependencies, even those that might
# not be used for testing this particular library.
BuildRequires:  cmake(ogg)
BuildRequires:  cmake(flac)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(libmpg123)
# For generating some sample wav files
BuildRequires:  sox
%endif

# Header-only library
%global debug_package %{nil}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n dr_wav-devel
Summary:        %{summary}

BuildArch:      noarch

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       dr_wav-static = %{epoch}:%{version}-%{release}

%description -n dr_wav-devel %{common_description}


%install
# There are no install targets in CMakeLists.txt, so %%cmake_install would do
# nothing. We install manually instead:
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_includedir}' dr_wav.h


%check
%if %{with ctest}
# Don’t bother with %%ctest; it would not run anything.

# Generate a few sample wav files. These were suggested by Nikita Sizikov in
# https://bugzilla.redhat.com/show_bug.cgi?id=2571927#c1. Put them in
# “database” layout, in the same default location where the contents of
# https://github.com/mackron/audiovectors would normally go. We can’t use that
# repository in its entirety because it is unpleasantly large and not all of
# the files are under clear and acceptable licenses. If we were feeling very
# thorough, we could possibly use tools/generate.sh from that repository (under
# a public-domain dedication) with ffmpeg to generate a few more test files,
# but this seems unnecessary.
gen() { 
  sox --null --rate 44100 --channels 2 "$@" synth 1 sine 440
}
mkdir --parents external/audiovectors/vectors/wav
pushd external/audiovectors/vectors/wav
gen --bits 16 s16.wav
gen --bits 8 --encoding unsigned-integer u8.wav
gen --bits 24 s24.wav
gen --bits 32 s32.wav
gen --bits 32 --encoding floating-point f32.wav
gen --bits 64 --encoding floating-point f64.wav
gen --encoding u-law ulaw.wav
gen --encoding a-law alaw.wav
gen --encoding ima-adpcm ima.wav
gen --encoding ms-adpcm msadpcm.wav
gen --bits 16 s16.w64
gen --bits 16 s16.aiff
popd

%{_vpath_builddir}/dr_libs_test
%endif


%files -n dr_wav-devel
%license LICENSE
%doc README.md
%{_includedir}/dr_wav.h


%changelog
%autochangelog
