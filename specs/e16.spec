Summary:       The Enlightenment window manager, DR16
Name:          e16
Version:       1.0.30
Release:       3%{?dist}
# Automatically converted from old format: MIT with advertising and GPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-MIT-with-advertising AND GPL-2.0-or-later
URL:           http://www.enlightenment.org/
Source0:       http://downloads.sourceforge.net/enlightenment/e16-%{version}.tar.xz
BuildRequires: gcc
BuildRequires: imlib2-devel
BuildRequires: freetype-devel
BuildRequires: xorg-x11-xbitmaps
BuildRequires: libsndfile-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libXrandr-devel
BuildRequires: libSM-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: libXfixes-devel
BuildRequires: libXrender-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXft-devel
BuildRequires: libXxf86vm-devel
BuildRequires: pango-devel
BuildRequires: dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: make
Requires:      dejavu-sans-fonts

%description
Enlightenment is a window manager for the X Window System that is
designed to be powerful, extensible, configurable and pretty darned
good looking! It is one of the more graphically intense window
managers.

Enlightenment goes beyond managing windows by providing a useful and
appealing graphical shell from which to work. It is open in design and
instead of dictating a policy, allows the user to define their own
policy, down to every last detail.

This package will install the Enlightenment window manager, development
release 16.

%prep
%autosetup

%build
%configure --enable-pango   \
           --enable-mans    \
           --enable-modules \
           --enable-dbus \
           --enable-visibility-hiding
make %{?_smp_mflags} V=1
for f in ChangeLog AUTHORS ; do
    mv $f $f.iso88591
    iconv -o $f -f iso88591 -t utf8 $f.iso88591
    rm -f $f.iso88591
done

%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
rm -f %{buildroot}%{_libdir}/%{name}/libhack*.{a,la}
chmod 0644 %{buildroot}%{_datadir}/%{name}/themes/winter/ABOUT/MAIN

# Vera -> DejaVu
rm -f %{buildroot}%{_datadir}/%{name}/fonts/COPYRIGHT.Vera
rm -f %{buildroot}%{_datadir}/%{name}/fonts/*.ttf
ln -s ../../fonts/dejavu/DejaVuSans.ttf %{buildroot}%{_datadir}/%{name}/fonts/normal.ttf
ln -s ../../fonts/dejavu/DejaVuSans-Bold.ttf %{buildroot}%{_datadir}/%{name}/fonts/bold.ttf

# Remove unwanted files
find %{buildroot}%{_libdir}/e16 -name lib*.la -delete
rm -rf %{buildroot}%{_datadir}/doc/%{name}

# Desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Fix absolute symlink
rm %{buildroot}/%{_bindir}/starte16
ln -s ../share/e16/misc/starte16 %{buildroot}/%{_bindir}/starte16

%find_lang %{name}
%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog COMPLIANCE
%doc docs/e16.html
%{_bindir}/e*
%{_bindir}/starte16
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib*.so
%{_datadir}/%{name}
%{_datadir}/xsessions/*
%{_datadir}/gnome-session/sessions/%{name}-gnome.session
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.30-2
- convert license to SPDX

* Tue Aug 27 2024 Terje Rosten <terjeros@gmail.com> - 1.0.30-1
- 1.0.30

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Terje Rosten <terje.rosten@ntnu.no> - 1.0.29-1
- 1.0.29

* Sun Sep 10 2023 Terje Rosten <terje.rosten@ntnu.no> - 1.0.28-1
- 1.0.28

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Leigh Scott <leigh123linux@gmail.com> - 1.0.23-5
- Rebuild fo new imlib2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 04 2021 Terje Rosten <terje.rosten@ntnu.no> - 1.0.23-1
- 1.0.23
- Enable D-Bus support

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.0.21-1
- 1.0.21

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 14 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.0.19-1
- 1.0.19

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 25 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.0.18-1
- 1.0.18

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 02 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.0.17-1
- 1.0.17

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.0.16-1
- 1.0.16

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.0.13-1
- 1.0.13

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.0.11-1
- 1.0.11

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 19 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.0.10-1
- 1.0.10

* Sun Jul 10 2011 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.8-1
- 1.0.8

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.7-1
- 1.0.7

* Sun Feb 14 2010 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.2-1
- 1.0.2
- Add DSO patch

* Mon Dec 07 2009 Terje Rosten <terjeros@phys.ntnu.no> - 1.0.1-1
- 1.0.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.8.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.15-2
- More font work

* Thu Jan  8 2009 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.15-1
- 0.16.8.15

* Sun Dec 28 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.14-4
- Various hacks (fonts dir, %%pretrans) to make update smooth

* Sat Dec 27 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.14-3
- Use Dejavu fonts

* Thu Dec 25 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.14-2
- Fix bz #473646
- Move font req.

* Fri Aug 22 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.14-1
- 0.16.8.14

* Fri May  2 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.13-2
- Rebuild

* Fri May  2 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.13-1
- 0.16.8.13

* Thu Mar 27 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.12-3
- Disable dbus

* Mon Mar 24 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.12-2
- Really fix license

* Sun Mar 23 2008 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.12-1
- 0.16.8.12
- fix license (thanks spot and kevin!)
- enable dbus and pango
- simplity setup and modify desc
- try to preserve timestamps

* Wed Oct 17 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.10-1
- 0.16.8.10
- libhack has moved to e16 subdir

* Mon Sep 17 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.9-2
- Add GPLv2+ to license
- Add some X devel package to buildreq
- Fix encoding on ChangeLog and AUTHORS
- Use fonts included in bitstream-vera-fonts

* Mon Aug 20 2007 Terje Rosten <terjeros@phys.ntnu.no> - 0.16.8.9-1
- Initial build (based on upstream spec, thanks!)
