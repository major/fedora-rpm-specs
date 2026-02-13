%global forgeurl https://github.com/epsilonrt/mbpoll

Name:     mbpoll
Version:  1.5.4
Release:  %autorelease
Summary:  Command line utility to communicate with ModBus slave (RTU or TCP)
%forgemeta

License:  GPL-3.0-or-later
URL:      %{forgeurl}
Source0:   %{forgesource}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(libmodbus)

%description
mbpoll is a command-line utility used to communicate with ModBus slave devices
over RTU or TCP. It supports reading discrete inputs, binary outputs (coils),
input registers, and holding registers, with values expressed in decimal,
hexadecimal, or single‑precision floating‑point formats. The tool is compatible
with libmodbus and provides functionality similar to the original modpoll
program while being fully independent and open source.

%prep
%autosetup

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md AUTHORS
%{_bindir}/mbpoll
%{_mandir}/man1/mbpoll.1*

%changelog
%autochangelog
