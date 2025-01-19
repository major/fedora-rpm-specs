Name:           libwebcam
Version:        0.2.5
Release:        19%{?dist}
Summary:        A library for user-space configuration of the uvcvideo driver
License:        LGPL-3.0-or-later
URL:            http://sourceforge.net/p/libwebcam/wiki/Home/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gengetopt
BuildRequires:  gcc
BuildRequires:  libxml2-devel


%description
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.


%package devel
Summary:        Development libraries and headers for libwebcam
Requires:       %{name} = %{version}-%{release}

%description devel
Development libraries and headers for libwebcam.


%package -n uvcdynctrl
Summary:        Command line interface to libwebcam
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
Requires:       %{name} = %{version}-%{release}
Requires:       uvcdynctrl-data = %{version}-%{release}

%description -n uvcdynctrl
Uvcdynctrl is a command line interface for manipulating settings in
UVC-type webcams. It uses the libwebcam library for webcam access.


%package -n uvcdynctrl-data
Summary:        XML control file for the uvcdynctrl package
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
Requires:       uvcdynctrl = %{version}-%{release}
BuildArch:      noarch

%description -n uvcdynctrl-data
XML control file for the uvcdynctrl package.


%prep
%setup -q -n %{name}-%{version}
# Remove backup file included in the archive by mistake
# https://sourceforge.net/p/libwebcam/discussion/general/thread/573c86ef22/
rm uvcdynctrl/data/046d/logitech.xml~


%build
%cmake
%cmake_build


%install
%cmake_install
rm $RPM_BUILD_ROOT%{_libdir}/libwebcam.a


%ldconfig_scriptlets


%files
%doc libwebcam/README libwebcam/COPYING.LESSER
%{_libdir}/libwebcam.so.*


%files devel
%{_includedir}/dynctrl-logitech.h
%{_includedir}/webcam.h
%{_libdir}/libwebcam.so
%{_libdir}/pkgconfig/libwebcam.pc


%files -n uvcdynctrl
%doc uvcdynctrl/README uvcdynctrl/COPYING
%{_bindir}/uvcdynctrl*
/lib/udev/uvcdynctrl
/lib/udev/rules.d/80-uvcdynctrl.rules
%{_mandir}/man1/uvcdynctrl*.1*


%files -n uvcdynctrl-data
%{_datadir}/uvcdynctrl


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.5-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.5-16
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Göran Uddeborg <goeran@uddeborg.se> - 0.2.4-13
- Remove backup file packaged in the tar file, BZ 2239034

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Michael Cronenworth <mike@cchtml.com> - 0.2.5-1
- version update

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Michael Cronenworth <mike@cchtml.com> - 0.2.2-5
- Add patch to remove deprecated V4L2 controls.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Hans de Goede <hdegoede@redhat.com> - 0.2.2-1
- New upstream release 0.2.2
- This fixes uvcdynctrl not working with recent kernels

* Thu Jan 05 2012 Michael Cronenworth <mike@cchtml.com> - 0.2.0-5.20100322svn
- Rebuilt for GCC 4.7

* Tue Feb 08 2011 Michael Cronenworth <mike@cchtml.com> - 0.2.0-4.20100322svn
- Update V4Lv1 patch for another usage case

* Tue Feb 08 2011 Michael Cronenworth <mike@cchtml.com> - 0.2.0-3.20100322svn
- Remove V4Lv1 header (removed in kernel 2.6.38+)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2.20100322svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 19 2010 Michael Cronenworth <mike@cchtml.com> - 0.2.0-1.20100322svn
- Initial package.
