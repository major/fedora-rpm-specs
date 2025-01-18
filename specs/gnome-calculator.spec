%global gtksourceview_version 5.3.0
%global libadwaita_version 1.6~beta

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-calculator
Version:        47.1
Release:        2%{?dist}
Summary:        A desktop calculator

License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Calculator
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libmpc-devel
BuildRequires:  meson
BuildRequires:  mpfr-devel
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5) >= %{gtksourceview_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala
BuildRequires:  /usr/bin/appstream-util

Requires:       gtksourceview5%{?_isa} >= %{gtksourceview_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}

%description
gnome-calculator is a powerful graphical calculator with financial,
logical and scientific modes. It uses a multiple precision package
to do its arithmetic to give a high degree of accuracy.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name} --with-gnome --all-name


%check
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/org.gnome.Calculator.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.gnome.Calculator.desktop


%files -f %{name}.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gcalccmd
%{_bindir}/gnome-calculator
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GCalc-2.typelib
%{_libdir}/girepository-1.0/GCi-1.typelib
%{_libdir}/libgcalc-2.so.1*
%{_libdir}/libgci-1.so.0*
%{_libexecdir}/gnome-calculator-search-provider
%{_datadir}/applications/org.gnome.Calculator.desktop
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_datadir}/gnome-shell/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Calculator.*
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Calculator-symbolic.svg
%{_metainfodir}/org.gnome.Calculator.appdata.xml
%{_mandir}/man1/gnome-calculator.1*
%{_mandir}/man1/gcalccmd.1*

%files devel
%{_includedir}/gci-2/
%{_includedir}/gcalc-2/
%{_libdir}/libgcalc-2.so
%{_libdir}/libgci-1.so
%{_libdir}/pkgconfig/gcalc-2.pc
%{_libdir}/pkgconfig/gci-1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GCalc-2.gir
%{_datadir}/gir-1.0/GCi-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gcalc-2.deps
%{_datadir}/vala/vapi/gcalc-2.vapi
%{_datadir}/vala/vapi/gci-1.deps
%{_datadir}/vala/vapi/gci-1.vapi


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 47.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 17 2024 nmontero <nmontero@redhat.com> - 47.1-1
- Update to 47.1

* Mon Sep 16 2024 nmontero <nmontero@redhat.com> - 47.0-1
- Update to 47.0

* Sun Sep 01 2024 David King <amigadave@amigadave.com> - 47~rc-1
- Update to 47.rc

* Sun Aug 04 2024 David King <amigadave@amigadave.com> - 47~beta-1
- Update to 47.beta

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 47~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 David King <amigadave@amigadave.com> - 47~alpha-1
- Update to 47.alpha

* Tue May 07 2024 Nieves Montero <nmontero@redhat.com> - 46.1-1
- Update to 46.1

* Sat Mar 16 2024 David King <amigadave@amigadave.com> - 46.0-1
- Update to 46.0

* Mon Mar 04 2024 David King <amigadave@amigadave.com> - 46~rc-1
- Update to 46.rc

* Wed Feb 14 2024 David King <amigadave@amigadave.com> - 46~beta-1
- Update to 46.beta

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 David King <amigadave@amigadave.com> - 46~alpha-1
- Update to 46.alpha

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 19 2023 Kalev Lember <klember@redhat.com> - 45.0.2-1
- Update to 45.0.2

* Tue Sep 05 2023 Kalev Lember <klember@redhat.com> - 45.0.1-1
- Update to 45.0.1

* Thu Aug 17 2023 Kalev Lember <klember@redhat.com> - 45.0-1
- Update to 45.0

* Thu Aug 03 2023 Kalev Lember <klember@redhat.com> - 45~beta-1
- Update to 45.beta

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 45~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Kalev Lember <klember@redhat.com> - 45~alpha-1
- Update to 45.alpha

* Sat Mar 18 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Sun Mar 05 2023 David King <amigadave@amigadave.com> - 44~rc-1
- Update to 44.rc

* Thu Feb 16 2023 David King <amigadave@amigadave.com> - 44~alpha-1
- Update to 44.beta

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 43.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43.0.1-1
- Update to 43.0.1

* Tue Sep 06 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc
- Switch to libsoup3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 43~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Kalev Lember <klember@redhat.com> - 43~alpha-1
- Update to 43.alpha

* Wed Jul 06 2022 David King <amigadave@amigadave.com> - 42.2-1
- Update to 42.2

* Sun May 29 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1

* Sun Mar 20 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Tue Mar 08 2022 David King <amigadave@amigadave.com> - 42~rc-1
- Update to 42.rc

* Mon Feb 14 2022 David King <amigadave@amigadave.com> - 42~beta-1
- Update to 42.beta

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~alpha-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 David King <amigadave@amigadave.com> - 42~alpha-1
- Update to 42.alpha

* Tue Dec 07 2021 Kalev Lember <klember@redhat.com> - 41.1-1
- Update to 41.1

* Sat Sep 18 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41~rc-1
- Update to 41.rc

* Thu Aug 19 2021 Kalev Lember <klember@redhat.com> - 41~alpha-1
- Update to 41.alpha

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 40~beta-1
- Update to 40.beta
- Drop old gcalctool obsoletes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Mon Oct  5 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Fri Sep 11 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Sun Sep 06 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Mon Mar 02 2020 Kalev Lember <klember@redhat.com> - 3.35.92-1
- Update to 3.35.92

* Sun Feb 02 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 3.34.1-2
- Rebuild for mpfr 4

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.33.3-2
- Rebuilt for vala 0.46

* Tue Jun 18 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Tue May 21 2019 Kalev Lember <klember@redhat.com> - 3.33.2-1
- Update to 3.33.2
- Add new -devel subpackage

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-2
- Rebuild with Meson fix for #1699099

* Tue Apr 09 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Mon Feb 04 2019 Phil Wyett <philwyett@kathenas.org> - 3.31.90-1
- Update to 3.31.90

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.31.3-1
- Update to 3.31.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 3.29.90-1
- Update to 3.29.90

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1
- Switch to the meson build system

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Bastien Nocera <bnocera@redhat.com> - 3.26.0-3
+ gnome-calculator-3.26.0-3
- Fix reusing result in fr locales (#1536368)

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.0-2
- Remove obsolete scriptlets

* Thu Nov 02 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Fri Aug 25 2017 Kalev Lember <klember@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 3.25.2-1
- Update to 3.25.2

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92

* Tue Feb 28 2017 Richard Hughes <rhughes@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Mon Feb 13 2017 Richard Hughes <rhughes@redhat.com> - 3.23.4-1
- Update to 3.23.4

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 01 2016 Kalev Lember <klember@redhat.com> - 3.23.2-1
- Update to 3.23.2

* Sun Oct 30 2016 Kalev Lember <klember@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1
- Don't set group tags

* Tue Sep 20 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Kalev Lember <klember@redhat.com> - 3.21.92-1
- Update to 3.21.92

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Wed Jun 22 2016 Richard Hughes <rhughes@redhat.com> - 3.21.2-1
- Update to 3.21.2

* Sun May 08 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Tue Mar 01 2016 Richard Hughes <rhughes@redhat.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Wed Nov 25 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Sun Sep 20 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0
- Use make_install macro

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Sun Jun 21 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.2-1
- Update to 3.17.2

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 03 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.15.4-1
- Update license tag to GPLv3+

* Fri Jan 23 2015 David King <amigadave@amigadave.com> - 3.15.4-1
- Update to 3.15.4
- Update URL
- Update man page globs in files section
- Use pkgconfig for BuildRequires
- Remove obsolete glib2 dependencies for GSettings schema
- Validate AppData in check
- Preserve timestamps during install

* Fri Dec 19 2014 Richard Hughes <rhughes@redhat.com> - 3.15.1-1
- Update to 3.15.1

* Sun Oct 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-1
- Update to 3.13.3
- Drop an upstreamed patch
- Include new gnome-shell search provider

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu Apr 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Sat Mar 08 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Tue Feb 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.5-1
- Update to 3.11.5

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Thu Nov 14 2013 Richard Hughes <rhughes@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92
- Include the appdata file

* Wed Aug 28 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 3.9.4-1
- Update to 3.9.4

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.3-1
- Update to 3.9.3

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Mon Apr 15 2013 Richard Hughes <rhughes@redhat.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Fri Feb 22 2013 Adel Gadllah <adel.gadllah@gmail.com> - 3.7.90-2
- Bump obsolete (mass rebuild bumped the gcalcool nevr)

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.90-1
- Update to 3.7.90

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Wed Jan 16 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.4-2
- Fix keyword translations in desktop file

* Wed Jan 16 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.4-1
- Renamed package from gcalctool to gnome-calculator
