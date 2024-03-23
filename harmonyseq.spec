Name:           harmonyseq
Summary:        MIDI sequencer designed for live performances
Version:        0.17
Release:        %autorelease

# The entire source is GPL-3.0-or-later, except:
#   - org.cielak.harmonyseq.metainfo.xml is CC0-1.0, which is only allowed for
#     content
#
# Additionally, the contents of images/ (also content) are CC0-1.0, but they
# are not included in the binary RPMs.
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://harmonyseq.wordpress.com/
%global forgeurl https://github.com/rafalcieslak/harmonySEQ
Source:         %{forgeurl}/archive/v%{version}/harmonySEQ-%{version}.tar.gz

# https://github.com/rafalcieslak/harmonySEQ/issues/7
Patch:          harmonyseq-0.17-missing-include.patch
# https://github.com/rafalcieslak/harmonySEQ/issues/5
# https://github.com/rafalcieslak/harmonySEQ/issues/6
# https://github.com/rafalcieslak/harmonySEQ/pull/8
Patch:          harmonyseq-0.17-pr-8-metadata-improvements.patch
# Fix incompatible function signatures in lo_method_handler callbacks
# https://github.com/rafalcieslak/harmonySEQ/pull/12
#
# Fixes:
#
# Callbacks of type lo_message_handler have the wrong signature
# https://github.com/rafalcieslak/harmonySEQ/issues/11
Patch:          %{forgeurl}/pull/12.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# The 'UNIX Makefiles' backend would have worked fine too; we choose ninja.
BuildRequires:  ninja-build

#BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  alsa-lib-devel
BuildRequires:  boost-devel

BuildRequires:  desktop-file-utils
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  hardlink

# For %%{_datadir}/share/mime/packages
Requires:       shared-mime-info

Provides:       harmonyseq-doc = %{version}-%{release}
Conflicts:      harmonyseq-doc = 0.17-1
Obsoletes:      harmonyseq-doc < 0.17-1

%global app_id org.cielak.harmonyseq

%description
A MIDI software sequencer designed for live performances and jams.

harmonySEQ operates a number of synchronized sequencers, each with its own
pattern, repeating looped melodies of different length, duration and MIDI
channel.

Main features include:

  • support for complex polyrhythms
  • multi-pattern configuration for each sequencer
  • customizable action triggers - exceptionally useful for live performances
  • chord management system which allows to easily organize melodies that sound
    great together
  • support for sequencing MIDI control messages
  • an easy-to-use yet powerful interface, with a rich piano-roll pattern
    editor

As for now harmonySEQ works on Linux only. It uses ALSA (asound) library, and
GTKmm for graphical interface.

No official user documentation exists at the moment, but you can refer to UI
tooltips - nearly everything has a detailed explanation.

More information can be found on the project’s (dated) website:
https://harmonyseq.wordpress.com


%prep
%autosetup -n harmonySEQ-%{version} -p1


%build
# We need the preprocessor macro RELEASE set so that src/main.cpp looks for
# resoures in the installation path (DATA_PATH). Normally this is set with
# -DCMAKE_BUILD_TYPE=Release, but this also asks to strip debugging symbols,
# which we do not want. Setting -DCMAKE_BUILD_TYPE=RelWithDebInfo does not set
# the preprocessor macro. Instead, we set it manually:
CFLAGS="${CFLAGS} -DRELEASE"
CXXFLAGS="${CXXFLAGS} -DRELEASE"

%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -GNinja
%cmake_build


%install
%cmake_install

# Not a standard size for GNOME icons, so gnome-icon-theme does not have the
# directories:
rm -rvf '%{buildroot}%{_datadir}/icons/gnome/192x192'

# There are some duplicate PNG and SVG icons that can be hardlinked to save a
# little space.
hardlink -c -v '%{buildroot}%{_datadir}/harmonySEQ'


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_id}.desktop
# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
# Matches what gnome-software and others use:
appstreamcli validate --no-net --explain \
    %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml


%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%doc examples/

%{_bindir}/harmonySEQ
%{_mandir}/man1/harmonySEQ.1*

%{_datadir}/harmonySEQ/

%{_datadir}/applications/%{app_id}.desktop
%{_metainfodir}/%{app_id}.metainfo.xml

%{_datadir}/mime/packages/harmonyseq-mime.xml


%changelog
%autochangelog
