%global forgeurl https://github.com/sonic-visualiser/sonic-visualiser

Name:           sonic-visualiser
Version:        5.0.1
Release:        %autorelease
Summary:        A program for viewing and exploring audio data

License:        GPL-2.0-or-later
URL:            https://sonicvisualiser.org/
Source:         %{forgeurl}/releases/download/sv_v%{version}/%{name}-%{version}.tar.gz
# include headers for uint32_t and uint8_t
# https://github.com/piper-audio/piper-vamp-cpp/pull/8
Patch:          sonic-visualiser-gcc15-cstdint.diff

BuildRequires:  meson
BuildRequires:  alsa-lib-devel
BuildRequires:  bzip2-devel
BuildRequires:  capnproto
BuildRequires:  dataquay-devel
BuildRequires:  desktop-file-utils
BuildRequires:  liblo-devel
BuildRequires:  pkgconfig(capnp)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(fishsound)
BuildRequires:  pkgconfig(id3tag)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libopusenc)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(oggz)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(raptor2)
BuildRequires:  pkgconfig(rubberband) >= 3.0.0
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sord-0)
BuildRequires:  qt6-qtbase-devel
# This is likely not really needed; if it is we need to scope it
# to only x86_64 and aarch64
# https://github.com/sonic-visualiser/sonic-visualiser/issues/95
# BuildRequires:  qt6-qtpdf-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-linguist
BuildRequires:  vamp-plugin-sdk-devel >= 2.10

Requires:       hicolor-icon-theme
# The automatic dependency on libvamp-hostsdk.so.3 is satisfied by
# the previous vamp-plugin-sdk-2.9 package, so we need to explicitly
# require v2.10 here to get the correct library build
Requires:       vamp-plugin-sdk%{?_isa} >= 2.10

%description
Sonic Visualiser is an application for viewing and analyzing the
contents of music audio files.

The aim of Sonic Visualiser is to be the first program you reach for
when want to study a musical recording rather than simply listen to
it.

As well as a number of features designed to make exploring audio data
as revealing and fun as possible, Sonic Visualiser also has powerful
annotation capabilities to help you to describe what you find, and the
ability to run automated annotation and analysis plugins in the Vamp
analysis plugin format – as well as applying standard audio effects.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/sonic-visualiser.desktop


%files
%license COPYING
%doc CHANGELOG CITATION README.*
%{_bindir}/piper-convert
%{_bindir}/piper-vamp-simple-server
%{_bindir}/sonic-visualiser
%{_bindir}/vamp-plugin-load-checker
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%changelog
%autochangelog
