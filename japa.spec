Summary:       Jack and ALSA Perceptual Audio Analyzer
Name:          japa
Version:       0.9.4
Release:       %autorelease
License:       GPL-2.0-or-later
URL:           https://kokkinizita.linuxaudio.org/
Source0:       https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# desktop file submitted upstream
Source1:       %{name}.desktop
Source2:       %{name}.png

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: fftw-devel
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: clthreads-devel
BuildRequires: clxclient-devel >= 3.9.0
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: make

%description
%{name} (JACK and ALSA Perceptual Analyser), is a 'perceptual' or
'psychoacoustic' audio spectrum analyser.

In contrast to JAAA, this is more an acoustical or musical tool than a
purely technical one. Possible uses include spectrum monitoring while
mixing or mastering, evaluation of ambient noise, and (using pink
noise), equalisation of PA systems.

%prep
%setup -q
sed -i -e "s|-march=native|%{optflags}|" source/Makefile

%build
cd source
make LDFLAGS="$RPM_LD_FLAGS" %{?_smp_mflags}

%install
cd source
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
  %{SOURCE1}
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
