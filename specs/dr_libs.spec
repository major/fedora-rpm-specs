%global commit 35b5c392cc15456736c440a68dbe073178bbffe0
%global snapdate 20261030

%bcond ctest 1

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
# See LICENSE. Note also that external/fs/ is a copy of
# https://github.com/mackron/fs, with the same (Unlicense OR MIT-0) license
# terms. We don’t treat it as a bundled dependency because it is used only for
# testing and does not contribute to the contents of the binary RPMs.
License:        Unlicense OR MIT-0

%global dr_flac_version 0.13.4^%{snapinfo}
%global dr_mp3_version 0.7.4^%{snapinfo}

Source:        %{url}/archive/%{commit}/dr_libs-%{commit}.tar.gz

BuildSystem:    cmake
BuildOption(conf): -DDR_LIBS_BUILD_TESTS:BOOL=%{with ctest}
BuildOption(conf): -DDR_LIBS_NO_WAV:BOOL=ON

BuildRequires:  gcc-c++

%if %{with ctest}
BuildRequires:  cmake(ogg)
BuildRequires:  cmake(flac)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(libmpg123)
%endif

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%description
%{summary}.


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


%install
# There are no install targets in CMakeLists.txt, so %%cmake_install would do
# nothing. We install manually instead:
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_includedir}' dr_flac.h dr_mp3.h


%check -p
# As a sanity check, verify that all of the subpackage version numbers appear
# in the corresponding headers.
while read -r version header
do
  grep --extended-regexp \
      "\\bv$(echo "${version}" | sed --regexp-extended 's/\./\\./g')\\b" \
      "%{buildroot}%{_includedir}/${header}" >/dev/null
done <<'EOF'
%(printf '%s\n' '%{dr_flac_version}' | sed --regexp-extended 's/[~^].*//') dr_flac.h
%(printf '%s\n' '%{dr_mp3_version}' | sed --regexp-extended 's/[~^].*//') dr_mp3.h
EOF


%files -n dr_flac-devel
%license LICENSE
%doc README.md
%{_includedir}/dr_flac.h


%files -n dr_mp3-devel
%license LICENSE
%doc README.md
%{_includedir}/dr_mp3.h


%changelog
%autochangelog
