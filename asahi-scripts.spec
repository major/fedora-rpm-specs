Name:           asahi-scripts
Version:        20220918.2
Release:        %autorelease
Summary:        Miscellaneous admin scripts for Asahi Linux

License:        MIT
URL:            https://github.com/AsahiLinux/asahi-scripts
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source:         update-m1n1.sysconfig
# PR#8: Various makefile fixes for Fedora
Patch:          %{url}/pull/8.patch
# PR#9: Add dracut module
Patch:          %{url}/pull/9.patch
# PR#10: update-vendor-firmware: explicitly overwrite files
Patch:          %{url}/pull/10.patch
# PR#11: Add asahi-fwextract script
Patch:          %{url}/pull/11.patch

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
Requires:       update-vendor-firmware = %{version}-%{release}
Provides:       dracut-config-asahi = %{version}-%{release}
Obsoletes:      dracut-config-asahi < 20220821-5

%description -n dracut-asahi
Dracut config for Apple Silicon Macs.

%package -n     update-m1n1
Summary:        Keep m1n1 up to date

Requires:       %{name} = %{version}-%{release}

Requires:       bash
Requires:       gzip
Requires:       m1n1
Requires:       uboot-images-armv8 >= 2022.10-0.3.rc1

%description -n update-m1n1
Keep m1n1 up to date on Apple Silicon systems.

%package -n     update-vendor-firmware
Summary:        Install and update firmware from the VendorFW package

Requires:       %{name} = %{version}-%{release}

Requires:       bash
Requires:       linux-firmware
Requires:       tar

%description -n update-vendor-firmware
Apple Silicon systems rely on some non-redistributable firmware blobs. This
package extracts and installs them from the VendorFW package provided in the
ESP.

%prep
%autosetup -p1

%build
# nothing to do here

%install
%make_install install-fedora \
  PREFIX="%{_prefix}" \
  BIN_DIR="%{_sbindir}" \
  CONFIG_DIR="%{_sysconfdir}/sysconfig"

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

%files -n update-m1n1
%license LICENSE
%config(noreplace) %{_sysconfdir}/m1n1.conf
%config(noreplace) %{_sysconfdir}/sysconfig/update-m1n1
%{_sbindir}/update-m1n1

%files -n update-vendor-firmware
%license LICENSE
%{_sbindir}/update-vendor-firmware

%changelog
%autochangelog
