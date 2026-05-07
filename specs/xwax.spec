Name:           xwax
Version:        1.10
Release:        %autorelease
Summary:        Open source vinyl emulation software for Linux
License:        GPL-3.0-only
URL:            https://www.xwax.org
Source0:        https://xwax.org/releases/%{name}-%{version}.tar.gz

BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  make
BuildRequires:  SDL2_ttf-devel
BuildRequires:  sdl2-compat-devel
Requires: cdparanoia
Requires: sox

%description
xwax is open-source vinyl emulation software for Linux. 
It allows DJs and turntablists to playback digital audio files 
(MP3, Ogg Vorbis, FLAC, AAC and more), controlled using a normal
pair of turntables via timecoded vinyls.

It's designed for both beat mixing and scratch mixing. Needle drops, pitch 
changes, scratching, spinbacks and rewinds are all supported, and feel just
like the audio is pressed onto the vinyl itself.

The focus is on an accurate vinyl feel which is efficient, stable and fast.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags} ALSA=yes JACK=yes PREFIX=%{_prefix} EXECDIR=%{_libexecdir}/%{name}

# Note even though xwax is a GUI application I don't think it deserves a .desktop file because the program
# is entirely controlled through keyboard and it's options are only adjustable on the command line
# Options depend on the hardware that the user has available and can't be known ahead of time.

%install
make ALSA=yes JACK=yes install PREFIX=%{buildroot}/%{_prefix} EXECDIR=%{buildroot}/%{_libexecdir}/%{name} DOCDIR=/tmp

%files
%{_bindir}/xwax
%{_libexecdir}/xwax/
%doc CHANGES COPYING README
%doc %{_mandir}/man1/xwax.1.gz

%changelog
%autochangelog
