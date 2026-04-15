# Shell script only, nothing to generate debuginfo for
%global debug_package %{nil}
# Salsa gitlab tag tarbals contain a dir with the full git hash in its name
%global commit eb480711892d8bd13aa235b1203dea1e20e9c23d

Name:           qcom-firmware-extract
Version:        17
Release:        2%{?dist}
Summary:        Script to extract Qualcomm firmware from Windows partition

License:        GPL-2.0-or-later
URL:            https://salsa.debian.org/debian/qcom-firmware-extract/
Source0:        %{url}/-/archive/debian/%{version}/%{name}-%{version}.tar.gz
# Unreleased patch from upstream
Patch:          0001-Add-Microsoft-Surface-Pro-11th-Edition.patch
# Fedora patches
Patch:          0002-qcom-firmware-extract-Modify-to-generate-install-an-.patch
Patch:          0003-qcom-firmware-extract-3-small-fixes.patch
Patch:          0004-qcom-firmware-extract-xz-compress-mbn-and-elf-files.patch

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
* Mon Apr 13 2026 Hans de Goede <johannes.goede@oss.qualcomm.com> - 17-2
- Properly install manpage under /usr/share/man/man8/

* Sun Apr 12 2026 Hans de Goede <johannes.goede@oss.qualcomm.com> - 17-1
- Initial Fedora package
