Name:           hackrf
Version:        2024.02.1
Release:        3%{?dist}
Summary:        HackRF Utilities

License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://greatscottgadgets.com/%{name}/
Source0:        https://github.com/greatscottgadgets/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

Patch0:         shebang.patch
Patch1:         static.patch

BuildRequires:  cmake
BuildRequires:  fftw3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libusbx-devel
BuildRequires:  systemd

# When the host software changes, we generally will also have to update the firmware.
Recommends:     %{name}-firmware = %{version}-%{release}

%description
Hardware designs and software for HackRF, a project to produce a low cost, open
source software radio platform.

NOTE: To upgrade to this release, you must update libhackrf and hackrf-tools on
your host computer.  You must also update firmware on your HackRF device.


%package devel
Summary:        Development files for %{name}
License:        BSD-3-Clause
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libusbx-devel

%description devel
Files needed to develop software against libhackrf.


%package doc
Summary:        Supplemental documentation for HackRF
License:        GPL-2.0-only
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Supplemental documentation for HackRF.  For more information, visit the project at
https://greatscottgadgets.com/hackrf


%package firmware
Summary:        Firmware for HackRF
License:        GPL-2.0-or-later
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description firmware
Firmware for HackRF.


%package hardware
Summary:        Hardware schematics / pcb layout for HackRF.
License:        CERN-OHL-P-2.0 AND GPL-2.0-only
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description hardware
Hardware schematics / pcb layout for HackRF.


%prep
%autosetup -p1

# Fix "plugdev" nonsense
sed -i -e 's/GROUP="@HACKRF_GROUP@"/ENV{ID_SOFTWARE_RADIO}="1"/g' host/libhackrf/53-hackrf.rules.in
sed -i -e 's/GROUP="plugdev"/ENV{ID_SOFTWARE_RADIO}="1"/g' host/libhackrf/53-hackrf.rules


%build
pushd host
%cmake \
  -DINSTALL_UDEV_RULES=on \
  -DUDEV_RULES_PATH:PATH=%{_udevrulesdir} \
  -DUDEV_RULES_GROUP=plugdev

%cmake_build
popd


%install
pushd host
%cmake_install
popd

# Docs, schematics, and firmware don't have any "make install", so do that manually.
mkdir -p %{buildroot}%{_docdir}/%{name} %{buildroot}%{_datadir}/%{name}
cp -a doc/* %{buildroot}%{_docdir}/%{name}
cp -a firmware-bin %{buildroot}%{_datadir}/%{name}
cp -a hardware %{buildroot}%{_datadir}/%{name}
(
  echo "Please see https://hackrf.readthedocs.io/en/latest/updating_firmware.html for"
  echo "instructions regarding updating the firmware on your HackRF device."
) > %{buildroot}%{_datadir}/%{name}/README-Fedora

%post
%{?ldconfig}
%udev_rules_update

%postun
%{?ldconfig}
%udev_rules_update


%files
%license COPYING
%doc Readme.md RELEASENOTES
%{_bindir}/hackrf_*
%{_libdir}/libhackrf.so.*
%{_udevrulesdir}/53-hackrf.rules

%files devel
%{_includedir}/libhackrf/hackrf.h
%{_libdir}/pkgconfig/libhackrf.pc
%{_libdir}/libhackrf.so

%files firmware
%{_datadir}/%{name}/README-Fedora
%{_datadir}/%{name}/firmware-bin

%files hardware
%{_datadir}/%{name}/hardware

%files doc
%{_docdir}/%{name}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2024.02.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2024.02.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 24 2024 Steven A. Falco <stevenfalco@gmail.com> - 2024.02.1-1
- Update to 2024.02.1

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.01.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.01.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.01.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 Steven A. Falco <stevenfalco@gmail.com> - 2023.01.1-4
- Do not build static subpackage

* Wed Feb 15 2023 Steven A. Falco <stevenfalco@gmail.com> - 2023.01.1-3
- HW and FW should be noarch

* Wed Feb 01 2023 Steven A. Falco <stevenfalco@gmail.com> - 2023.01.1-2
- Need new sources for 2023.01.1

* Wed Feb 01 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2023.01.1-1
- Update to 2023.01.1 (#2166397)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.09.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Steven A. Falco <stevenfalco@gmail.com> - 2022.09.1-6
- Update License

* Fri Dec 02 2022 Steven A. Falco <stevenfalco@gmail.com> - 2022.09.1-5
- Correct URLs
- Include fw / hw sub-packages

* Wed Nov 23 2022 Steven A. Falco <stevenfalco@gmail.com> - 2022.09.1-4
- Doc requires theme to bring in fonts, etc.

* Wed Nov 23 2022 Steven A. Falco <stevenfalco@gmail.com> - 2022.09.1-3
- Build doc package

* Tue Nov 22 2022 Steven A. Falco <stevenfalco@gmail.com> - 2022.09.1-2
- Remove F19 (and older) support
- Push/pop dirs for cmake

* Thu Nov 17 2022 Richard Shaw <hobbes1069@gmail.com> - 2022.09.1-1
- Update to 2022.09.1.
- Update license tag to SPDX format.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Scott K Logan <logans@cottsay.net> - 2018.01.1-8
- Resolve build issues due to CMake out-of-source build changes
- Re-arranged spec to better align to modern patterns
- Fix %%{_isa} in static subpackage dependency

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.01.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May  7 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 2018.01.1-1
- Update package to 2018.01.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.02.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Scott K Logan <logans@cottsay.net> - 2017.02.1-2
- Fix noarch dependency in doc package

* Thu Dec 14 2017 Sergey Avseyev <sergey.avseyev@gmail.com> - 2017.02.1-1
- Update package to 2017.02.1

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.07.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.07.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.07.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.07.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Scott K Logan <logans@cottsay.net> - 2015.07.2-1
- Update to 2015.07.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.08.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 23 2014 Scott K Logan <logans@cottsay.net> - 2014.08.1-1
- Initial package
