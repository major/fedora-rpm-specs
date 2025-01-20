Name:           pulseview
Version:        0.4.2
Release:        21%{?dist}
Summary:        Signal acquisition and analysis GUI for sigrok
# Combined GPLv3+ (libsigrok and libsigrokdecode) and GPLv2+ (pulseview)
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://www.sigrok.org
Source0:        %{url}/download/source/%{name}/%{name}-%{version}.tar.gz
# https://sigrok.org/gitweb/?p=pulseview.git;a=commitdiff;h=ae726b70a7ada9a4be5808e00f0c951318479684
Patch0:         pulseview-qt.patch
# Upstream commit ed643f0b4ac587204a5243451cda181ee1405d62
Patch1:         0001-Fix-broken-build-due-to-C-template-behind-C-linkage.patch
BuildRequires:  pkgconfig(libsigrokcxx) >= 0.5.2
BuildRequires:  pkgconfig(libsigrokdecode) >= 0.5.2
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
# https://bugzilla.redhat.com/show_bug.cgi?id=1819609
# needed for plugins that handle displaying SVG graphics
Requires:       qt5-qtsvg

%description
PulseView is an application for enabling data acquisition and analysis with
test and measurement devices such as logic analyzers, oscilloscopes,
mixed-signal devices, digital multimeters and sensors, etc. It uses sigrok
libraries under the hood.


%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DDISABLE_WERROR=True
%cmake_build

%install
%cmake_install

# Why you install appdata in bad location, you sigrok upstream?
mv %{buildroot}/%{_datadir}/metainfo %{buildroot}/%{_datadir}/appdata

desktop-file-validate \
	%{buildroot}/%{_datadir}/applications/org.sigrok.PulseView.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%doc README
%license COPYING
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}
%{_datadir}/applications/org.sigrok.PulseView.desktop
%{_datadir}/icons/hicolor/48x48/apps/pulseview.png
%{_datadir}/icons/hicolor/scalable/apps/pulseview.svg
%{_datadir}/appdata/org.sigrok.PulseView.appdata.xml

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.2-20
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 0.4.2-16
- Rebuilt for Boost 1.83

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.4.2-14
- Rebuilt for Boost 1.81

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.4.2-11
- Rebuilt for Boost 1.78

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.4.2-9
- Rebuilt for Boost 1.76

* Sun Aug 01 2021 Alexandru Gagniuc <mr.nuke.me[at]gmail[dot]com> - 0.4.2-8
- Add upstream patch to fix build error due to C++ template behind C linkage

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.4.2-5
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.4.2-2
- Rebuilt for Boost 1.73
- Replace qt5-devel with qt5-qtbase-devel, qt5-linguist, qt5-qtsvg-devel

* Wed Apr 01 2020 Dan Horák <dan[at]danny.cz> - 0.4.2-1
- updated to 0.4.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.4.1-2
- Rebuilt for Boost 1.69

* Wed Nov 28 2018 mrnuke <mr.nuke.me@gmail.com> - 0.4.1-1
- New and exciting PulseView 4.1 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Dan Horák <dan[at]danny.cz> - 0.4.0-9
- Fix FTBFS (#1556138)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.4.0-7
- Rebuilt for Boost 1.66

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-6
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4.0-3
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4.0-2
- Rebuilt for Boost 1.64

* Wed Jun 14 2017 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.4.0-1
- Update to PulseView 0.4.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 17 2017 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.3.0-3
- Work around build error with GCC6 due to crappy glibmm headers

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 13 2016 Till Maas <opensource@till.name> - 0.3.0-1
- Bring in zero-day upstream patches that fix build issues
- Use "license" macro instead of "doc" for COPYING

* Sat Feb 06 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.3.0-0
- Update to pulseview 0.3.0
- Bump libsigrokdecode-devel requirement to 0.4.0
- Replace libsigrok-devel dependency with libsigrok-cxx-devel
- Use pulseview.desktop file provided with the pulseview sources
- Call desktop-file-validate on pulseview.desktop file

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.2.0-9
- Rebuilt for Boost 1.60

* Thu Nov 12 2015 Kalev Lember <klember@redhat.com> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.2.0-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.2.0-5
- rebuild for Boost 1.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.2.0-2
- Rebuild for boost 1.57.0

* Sat Sep 20 2014 Dan Horák <dan[at]danny.cz> - 0.2.0-1
- Update to version 0.2.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.1.0-5
- Rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 0.1.0-3
- Rebuild for boost 1.54.0

* Mon May 06 2013 Alexandru Gagniuc mr.nuke.me[at]gmail[dot]com - 0.1.0-2
- Use {name} macro  instead of 'pulseview'
- Stop abusing wildcards in files section

* Wed Oct 10 2012 Alexandru Gagniuc mr.nuke.me[at]gmail[dot]com - 0.1.0-1
- Initial RPM release
