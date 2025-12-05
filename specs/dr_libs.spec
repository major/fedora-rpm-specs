%global commit 877b0967ce679148f60d69bb2d9173487717d8de
%global snapdate 20251201

Name:           dr_libs
# While the individual header-only libraries are versioned, the overall
# collection is not, and there are no releases. These libraries follow the
# general practices of stb, so see also:
#   https://github.com/nothings/stb/issues/359
#   https://github.com/nothings/stb/issues/1101
%global snapinfo ^%{snapdate}.%{sub %{commit} 1 7}
Version:        0%{snapinfo}
Release:        %autorelease
Summary:        Single-file audio decoding libraries for C/C++

URL:            https://github.com/mackron/dr_libs
# See LICENSE.
License:        Unlicense OR MIT-0

%global dr_flac_version 0.13.2
%global dr_mp3_version 0.7.2
%global dr_wav_version 0.14.2

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

Requires:       dr_flac-devel = %{dr_flac_version}%{snapinfo}-%{release}
Requires:       dr_flac-static = %{dr_flac_version}%{snapinfo}-%{release}
Requires:       dr_mp3-devel = %{dr_mp3_version}%{snapinfo}-%{release}
Requires:       dr_mp3-static = %{dr_mp3_version}%{snapinfo}-%{release}
Requires:       dr_wav-devel = %{dr_wav_version}%{snapinfo}-%{release}
Requires:       dr_wav-static = %{dr_wav_version}%{snapinfo}-%{release}

%description devel
The dr_libs-devel package contains libraries and header files for developing
applications that use dr_libs.

This is a metapackage that requires the -devel packages for all dr_libs
libraries.


%package -n dr_flac-devel
Summary:        FLAC audio decoder
Version:        %{dr_flac_version}%{snapinfo}

BuildArch:      noarch

Provides:       dr_flac-static = %{dr_flac_version}%{snapinfo}-%{release}

%description -n dr_flac-devel
FLAC audio decoder.


%package -n dr_mp3-devel
Summary:        MP3 audio decoder
Version:        %{dr_mp3_version}%{snapinfo}

BuildArch:      noarch

Provides:       dr_mp3-static = %{dr_mp3_version}%{snapinfo}-%{release}

%description -n dr_mp3-devel
MP3 audio decoder. Based off minimp3 (https://github.com/lieff/minimp3).


%package -n dr_wav-devel
Summary:        WAV audio loader and writer
Version:        %{dr_wav_version}%{snapinfo}

BuildArch:      noarch

Provides:       dr_wav-static = %{dr_wav_version}%{snapinfo}-%{release}

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
%{dr_flac_version} dr_flac.h
%{dr_mp3_version} dr_mp3.h
%{dr_wav_version} dr_wav.h
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
