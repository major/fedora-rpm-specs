Name:       swaybg
Version:    1.2.0
Release:    %{autorelease}
Summary:    Wallpaper tool for Wayland compositors

License:    MIT
URL:        https://github.com/swaywm/swaybg
Source0:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:    https://keys.openpgp.org/vks/v1/by-fingerprint/34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48

Patch:      0001-main.c-fix-build-against-gcc-14-Walloc-size.patch

# Swaybg was part of sway before sway 1.1
Conflicts:  sway < 1.1

BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-scanner)
# Man page compilation
BuildRequires:  scdoc

%description
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/swaybg
%{_mandir}/man1/swaybg.1*

%changelog
%{autochangelog}
