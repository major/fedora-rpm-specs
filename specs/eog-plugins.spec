%global tarball_version %%(echo %{version} | tr '~' '.')

%global __provides_exclude_from ^%{_libdir}/eog/plugins/.*\\.so$

Name:           eog-plugins
Version:        44.1
Release:        2%{?dist}
Summary:        A collection of plugins for the eog image viewer

License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/EyeOfGnome/Plugins
Source0:        https://download.gnome.org/sources/%{name}/44/%{name}-%{tarball_version}.tar.xz

BuildRequires:  pkgconfig(champlain-gtk-0.12)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(eog)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgdata)
BuildRequires:  pkgconfig(libpeas-1.0)
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  python3-devel

Requires:       eog-plugin-exif-display%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-export-to-folder%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-fit-to-width%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-fullscreenbg%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-light-theme%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-map%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-maximize-windows%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-postasa%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-pythonconsole%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-send-by-mail%{?_isa} = %{version}-%{release}
Requires:       eog-plugin-slideshowshuffle%{?_isa} = %{version}-%{release}

%description
It's a collection of plugins for use with the Eye of GNOME Image Viewer.
The included plugins provide a map view for where the picture was taken,
display of Exif information, Zoom to fit, etc.

%package        data
Summary:        Common data required by plugins
BuildArch:      noarch
Requires:       eog
# Plugin removed in 42.alpha. No suitable replacement.
# https://gitlab.gnome.org/GNOME/eog-plugins/-/merge_requests/5
Obsoletes:      eog-plugin-hide-titlebar < 42~alpha-1

%description    data
Common files required by all plugins.

%package -n     eog-plugin-exif-display
Summary:        eog exif-display plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-exif-display
The eog exif-display plugin.

%package -n     eog-plugin-export-to-folder
Summary:        eog export-to-folder plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-export-to-folder
The eog export-to-folder plugin.

%package -n     eog-plugin-fit-to-width
Summary:        eog fit-to-width plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-fit-to-width
The eog fit-to-width plugin.

%package -n     eog-plugin-fullscreenbg
Summary:        eog fullscreenbg plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-fullscreenbg
The eog fullscreenbg plugin.

%package -n     eog-plugin-light-theme
Summary:        eog light-theme plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-light-theme
The eog light-theme plugin.

%package -n     eog-plugin-map
Summary:        eog map plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-map
The eog map plugin.

%package -n     eog-plugin-maximize-windows
Summary:        eog maximize-windows plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-maximize-windows
The eog maximize-windows plugin.

%package -n     eog-plugin-postasa
Summary:        eog postasa plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-postasa
The eog postasa plugin.

%package -n     eog-plugin-pythonconsole
Summary:        eog pythonconsole plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-pythonconsole
The eog pythonconsole plugin.

%package -n     eog-plugin-send-by-mail
Summary:        eog send-by-mail plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}

%description -n eog-plugin-send-by-mail
The eog send-by-mail plugin.

%package -n     eog-plugin-slideshowshuffle
Summary:        eog slideshowshuffle plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       eog%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}

%description -n eog-plugin-slideshowshuffle
The eog slideshowshuffle plugin.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%py_byte_compile %{__python3} %{buildroot}%{_libdir}/eog/plugins/

%find_lang %{name}

%files

%files data -f eog-plugins.lang
%license COPYING
%doc NEWS

%files -n eog-plugin-exif-display
%{_libdir}/eog/plugins/exif-display.plugin
%{_libdir}/eog/plugins/libexif-display.so
%{_metainfodir}/eog-exif-display.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.exif-display.gschema.xml

%files -n eog-plugin-export-to-folder
%dir %{_libdir}/eog/plugins/__pycache__/
%{_libdir}/eog/plugins/__pycache__/export-to-folder.*.pyc
%{_libdir}/eog/plugins/export-to-folder.plugin
%{_libdir}/eog/plugins/export-to-folder.py
%{_metainfodir}/eog-export-to-folder.appdata.xml
%{_datadir}/eog/plugins/export-to-folder/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.export-to-folder.gschema.xml

%files -n eog-plugin-fit-to-width
%{_libdir}/eog/plugins/fit-to-width.plugin
%{_libdir}/eog/plugins/libfit-to-width.so
%{_metainfodir}/eog-fit-to-width.appdata.xml

%files -n eog-plugin-fullscreenbg
%dir %{_libdir}/eog/plugins/__pycache__/
%{_libdir}/eog/plugins/__pycache__/fullscreenbg.*.pyc
%{_libdir}/eog/plugins/fullscreenbg.plugin
%{_libdir}/eog/plugins/fullscreenbg.py
%{_metainfodir}/eog-fullscreenbg.appdata.xml
%{_datadir}/eog/plugins/fullscreenbg/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.fullscreenbg.gschema.xml

%files -n eog-plugin-light-theme
%{_libdir}/eog/plugins/liblight-theme.so
%{_libdir}/eog/plugins/light-theme.plugin
%{_metainfodir}/eog-light-theme.appdata.xml

%files -n eog-plugin-map
%{_libdir}/eog/plugins/libmap.so
%{_libdir}/eog/plugins/map.plugin
%{_metainfodir}/eog-map.appdata.xml

%files -n eog-plugin-maximize-windows
%dir %{_libdir}/eog/plugins/__pycache__/
%{_libdir}/eog/plugins/__pycache__/maximize-windows.*.pyc
%{_libdir}/eog/plugins/maximize-windows.py
%{_libdir}/eog/plugins/maximize-windows.plugin
%{_metainfodir}/eog-maximize-windows.appdata.xml

%files -n eog-plugin-postasa
%{_libdir}/eog/plugins/libpostasa.so
%{_libdir}/eog/plugins/postasa.plugin
%{_metainfodir}/eog-postasa.appdata.xml

%files -n eog-plugin-pythonconsole
%{_libdir}/eog/plugins/pythonconsole.plugin
%{_libdir}/eog/plugins/pythonconsole/
%{_metainfodir}/eog-pythonconsole.appdata.xml
%{_datadir}/eog/plugins/pythonconsole/
%{_datadir}/glib-2.0/schemas/org.gnome.eog.plugins.pythonconsole.gschema.xml

%files -n eog-plugin-send-by-mail
%{_libdir}/eog/plugins/send-by-mail.plugin
%{_libdir}/eog/plugins/libsend-by-mail.so
%{_metainfodir}/eog-send-by-mail.appdata.xml

%files -n eog-plugin-slideshowshuffle
%dir %{_libdir}/eog/plugins/__pycache__/
%{_libdir}/eog/plugins/__pycache__/slideshowshuffle.*.pyc
%{_libdir}/eog/plugins/slideshowshuffle.plugin
%{_libdir}/eog/plugins/slideshowshuffle.py
%{_metainfodir}/eog-slideshowshuffle.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 44.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 04 2024 David King <amigadave@amigadave.com> - 44.1-1
- Update to 44.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 19 2023 David King <amigadave@amigadave.com> - 44.0-1
- Update to 44.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 08 2023 David King <amigadave@amigadave.com> - 42.3-1
- Update to 42.3

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 42.2-1
- Update to 42.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 25 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1

* Sun Mar 20 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Tue Mar 08 2022 David King <amigadave@amigadave.com> - 42~rc-1
- Update to 42.rc

* Mon Feb 14 2022 David King <amigadave@amigadave.com> - 42~alpha-1
- Update to 42.alpha

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 David King <amigadave@amigadave.com> - 3.26.8-1
- Update to 3.26.8

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 3.26.7-1
- Update to 3.26.7

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 3.26.6-1
- Update to 3.26.6

* Fri Sep 18 2020 Kalev Lember <klember@redhat.com> - 3.26.5-5
- Explicitly byte-compile python files using py_byte_compile macro
- Fix FTBFS (#1863485)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.5-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.26.5-1
- Update to 3.26.5

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.26.4-1
- Update to 3.26.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Kalev Lember <klember@redhat.com> - 3.26.3-1
- Update to 3.26.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.26.2-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Remove obsolete scriptlets

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 25 2017 Kalev Lember <klember@redhat.com> - 3.25.1-1
- Update to 3.25.1

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 3.16.6-1
- Update to 3.16.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.16.5-1
- Update to 3.16.5
- Don't set group tags

* Tue May 10 2016 Kalev Lember <klember@redhat.com> - 3.16.4-1
- Update to 3.16.4

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Kalev Lember <klember@redhat.com> - 3.16.3-1
- Update to 3.16.3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 28 2015 Kalev Lember <klember@redhat.com> - 3.16.2-1
- Update to 3.16.2

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 3.16.1-1
- Update to 3.16.1
- Use make_install macro

* Sat Jul 04 2015 Kalev Lember <klember@redhat.com> - 3.16.0-4
- Require libpeas-loader-python3 for Python 3 plugin support (#1226879)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 David King <amigadave@amigadave.com> - 3.16.0-2
- Rebuild for libgdata soname bump

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Tue Mar 17 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.92-1
- Update to 3.15.92

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.90-2
- Add new eog-plugin-maximize-windows plugin to the eog-plugins metapackage

* Tue Feb 17 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use pkgconfig for BuildRequires
- Update URL

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.92-1
- Update to 3.13.92

* Thu Sep 04 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-2
- Split each plugin into separate subpackage

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Apr 17 2014 Adam Williamson <awilliam@redhat.com> - 3.12.1-2
- rebuild for new libgdata

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.92-1
- Update to 3.11.92

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.4-4
- Rebuilt for cogl soname bump

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 3.11.4-3
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.11.4-2
- Build with Python 3

* Tue Jan 14 2014 Richard Hughes <rhughes@redhat.com> - 3.11.4-1
- Update to 3.11.4

* Mon Oct 28 2013 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Sat Aug 10 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-1
- Update to 3.9.5

* Fri Aug 09 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-3
- Rebuilt for cogl 1.15.4 soname bump

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Wed Mar 20 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Mon Mar 18 2013 Richard Hughes <rhughes@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Thu Feb 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.6.1-3
- Rebuilt for cogl soname bump

* Fri Jan 25 2013 Peter Robinson <pbrobinson@fedoraproject.org> 3.6.1-2
- Rebuild for new cogl

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Kalev Lember <kalevlember@gmail.com> - 3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 3.5.91-1
- Update to 3.5.91

* Tue Aug 28 2012 Matthias Clasen <mclasen@redhat.com> - 3.5.5-2
- Rebuild against new cogl/clutter

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.5-1
- Update to 3.5.5

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92
- Package the python console plugin

* Sat Mar 10 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-2
- Rebuild for new cogl

* Tue Mar  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Sun Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.90-1
- Update to 3.3.90

* Tue Jan 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.2-4
- Rebuild for cogl soname bump

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 27 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.2-2
- Rebuild for new clutter

* Tue Nov 22 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.2.2-1
- Update to 3.2.2

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Fri Apr 22 2011 Christopher Aillon <caillon@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.30.2-1
- Update to 2.30.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Wed Jul  7 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-2
- Rebuild against new libchamplain

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.91-1
- Update to 2.29.91

* Mon Feb 15 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.90-1
- Update to 2.29.90

* Wed Jan 13 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.5-1
- Update to 2.29.5

* Tue Sep 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Tue Sep  8 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Fri Aug 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-2
- Build verbosely

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Initial packaging
