Name:           drm_info
Version:        2.8.0
Release:        %autorelease
Summary:        Small utility to dump info about DRM devices

# SPDX:MIT
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/drm_info
Source0:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz
Source1:        %{url}/-/releases/v%{version}/downloads/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libdrm) >= 2.4.125
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  python3-devel

%description
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
%autochangelog
