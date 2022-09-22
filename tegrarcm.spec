Name:           tegrarcm
Version:        1.8
Release:        14%{?dist}
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
BuildRequires:  pkgconfig(cryptopp)


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
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.8-10
- Rebuilt for new cryptopp

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.8-5
- Rebuilt for cryptopp

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.8-3
- Rebuilt for cryptopp

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.8-1
- Update to 1.8

* Thu Feb 22 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.7-8
- Rebuilt for cryptopp-6.1.0

* Tue Feb 20 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.7-7
- Rebuild and minor spec update

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 20 2015 Nicolas Chauvet <kwizart@gmail.com> - 1.7-1
- Update to 1.7

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.6-1
- Update to 1.6

* Tue Apr 08 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.5-2
- Backport ODM_SECURE patch

* Tue Mar 04 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.5-1
- Update to 1.5

* Sat Oct 05 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4-1
- Update to 1.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 13 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.3-1
- Update to 1.3

* Sat Apr 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2-1
- Initial package

