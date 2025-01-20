Name: plug
Version: 1.4.5
Release: 5%{?dist}
Summary: Linux software for Fender Mustang amplifiers
License: GPL-3.0-or-later
Url: https://github.com/offa/plug

Source0: https://github.com/offa/plug/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: desktop-file-utils
# For unittests.
BuildRequires: gmock-devel


%description
Linux replacement for Fender FUSE software for Mustang amps.


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF

%cmake_build


%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Remove unwanted files.
rm -rf %{buildroot}%{_libdir}/cmake/plug


%check
make unittest -C %__cmake_builddir


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_udevrulesdir}/50-mustang.rules
%{_udevrulesdir}/70-mustang-*.rules
%{_datadir}/icons/hicolor/scalable/apps/mustang-plug.svg


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 12 2023 Dan Horák <dan[at]danny.cz> - 1.4.5-1
- Updated to 1.4.5 (rhbz#2253592)

* Tue Dec 05 2023 Dan Horák <dan[at]danny.cz> - 1.4.4-1
- Updated to 1.4.4
- Resolves: rbhz#2252689

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 01 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.3-3
- Add patch: fix_gcc_13_ftbfs.patch

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Phil Wyett <philip.wyett@kathenas.org> - 1.4.3-1
- New upstream version 1.4.3.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Dan Horák <dan[at]danny.cz> - 1.4.2-1
- Updated to 1.4.2 with new upstream

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Dan Horák <dan[at]danny.cz> - 1.2.1-1
- Updated to 1.2.1
- Switched to Qt5

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.1-19
- Better Qt dep, use %%license

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.1-13
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-11
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-6
- Change udev rules to be systemd conformant (See BZ 856002 comment 6)
- No longer created the plugdev group
- Drop unneeded README.Fedora file

* Sun Sep 30 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-5
- Change Group to Applications/System
- Untabify spec file
- Fix Source URL

* Sun Sep 23 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-4
- Remove BuildRequires for gcc-c++
- Use pkgconfig style BuildRequires for qt-devel

* Mon Sep 10 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-3
- Add patch to allow updating of firmware for Mustang III, IV, V models

* Sun Sep  9 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-2
- Add udev rules
- Add creation of group "plugdev" on package install
- Add README.Fedora file

* Sun Sep  9 2012 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 1.1-1
- Initial package

