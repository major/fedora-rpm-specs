Summary:    Check operability of computer hardware and find drivers
Name:       hw-probe
Version:    1.6.5
Release:    7%{?dist}
BuildArch:  noarch
License:    LGPL-2.1-or-later OR BSD-4-Clause
URL:        https://github.com/linuxhw/hw-probe
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:   perl-libwww-perl
Requires:   curl
Requires:   hwinfo
Requires:   pciutils
Requires:   usbutils
Requires:   smartmontools
Requires:   hdparm
Requires:   sysstat
Requires:   util-linux
Requires:   lm_sensors
%if 0%{?fedora} >= 24
Recommends: dmidecode
Recommends: mcelog
Recommends: acpica-tools
Recommends: edid-decode xdpyinfo xinput xrandr xvinfo
Recommends: glx-utils
%endif
%if 0%{?el6}%{?el7}
Requires:   dmidecode
%endif
%if 0%{?el8}
Recommends: dmidecode
Recommends: mcelog
%endif
BuildRequires: perl(Getopt::Long)
BuildRequires: perl-generators
BuildRequires: make

%description
A tool to probe for hardware, check operability and find drivers
with the help of Linux hardware database:

    sudo -E hw-probe -all -upload

%prep
%autosetup

%build
# Nothing to build yet

%install
mkdir -p %{buildroot}%{_prefix}
%make_install prefix=%{_prefix}

%files
%doc README.md
%license LICENSES/LGPL-2.1-or-later
%{_bindir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.5-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May  8 2023 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.6.5-1
- Update to 1.6.5

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 11 2022 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.6.4-1
- Update to 1.6.4

* Tue Mar 22 2022 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.6.3-2
- Update to 1.6.3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 22 2021 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.6-1
- Update to 1.6

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 1.5-4
- Recommend edid-decode xdpyinfo xinput xrandr xvinfo, not xorg-x11-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.5-1
- Update to 1.5

* Mon Oct  7 2019 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-15
- Support for EL-8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  9 2019 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-12
- Do not require mesa-demos and redhat-lsb-core.

* Wed Dec 19 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-11
- Recommends acpica-tools.
- Fix dmidecode dependency.

* Wed Dec 19 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-10
- Recommends glx-utils for glxinfo.

* Wed Dec 19 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-9
- Recommends xorg-x11-utils for edid-decode and mesa-demos for glxgears.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-8
- Recommends dmidecode.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-7
- Exclude arm.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-6
- Fix ifdef for armhfp.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-5
- No dmidecode for armhfp.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-4
- Fix bogus date in changelog.

* Fri Dec 14 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-3
- Recommends mcelog only for Fedora 24 or newer.

* Tue Dec 11 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-2
- Require perl(Getopt::Long) at build time.

* Mon Dec  3 2018 Andrey Ponomarenko <andrewponomarenko@yandex.ru> - 1.4-1
- Initial Fedora package.
