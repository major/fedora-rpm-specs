Name:           camorama
Version:        0.21.2
Release:        10%{?dist}
Summary:        Gnome webcam viewer
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/alessio/camorama
Source0:        https://linuxtv.org/downloads/camorama/camorama-%{version}.tar.gz
Patch0:		fix_crash_on_device_change.patch
BuildRequires:  gcc desktop-file-utils libappstream-glib
BuildRequires:  gettext-devel libv4l-devel gtk3-devel cairo-devel
BuildRequires:  gdk-pixbuf2-devel gnome-common make
Requires:       hicolor-icon-theme

%description
A simple Gnome webcam viewer, with the ability to apply some video effects.


%prep
%autosetup -p1

%build
./autogen.sh
%configure --prefix /usr
%make_build


%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%make_install
%find_lang %{name}

# below is the desktop file and icon stuff.
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml


%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md THANKS TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/camorama.desktop
%{_datadir}/icons/hicolor/*x*/devices/%{name}.png
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.21.2-9
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 24 2022 Mauro Carvalho Chehab <mchehab@kernel.org> - 0.21.2-1
- Fix a crash when device is changed while control window is open

* Thu Mar 24 2022 Mauro Carvalho Chehab <mchehab@kernel.org> - 0.21.2
- Bump to Version 0.21.2: better handle controls and sliders

* Sat Mar 19 2022 Mauro Carvalho Chehab <mchehab@kernel.org> - 0.21.1
- Bump to Version 0.21.1: fix image capture regression

* Thu Mar 10 2022 Mauro Carvalho Chehab <mchehab@kernel.org> - 0.21
- Bump to Version 0.21: lots of fixes and improvements

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Hans de Goede <hdegoede@redhat.com> - 0.20.7-5
- Fix FTBFS (rhbz#1799206)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org) - 0.20.7-1
- Bump to Version 0.20.7: bug fixes and support for zoom control added

* Tue Nov 20 2018 Hans de Goede <hdegoede@redhat.com> - 0.20.6-2
- Fix "Could not create directory '~/Webcam_Pictures'." error (rhbz#1650646)

* Fri Sep 21 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org) - 0.20.6-1
- Bump to Version 0.20.6: fix for stepwise cameras and adds device selection at GUI

* Wed Sep 19 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org) - 0.20.5-1
- Bump to Version 0.20.5, with GSettings and frame rate display

* Fri Sep  7 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org) - 0.20.3-1
- Bump to Version 0.20.3, with several bugs fixed and minor interface improvements

* Wed Sep  5 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org) - 0.20.2-1
- Bump to Version 0.20.2, fixing support for Wayland

* Mon Sep  3 2018 Mauro Carvalho Chehab <mchehab+samsung@kernel.org) - 0.20.1-1
- Bump to Version 0.20.1

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.19-22
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 28 2016 Hans de Goede <hdegoede@redhat.com> - 0.19-18
- Fix crash when adding filters on 64 bit systems (rhbz#1312662)
- Add appdata
- Add manpage (courtesy of Debian)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Richard Hughes <richard@hughsie.com> - 0.19-15
- Rebuilt for gdk-pixbuf2-xlib split

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Hans de Goede <hdegoede@redhat.com> - 0.19-11
- Remove no longer needed autoreconf call, %%configure from redhat-rpm-config
  >= 9.1.0-42 updates config.guess and config.sub for new architecture support

* Wed May  1 2013 Hans de Goede <hdegoede@redhat.com> - 0.19-10
- run autoreconf for aarch64 support (rhbz#925128)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 10 2011 Hans de Goede <hdegoede@redhat.com> - 0.19-6
- Fix building with latest glib2

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.19-5
- Rebuild for new libpng

* Wed Feb 09 2011 Hans de Goede <hdegoede@redhat.com> - 0.19-4
- Fix building with kernels >= 2.6.38

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 28 2009 Hans de Goede <hdegoede@redhat.com> 0.19-2
- Don't install gconf files during build (#507830)
- Add comments describing the patches (#507830)

* Tue Jun 23 2009 Hans de Goede <hdegoede@redhat.com> 0.19-1
- Initial Fedora package
