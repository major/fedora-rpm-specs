# Shell script only, nothing to generate debuginfo for
%global debug_package %{nil}
# Salsa gitlab tag tarbals contain a dir with the full git hash in its name
%global commit 3df4f19ec8f4bac8d38a080070298989e453e452

Name:           qcom-firmware-extract
Version:        21
Release:        1%{?dist}
Summary:        Script to extract Qualcomm firmware from Windows partition

License:        GPL-2.0-or-later
URL:            https://salsa.debian.org/debian/qcom-firmware-extract/
# Upstream forgot to add the tag for version 21
# Source0:        %{url}/-/archive/debian/%{version}/%{name}-%{version}.tar.gz
Source0:        %{url}/-/archive/%{commit}/%{name}-%{version}.tar.gz
# Fedora patches
Patch:          0001-qcom-firmware-extract-Modify-to-generate-install-an-.patch
Patch:          0002-qcom-firmware-extract-2-small-fixes.patch
Patch:          0003-qcom-firmware-extract-xz-compress-mbn-and-elf-files.patch
Patch:          0004-qcom-firmware-extract-Add-support-for-UFS-storage.patch
Patch:          0005-qcom-firmware-extract-Add-Samsung-Galaxy-Book-Go.patch

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
# Upstream forgot to add the tag for version 21
# #autosetup -p1 -n %{name}-debian-%{version}-%{commit}
%autosetup -p1 -n %{name}-%{commit}


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
* Sun Sep 20 2026 Hans de Goede <johannes.goede@oss.qualcomm.com> - 21-1
- New upstream release 21 with support for more devices
- Fix firmware install not working on Fedora 45+ due to new rpm signature policy

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
