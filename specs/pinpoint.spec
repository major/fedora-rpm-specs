Name:           pinpoint
Version:        0.1.8
Release:        22%{?dist}
Summary:        A tool for making hackers do excellent presentations

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Apps/Pinpoint
Source0:        https://download.gnome.org/sources/pinpoint/0.1/pinpoint-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  clutter-devel >= 1.4
BuildRequires:  clutter-gst3-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  glib2-devel
BuildRequires:  librsvg2-devel

%description
Pinpoint a simple presentation tool that hopes to avoid audience death
by bullet point and instead encourage presentations containing
beautiful images and small amounts of concise text in slides.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%license COPYING
%doc AUTHORS NEWS README introduction.pin *.jpg
%{_bindir}/pinpoint
%{_datadir}/pinpoint


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.8-21
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 0.1.8-1
- Update to 0.1.8
- Update URL

* Sat Aug 08 2015 Till Maas <opensource@till.name> - 0.1.6-2
- Fix --ignore-comments

* Tue Jul 28 2015 Kalev Lember <klember@redhat.com> - 0.1.6-1
- Update to 0.1.6
- Build with clutter-gst3
- Use license macro for COPYING

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Feb 23 2014 Richard Hughes <rhughes@redhat.com> - 0.1.4-19
- Rebuilt against clutter-gst2 rather than the old clutter-gst

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.4-18
- Rebuilt for cogl soname bump

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 0.1.4-17
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.4-16
- Rebuilt for cogl soname bump

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 0.1.4-15
- Rebuilt for cogl 1.15.4 soname bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Paul W. Frields <stickster@gmail.com> - 0.1.4-13
- Fix racy video, finally (#842063, #952798)

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 0.1.4-12
- Rebuilt for cogl soname bump

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.4-11
- Rebuild for new cogl

* Wed Sep 12 2012 Bastien Nocera <bnocera@redhat.com> 0.1.4-10
- Rebuild against new cogl

* Tue Aug 21 2012 Paul W. Frields <stickster@gmail.com> - 0.1.4-9
- Rebuild against udpated clutter-gst
- Fix upgrade path F17 to F18

* Fri Aug 17 2012 Paul W. Frields <stickster@gmail.com> - 0.1.4-8
- Rebuild for new cogl

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 20 2012 Paul W. Frields <stickster@gmail.com> - 0.1.4-6
- Rebuild for new cogl

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Paul W. Frields <stickster@gmail.com> - 0.1.4-4
- Rebuild for new clutter-glx/cogl

* Tue Nov 15 2011 Paul W. Frields <stickster@gmail.com> - 0.1.4-3
- Add introduction.pin to package for example purposes

* Tue Nov 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.4-2
- add rsvg support for embedded SVG support

* Tue Nov 15 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4
- http://ftp.gnome.org/pub/GNOME/sources/pinpoint/0.1/pinpoint-0.1.4.news

* Sat Jun 11 2011 Paul W. Frields <stickster@gmail.com> - 0.1.2-1
- Initial RPM package

