Name:           drm_info
Version:        2.3.0
Release:        %autorelease
Summary:        Small utility to dump info about DRM devices

# SPDX:MIT
License:        MIT
URL:            https://github.com/ascent12/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/ascent12/drm_info/pull/88
Patch:          drm_info-2.3.0-Add-a-manpage.patch

BuildRequires:  gcc
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libdrm) >= 2.4.104
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  python3-devel

%description
%{summary}.


%prep
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
