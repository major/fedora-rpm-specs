Name:           tegrarcm
Version:        1.8
Release:        %autorelease
Summary:        Send code to a Tegra device in recovery mode

# Most of the code here is BSD, except for the firmware in
# tegra20-miniloader.h and tegra30-miniloader.h, which is under
# specific licensing that is acceptable under the Fedora Binary
# Firmware Exception:
# https://fedoraproject.org/wiki/Licensing#Binary_Firmware
# See "LICENSE" for details.
License:        BSD and Redistributable, no modification permitted
URL:            https://github.com/NVIDIA/tegrarcm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

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
%setup -q
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
