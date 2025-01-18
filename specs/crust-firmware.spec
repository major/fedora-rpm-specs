# Binaries are firmware and OpenRISC so debuginfo is useless
%global debug_package %{nil}

Name:    crust-firmware
Version: 0.6
Release: 4%{?dist}
Summary: An Open Source SCP firmware for AllWinner SoCs
License: BSD-3-clause OR GPL-2.0-only
URL:     https://github.com/crust-firmware/crust

Source0: https://github.com/crust-firmware/crust/archive/refs/tags/crust-%{version}.tar.gz
Patch1:  0001-socs-Add-SoC-level-defaults-for-each-type-we-support.patch

# While the SoCs are aarch64 the SCP firmware co-processor is OpenRISC which Fedora
# doesn't have a target for so we have to cross compile so we can build with Feodra.
BuildArch:   noarch
BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc
BuildRequires: make
BuildRequires: binutils-openrisc-linux-gnu
BuildRequires: gcc-openrisc-linux-gnu

%description
Crust is a standards based System Control Processor (SCP) open firmware for most
AllWinner based SoCs used for things like power managemenet and suspend resume.

%prep
%autosetup -p1 -n crust-%{version}

%build

mkdir -p builds
for soc in a64 h5 h6
do
  make CROSS_COMPILE="/usr/bin/openrisc-linux-gnu-" V=1 $(echo $soc)_defconfig O=build/$(echo $soc)/
  make CROSS_COMPILE="/usr/bin/openrisc-linux-gnu-" V=1 O=build/$(echo $soc)/
  mv build/ builds/$(echo $soc)
done

%install

mkdir -p %{buildroot}%{_datadir}/%{name}

for soc in a64 h5 h6
do
  mkdir %{buildroot}%{_datadir}/%{name}/$(echo $soc)
  cp builds/$(echo $soc)/scp/scp.bin %{buildroot}%{_datadir}/%{name}/$(echo $soc)/
done


%files
%license LICENSE.md
%{_datadir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 01 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6-3
- Use a capital OR

* Sun Sep 01 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6-2
- Update license field

* Sun Sep 01 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6-1
- Initial package
