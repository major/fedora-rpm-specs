%global commit e1281d4de9166b7254ba30bb58f9191fc2c9e7fb
%global date 20240305
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Summary: Configure MMC storage devices from userspace
Name: mmc-utils
Version: 0~%{date}git%{shortcommit}
Release: 4%{?dist}
URL: https://docs.kernel.org/driver-api/mmc/mmc-tools.html
Source0: https://git.kernel.org/pub/scm/utils/mmc/mmc-utils.git/snapshot/mmc-utils-%{commit}.tar.gz
Patch0: https://sources.debian.org/data/main/m/mmc-utils/0%2Bgit20220624.d7b343fd-1/debian/patches/0001-Fix-typo.patch
Patch1: https://sources.debian.org/data/main/m/mmc-utils/0%2Bgit20220624.d7b343fd-1/debian/patches/0002-man-mmc.1-Fix-warning-macro-not-defined.patch
# remove -Werror from CFLAGS
Patch2: %{name}-no-Werror.patch
License: GPL-2.0-only AND BSD-3-Clause
BuildRequires: gcc
BuildRequires: make
# BSD-licensed HMAC-SHA-224/256/384/512 implementation from http://www.ouah.org/ogay/hmac/
# 3rdparty/hmac_sha
Provides: bundled(hmac)

%description
The mmc-utils tools can do the following:

* Print and parse extcsd data.
* Determine the eMMC writeprotect status.
* Set the eMMC writeprotect status.
* Set the eMMC data sector size to 4KB by disabling emulation.
* Create general purpose partition.
* Enable the enhanced user area.
* Enable write reliability per partition.
* Print the response to STATUS_SEND (CMD13).
* Enable the boot partition.
* Set Boot Bus Conditions.
* Enable the eMMC BKOPS feature.
* Permanently enable the eMMC H/W Reset feature.
* Permanently disable the eMMC H/W Reset feature.
* Send Sanitize command.
* Program authentication key for the device.
* Counter value for the rpmb device will be read to stdout.
* Read from rpmb device to output.
* Write to rpmb device from data file.
* Enable the eMMC cache feature.
* Disable the eMMC cache feature.
* Print and parse CID data.
* Print and parse CSD data.
* Print and parse SCR data.

%prep
%autosetup -n %{name}-%{commit} -p1

%build
%make_build GIT_VERSION=%{shortcommit}

%install
%make_install bindir=%{_bindir}
install -D -pm0644 -t %{buildroot}%{_mandir}/man1 man/mmc.1

%files
%doc README
%{_bindir}/mmc
%{_mandir}/man1/mmc.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0~20240305gite1281d4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0~20240305gite1281d4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 22 2024 Dominik Mierzejewski <rpm@greysector.net> 0~20240305gite1281d4-2
- declare bundled hmac_sha code and update License tag

* Tue Mar 19 2024 Dominik Mierzejewski <rpm@greysector.net> 0~20240305gite1281d4-1
- update to latest git snapshot
- use correct snapshot versioning
- use patch instead of cflags override

* Tue Apr 04 2023 Dominik Mierzejewski <rpm@greysector.net> 0.1-2.20230209gitd4c2910
- fixed build on rawhide

* Mon Apr 03 2023 Dominik Mierzejewski <rpm@greysector.net> 0.1-1.20230209gitd4c2910
- initial build
