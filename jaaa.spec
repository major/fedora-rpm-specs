Summary:       JACK and ALSA Audio Analyzer
Name:          jaaa
Version:       0.9.2
Release:       %autorelease
License:       GPL-2.0-or-later
URL:           https://kokkinizita.linuxaudio.org/
Source0:       https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# desktop file submitted upstream
Source1:       %{name}.desktop
Source2:       %{name}.png

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: clthreads-devel >= 2.4.0
BuildRequires: clxclient-devel >= 3.9.0
BuildRequires: fftw-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: zita-alsa-pcmi-devel >= 0.2.0
BuildRequires: make

%description
%{name} (JACK and ALSA Audio Analyzer, is an audio signal generator and
spectrum analyzer designed to make accurate measurements.

%prep
%setup -q
cd source
sed -i -e "s|-march=native|%{optflags}|" Makefile

%build
cd source
make "PREFIX=%{_prefix}" %{?_smp_mflags}

%install
cd source
make "DESTDIR=%{buildroot}" "PREFIX=%{_prefix}" install

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
