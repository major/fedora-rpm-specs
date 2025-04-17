Name:           waynergy
Version:        0.0.17
Release:        1%{?dist}
Summary:        Synergy client for Wayland compositors
# Most sources are MIT or ISC, uSynergy header is zlib
# KDE Wayland protocol XML files are LGPL-2.1-or-later
SourceLicense:  MIT and ISC and zlib and LGPL-2.1-or-later
License:        MIT
URL:            https://github.com/r-c-f/waynergy
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libtls)
Requires:       wl-clipboard

%description
An implementation of a Synergy client for wayland compositors. Based
on the upstream uSynergy library (heavily modified for more protocol
support and a bit of paranoia).


%package kde
Summary:        KDE Plasma Desktop integration for Waynergy
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description kde
An implementation of a Synergy client for wayland compositors. Based
on the upstream uSynergy library (heavily modified for more protocol
support and a bit of paranoia).

This package provides a waynergy.desktop file to enable usage of
KDE private protocol functionality.

%prep
%autosetup -p1


%conf
%meson


%build
%meson_build


%install
%meson_install


%files
%doc README.md
%license LICENSE
%{_bindir}/waynergy
%{_bindir}/waynergy-clip-update
%{_bindir}/waynergy-mapper


%files kde
%{_datadir}/applications/waynergy.desktop


%changelog
* Tue Apr 15 2025 Neal Gompa <ngompa@fedoraproject.org> - 0.0.17-1
- Initial package
