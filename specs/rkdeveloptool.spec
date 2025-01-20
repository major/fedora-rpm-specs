Name:          rkdeveloptool
Version:       1.32
Release:       11%{?dist}
Summary:       A simple way to read/write Rock Chips rockusb devices
License:       GPL-2.0-only
URL:           http://opensource.rock-chips.com/wiki_Rkdeveloptool
# Upstream doesn't currently push the release tags, upstream issue filed
# https://github.com/rockchip-linux/rkdeveloptool/issues/36
# git archive --format=tar --prefix=%{name}-%{version}/ 46bb4c0 | xz > ~/%{name}-%{version}.tar.xz
Source0:       %{name}-%{version}.tar.xz
# Source0:       https://github.com/rockchip-linux/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://build.opensuse.org/package/view_file/hardware/rkdeveloptool/99-rkdeveloptool.rules
Source1:       99-rkdeveloptool.rules
# https://github.com/rockchip-linux/rkdeveloptool/pull/57
Patch0:        rkdeveloptool-gcc-fixes.patch

BuildRequires: make
BuildRequires: autoconf automake
BuildRequires: gcc-c++
BuildRequires: libusbx-devel
BuildRequires: systemd-devel

%description
A simple way to read/write rockusb devices for flashing firmware to Rock Chips
SoC based devices such as those based on the rk3399/3368/3328/3288 etc.

%prep
%autosetup -p1

%build
NOCONFIGURE=1 autoreconf -vif
%configure

%make_build

%install
%make_install
install -D -m 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-rkdeveloptool.rules

%files
%license license.txt
%doc Readme.txt
%{_bindir}/rkdeveloptool
%{_udevrulesdir}/99-rkdeveloptool.rules

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.32-6
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Dan Horák <dan[at]danny.cz> - 1.32-1
- updated to 1.32

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-2
- Add udev rules for device detection

* Fri Jun 28 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-1
- Initial package
