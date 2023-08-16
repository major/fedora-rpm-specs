Name:           wl-mirror
Version:        0.13.2
Release:        %autorelease
Summary:        Simple Wayland output mirror client

License:        GPL-3.0-or-later
URL:            https://github.com/Ferdi265/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# Ferdinand Bachmann <ferdinand.bachmann@yrlf.at> at keys.openpgp.org
Source2:        gpgkey-BC1D9BD570235175.asc

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  wayland-protocols-devel

# wlr-protocols may have different licenses, but it does not affect
# the generated code or the binary file license
Provides:       bundled(wlr-protocols) = 0^20220627g8cdeaac

%description
Simple output mirror client for Wlroots-based compositors.

wl-mirror attempts to provide a solution to sway's lack of output
mirroring by mirroring an output onto a client surface.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
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
