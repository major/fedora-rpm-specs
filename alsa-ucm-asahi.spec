Name:           alsa-ucm-asahi
Version:        2
Release:        %autorelease
Summary:        ALSA Use Case Manager configuration (and topologies) for Apple silicon devices
License:        BSD-3-Clause

URL:            https://github.com/AsahiLinux/alsa-ucm-conf-asahi
Source:         %{url}/archive/v%{version}/alsa-ucm-conf-asahi-%{version}.tar.gz

BuildArch:      noarch

Requires:       alsa-ucm >= 1.2.7.2

%description
The ALSA Use Case Manager configuration (and topologies) for Apple silicon devices.

%prep
%autosetup -n alsa-ucm-conf-asahi-%{version}

%install
install -dm 755 %{buildroot}%{_datadir}/alsa/ucm2/conf.d/
cp -a ucm2/conf.d/macaudio/ %{buildroot}%{_datadir}/alsa/ucm2/conf.d/

%files
%license LICENSE.asahi
%doc README.asahi
%{_datadir}/alsa/ucm2/conf.d/macaudio/

%changelog
%autochangelog
