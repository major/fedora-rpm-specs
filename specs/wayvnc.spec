# -*-Mode: rpm-spec -*-

%global nvnc_version 0.9.0

Name:     wayvnc
Version:  0.9.1
Release:  2%{?dist}
Summary:  A VNC server for wlroots based Wayland compositors
License:  ISC
URL:      https://github.com/any1/wayvnc
Source:   %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(aml) >= 0.2.2
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(neatvnc) >= %{nvnc_version}
BuildRequires: pam-devel
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon) >= 1.0.0
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(aml) >= 0.3.0
BuildRequires: scdoc

Requires: (sway >= 1.6 if sway)
Requires: aml >= 0.3.0
Requires: neatvnc >= %{nvnc_version}

%description

This is a VNC server for wlroots based Wayland compositors. It
attaches to a running Wayland session, creates virtual input devices
and exposes a single display via the RFB protocol. The Wayland session
may be a headless one, so it is also possible to run wayvnc without a
physical display attached.

%prep
%autosetup

%build
%meson

%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%{_bindir}/%{name}ctl

%doc README.md FAQ.md
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}ctl.1.*

%license COPYING

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 21 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1

* Wed Nov 20 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Bob Hepple <bob.hepple@gmail.com> - 0.8.0-2
- require neatvnc >= 0.8.0

* Wed Feb 28 2024 Bob Hepple <bob.hepple@gmail.com> - 0.8.0-1
- new version

* Tue Feb 06 2024 František Zatloukal <fzatlouk@redhat.com> - 0.7.2-3
- Rebuilt for turbojpeg 3.0.2

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Bob Hepple <bob.hepple@gmail.com> - 0.7.2-1
- new version

* Sat Oct 07 2023 Bob Hepple <bob.hepple@gmail.com> - 0.7.1-1
- new version

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 31 2023 Bob Hepple <bob.hepple@gmail.com> - 0.6.2-2
- add versioning for aml & neatvnc

* Tue Jan 31 2023 Bob Hepple <bob.hepple@gmail.com> - 0.6.2-1
- new version

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Bob Hepple <bob.hepple@gmail.com> - 0.5.0-1
- new version

* Fri Dec 17 2021 Bob Hepple <bob.hepple@gmail.com> - 0.4.1-1
- new version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Bob Hepple <bob.hepple@gmail.com> - 0.4.0-3
- need xkbcommon >= 1.0.0

* Mon Jan 04 2021 Bob Hepple <bob.hepple@gmail.com> - 0.4.0-2
- rebuilt - no longer any need for fix-man-dir patch

* Mon Jan 04 2021 Bob Hepple <bob.hepple@gmail.com> - 0.4.0-1
- new version

* Tue Sep 29 2020 Bob Hepple <bob.hepple@gmail.com> - 0.3.0-1
- new version

* Wed Aug 05 2020 Bob Hepple <bob.hepple@gmail.com> - 0.2.0-1
- new version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Robert Hepple - 0.1.2-3
- fixes per RHBZ#1823265

* Wed Apr 15 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.2-2
- fixes per RHBZ#1823265

* Sun Apr 12 2020 Bob Hepple <bob.hepple@gmail.com> - 0.1.2-1
- Initial version of the package
