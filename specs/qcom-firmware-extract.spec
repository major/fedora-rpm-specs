# Shell script only, nothing to generate debuginfo for
%global debug_package %{nil}
# Salsa gitlab tag tarbals contain a dir with the full git hash in its name
%global commit aa1055d6551392d97f4f0e0220d15f95363ee859

Name:           qcom-firmware-extract
Version:        20
Release:        2%{?dist}
Summary:        Script to extract Qualcomm firmware from Windows partition

License:        GPL-2.0-or-later
URL:            https://salsa.debian.org/debian/qcom-firmware-extract/
Source0:        %{url}/-/archive/debian/%{version}/%{name}-%{version}.tar.gz
# Fedora patches
Patch:          0002-qcom-firmware-extract-Modify-to-generate-install-an-.patch
Patch:          0003-qcom-firmware-extract-3-small-fixes.patch
Patch:          0004-qcom-firmware-extract-xz-compress-mbn-and-elf-files.patch
Patch:          0005-qcom-firmware-extract-Add-support-for-UFS-storage.patch
Patch:          0006-qcom-firmware-extract-Add-Samsung-Galaxy-Book-Go.patch

Requires:       bash
Requires:       coreutils
Requires:       dislocker
Requires:       grep
Requires:       ntfs-3g
Requires:       util-linux
Requires:       rpm-build
Requires:       xz

ExclusiveArch:  aarch64

%description
This package contains a script used to extract firmware from Qualcomm
Snapdragon X Elite powered machines such as the Thinkpad T14s Gen 6.
It is intended as a temporary solution until the firmware is distributable
under an appropriate license.


%prep
%autosetup -p1 -n %{name}-debian-%{version}-%{commit}


%build
# nothing to build


%install
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
cp -p %{name} $RPM_BUILD_ROOT%{_sbindir}
cp -p %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8


%files
%license LICENSE
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Fri Jul 24 2026 Hans de Goede <johannes.goede@oss.qualcomm.com> - 20-2
- Add UFS storage support
- Add support for Samsung Galaxy Go (LTE) NP345XLA

* Fri Jul 24 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 20-1
- Update to v20

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon Apr 13 2026 Hans de Goede <johannes.goede@oss.qualcomm.com> - 17-2
- Properly install manpage under /usr/share/man/man8/

* Sun Apr 12 2026 Hans de Goede <johannes.goede@oss.qualcomm.com> - 17-1
- Initial Fedora package
