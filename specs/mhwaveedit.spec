Summary:    WAV Editing Package
Name:       mhwaveedit
Version:    1.4.24
Release:    2%{?dist}
Url:        https://github.com/magnush/mhwaveedit
License:    GPL-2.0-or-later
%global     forgeurl https://github.com/magnush/mhwaveedit

%forgemeta
Source0:    %{forgesource}
Source1:    mhwaveedit.metainfo.xml

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ladspa-devel
BuildRequires:  lame-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(samplerate)

Requires:       hicolor-icon-theme
# For default mixer (alsamixer)
Requires:       alsa-utils

%description
mhWaveEdit is a graphical program for editing sound files.
It is completely free (GPL) and written by Magnus Hjorth.
It is intended to be user-friendly and robust.
OGG and LAME support are available if installed.

%prep
%autosetup

%build
%global _pkg_extra_cflags -std=gnu17

%configure --prefix=/usr \
        --without-arts \
        --without-esound \
        --without-oss \
        --without-sun \
        --with-double-samples

%make_build

%install
%make_install
%find_lang %{name}
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Wed Apr 29 2026 peterbb <peter@pblackman.plus.com> - 1.4.24-1
- Reintroduce to Fedora
