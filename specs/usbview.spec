Name:           usbview
Version:        3.1
Release:        5%{?dist}
Summary:        USB topology and device viewer
License:        GPL-2.0-only
URL:            http://www.kroah.com/linux-usb/
Source0:        http://www.kroah.com/linux-usb/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  ImageMagick
BuildRequires:  make
BuildRequires:  libappstream-glib
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
Requires:       gdk-pixbuf2-modules-extra
%endif
Requires:       hicolor-icon-theme

%description
Display information about the topology of the devices connected to the USB bus
on a Linux machine. It also displays detailed information on the individual
devices.


%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/com.kroah.usbview.metainfo.xml

%files
%license LICENSES/GPL-2.0-only.txt
%{_bindir}/usbview*
%{_mandir}/man8/usbview*
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*%{name}.desktop
%{_metainfodir}/com.kroah.usbview.metainfo.xml


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 24 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 3.1-4
- Update dependencies

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Vojtech Trefny <vtrefny@redhat.com> - 3.1-1
- New upstream release 3.1

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 FeRD (Frank Dana> <ferdnyc@gmail.com> - 3.0-1
- New upstream release

* Sat Jan 22 2022 Peter Robinson <pbrobinson@fedoraproject.org> - 2.2-1
- Update to 2.2 (fixes (CVE-2022-23220)
- Move to upstream desktop/polkit policy
- Use %%license
- Cleanup spec

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0-11
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 2.0-2
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Sat Apr  6 2013 Hans de Goede <hdegoede@redhat.com> - 2.0-1
- New upstream release 2.0
- Drop patches (all upstreamed)
- Fix usbview not working with newer kernels due to debugfs permission changes
  by using pxexec. Ideally usbview would be rewritten to use the public parts
  of sysfs instead.

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.1-10
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 14 2012 Hans de Goede <hdegoede@redhat.com> - 1.1-8
- Fix usbview not working due to missing usbfs (rhbz#806595)
- Port to gtk3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.1-6
- Rebuild for new libpng

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 15 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-4
- include --vendor fedora in desktop-file-install (required for EL-5)

* Fri Dec 11 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-3
- increasy usage of macros, fix icon permission

* Fri Dec 11 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-2
- install desktop icon

* Sun Nov 29 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.1-1
- Initial RPM for fedora

