Name:           8088_bios
Version:        1.0.2
Release:        %autorelease
Summary:        BIOS for Intel 8088 based computers

License:        GPL-3.0-or-later
URL:            https://github.com/skiselev/8088_bios
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  nasm
BuildRequires:  xtideuniversalbios

BuildArch:      noarch

%description
This package provides a BIOS for Sergey Kiselev's IBM PC/XT compatible systems:
Micro 8088, Xi 8088 and Sergey's XT.

%prep
%autosetup

# Replace bundled files in xtide_r625/ with Fedora packaged version padded to 8 kB
dd if=%{_datadir}/xtideuniversalbios/ide_xt.bin of=xtide_r625/ide_xt-cf-lite_300h.bin bs=8k count=1 conv=sync
dd if=%{_datadir}/xtideuniversalbios/ide_xtp.bin of=xtide_r625/ide_xtp-cf-lite_300h.bin bs=8k count=1 conv=sync
dd if=%{_datadir}/xtideuniversalbios/ide_xt.bin of=xtide_r625/ide_xt-cf-lite_320h.bin bs=8k count=1 conv=sync
dd if=%{_datadir}/xtideuniversalbios/ide_xt.bin of=xtide_r625/ide_xt-xt-ide-v2-300h.bin bs=8k count=1 conv=sync
dd if=%{_datadir}/xtideuniversalbios/ide_xtp.bin of=xtide_r625/ide_xtp-xt-ide-v2-300h.bin bs=8k count=1 conv=sync

%build
%cmake
%cmake_build

%install
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name} %{__cmake_builddir}/bios*.bin
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name} %{__cmake_builddir}/bios*.rom

%check
# Sanity check to ensure the output binaries are not empty
test -s %{__cmake_builddir}/bios-micro8088.bin
test -s %{__cmake_builddir}/bios-xi8088.bin

%files
%license LICENSE.txt copyright.tmpl
%doc README.md
%{_datadir}/%{name}/

%changelog
%autochangelog
