%global commit d6e1d922fb7f5c2e0052da566a8a30f0e6b8f613
%global snapdate 20251216

Name:           dr_libs
# While the individual header-only libraries are versioned, the overall
# collection is not, and there are no releases. These libraries follow the
# general practices of stb, so see also:
#   https://github.com/nothings/stb/issues/359
#   https://github.com/nothings/stb/issues/1101
%global snapinfo %{snapdate}.%{sub %{commit} 1 7}
Version:        0^%{snapinfo}
Release:        %autorelease
Summary:        Single-file audio decoding libraries for C/C++

URL:            https://github.com/mackron/dr_libs
# See LICENSE.
License:        Unlicense OR MIT-0

%global dr_flac_version 0.13.2^%{snapinfo}
# We package a pre-release of 0.7.3; this is the same as 0.7.2, plus:
#   dr_mp3: Fix an error in drmp3_open_and_read_pcm_frames_s16() and family.
#
#   This fixes an issue where an invalid pointer can be returned when memory
#   allocation fails.
#
#   https://github.com/mackron/dr_libs/commit/d6e1d922fb7f5c2e0052da566a8a30f0e6b8f613
#
# which fixes the issue reported in:
#
#   Fixed the issue of returning a wild pointer when MP3 memory allocation
#   fails during reading.
#
#   https://github.com/mackron/dr_libs/pull/293
#
# TODO: change ~ to ^ once we are no longer packaging a pre-release
%global dr_mp3_version 0.7.3~%{snapinfo}
%global dr_wav_version 0.14.3^%{snapinfo}

Source:        %{url}/archive/%{commit}/dr_libs-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

# For tests:
BuildRequires:  pkgconfig(flac)
BuildRequires:  libsndfile-devel

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%description
%{summary}.


%package devel
Summary:        Development files for dr_libs

BuildArch:      noarch

# Dependent packages should prefer to BuildRequire the -static packages for the
# specific dr_libs libraries they use.
Provides:       dr_libs-static = %{version}-%{release}

Requires:       dr_flac-devel = %{dr_flac_version}-%{release}
Requires:       dr_flac-static = %{dr_flac_version}-%{release}
Requires:       dr_mp3-devel = %{dr_mp3_version}-%{release}
Requires:       dr_mp3-static = %{dr_mp3_version}-%{release}
Requires:       dr_wav-devel = %{dr_wav_version}-%{release}
Requires:       dr_wav-static = %{dr_wav_version}-%{release}

%description devel
The dr_libs-devel package contains libraries and header files for developing
applications that use dr_libs.

This is a metapackage that requires the -devel packages for all dr_libs
libraries.


%package -n dr_flac-devel
Summary:        FLAC audio decoder
Version:        %{dr_flac_version}

BuildArch:      noarch

Provides:       dr_flac-static = %{dr_flac_version}-%{release}

%description -n dr_flac-devel
FLAC audio decoder.


%package -n dr_mp3-devel
Summary:        MP3 audio decoder
Version:        %{dr_mp3_version}

BuildArch:      noarch

Provides:       dr_mp3-static = %{dr_mp3_version}-%{release}

%description -n dr_mp3-devel
MP3 audio decoder. Based off minimp3 (https://github.com/lieff/minimp3).


%package -n dr_wav-devel
Summary:        WAV audio loader and writer
Version:        %{dr_wav_version}

BuildArch:      noarch

Provides:       dr_wav-static = %{dr_wav_version}-%{release}

%description -n dr_wav-devel
WAV audio loader and writer.


%package doc
Summary:        Documentation for dr_libs

BuildArch:      noarch

%description doc
Documentation for dr_libs.


%prep
%autosetup -n dr_libs-%{commit}

# Omit the "playback" tests. We cannot run these anyway, so we would hae to
# skip them, and by not even compiling them, we can avoid a BuildRequires on
# miniaudio.
sed -r -i 's/^([[:blank:]]*)(.*_playback)/\1# \2/' CMakeLists.txt

mkdir -p tests/testvectors/mp3/tests


%conf
%cmake -DDR_LIBS_BUILD_TESTS:BOOL=ON


%build
%cmake_build


%install
# There are no install targets in CMakeLists.txt, so %%cmake_install would do
# nothing. We install manually instead:
install -t '%{buildroot}%{_includedir}' -p -m 0644 -D dr_*.h


%check
skips='^($.'
# Fails with “No output file specified.”
skips="${skips}|wav_encoding"
# These require files in tests/testvectors/mp3/tests/ that are not distributed:
skips="${skips}|mp3_(basic|extract)"
skips="${skips})$"

%ctest --exclude-regex "${skips}"

# As a sanity check, verify that all of the subpackage version numbers appear
# in the corresponding headers.
while read -r version header
do
  grep -E "\\bv$(echo "${version}" | sed -r 's/\./\\./g')\\b" \
      "%{buildroot}%{_includedir}/${header}" >/dev/null
done <<'EOF'
%(printf '%s\n' '%{dr_flac_version}' | sed -r 's/[~^].*//') dr_flac.h
%(printf '%s\n' '%{dr_mp3_version}' | sed -r 's/[~^].*//') dr_mp3.h
%(printf '%s\n' '%{dr_wav_version}' | sed -r 's/[~^].*//') dr_wav.h
EOF


%files devel
# Empty metapackage


%files doc
%license LICENSE
%doc README.md


%files -n dr_flac-devel
%license LICENSE
%{_includedir}/dr_flac.h


%files -n dr_mp3-devel
%license LICENSE
%{_includedir}/dr_mp3.h


%files -n dr_wav-devel
%license LICENSE
%{_includedir}/dr_wav.h


%changelog
%autochangelog
