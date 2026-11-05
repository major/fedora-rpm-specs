Name:           plasma-pipewire-settings
Version:        1.2.1
Release:        %autorelease
Summary:        Simple Plasma 6 widget to change Pipewire quantum and sample rate

License:        GPL-3.0-or-later
URL:            https://github.com/magillos/Pipewire-Settings-Widget-for-Plasma-6
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       plasma-desktop

%description
An easy-to-use widget to change Pipewire's quantum and sample rate from
the KDE Plasma 6 Desktop Environment.


%prep
%autosetup -C

%build
# No build required

%check
# Upstream does not provide an automated test suite

%install
mkdir -p %{buildroot}%{_datadir}/plasma/plasmoids/com.github.magillos.pipewiresettings
cp -r package/* %{buildroot}%{_datadir}/plasma/plasmoids/com.github.magillos.pipewiresettings/

%files
%license LICENSE
%doc README.md
%{_datadir}/plasma/plasmoids/com.github.magillos.pipewiresettings/

%changelog
%autochangelog
