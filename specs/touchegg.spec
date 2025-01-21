Name:           touchegg
Version:        2.0.17
Release:        2%{?dist}
Summary:        Multi-touch gesture recognizer

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/JoseExposito/touchegg
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         add_missing_include.patch

ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

%description
Touchégg is an app that runs in the background and transform the gestures you
make on your touchpad or touchscreen into visible actions in your desktop.

For example, you can swipe up with 3 fingers to maximize a window or swipe left
with 4 finger to switch to the next desktop.

Many more actions and gestures are available and everything is easily
configurable.


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
# We cannot restart the service on update, because it breaks clients.
# https://github.com/JoseExposito/touchegg/issues/453
%systemd_postun %{name}.service


%files
%license COPYING COPYRIGHT
%doc README.md CHANGELOG.md
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_unitdir}/%{name}.service


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Leigh Scott <leigh123linux@gmail.com> - 2.0.17-1
- Update to 2.0.17

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.16-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Maíra Canal <mairacanal@riseup.net> - 2.0.16-1
- Update to 2.0.16.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 18 2022 Maxwell G <gotmax@e.email> - 2.0.15-1
- Update to 2.0.15. Fixes rhbz#2143434.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 02 2022 Maxwell G <gotmax@e.email> - 2.0.14-1
- Update to 2.0.14.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Fabio Valentini <decathorpe@gmail.com> - 2.0.13-1
- Update to version 2.0.13; Fixes RHBZ#2038561

* Sun Dec 26 2021 Maxwell G <gotmax@e.email> - 2.0.12-1
- Perform initial import. Close rhbz#2035944.
