%global commit 5c769634b5b8d9fb643f198f3f6ea49abdf305fd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20250724
%bcond bundled_dr_libs 1

Name:           SDL3_sound
Version:        3.0.0~%{date}git%{shortcommit}
Release:        %autorelease
Summary:        An abstract soundfile decoder library
# src/dr_{flac,mp3}.h: Unlicense or MIT-0
# src/stb_vorbis.h: MIT or Unlicense
# src/libmodplug: Public-Domain
# src/timidity: LGPL-2.1-or-later or Artistic-1.0-Perl (See https://gitlab.com/fedora/legal/fedora-license-data/-/issues/589)
License:        Zlib AND LGPL-2.1-or-later AND (Unlicense OR MIT-0) AND (MIT OR Unlicense) AND LicenseRef-Fedora-Public-Domain
URL:            https://www.icculus.org/SDL_sound
Source0:        https://github.com/icculus/SDL_sound/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-unbundle-dr_libs.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  SDL3-devel
# https://github.com/icculus/SDL_sound/issues/42
Provides:       bundled(libmodplug) = 0.8.9.1
%if %{with bundled_dr_libs}
Provides:       bundled(dr_flac) = 0.13.0
Provides:       bundled(dr_mp3) = 0.7.0
%else
# Header-only libraries (thus the -static)
BuildRequires:  dr_flac-static >= 0.13.0
BuildRequires:  dr_mp3-static >= 0.7.0
%endif
# This has been forked; see "#ifdef __SDL_SOUND_INTERNAL__"
Provides:       bundled(stb_vorbis) = 1.22
# SDL_mixer fork, stripped further, see https://github.com/icculus/SDL_sound/tree/main/src/timidity/CHANGES
Provides:       bundled(timidity) = 0.2i

%description
SDL_sound is a library that handles the decoding of several popular sound
file formats, such as .WAV and .OGG. It is meant to make the programmer's
sound playback tasks simpler. The programmer gives SDL_sound a filename,
or feeds it data directly from one of many sources, and then reads the
decoded waveform data back at her leisure. If resource constraints are a
concern, SDL_sound can process sound data in programmer-specified blocks.
Alternately, SDL_sound can decode a whole sound file and hand back a
single pointer to the whole waveform. SDL_sound can also handle sample
rate, audio format, and channel conversion on-the-fly and
behind-the-scenes, if the programmer desires.

%package        devel
Summary:        %{summary}
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconfig
Requires:       SDL3-devel
# manpages conflict
Conflicts:      SDL_sound-devel
Conflicts:      SDL2_sound-devel

%description    devel
This package contains the headers and libraries for SDL_sound development.

%prep
%setup -q -n SDL_sound-%{commit}
%if %{without bundled_dr_libs}
%patch -P0 -p1 -b .orig
# Unbundle dr_flac and dr_mp3, from dr_libs.
rm src/dr_flac.h src/dr_mp3.h
%endif

%build
%cmake \
    -DSDLSOUND_BUILD_STATIC:BOOL=OFF \
    -DSDLSOUND_DECODER_MIDI:BOOL=ON \

%cmake_build
doxygen docs/Doxyfile

%install
%cmake_install
# Add namespaces to man pages (livna bug #1181)
cp -a docs/man/man3 man3
pushd man3
mv actual.3 Sound_Sample::actual.3
mv author.3 Sound_DecoderInfo::author.3
mv buffer.3 Sound_Sample::buffer.3
mv buffer_size.3 Sound_Sameple::buffer_size.3
mv channels.3 Sound_AudioInfo::channels.3
mv decoder.3 Sound_Sample::decoder.3
mv description.3 Sound_DecoderInfo::description.3
mv desired.3 Sound_Sample::desired.3
mv extensions.3 Sound_DecoderInfo::extensions.3
mv flags.3 Sound_Sample::flags.3
mv format.3 Sound_AudioInfo::format.3
mv major.3 Sound_Version::major.3
mv minor.3 Sound_Version::minor.3
mv opaque.3 Sound_Sample::opaque.3
mv patch.3 Sound_Version::patch.3
mv rate.3 Sound_AudioInfo::rate.3
mv url.3 Sound_DecoderInfo::url.3
popd

mkdir -p %{buildroot}/%{_mandir}
mv man3 %{buildroot}/%{_mandir}

%files
%license LICENSE.txt
%doc docs/CREDITS.txt README.md
%{_bindir}/playsound
%{_libdir}/libSDL3_sound.so.3{,.*}

%files devel
%doc docs/html
%{_libdir}/libSDL3_sound.so
%{_includedir}/SDL3_sound/SDL_sound.h
%{_mandir}/man3/*
%{_libdir}/cmake/SDL3_sound
%{_libdir}/pkgconfig/sdl3-sound.pc

%changelog
%autochangelog
