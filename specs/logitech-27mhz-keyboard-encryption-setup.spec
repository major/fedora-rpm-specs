Name:           logitech-27mhz-keyboard-encryption-setup
Version:        0.1
Release:        11%{?dist}
Summary:        Logitech 27MHz keyboard encryption setup tool
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.freedesktop.org/jwrdegoede/logitech-27mhz-keyboard-encryption-setup
Source0:        https://gitlab.freedesktop.org/jwrdegoede/logitech-27mhz-keyboard-encryption-setup/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  make gcc libusb1-devel

%description
A tool for enabling encryption on the 27 MHz wireless connection
used by some (somewhat older) Logitech keyboards.

%prep
%autosetup -n %{name}-v%{version}


%build
%make_build PREFIX=%{_prefix} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
%make_install PREFIX=%{_prefix}


%files
%doc README.md
%license LICENSE
%{_bindir}/lg-27MHz-keyboard-encryption-setup


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr  4 2021 Hans de Goede <hdegoede@redhat.com> - 0.1-1
- Initial Fedora package
