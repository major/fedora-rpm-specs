%global gitcommit0 debbac012a3f67bd0864a0f4ad8bfe8e4e57844e

Name:           tegrarcm
Version:        1.9
Release:        %autorelease
Summary:        Send code to a Tegra device in recovery mode

# Most of the code here is BSD, except for the firmware in
# tegra20-miniloader.h and tegra30-miniloader.h, which is under
# specific licensing that is acceptable under the Fedora Binary
# Firmware Exception:
# https://fedoraproject.org/wiki/Licensing#Binary_Firmware
# See "LICENSE" for details.
License:        BSD-3-Clause AND LicenseRef-Fedora-Firmware
URL:            https://gitlab.com/grate-driver/tegrarcm
Source0:        %{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libtool

BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libcryptopp)


%description
This program is used to send code to a Tegra device in recovery mode.
It does not supported locked devices with an encrypted boot key, only
open devices such as the ventana, cardhu, or dalmore reference boards.
It is not capable of flashing firmware to a device, but can be used to
download firmware that is then capable of flashing.  For example in
ChromeOS tegrarcm is used to download a special build of u-boot to the
target Tegra device with a payload that it then flashes to the boot
device.


%prep
%autosetup -p1 -n %{name}-v%{version}-%{gitcommit0}
./autogen.sh


%build
%configure
%make_build


%install
%make_install


%files
%doc README
%license LICENSE
%{_bindir}/tegrarcm
%{_mandir}/man1/tegrarcm.1.*

%changelog
%autochangelog
