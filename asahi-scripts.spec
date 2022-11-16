Name:           asahi-scripts
Version:        20221027
Release:        %autorelease
Summary:        Miscellaneous admin scripts for Asahi Linux

License:        MIT
URL:            https://github.com/AsahiLinux/asahi-scripts
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source:         update-m1n1.sysconfig
# Add asahi-fwextract script
Patch:          %{url}/commit/c749ccaa5d9b16d49b8ae49052f14c5838917cd7.patch
# asahi-fwextract: fix overzealous quoting
Patch:          %{url}/commit/780b7f21f8dc002a3a073b34036291655af7dd38.patch
# Makefile: Rework to split out initramfs script installation/removal
Patch:          %{url}/commit/594967c090cd7c64ee7e8bdb1bc0696f00e4a3ec.patch
# dracut: Add firmware loading module
Patch:          %{url}/commit/f933d5510543e8adeb215c450b1002910fecdde7.patch
# dracut: Fix symlink direction
Patch:          %{url}/commit/f67757c036dd16334ec1fd3b8463e66667e71269.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  sed

Requires:       coreutils
Requires:       grep
Requires:       sed
Requires:       util-linux-core

%description
This package contains miscellaneous admin scripts for the Asahi Linux reference
distro.

%package -n     asahi-fwextract
Summary:        Asahi Linux firmware extractor

Requires:       %{name} = %{version}-%{release}
Requires:       python3dist(asahi-firmware)

%description -n asahi-fwextract
Asahi Linux firmware extractor.

%package -n     dracut-asahi
Summary:        Dracut config for Apple Silicon Macs

Requires:       dracut
Requires:       linux-firmware-vendor = %{version}-%{release}
Provides:       dracut-config-asahi = %{version}-%{release}
Obsoletes:      dracut-config-asahi < 20220821-5
Provides:       update-vendor-firmware = %{version}-%{release}
Obsoletes:      update-vendor-firmware < 20220918.2-8

%description -n dracut-asahi
Dracut config for Apple Silicon Macs.

%package -n     linux-firmware-vendor
Summary:        Ensure /lib/firmware/vendor exists for firmware handoff
Requires:       linux-firmware

%description -n linux-firmware-vendor
This package ensures /lib/firmware/vendor exists so that firmware can be handed
over properly from the initramfs.

%package -n     update-m1n1
Summary:        Keep m1n1 up to date

Requires:       %{name} = %{version}-%{release}

Requires:       bash
Requires:       gzip
Requires:       m1n1
Requires:       uboot-images-armv8

%description -n update-m1n1
Keep m1n1 up to date on Apple Silicon systems.

%prep
%autosetup -p1

%build
# nothing to do here

%install
%make_install install-fedora \
  PREFIX="%{_prefix}" \
  BIN_DIR="%{_sbindir}" \
  CONFIG_DIR="%{_sysconfdir}/sysconfig"

install -Ddpm0755 %{buildroot}%{_prefix}/lib/firmware/vendor
install -Dpm0644 %SOURCE1 %{buildroot}%{_sysconfdir}/sysconfig/update-m1n1

%transfiletriggerin -n update-m1n1 -- %{_libdir}/m1n1 %{_datadir}/uboot/apple_m1 /boot/dtb-
%{_sbindir}/update-m1n1 || :

%files
%license LICENSE
%{_datadir}/%{name}/

%files -n asahi-fwextract
%license LICENSE
%{_sbindir}/asahi-fwextract

%files -n dracut-asahi
%license LICENSE
%{_prefix}/lib/dracut/dracut.conf.d/10-asahi.conf
%{_prefix}/lib/dracut/modules.d/99asahi-firmware/

%files -n linux-firmware-vendor
%license LICENSE
%dir %{_prefix}/lib/firmware/vendor

%files -n update-m1n1
%license LICENSE
%config(noreplace) %{_sysconfdir}/m1n1.conf
%config(noreplace) %{_sysconfdir}/sysconfig/update-m1n1
%{_sbindir}/update-m1n1

%changelog
%autochangelog
