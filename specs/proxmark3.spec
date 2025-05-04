Name:		proxmark3
Version:	4.20142
Release:	%autorelease
Summary:	The Swiss Army Knife of RFID Research - RRG/Iceman repo
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/RfidResearchGroup/proxmark3
Source0:	https://github.com/RfidResearchGroup/proxmark3/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	make, gcc, g++, readline-devel, arm-none-eabi-gcc, arm-none-eabi-newlib, bzip2-devel, libatomic, openssl-devel, python3-devel, jansson-devel, bluez-libs-devel, qt5-qtbase-devel, lz4-devel, gd-devel, gd
Requires:	bzip2-libs, readline, python3, bluez, qt5-qtbase, gd
ExcludeArch:	ppc64le s390x i686

%description
The Swiss Army Knife of RFID Research - RRG/Iceman repo

%define __strip /bin/true

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} V=1 clean
make %{?_smp_mflags} V=1 
rm -rf %{buildroot}/doc/datasheets/
rm -rf %{buildroot}/doc/original_proxmark3/

%install
chmod -x ./client/luascripts/examples/example_cmdline.lua
chmod -x ./client/cmdscripts/rdv4_init_extflash.cmd
chmod -x ./client/pyscripts/xorcheck.py
chmod -x ./client/cmdscripts/example.cmd
sed -i 's|^TOOLS_PATH \?= \?None|TOOLS_PATH="/usr/share/proxmark3/"|' ./client/pyscripts/pm3_resources.py
sed -i 's|^DICTS_PATH \?= \?None|DICTS_PATH="/usr/share/proxmark3/dictionaries"|' ./client/pyscripts/pm3_resources.py
make %{?_smp_mflags} V=1 install PREFIX=%{buildroot}/usr UDEV_PREFIX=%{buildroot}/etc/udev/rules.d/
chmod -x %{buildroot}/usr/share/proxmark3/firmware/fullimage.elf
chmod -x %{buildroot}/usr/share/proxmark3/firmware/bootrom.elf
rm -rf %{buildroot}%{_datadir}/doc/proxmark3

%files
%{_sysconfdir}/udev/rules.d/77-pm3-usb-device-blacklist.rules
%{_bindir}/pm3
%{_bindir}/pm3-flash
%{_bindir}/pm3-flash-all
%{_bindir}/pm3-flash-bootrom
%{_bindir}/pm3-flash-fullimage
%{_bindir}/proxmark3
%{_datadir}/proxmark3

%license LICENSE.txt
%doc doc/ AUTHORS.md CHANGELOG.md COMPILING.txt CONTRIBUTING.md README.md

%changelog

* Thu May 01 2025 Marlin Soose <marlin.soose@esque.ca> - 4.20142
- Include lua scripting capabilities
- Bumping package to v4.20142

* Fri Nov 22 2024 Marlin Soose <marlin.soose@esque.ca> - 4.19552
- Bumping package to v4.19552

* Thu Sep 12 2024 Marlin Soose <marlin.soose@esque.ca> - 4.18994
- Bumping package to v4.18994

* Tue Jul 30 2024 Marlin Soose <marlin.soose@esque.ca> - 4.18589
- Bumping package to v4.18589 and dropping i686 support

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 4.18218-1
- convert license to SPDX

* Sun Feb 18 2024 Marlin Soose <marlin.soose@esque.ca> - 4.18218
- Bumping package to v4.18218

* Tue Nov 7 2023 Marlin Soose <marlin.soose@esque.ca> - 4.17511
- Bumping package to v4.17511

* Tue Nov 7 2023 Marlin Soose <marlin.soose@esque.ca> - 4.17140
- Bumping package to v4.17140, add lz4-devel build dep

* Tue Jun 27 2023 Marlin Soose <marlin.soose@esque.ca> - 4.16717-6
- Bumping package to v4.16717

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 4.16191-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.15864-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Marlin Soose <marlin.soose@esque.ca> - 4.15864
- Bumping package to v4.15864

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14831-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.14831-2
- Rebuilt for Python 3.11

* Tue Apr 19 2022 Marlin Soose <marlin.soose@esque.ca> - 4.14831
- Initial version of the package
