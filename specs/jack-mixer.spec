Name:           jack-mixer
Version:        14
Release:        %autorelease
Summary:        JACK Audio Mixer

# nsmclient.py is expat, everything else is GPLv2
# Automatically converted from old format: GPLv2 and MIT - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-MIT

URL:            https://rdio.space/jackmixer/
Source0:        https://github.com/%{name}/jack_mixer/archive/release-%{version}/%{name}-%{version}.tar.gz

# Build fails on these archs, upstream doesn't care.
ExcludeArch:    armv7hl
ExcludeArch:    i686

BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  python3-gobject-devel
BuildRequires:  python3dist(pycairo)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  glib2-devel
BuildRequires:  desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

%description
jack_mixer is an audio mixer for JACK with a look similar to its hardware
counterparts. Many features are available, here is a short list:

 - Mix any number of input channels (mono or stereo).
 - Control balance and faders with MIDI commands.
 - Handle session management with LASH.
 - Create as many outputs as necessary.
 - Quickly monitor inputs (PFL) and outputs.

%prep
%setup -q -n jack_mixer-release-%{version}


%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build


%install
%make_install
rm %{buildroot}%{python3_sitelib}/jack_mixer_c.la
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{python3_sitelib}/* %{buildroot}%{python3_sitearch}
desktop-file-validate %{buildroot}%{_datadir}/applications/jack_mixer.desktop
%py3_shebang_fix %{buildroot}%{_bindir}/jack_mixer.py

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/jack_mix_box
%{_bindir}/jack_mixer
%{_bindir}/jack_mixer.py
%{python3_sitearch}/*
%{_datadir}/applications/jack_mixer.desktop
%{_datadir}/icons/hicolor/*/apps/jack_mixer.*
%{_datadir}/jack_mixer/


%changelog
%autochangelog
