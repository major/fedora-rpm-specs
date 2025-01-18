%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-backgrounds
Version:        47.0
Release:        2%{?dist}
Summary:        Desktop backgrounds packaged with the GNOME desktop

License:        CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/gnome-backgrounds
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  meson

# svg and jxl pixbuf loaders
Requires: (librsvg2 if gdk-pixbuf2)
Requires: (jxl-pixbuf-loader if gdk-pixbuf2)

%description
The gnome-backgrounds package contains the default
desktop background, known as the Adwaita background,
for the GNOME Desktop version

%package        extras
Summary:        Additional GNOME Backgrounds
Requires:       %{name} = %{version}-%{release}

%description    extras
This package contains the additional desktop backgrounds
which are packaged with the GNOME desktop.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/images

# all translations are merged back into xml by intltool
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/gnome-background-properties/adwaita.xml
%{_datadir}/gnome-background-properties/blobs.xml
%{_datadir}/gnome-background-properties/drool.xml
%{_datadir}/gnome-background-properties/pills.xml
%{_datadir}/backgrounds/gnome/adwaita-d.jxl
%{_datadir}/backgrounds/gnome/adwaita-l.jxl
%{_datadir}/backgrounds/gnome/blobs-d.svg
%{_datadir}/backgrounds/gnome/blobs-l.svg
%{_datadir}/backgrounds/gnome/drool-d.svg
%{_datadir}/backgrounds/gnome/drool-l.svg
%{_datadir}/backgrounds/gnome/pills-d.jxl
%{_datadir}/backgrounds/gnome/pills-l.jxl

%files extras
%{_datadir}/gnome-background-properties/amber.xml
%{_datadir}/gnome-background-properties/fold.xml
%{_datadir}/gnome-background-properties/geometrics.xml
%{_datadir}/gnome-background-properties/glass-chip.xml
%{_datadir}/gnome-background-properties/lcd.xml
%{_datadir}/gnome-background-properties/lcd-rainbow.xml
%{_datadir}/gnome-background-properties/map.xml
%{_datadir}/gnome-background-properties/mollnar.xml
%{_datadir}/gnome-background-properties/morphogenesis.xml
%{_datadir}/gnome-background-properties/neogeo.xml
%{_datadir}/gnome-background-properties/pixels.xml
%{_datadir}/gnome-background-properties/ring.xml
%{_datadir}/gnome-background-properties/sheet.xml
%{_datadir}/gnome-background-properties/swoosh.xml
%{_datadir}/gnome-background-properties/symbolic.xml
%{_datadir}/gnome-background-properties/symbolic-soup.xml
%{_datadir}/gnome-background-properties/tarka.xml
%{_datadir}/gnome-background-properties/vnc.xml
%{_datadir}/backgrounds/gnome/amber-d.jxl
%{_datadir}/backgrounds/gnome/amber-l.jxl
%{_datadir}/backgrounds/gnome/fold-d.jxl
%{_datadir}/backgrounds/gnome/fold-l.jxl
%{_datadir}/backgrounds/gnome/geometrics-d.jxl
%{_datadir}/backgrounds/gnome/geometrics-l.jxl
%{_datadir}/backgrounds/gnome/glass-chip-d.jxl
%{_datadir}/backgrounds/gnome/glass-chip-l.jxl
%{_datadir}/backgrounds/gnome/lcd-d.jxl
%{_datadir}/backgrounds/gnome/lcd-l.jxl
%{_datadir}/backgrounds/gnome/lcd-rainbow-d.jxl
%{_datadir}/backgrounds/gnome/lcd-rainbow-l.jxl
%{_datadir}/backgrounds/gnome/map-d.svg
%{_datadir}/backgrounds/gnome/map-l.svg
%{_datadir}/backgrounds/gnome/mollnar-d.svg
%{_datadir}/backgrounds/gnome/mollnar-l.svg
%{_datadir}/backgrounds/gnome/morphogenesis-d.svg
%{_datadir}/backgrounds/gnome/morphogenesis-l.svg
%{_datadir}/backgrounds/gnome/neogeo-d.jxl
%{_datadir}/backgrounds/gnome/neogeo-l.jxl
%{_datadir}/backgrounds/gnome/pixels-d.jxl
%{_datadir}/backgrounds/gnome/pixels-l.jxl
%{_datadir}/backgrounds/gnome/ring-d.jxl
%{_datadir}/backgrounds/gnome/ring-l.jxl
%{_datadir}/backgrounds/gnome/sheet-d.jxl
%{_datadir}/backgrounds/gnome/sheet-l.jxl
%{_datadir}/backgrounds/gnome/swoosh-d.jxl
%{_datadir}/backgrounds/gnome/swoosh-l.jxl
%{_datadir}/backgrounds/gnome/symbolic-d.png
%{_datadir}/backgrounds/gnome/symbolic-l.png
%{_datadir}/backgrounds/gnome/symbolic-soup-d.jxl
%{_datadir}/backgrounds/gnome/symbolic-soup-l.jxl
%{_datadir}/backgrounds/gnome/tarka-d.jxl
%{_datadir}/backgrounds/gnome/tarka-l.jxl
%{_datadir}/backgrounds/gnome/vnc-d.png
%{_datadir}/backgrounds/gnome/vnc-l.png

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Sun Aug 18 2024 David King <amigadave@amigadave.com> - 47~beta-1
- Update to 47.beta

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 19 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Wed Feb 14 2024 David King <amigadave@amigadave.com> - 46~beta-1
- Update to 46.beta

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 David King <amigadave@amigadave.com> - 46~alpha-1
- Update to 46.alpha

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Tue Sep 05 2023 Kalev Lember <klember@redhat.com> - 45~rc-1
- Update to 45.rc
- Remove webp-pixbuf-loader dep as webp images are no longer installed

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45~beta-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 David King <amigadave@amigadave.com> - 45~beta-1
- Update to 45.beta

* Mon Mar 20 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Fri Feb 17 2023 David King <amigadave@amigadave.com> - 44~beta-1
- Update to 44.beta

* Wed Feb 15 2023 David King <amigadave@amigadave.com> - 43.1-1
- Update to 43.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43-1
- Update to 43

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc

* Sat Aug 13 2022 Kalev Lember <klember@redhat.com> - 43~beta-1
- Update to 43.beta
- Add rich deps to pull in svg and webp pixbuf loaders (#2112390)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Thu Mar 10 2022 David King <amigadave@amigadave.com> - 42~beta-2
- Move some backgrounds to base package (#2062471)

* Wed Feb 16 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 41.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 13 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Tue Apr 13 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Thu Mar 18 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc
- Make -extras subpackage require the main package
- Drop move-adwaita-backgrounds.patch
- Remove old obsoletes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 14 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Tue Sep 01 2020 Kalev Lember <klember@redhat.com> - 3.37.92.1-1
- Update to 3.37.92.1
- Rebase move-adwaita-backgrounds.patch

* Tue Sep 01 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Kalev Lember <klember@redhat.com> - 3.37.2-1
- Update to 3.37.2

* Sun Mar 08 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Feb 18 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0
- Rebase move-adwaita-backgrounds.patch

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 15 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Tue Aug 01 2017 Kalev Lember <klember@redhat.com> - 3.25.4-1
- Update to 3.25.4
- Rebase move-adwaita-backgrounds.patch
- Switch to the meson build system

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Kalev Lember <klember@redhat.com> - 3.24.0-3
- Make sure both gnome-backgrounds and -extras get installed on upgrades
  (#1464555)

* Wed May 10 2017 Ryan Lerch <rlerch@redhat.com> - 3.24.0-2
- Split the package into gnome-backgrounds for the default adwaita background,
  and gnome-backgrounds-extras for the other standard GNOME wallpapers.

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 David King <amigadave@amigadave.com> - 3.23.91-1
- Update to 3.23.91
- Use make_build macro

* Tue Oct 04 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Wed Sep 21 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91
- Don't set group tags

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20-1
- Update to 3.20

* Mon Feb 22 2016 David King <amigadave@amigadave.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Thu Jun 25 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3
- Preserve timestamps during install

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91
- Use the %%license macro for the COPYING file

* Tue Feb 17 2015 Richard Hughes <rhughes@redhat.com> - 3.15.90-1
- Update to 3.15.90

* Sat Nov 29 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Wed Mar 27 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Tue Jan 15 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.4-1
- Update to 3.7.4

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Richard Hughes <hughsient@gmail.com> - 3.4.2-1
- Update to 3.4.2

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Mon Mar  5 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Sep  6 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.91-1
- Update to 3.1.91

* Wed Jun 15 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 Matthias Clasen <mclasen@redhat.com> 2.32.0-1
- Update to 2.32.0

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> 2.30.0-1
- Update to 2.30.0

* Tue Mar 09 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-1
- Update to 2.29.92

* Mon Mar  1 2010 Matthias Clasen <mclasen@redhat.com> - 2.28.0-2
- Drop ownership of a directory that is now owned by filesystem

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Sun Aug  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-3
- Co-own /usr/share/backgrounds instead of requiring desktop-backgrounds-basic

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Oct 28 2008 Lennart Poettering <lpoetter@redhat.com> - 2.24.0-3
- Include AUTHORS file in package

* Fri Oct 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-2
- Don't ship unneeded translations

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.0-1
- Update to 2.23.0

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Wed Aug 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.3-2
- Small fixes from package review

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.3-1
- Update to 2.18.3
- Update the license field

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.16.2-1
- Update to 2.16.2
- Require desktop-backgrounds-basic for directory ownership

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Mon Aug 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.92-1.fc6
- Update to 2.15.92

* Fri Jun  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2.1-3
- Add missing BuildRequires

* Thu Jun  1 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.2.1-2
- Update to 2.14.2.1

* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Mon Jan 31 2005 Matthias Clasen <mclasen@redhat.com> - 2.9.90-1
- Initial build.
