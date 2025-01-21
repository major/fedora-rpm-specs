Name:           wayland-utils
Version:        1.2.0
Release:        6%{?dist}
Summary:        Wayland utilities

License:        MIT
URL:            https://wayland.freedesktop.org/
Source0:        https://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(wayland-client) >= 1.20
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109

%description
wayland-utils contains wayland-info, a standalone version of weston-info,
a utility for displaying information about the Wayland protocols supported
by the Wayland compositor.
wayland-info also provides additional information for a subset of Wayland
protocols it knows about, namely Linux DMABUF, presentation time, tablet and
XDG output protocols.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/wayland-info
%{_mandir}/man1/wayland-info.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 11 2023 Olivier Fourdan <ofourdan@redhat.com> - 1.2.0-3
- migrated to SPDX license

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun  8 2023 Olivier Fourdan <ofourdan@redhat.com> - 1.2.0-1
- wayland-utils 1.2.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Olivier Fourdan <ofourdan@redhat.com> - 1.1.0-1
- wayland-utils 1.1.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug  3 2020 Olivier Fourdan <ofourdan@redhat.com> - 1.0.0-1
- Initial package
