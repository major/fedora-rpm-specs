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

BuildArch:      noarch

BuildRequires:  coreutils

%description
SpacemiT firmware for the internal MCU on their X60 series SOC's
and eventually other chips

%prep
cp -av %{SOURCE1} .


%build

%install
install -D -m644 %{SOURCE0} %{buildroot}/lib/firmware/esos.elf


%files
%license LICENSE.spacemit_esos
%dir /lib/firmware
/lib/firmware/esos.elf

%changelog
%autochangelog
