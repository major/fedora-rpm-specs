%global commit 60170bfe8de166b2947ea2d604506f0bdfa0565c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%ifarch x86_64
%global niarch x64
%endif
%ifarch %{ix86}
%global niarch x86
%endif
%ifarch %arm
%global niarch Arm
%endif


Name:           openni-primesense
Version:        5.1.6.6
Release:        29%{?gitrev}%{?dist}
Summary:        PrimeSensor/Kinect Modules for OpenNI
License:        Apache-2.0
URL:            https://github.com/PrimeSense/Sensor

Source0:        https://github.com/PrimeSense/Sensor/archive/%{commit}/Sensor-%{commit}.tar.gz
Source1:        openni-primesense-55-primesense-usb.rules
Patch0:         openni-primesense-5.1.6.6-fedora.patch
Patch1:         openni-primesense-5.1.6.6-willowgarage.patch
Patch2:         openni-primesense-5.1.6.6-sse.patch
Patch3:         openni-primesense-5.1.6.6-softfloat.patch
ExclusiveArch:  x86_64 %{arm}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  openni-devel >= 1.5.0.0
BuildRequires:  libjpeg-devel
BuildRequires:  systemd-rpm-macros
Requires:       openni >= 1.5.0.0
Requires:       udev
Requires(pre):  shadow-utils

%description
This modules enables OpenNI to make use of the PrimeSense, also known as
Kinect depth camera.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       openni-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n Sensor-%{commit}
%patch 0 -p0 -b .fedora
%patch 1 -p0 -b .willow
%patch 2 -p0 -b .sse
%patch 3 -p0 -b .softfloat

rm -rf Source/External/LibJPEG
rm -rf Platform/Android Platform/Win32

%build
cd Platform/Linux/CreateRedist
# Add SSE_GENERATION=2 (or 3) to enable SSE
sed -i 's|make -j$(calc_jobs_number) -C ../Build|make -C ../Build CFLAGS_EXT="%{optflags} -Wno-unknown-pragmas" LDFLAGS_EXT="%{optflags}" DEBUG=1|' RedistMaker
./RedistMaker


%install
rm -rf $RPM_BUILD_ROOT
pushd Platform/Linux/Redist/Sensor-Bin-Linux-%{niarch}-v%{version}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/
mkdir -p $RPM_BUILD_ROOT%{_udevrulesdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir}/ \
INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir}/ \
INSTALL_ETC=$RPM_BUILD_ROOT%{_sysconfdir}/openni/primesense/ \
SERVER_LOGS_DIR=$RPM_BUILD_ROOT%{_var}/log/primesense/ \
INSTALL_RULES=$RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/ \
./install.sh -n
popd

#mkdir $RPM_BUILD_ROOT%{_bindir}
#install -p -m 0755 Platform/Linux/Redist/Sensor-Bin-Linux-%{niarch}-v%{version}/Bin/XnSensorServer $RPM_BUILD_ROOT%{_bindir}/XnSensorServer

rm -rf $RPM_BUILD_ROOT%{_var}/log/primesense

rm $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/55-primesense-usb.rules
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_udevrulesdir}/55-primesense-usb.rules


%pre
getent group primesense >/dev/null || groupadd -r primesense
exit 0

%post
/sbin/ldconfig
if [ $1 == 1 ]; then
  niReg -r %{_libdir}/libXnDeviceSensorV2.so
  niReg -r %{_libdir}/libXnDeviceFile.so
fi


%preun
if [ $1 == 0 ]; then
  niReg -u %{_libdir}/libXnDeviceSensorV2.so
  niReg -u %{_libdir}/libXnDeviceFile.so
fi


%postun -p /sbin/ldconfig


%files
%doc LICENSE 
%dir %{_sysconfdir}/openni/primesense
%config(noreplace) %{_sysconfdir}/openni/primesense/*
%{_udevrulesdir}/55-primesense-usb.rules
%{_libdir}/*.so
%{_bindir}/XnSensorServer

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 03 2024 Scott K Logan <logans@cottsay.net> - 5.1.6.6-27
- Disable parallelism in makefile to avoid an unknown bug
- Switch to new patch macro syntax
- Drop unused BuildDepends: dos2unix
- Switch to SPDX license identifier
- Disable i686 build due to missing upstream openni-devel

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Rich Mattes <richmattes@gmail.com> - 5.1.6.6-17
- Install udev rules to udevrulesdir (rhbz#1602381)
- Add a primesense group, and lock down udev rules for only primesense group members (rhbz#1226700)

* Thu Apr 23 2020 Rich Mattes <richmattes@gmail.com> - 5.1.6.6-16
- Remove Python BuildRequires (rhbz#1808332)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.1.6.6-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.1.6.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Rich Mattes <richmattes@gmail.com> - 5.1.6.6-1
- Update to release 5.1.6.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 5.0.3.3-5
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 5.0.3.3-4
- rebuild against new libjpeg

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Tim Niemueller <tim@niemueller.de> - 5.0.3.3-1
- Drop git suffix, we package a stable version
- Update udev file not to use deprecated SYSFS entries

* Mon Dec 19 2011 Tim Niemueller <tim@niemueller.de> - 5.0.3.3-0.2.git342e334c
- Disable SSE

* Thu Sep 01 2011 Tim Niemueller <tim@niemueller.de> - 5.0.3.3-0.1.git342e334c
- Update to 5.0.3.3, closer to upstream, including Willow Garage patch

* Mon Jun 27 2011 Rex Dieter <rdieter@fedoraproject.org> 5.0.0.25-0.5.git894cea01
- ExclusiveArch: %%ix86 x86_64 (#709720)

* Thu Mar 03 2011 Tim Niemueller <tim@niemueller.de> - 5.0.0.25-0.4.git894cea01
- Exclude arch ppc64 (openni not available)

* Sat Feb 26 2011 Tim Niemueller <tim@niemueller.de> - 5.0.0.25-0.3.git894cea01
- BuildRequire libjpeg-devel

* Sat Feb 19 2011 Tim Niemueller <tim@niemueller.de> - 5.0.0.25-0.2.git894cea01
- Fix version number according to guidelines
- Fix line endings of license file
- Do not package meaningless README file
- Use only SYSFS and not both, SYSFS and ATTRS in udev rules
- Remove jpeg lib coming with the package in setup phase, add according patch

* Thu Jan 20 2011 Tim Niemueller <tim@niemueller.de> - 5.0.0.25-0.1.git894cea01
- Initial revision
