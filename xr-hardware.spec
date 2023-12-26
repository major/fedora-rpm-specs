Name:           xr-hardware
Version:        1.1.0
Release:        %autorelease
Summary:        Udev rules files for normal user access to XR input devices

License:        BSL-1.0
URL:            https://gitlab.freedesktop.org/monado/utilities/xr-hardware
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

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
%autosetup -p1

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
