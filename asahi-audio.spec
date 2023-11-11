Name:           asahi-audio
Version:        0.4
Release:        %autorelease
Summary:        PipeWire DSP profiles for Apple Silicon machines
License:        MIT
URL:            https://github.com/AsahiLinux/asahi-audio
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  make
Requires:       pipewire >= 0.3.84-3
Requires:       wireplumber >= 0.4.15
Requires:       pipewire-module-filter-chain-lv2
Requires:       lsp-plugins-lv2
Requires:       lv2-bankstown
Recommends:     speakersafetyd

%description
PipeWire and WirePlumber DSP profiles and configurations to
drive the speaker arrays in Apple Silicon laptops and desktops.

%prep
%autosetup

%build
%make_build

%install
%make_install PREFIX=%{_prefix} DATA_DIR=%{_datadir}

%files
%license LICENSE
%doc README.md
%{_datadir}/asahi-audio/
%{_datadir}/wireplumber/policy.lua.d/99-asahi-policy.lua
%{_datadir}/wireplumber/main.lua.d/99-asahi.lua
%{_datadir}/pipewire/pipewire.conf.d/99-asahi.conf
%{_datadir}/pipewire/pipewire-pulse.conf.d/99-asahi.conf

%changelog
%autochangelog
