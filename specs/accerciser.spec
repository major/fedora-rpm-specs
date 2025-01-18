# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           accerciser
Version:        3.44.1
Release:        2%{?dist}
Summary:        Interactive Python accessibility explorer for the GNOME desktop

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://wiki.gnome.org/Apps/Accerciser
Source0:        https://download.gnome.org/sources/accerciser/%{release_version}/accerciser-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3
BuildRequires:  python3-devel

Requires:       libwnck3
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-ipython-console
Requires:       python3-pyatspi
Requires:       python3-xlib

%description
Accerciser is an interactive Python accessibility explorer for the GNOME
desktop. It uses AT-SPI to inspect and control widgets, allowing you to check
if an application is providing correct information to assistive technologies
and automated test frameworks. Accerciser has a simple plugin framework which
you can use to create custom views of accessibility information.


%prep
%autosetup -p1


%build
export PYTHON=%{python3}
%meson
%meson_build


%install
%meson_install

%find_lang accerciser --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/accerciser.desktop


%files -f accerciser.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/accerciser
%{python3_sitelib}/accerciser/
%{_datadir}/accerciser/
%{_datadir}/applications/accerciser.desktop
%{_datadir}/glib-2.0/schemas/org.a11y.Accerciser.gschema.xml
%{_datadir}/gnome-shell/extensions/accerciser@accerciser.gnome.org/
%{_datadir}/icons/hicolor/*/apps/accerciser.png
%{_datadir}/icons/hicolor/scalable/apps/accerciser.svg
%{_datadir}/icons/hicolor/symbolic/apps/accerciser-symbolic.svg
%{_metainfodir}/org.gtk.accerciser.metainfo.xml
%{_mandir}/man1/accerciser.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.44.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 30 2024 David King <amigadave@amigadave.com> - 3.44.1-1
- Update to 3.44.1

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.42.0-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.42.0-4
- Rebuilt for Python 3.13

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Kalev Lember <klember@redhat.com> - 3.42.0-1
- Update to 3.42.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 3.40.0-3
- Rebuilt for Python 3.12

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 29 2022 Kalev Lember <klember@redhat.com> - 3.40.0-1
- Update to 3.40.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.39.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.39.1-3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.39.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Kalev Lember <klember@redhat.com> - 3.39.1-1
- Update to 3.39.1
- Use make_build macro

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.38.0-3
- Rebuilt for Python 3.10

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Kalev Lember <klember@redhat.com> - 3.37.1-1
- Update to 3.37.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.36.1-2
- Rebuilt for Python 3.9

* Sat Apr 25 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Thu Mar 05 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Wed Feb 12 2020 Kalev Lember <klember@redhat.com> - 3.34.4-1
- Update to 3.34.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.34.3-2
- Add missing python3-xlib dependency (#1788638)

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.34.3-1
- Update to 3.34.3

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.2-1
- Update to 3.34.2

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Sat Sep 07 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Wed Aug 21 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.33.4-2
- Rebuilt for Python 3.8

* Mon Aug 12 2019 Kalev Lember <klember@redhat.com> - 3.33.4-1
- Update to 3.33.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Thu May 09 2019 Kalev Lember <klember@redhat.com> - 3.33.2-1
- Update to 3.33.2

* Sun Apr 07 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Sat Mar 23 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.22.0-7
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.22.0-5
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.22.0-2
- Rebuild for Python 3.6

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Use make_install macro
- Use license macro for COPYING

* Tue Oct 04 2016 Kalev Lember <klember@redhat.com> - 3.14.0-6
- Update project URLs (#1380982)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Wed Mar 19 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92.1-1
- Update to 3.11.92.1

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Tue Mar 04 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.8.2-1
- Update to 3.8.2

* Wed Apr 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-2
- Update the dependencies for python3
- Add HighContrast icons and scriptlets

* Tue Mar 26 2013 Richard Hughes <rhughes@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Mon Mar 18 2013 Richard Hughes <rhughes@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 3.7.4-1
- Update to 3.7.4

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.3-1
- Update to 3.7.3

* Tue Nov 13 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.2-1
- Update to 3.6.2

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Thu Aug 30 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.90-2
- Update the runtime deps for ipython package rename

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.90-1
- Update to 3.5.90

* Tue Aug 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.1-1
- Initial RPM release
