%global forgeurl  https://gitlab.freedesktop.org/monado/utilities/xr-hardware
%global commit    56084b46e80935a3c2e2ab7b7703a2e3f75070ce
%global date      20241211
%forgemeta

Name:           xr-hardware
Version:        1.1.1
Release:        %autorelease
Summary:        Udev rules files for normal user access to XR input devices

License:        BSL-1.0
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(flake8)
BuildRequires:  systemd-rpm-macros

Requires:       systemd-udev

BuildArch:      noarch

%description
This package contains a udev rules file to permit access to virtual reality
(VR) and augmented reality (AR), collectively "XR", interaction devices as a
normal user.

%prep
%forgeautosetup -p1

%build
%make_build

%install
%make_install RULES_DIR="%{_udevrulesdir}"

%check
make test

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_udevrulesdir}/70-xrhardware.rules

%changelog
%autochangelog
