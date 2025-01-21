Summary:    X.Org X11 driver installation package
Name:       xorg-x11-drivers
Version:    2022
Release:    9%{?dist}
License:    MIT

Requires:   xorg-x11-drv-dummy
Requires:   xorg-x11-drv-evdev
Requires:   xorg-x11-drv-libinput

%if !0%{?rhel}

%ifnarch aarch64 s390x
Requires:   xorg-x11-drv-qxl
%endif

# only non-s390x
%ifnarch s390x
Requires:   xorg-x11-drv-ati
Requires:   xorg-x11-drv-nouveau
Requires:   xorg-x11-drv-wacom
%endif

%ifarch %{ix86} x86_64
Requires:   xorg-x11-drv-intel
Requires:   xorg-x11-drv-vmware
Requires:   xorg-x11-drv-openchrome
%endif

%endif

%description
The purpose of this package is to require all of the individual X.Org driver
rpms, to allow the OS installation software to install all drivers all at once,
without having to track which individual drivers are present on each
architecture.  By installing this package, it forces all of the individual
driver packages to be installed.

%files

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2022-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 27 2024 Simone Caronni <negativo17@gmail.com> - 2022-8
- Drop xorg-x11-drv-modesetting requirement.
- Clean up SPEC file.

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2022-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 07 2023 José Expósito <jexposit@redhat.com>
- SPDX migration: license is already SPDX compatible

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 01 2022 Adam Jackson <ajax@redhat.com> - 2022-3
- Drop vesa and fbdev for https://fedoraproject.org/wiki/Changes/LegacyXorgDriverRemoval

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Adam Jackson <ajax@redhat.com> - 2022-1
- Drop v4l

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
