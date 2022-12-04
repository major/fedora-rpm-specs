Name:           systemd-boot
Version:        251~rc2
Release:        %autorelease
Summary:        UEFI boot manager

License:        LGPLv2+
URL:            https://systemd.io

# This will be changed to systemd-boot-unsigned after it has been split out.
%global source_rpm_name systemd-udev

# Note: this package just signs an existing binary that was provided by
# %%source_rpm_name. This package should be rebuilt whenever %%source_rpm_name
# is updated or rebuilt in a way that is relevant for the boot loader.
#
# This way we don't need to duplicate the build dependencies and logic
# that is provided by the main systemd package.

BuildRequires:  systemd
BuildRequires:  %{source_rpm_name} = %{version}
BuildRequires:  pesign

ExclusiveArch:  %efi

Provides: systemd-boot-signed-%{efi_arch} = %version-%release
Provides: bundled(%{source_rpm_name}) = %(rpm -q --qf '%%{VERSION}-%%{RELEASE}' %{source_rpm_name})

# Obsolete the package with the version before the split to install all
# obsoleting packages on upgrades (i.e. systemd-udev, systemd-boot-unsigned,
# systemd-boot).
Obsoletes:      systemd-udev < 251~rc2-1

%description
systemd-boot (short: sd-boot) is a simple UEFI boot manager. It provides a
graphical menu to select the entry to boot and an editor for the kernel command
line. systemd-boot supports systems with UEFI firmware only.

This package contains the signed version that that works with Secure Boot.

Built from %(rpm -q %{source_rpm_name}).

%install
mkdir -p %{buildroot}%{_prefix}/lib/systemd/boot/efi
%pesign -s -i %{_prefix}/lib/systemd/boot/efi/systemd-boot%{efi_arch}.efi -o %{buildroot}%{_prefix}/lib/systemd/boot/efi/systemd-boot%{efi_arch}.efi.signed

install -m0644 -Dt %{buildroot}%{_licensedir}/%{name}/ %{_datadir}/licenses/systemd/LICENSE.LGPL2.1

%postun
# This part will need to be updated in bootctl first, and then here.
if [ $1 -ge 1 ] && bootctl is-installed &>/dev/null; then
  echo "Updating systemd-boot…"
  bootctl update || :
fi

%files
%license %{_licensedir}/%{name}/LICENSE.LGPL2.1
%dir %{_prefix}/lib/systemd
%dir %{_prefix}/lib/systemd/boot
%dir %{_prefix}/lib/systemd/boot/efi
%{_prefix}/lib/systemd/boot/efi/systemd-boot%{efi_arch}.efi.signed

# Man pages are provided by systemd-udev subpackage.
# If we copied them to this package, we'd need to either rename them
# or worry about file conflicts. Since it is very very unlikely that
# somebody will have this package installed but not the systemd-udev,
# let's not duplicate the page.

%changelog
%autochangelog
