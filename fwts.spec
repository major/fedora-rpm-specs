Name:    fwts
Version: 24.01.00
Release: 1%{?dist}
Summary: Firmware Test Suite

# The ACPICA code is licensed under both GPLv2 and Intel ACPI, a few
# files are licensed under the LGPL. Please see copyright file for details.
License: GPLv2 and LGPLv2 and (GPLv2 or Intel ACPI)

URL: https://wiki.ubuntu.com/FirmwareTestSuite
Source0: http://fwts.ubuntu.com/release/fwts-V%{version}.tar.gz
# Upstream refuses to remove -Werror: https://bugs.launchpad.net/bugs/1687052
Patch0: fwts-Remove-Werror-from-build.patch

# The tests in this package only make sense on the below architectures.
ExclusiveArch: x86_64 %{arm} aarch64 s390x riscv64 %{power64}

BuildRequires: acpica-tools
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: dkms
BuildRequires: flex
BuildRequires: glib2-devel
BuildRequires: json-c-devel
BuildRequires: kernel-devel
BuildRequires: libbsd-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: pciutils-devel

%description
Firmware Test Suite (FWTS) is a test suite that performs sanity checks on
Intel/AMD PC firmware. It is intended to identify BIOS and ACPI errors and if
appropriate it will try to explain the errors and give advice to help
workaround or fix firmware bugs. It is primarily intended to be a Linux-specific
firmware troubleshooting tool.

%prep
%autosetup -a 0 -c -p1

%build
# This package has cases where a symbol is used as both a function
# and a simple integer (with global visibility).  This is broken and
# LTO flags it as an error.  Disable LTO for now
%define _lto_cflags %{nil}

autoreconf -ivf
%configure
# Doesn't currently parallel build, numerous reports across distros
%make_build -j1

%check
%make_build check

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete
find %{buildroot} -type f -name "*.so" -delete

%files
# per-file specific copyright information:
%license debian/copyright
%doc README README_ACPICA.txt
%{_bindir}/fwts
%{_bindir}/kernelscan
%{_datadir}/fwts/
%{_datadir}/bash-completion/completions/fwts*
%{_libdir}/fwts/
%{_mandir}/man1/fwts*

%changelog
* Sat Jan 27 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 24.01.00-1
- Update to 24.01.00

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.03.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.03.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.03.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 21.03.00-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.03.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.03.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.03.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 30 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 21.03.00-1
- Update to 21.03.00
- Spec cleanups

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.11.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Benjamin Berg <bberg@redhat.com> - 20.11.00-1
- New upstream release 20.11.00 (#1815208)
- This release also enables building on riscv

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.02.00-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 20.02.00-4
- Disable LTO

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.02.00-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 20.02.00-2
- Rebuild (json-c)
- Add patch for compatibility with json-c 0.14

* Tue Mar 03 2020 Benjamin Berg <bberg@redhat.com> - 20.02.00-1
- New upstream release 20.02.00
  Resolves: #1690806
- Add patch to fix linking issues due to symbol visibility/declarations
  Resolves: #1799379

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.02.00-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 08 2019 Benjamin Berg <bberg@redhat.com> - 19.02.00-3
- Drop i686 support as it requires an i686 kernel build (#1735231)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.02.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Benjamin Berg <bberg@redhat.com> - 19.02.00-1
- New upstream release (19.02.00) (#1593747)
- Include upstream patches to fix linking issues (#1674912)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.06.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.06.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Benjamin Berg <bberg@redhat.com> - 18.06.02-1
- New upstream release 18.06.02 (#1593747)

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 18.01.00-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Tue Feb 06 2018 Benjamin Berg <bberg@redhat.com> - 18.01.00-1
- Package new upstream version 18.01.00.

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 17.09.00-2
- Rebuilt for libjson-c.so.3

* Mon Aug 21 2017 Benjamin Berg <bberg@redhat.com> - 17.09.00-1
- Initial package version for 17.09.00.

