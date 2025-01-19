%global majorminor 1.0
%global date 20120405
# Avoid to emit gstreamer provides - rhbz#1184975
%undefine __gstreamer1_provides

Summary:       Broadcom Crystal HD device interface library
Name:          libcrystalhd
Version:       3.10.0
Release:       35%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2
URL:           http://www.broadcom.com/support/crystal-hd/
ExcludeArch:   s390 s390x

#Source:       http://www.broadcom.com/docs/support/crystalhd/crystalhd_linux_20100703.zip
# This tarball and README are inside the above zip file...
# Patch generated from http://git.linuxtv.org/jarod/crystalhd.git
Source0:       libcrystalhd-%{date}.tar.bz2
Source1:       README_07032010
# We're going to use even newer firmware for now
Source2:       bcm70012fw.bin
Source3:       bcm70015fw.bin
# LICENSE file is copy-n-pasted from http://www.broadcom.com/support/crystal_hd/
Source4:       LICENSE
Source5:       libcrystalhd-snapshot.sh
Patch0:        libcrystalhd-nosse2.patch
# https://patchwork2.kernel.org/patch/2247431/
Patch1:        crystalhd-gst-Port-to-GStreamer-1.0-API.patch

BuildRequires: gcc-c++
BuildRequires: autoconf automake libtool
BuildRequires: gstreamer1-devel >= %{majorminor}
BuildRequires: gstreamer1-plugins-base-devel >= %{majorminor}
BuildRequires: make
Requires:      crystalhd-firmware

%description
The libcrystalhd library provides userspace access to Broadcom Crystal HD
video decoder devices. The device supports hardware decoding of MPEG-2,
h.264 and VC1 video codecs, up to 1080p at 40fps for the first-generation
bcm970012 hardware, and up to 1080p at 60fps for the second-generation
bcm970015 hardware.

%package devel
Summary:       Development libs for libcrystalhd
Requires:      %{name} = %{version}-%{release}

%description devel
Development libraries needed to build applications against libcrystalhd.

%package -n crystalhd-firmware
Summary:       Firmware for the Broadcom Crystal HD video decoder
# Automatically converted from old format: Redistributable, no modification permitted - review is highly recommended.
License:       LicenseRef-Callaway-Redistributable-no-modification-permitted
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}

%description -n crystalhd-firmware
Firmwares for the Broadcom Crystal HD (bcm970012 and bcm970015)
video decoders.

%package -n gstreamer-plugin-crystalhd
Summary:       Gstreamer crystalhd decoder plugin
Requires:      %{name} = %{version}-%{release}
Requires:      gstreamer1-plugins-base

%description -n gstreamer-plugin-crystalhd
Gstreamer crystalhd decoder plugin

%prep
%setup -q -n libcrystalhd-%{date}
cp %{SOURCE1} %{SOURCE4} .
%ifnarch %{ix86} ia64 x86_64
%patch -P0 -p1 -b .nosse2
sed -i -e 's|-msse2||' linux_lib/libcrystalhd/Makefile
%endif
%patch -P1 -p1 -b .gst1

%build
pushd linux_lib/libcrystalhd/ > /dev/null 2>&1
sed -i -e 's|-D__LINUX_USER__|-D__LINUX_USER__ %{optflags}|' Makefile
%{make_build}
popd > /dev/null 2>&1

pushd filters/gst/gst-plugin/ > /dev/null 2>&1
sh autogen.sh || :

%configure
make %{?_smp_mflags} \
  CFLAGS="%{optflags} -I%{_builddir}/%{buildsubdir}/include -I%{_builddir}/%{buildsubdir}/linux_lib/libcrystalhd" \
  BCMDEC_LDFLAGS="%{?__global_ldflags} -L%{_builddir}/%{buildsubdir}/linux_lib/libcrystalhd -lcrystalhd"
popd > /dev/null 2>&1

%install
pushd linux_lib/libcrystalhd/ > /dev/null 2>&1
make install LIBDIR=%{_libdir} DESTDIR=$RPM_BUILD_ROOT
popd > /dev/null 2>&1

pushd filters/gst/gst-plugin/ > /dev/null 2>&1
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstbcmdec.{a,la}
popd > /dev/null 2>&1

rm -rf $RPM_BUILD_ROOT/lib/firmware/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/firmware/
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_prefix}/lib/firmware/
install -pm 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_prefix}/lib/firmware/

#Install udev rule
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/udev/rules.d
install -pm 0644 driver/linux/20-crystalhd.rules \
  $RPM_BUILD_ROOT%{_prefix}/lib/udev/rules.d


%ldconfig_scriptlets

%files
%doc README_07032010 LICENSE
%{_libdir}/libcrystalhd.so.*

%files devel
%dir %{_includedir}/libcrystalhd
%{_includedir}/libcrystalhd/*
%{_libdir}/libcrystalhd.so

%files -n crystalhd-firmware
%doc LICENSE
%{_prefix}/lib/udev/rules.d/20-crystalhd.rules
%{_prefix}/lib/firmware/bcm70012fw.bin
%{_prefix}/lib/firmware/bcm70015fw.bin

%files -n gstreamer-plugin-crystalhd
%{_libdir}/gstreamer-%{majorminor}/*.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.10.0-34
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-20
- Add missng cc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-15
- Add cflags/ldflags - rhbz#1411018

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 20 2016 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-13
- Fix perm on firmware files - rhbz#1321530

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 03 2015 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-11
- Avoid to emit gstreamer1 provides - rhbz#1184975

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.10.0-9
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 07 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-6
- Don't install udev rules in /etc/udev/rules.d - rhbz#979542

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.10.0-4
- Add patch to port to gstreamer 1.0 and update spec

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-2
- Fix build on non-SSE2 arches
- Install CrystalHD udev rule
- Clean spec file

* Thu Apr 05 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Jarod Wilson <jarod@redhat.com> - 3.5.1-1
- Update to v3.5.1, now with nv12 support

* Sun Jul 25 2010 Jarod Wilson <jarod@redhat.com> - 3.5.0-2
- Tarball had object files in it, clean them out before building

* Sat Jul 24 2010 Jarod Wilson <jarod@redhat.com> - 3.5.0-1
- Rebase to 07032010 crystalhd sources
- Large version-bump as driver and lib are now essentially 100%
  in sync with the Windows driver and lib
- Ship firmware, now that Broadcom has posted a redistribution,
  no modification license to cover it
- Build the gstreamer decoder plugin (will be moved to its own
  package sooner or later)

* Sun Apr 04 2010 Jarod Wilson <jarod@redhat.com> - 0.9.25-4
- Fix segfault on firmware upload

* Fri Mar 26 2010 Jarod Wilson <jarod@redhat.com> - 0.9.25-3
- Update to pre-0.9.26 libcrystalhd, which contains support
  for the new Broadcom BCM970015 Crystal HD decoder card

* Thu Mar 11 2010 Jarod Wilson <jarod@redhat.com> - 0.9.25-2
- Minor fixups to the as-yet-not-enabled firmware sub-package

* Wed Jan 06 2010 Jarod Wilson <jarod@redhat.com> - 0.9.25-1
- Initial package
