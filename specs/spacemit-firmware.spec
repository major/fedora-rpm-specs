%define __strip /bin/true

Name:           spacemit-firmware
Version:        20240829
Release:        %{autorelease}
Summary:        SpacemiT firmware

License:        LicenseRef-Fedora-Firmware
URL:            https://bianbu-linux.spacemit.com/en/faqs/
# gitee.com is weird about client IPs or/and http agent request details. depending on where you are or how you try
# it might serve you the file without issues or redirect you to a requirement to open an account there
Source0:        https://gitee.com/bianbu-linux/buildroot-ext/raw/bl-v2.0.y/board/spacemit/k1/target_overlay/lib/firmware/esos.elf
Source1:        https://gitee.com/bianbu-linux/buildroot-ext/raw/k1-bl-v2.2.y/board/spacemit/k1/target_overlay/lib/firmware/LICENSE.spacemit_esos
Source2:        spacemit-firmware.conf

BuildArch:      noarch

BuildRequires:  coreutils

%description
SpacemiT firmware for the internal MCU on their X60 series SOC's
and eventually other chips

%package dracut
Requires: spacemit-firmware

Summary: A dracut.conf.d file for spacemit-firmware

%description dracut
Provides /etc/dracut.cond.d/spacemit-firmware.conf to ensure the
spacemit firmware is included in the initramfs

%prep
cp -av %{SOURCE1} .


%build

%install
install -D -m644 %{SOURCE0} %{buildroot}/lib/firmware/esos.elf
install -D -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dracut.conf.d/spacemit-firmware.conf


%files
%license LICENSE.spacemit_esos
%dir /lib/firmware
/lib/firmware/esos.elf

%files dracut
%{_sysconfdir}/dracut.conf.d/spacemit-firmware.conf

%changelog
%autochangelog
