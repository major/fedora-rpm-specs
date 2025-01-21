Name:       xisxwayland
Version:    2
Release:    6%{?dist}
Summary:    Tool to check if the X server is XWayland

License:    MIT
URL:        https://www.x.org
Source0:    https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  meson gcc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)

Obsoletes:  xorg-x11-server-utils < 7.7-40

%description
xisxwayland is a tool to be used within shell scripts to determine whether
the X server in use is Xwayland. It exits with status 0 if the server is an
Xwayland server and 1 otherwise.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/xisxwayland
%{_mandir}/man1/xisxwayland.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 08 2023 Peter Hutterer <peter.hutterer@redhat.com>
- SPDX migration: MIT, nothing to do

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Peter Hutterer <peter.hutterer@redhat.com> - 2-1
- xisxwayland 2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Peter Hutterer <peter.hutterer@redhat.com> 1-1
- Split xisxwayland out from xorg-x11-server-utils into its own package
  (#1932760)
