%bcond_without tests

%global forgeurl https://github.com/monocasual/giada

%global rtaudio_forgeurl https://github.com/monocasual/rtaudio
# Version for the bundled rtaudio fork
%global rtaudio_version 6.0.0~beta1
# Commit hash for the bundled rtaudio fork, included as a git submodule:
%global rtaudio_commit 885b71dfb6e3b66852ea987a6b10c2d305c505fd
%global rtaudio_shortcommit %(echo %{rtaudio_commit} | cut -b -8)

%global mas_forgeurl https://github.com/monocasual/mcl-atomic-swapper
# Commit hash for the bundled mcl-atomic-swapper, included as a git submodule:
%global mas_commit acc48c7ab416575f2fde1afd19faa0be378bb595
%global mas_shortcommit %(echo %{mas_commit} | cut -b -8)

%global mab_forgeurl https://github.com/monocasual/mcl-audio-buffer
# Commit hash for the bundled mcl-audio-buffer, included as a git submodule:
%global mab_commit d641e3e40219ea931e2a9945a1ef0aa2f54f4d2c
%global mab_shortcommit %(echo %{mab_commit} | cut -b -8)

Name:           giada
Version:        0.22.0
Release:        %autorelease
Summary:        Your hardcore loop machine

%global app_id com.giadamusic.Giada

# LICENSING NOTE:
#
# The upstream source, when downloaded from the main website (i.e.,
# %%{url}/data/giada-%%{version}-src.tar.gz), contains excerpts from the
# Steinberg VST 3 SDK, which has additional restrictions on top of the GPLv3
# that make it unsuitable for distribution in Fedora. See
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/FMFIZU22AP36J3DOUVCXUPHQ3MNDN5P6/.
#
# These problematic components may be filtered from the upstream source archive
# using a script to produce a distributable source archive. At one point, this
# package followed that approach. Now we use the GitHub release tarball; since
# the problematic components (vst3sdk and juce) are git submodules, they are
# not included in the automatically-generated release tarball.
#
# Note that this means Giada will *not* be built with VST3 support in Fedora.
# (The situation for VST2 is even worse, as it is available only under a
# proprietary license.)
#
# Additional git submodules are handled as follows:
#   • json: unbundled downstream
#   • geompp: unbundled downstream
#   • rtaudio: bundled, provided as an additional source, since it is a
#     giada-specific fork
#   • mcl-atomic-swapper: bundled, provided as an additional source; this is
#     managed under the same GitHub organization as giada, and does not yet
#     have its own releases.
#   • mcl-audio-buffer: bundled, provided as an additional source; this is
#     managed under the same GitHub organization as giada, and does not yet
#     have its own releases. More importantly, it is not header-only but does
#     not yet have a build system configuration, so we really cannot package it
#     separately.

# The entire source is GPL-3.0-or-later, except:
#   - src/deps/rtaudio (i.e., the contents of Source1) is MIT, except:
#     * src/deps/rtaudio/include/soundcard.h is BSD-2-Clause
License:        GPL-3.0-or-later AND MIT AND BSD-2-Clause
URL:            https://www.giadamusic.com
Source0:        %{forgeurl}/archive/v%{version}/giada-%{version}.tar.gz
Source1:        %{rtaudio_forgeurl}/archive/%{rtaudio_commit}/rtaudio-%{rtaudio_shortcommit}.tar.gz
Source2:        %{mas_forgeurl}/archive/%{mas_commit}/mcl-atomic-swapper-%{mas_shortcommit}.tar.gz
Source3:        %{mab_forgeurl}/archive/%{mab_commit}/mcl-audio-buffer-%{mab_shortcommit}.tar.gz

# This is a C++ logging wrapper that passes its format string parameter through
# to std::fprintf, which inherently means the format string cannot be a
# literal. We use GCC pragmas to suppress the warning in just this one spot.
# See https://github.com/monocasual/giada/issues/447, where this is discussed,
# and the patch is offered, upstream.
Patch:          giada-0.17.2-suppress-format-security.patch
# Remove duplicate Comment in desktop file
# https://github.com/monocasual/giada/pull/589
Patch:          %{forgeurl}/pull/589.patch
# Support external nlohmann_json
# https://github.com/monocasual/giada/pull/590
Patch:          %{forgeurl}/pull/590.patch
# Downstream patch to use rtmidi 4.0, until the package is updated to 5.0,
# RHBZ#2023879. We just patch out the case for RtMidi::Api::WEB_MIDI_API,
# which is an rtmidi 5.0 feature, from a logging function.
#
# Once we can drop this patch, we should amend the BR to:
#   BuildRequires:  pkgconfig(rtmidi) >= 5.0.0
Patch:          0001-Patch-for-RtMidi-4.patch

BuildRequires:  desktop-file-utils
# For AppData file validation
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  gcc-c++
BuildRequires:  cmake
# It is our choice whether to use the make backend or the ninja backend.
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(rtmidi)

BuildRequires:  cmake(FLTK)
# CMakeLists.txt has:
#   set(FLTK_SKIP_FLUID TRUE)  # Don't search for FLTK's fluid
# but this doesn’t seem to be working. See also:
#   https://cmake.org/cmake/help/latest/module/FindFLTK.html
# The easiest workaround is just to ensure it is present:
BuildRequires:  fltk-fluid
# The static version of fltk appears to be required as well. However, this
# seems to be only a CMake config quirk, as we have verified (with ldd) that
# the giada executable links the libfltk.so[…] shared library.
BuildRequires:  fltk-static

BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  cmake(fmt)

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(freetype2)

BuildRequires:  cmake(nlohmann_json)
BuildRequires:  json-static
BuildRequires:  geompp-devel
BuildRequires:  geompp-static

%if %{with tests}
BuildRequires:  cmake(Catch2)
# Support graphical tests in non-graphical environment
BuildRequires:  xorg-x11-server-Xvfb
%endif

# For /usr/share/icons/hicolor/*/apps
Requires:  hicolor-icon-theme

# ============================================================================
# RtAudio (https://github.com/thestk/rtaudio)
#
# This version is slightly forked, so it is not possible to build with the
# system copy of RtAudio. See
# https://giadamusic.com/forum/viewtopic.php?f=2&t=177, where upstream
# discusses the decision to maintain a forked copy of RtAudio in the Giada
# source tree.
#
# The version comes from “#define RTAUDIO_VERSION” in
# src/deps/rtaudio/RtAudio.h and/or AC_INIT in configure.ac.
Provides:  bundled(rtaudio) = %{rtaudio_version}
# ============================================================================

# ============================================================================
# mcl-audio-buffer (https://github.com/monocasual/mcl-audio-buffer/)
#
# Currently, this is effectively still a part of giada. It has never had a
# version or a release, and it has no build system of its own. Since it is not
# header-only (compare to geompp), this makes it impractical to package it as a
# stand-alone library. Therefore we must bundle it as a part of giada until and
# unless it grows into a full-fledged project of its own.
Provides:  bundled(mcl-audio-buffer)
# ============================================================================

%description
Giada is an open source, minimalistic and hardcore music production tool.
Designed for DJs, live performers and electronic musicians.


%prep
%autosetup -p1

%setup -q -T -D -b 1 -n giada-%{version}
rm -rvf src/deps/rtaudio
cp -rp ../rtaudio-%{rtaudio_commit} src/deps/rtaudio
cp -p src/deps/rtaudio/LICENSE LICENSE-rtaudio

%setup -q -T -D -b 2 -n giada-%{version}
rm -rvf src/deps/mcl-atomic-swapper
cp -rp ../mcl-atomic-swapper-%{mas_commit} src/deps/mcl-atomic-swapper
cp -p src/deps/mcl-atomic-swapper/LICENSE LICENSE-mcl-atomic-swapper

%setup -q -T -D -b 3 -n giada-%{version}
rm -rvf src/deps/mcl-audio-buffer
cp -rp ../mcl-audio-buffer-%{mab_commit} src/deps/mcl-audio-buffer
cp -p src/deps/mcl-audio-buffer/LICENSE LICENSE-mcl-audio-buffer

# This is a last safeguard against something with an inappropriate license
# slipping into the source tarball. It is no substitute for manual auditing.
echo 'Checking for inappropriate source files:'
echo '> Possible Steinberg proprietary license?'
if grep -Frl 'This Software Development Kit may not be' .
then
  echo 'Found some concerning files!'
  exit 1
else
  echo '> No concerning files were found.'
fi
echo '> Possible Steinberg VST 3 SDK (GPLv3 with conditions)?'
if grep -Erli 'Project[[:blank:]]*:[[:blank:]]*VST SDK' .
then
  echo 'Found some concerning files!'
  exit 1
else
  echo '> No concerning files were found.'
fi

# Link fltk as a shared library:
sed -r -i 's/\b(fltk.*)\b/\1_SHARED/g' CMakeLists.txt

# Unbundle geompp; we can just use a symlink since it is a header-only library.
rm -rvf 'src/deps/geompp'
mkdir 'src/deps/geompp'
ln -s '%{_includedir}/geompp' 'src/deps/geompp/src'


%build
# Make sure any build flags for unbundled libraries are set. For
# json/nlohmann_json, we expect that none are needed in practice.
%set_build_flags
export CFLAGS="${CFLAGS} $(pkgconf --cflags nlohmann_json)"
export CXXFLAGS="${CXXFLAGS} $(pkgconf --cflags nlohmann_json)"
export LDFLAGS="${CXXFLAGS} $(pkgconf --libs nlohmann_json)"

# VST 2 SDK is only available under a proprietary license, and VST 3 SDK is
# dual-licensed with a proprietary license and GPLv3, but additional
# trademark-related conditions are imposed that are not acceptable in Fedora.
# See the notes near the beginning of this spec file. Therefore the VST 3 SDK
# and JUCE sources have been excluded, and all VST support must be disabled at
# build time.
%cmake \
    -DWITH_VST2:BOOL=OFF -DWITH_VST3:BOOL=OFF \
    -DWITH_TESTS:BOOL=%{?with_tests:ON}%{?!with_tests:OFF} \
    -DWITH_SYSTEM_JSON:BOOL=ON \
    -GNinja
%cmake_build


%install 
%cmake_install


%check
# Verify the bundled rtaudio version in the spec file matches the header in the
# source tree.
[ '"%(echo '%{rtaudio_version}' | tr -d '~')"' = "$(
  awk '$1 == "#define" && $2 == "RTAUDIO_VERSION" { print $3; exit }' \
      src/deps/rtaudio/RtAudio.h)" ]
# This comment fixes broken vim syntax highlighting --> "

# Validate the installed desktop file as required by
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_desktop_file_install_usage.
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop

# Validate the installed AppData file. Fedora guidelines require validate-relax
# to pass (but not validate-strict), and do require validation at build time.
#
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
# Matches what gnome-software and others use:
appstreamcli validate --nonet \
    %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml

%if %{with tests}
xvfb-run -a %{buildroot}%{_bindir}/giada --run-tests
%endif


%files
%license COPYING LICENSE-rtaudio LICENSE-mcl-audio-buffer
%doc ChangeLog README.md

%{_bindir}/giada

%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_id}.svg


%changelog
%autochangelog
