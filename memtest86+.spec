# Prevent stripping
%global __spec_install_post /usr/lib/rpm/brp-compress
# Turn off debuginfo package
%global debug_package %{nil}
%global common_description %{expand:
Memtest86+ is a thorough stand-alone memory test for x86 and x86-64
architecture computers. BIOS based memory tests are only a quick
check and often miss many of the failures that are detected by
Memtest86+.
}
%ifarch x86_64
%global mt_isa x64
%endif
%ifarch %{ix86}
%global mt_isa ia32
%endif

Name:                memtest86+
Version:             6.20
Release:             %autorelease
Summary:             Stand-alone memory tester for x86-64 computers
License:             GPL-2.0-only
URL:                 https://www.memtest.org/
Source0:             https://github.com/memtest86plus/memtest86plus/archive/v%{version}/memtest86-plus-%{version}.tar.gz

BuildRequires:       gcc, make, xorriso, dosfstools, mtools
ExclusiveArch:       x86_64 %{ix86}

%description
%wordwrap -v common_description


%prep
%autosetup -n memtest86plus-%{version} -p1


%build
pushd build%{__isa_bits}
make
make iso
popd


%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_datarootdir}/%{name}

pushd build%{__isa_bits}
install -m 0644 memtest.efi %{buildroot}%{_libdir}/%{name}/memtest86+%{mt_isa}.efi
install -m 0644 memtest.bin %{buildroot}%{_libdir}/%{name}/memtest86+%{mt_isa}.bin
install -m 0644 memtest.iso %{buildroot}%{_datarootdir}/%{name}/memtest86+%{mt_isa}.iso
popd


%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}/memtest86+%{mt_isa}.*
%{_datarootdir}/%{name}/memtest86+%{mt_isa}.iso

%posttrans
install -m 0644 %{_libdir}/%{name}/memtest86+%{mt_isa}.* /boot/
if [ -d /sys/firmware/efi/ ]; then
cat << EOBLSEFI > /boot/loader/entries/`cat /etc/machine-id`-0-memtest86+-%{version}-uefi.%{mt_isa}.conf
title Memtest86+ v%{version} %{mt_isa} UEFI
linux /memtest86+%{mt_isa}.efi
EOBLSEFI
else
cat << EOBLSBIN > /boot/loader/entries/`cat /etc/machine-id`-0-memtest86+-%{version}-bios.%{mt_isa}.conf
title Memtest86+ v%{version} %{mt_isa} BIOS
linux /memtest86+%{mt_isa}.bin
EOBLSBIN
fi
exit 0

%postun
if [ $1 -eq 0 ]; then
rm -f /boot/memtest86+%{mt_isa}.*
rm -f /boot/loader/entries/`cat /etc/machine-id`-0-memtest86+-%{version}-*.%{mt_isa}.conf
fi
exit 0


%changelog
%autochangelog
