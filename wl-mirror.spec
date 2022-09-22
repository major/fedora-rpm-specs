Name:           wl-mirror
Version:        0.12.1
Release:        %autorelease
Summary:        Simple Wayland output mirror client

License:        GPLv3
URL:            https://github.com/Ferdi265/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libglvnd-devel
BuildRequires:  scdoc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

# wlr-protocols may have different licenses, but it does not affect
# the generated code or the binary file license
Provides:       bundled(wlr-protocols) = 0^20211229g0c7437e

%description
Simple output mirror client for Wlroots-based compositors.

wl-mirror attempts to provide a solution to sway's lack of output
mirroring by mirroring an output onto a client surface.

%prep
%autosetup
# remove bundled wayland-protocols, just in case
rm -rf proto/wayland-protocols


%build
%cmake \
    -DFORCE_SYSTEM_WL_PROTOCOLS:BOOL=ON \
    -DINSTALL_DOCUMENTATION:BOOL=ON
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
