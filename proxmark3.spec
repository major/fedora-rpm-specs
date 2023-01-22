Name:		proxmark3
Version:	4.15864
Release:	4%{?dist}
Summary:	The Swiss Army Knife of RFID Research - RRG/Iceman repo
License:	GPLv3+
URL:		https://github.com/RfidResearchGroup/proxmark3
Source0:	https://github.com/RfidResearchGroup/proxmark3/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	make, gcc, g++, readline-devel, arm-none-eabi-gcc, arm-none-eabi-newlib, bzip2-devel, libatomic, openssl-devel, python3-devel, jansson-devel, bluez-libs-devel, qt5-qtbase-devel
Requires:	bzip2-libs, readline, python3, bluez, qt5-qtbase
ExcludeArch:	ppc64le s390x

%description
The Swiss Army Knife of RFID Research - RRG/Iceman repo

%define __strip /bin/true

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} V=1 clean
make %{?_smp_mflags} V=1 SKIPLUASYSTEM=1
rm -rf %{buildroot}/doc/datasheets/
rm -rf %{buildroot}/doc/original_proxmark3/

%install
chmod -x ./client/luascripts/examples/example_cmdline.lua
chmod -x ./client/cmdscripts/rdv4_init_extflash.cmd
chmod -x ./client/pyscripts/xorcheck.py
chmod -x ./client/cmdscripts/example.cmd
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
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.15864-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild


* Mon Nov 14 2022 Marlin Soose <marlin.soose@laro.se> - 4.15864
- Bumping package to v4.15864

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.14831-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.14831-2
- Rebuilt for Python 3.11

* Tue Apr 19 2022 Marlin Soose <marlin.soose@laro.se> - 4.14831
- Initial version of the package
