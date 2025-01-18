# Filter provides for plugin .so files
%global __provides_exclude_from ^%{_libdir}/gedit/plugins/

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gedit-plugins
Version:        46.0
Release:        4%{?dist}
Summary:        Plugins for gedit

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/Gedit
Source0:        https://download.gnome.org/sources/%{name}/46/%{name}-%{tarball_version}.tar.xz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gedit) >= 46.0
BuildRequires:  pkgconfig(libpeas-1.0)

# this is a metapackage dragging in all the plugins
Requires:       gedit-plugin-bookmarks
Requires:       gedit-plugin-bracketcompletion
%if !0%{?rhel}
Requires:       gedit-plugin-charmap
%endif
Requires:       gedit-plugin-codecomment
Requires:       gedit-plugin-colorpicker
Requires:       gedit-plugin-drawspaces
%if !0%{?rhel}
Requires:       gedit-plugin-git
%endif
Requires:       gedit-plugin-joinlines
Requires:       gedit-plugin-multiedit
Requires:       gedit-plugin-sessionsaver
Requires:       gedit-plugin-smartspaces
Requires:       gedit-plugin-terminal
Requires:       gedit-plugin-textsize
Requires:       gedit-plugin-wordcompletion

%description
A collection of plugins for gedit.

%package data
Summary:        Common data required by plugins
Requires:       gedit
Requires:       python3-gobject
%description data
Common files required by all plugins.

%package -n     gedit-plugin-bookmarks
Summary:        gedit bookmarks plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-bookmarks
The gedit bookmarks plugin.

%package -n     gedit-plugin-bracketcompletion
Summary:        gedit bracketcompletion plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-bracketcompletion
The gedit bracketcompletion plugin.

%if !0%{?rhel}
%package -n     gedit-plugin-charmap
Summary:        gedit charmap plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       gucharmap-libs
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-charmap
The gedit charmap plugin.
%endif

%package -n     gedit-plugin-codecomment
Summary:        gedit codecomment plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-codecomment
The gedit codecomment plugin.

%package -n     gedit-plugin-colorpicker
Summary:        gedit colorpicker plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-colorpicker
The gedit colorpicker plugin.

%package -n     gedit-plugin-drawspaces
Summary:        gedit drawspaces plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-drawspaces
The gedit drawspaces plugin.

%if !0%{?rhel}
%package -n     gedit-plugin-git
Summary:        gedit git plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libgit2-glib
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-git
The gedit git plugin.
%endif

%package -n     gedit-plugin-joinlines
Summary:        gedit joinlines plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-joinlines
The gedit joinlines plugin.

%package -n     gedit-plugin-multiedit
Summary:        gedit multiedit plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-multiedit
The gedit multiedit plugin.

%package -n     gedit-plugin-sessionsaver
Summary:        gedit sessionsaver plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-sessionsaver
The gedit sessionsaver plugin.

%package -n     gedit-plugin-smartspaces
Summary:        gedit smartspaces plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-smartspaces
The gedit smartspaces plugin.

%package -n     gedit-plugin-terminal
Summary:        gedit terminal plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
Requires:       vte291
%description -n gedit-plugin-terminal
The gedit terminal plugin.

%package -n     gedit-plugin-textsize
Summary:        gedit textsize plugin
Requires:       %{name}-data = %{version}-%{release}
Requires:       libpeas-loader-python3%{?_isa}
%description -n gedit-plugin-textsize
The gedit textsize plugin.

%package -n     gedit-plugin-wordcompletion
Summary:        gedit wordcompletion plugin
Requires:       %{name}-data = %{version}-%{release}
%description -n gedit-plugin-wordcompletion
The gedit wordcompletion plugin.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
%if 0%{?rhel}
  -Dplugin_charmap=false \
  -Dplugin_git=false \
%endif
  %nil
%meson_build

%install
%meson_install

%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gedit/plugins/

%find_lang %{name} --with-gnome
%find_lang gedit --with-gnome

%check
[ -f ${RPM_BUILD_ROOT}%{_libdir}/gedit/plugins/terminal.py ]

# Empty files section for the metapackage to make sure it's created
%files

%files data -f %{name}.lang -f gedit.lang
%license COPYING
%doc README.md NEWS
%dir %{_libdir}/gedit/plugins/
%dir %{_libdir}/gedit/plugins/__pycache__/
%dir %{_datadir}/gedit/plugins/
%{_libdir}/gedit/plugins/gpdefs.*
%{_libdir}/gedit/plugins/__pycache__/gpdefs.*

%files -n gedit-plugin-bookmarks
%{_libdir}/gedit/plugins/bookmarks.plugin
%{_libdir}/gedit/plugins/libbookmarks.so
%{_metainfodir}/gedit-bookmarks.metainfo.xml

%files -n gedit-plugin-bracketcompletion
%{_libdir}/gedit/plugins/bracketcompletion.*
%{_libdir}/gedit/plugins/__pycache__/bracketcompletion.*
%{_metainfodir}/gedit-bracketcompletion.metainfo.xml

%if !0%{?rhel}
%files -n gedit-plugin-charmap
%{_libdir}/gedit/plugins/charmap
%{_libdir}/gedit/plugins/charmap.plugin
%{_metainfodir}/gedit-charmap.metainfo.xml
%endif

%files -n gedit-plugin-codecomment
%{_libdir}/gedit/plugins/codecomment.*
%{_libdir}/gedit/plugins/__pycache__/codecomment.*
%{_metainfodir}/gedit-codecomment.metainfo.xml

%files -n gedit-plugin-colorpicker
%{_libdir}/gedit/plugins/colorpicker.*
%{_libdir}/gedit/plugins/__pycache__/colorpicker.*
%{_metainfodir}/gedit-colorpicker.metainfo.xml

%files -n gedit-plugin-drawspaces
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.drawspaces.gschema.xml
%{_libdir}/gedit/plugins/drawspaces.plugin
%{_libdir}/gedit/plugins/libdrawspaces.so
%{_metainfodir}/gedit-drawspaces.metainfo.xml

%if !0%{?rhel}
%files -n gedit-plugin-git
%{_libdir}/gedit/plugins/git
%{_libdir}/gedit/plugins/git.plugin
%{_metainfodir}/gedit-git.metainfo.xml
%endif

%files -n gedit-plugin-joinlines
%{_libdir}/gedit/plugins/joinlines.*
%{_libdir}/gedit/plugins/__pycache__/joinlines.*
%{_metainfodir}/gedit-joinlines.metainfo.xml

%files -n gedit-plugin-multiedit
%{_libdir}/gedit/plugins/multiedit
%{_libdir}/gedit/plugins/multiedit.plugin
%{_metainfodir}/gedit-multiedit.metainfo.xml

%files -n gedit-plugin-sessionsaver
%{_datadir}/gedit/plugins/sessionsaver
%{_libdir}/gedit/plugins/sessionsaver
%{_libdir}/gedit/plugins/sessionsaver.plugin

%files -n gedit-plugin-smartspaces
%{_libdir}/gedit/plugins/libsmartspaces.so
%{_libdir}/gedit/plugins/smartspaces.plugin
%{_metainfodir}/gedit-smartspaces.metainfo.xml

%files -n gedit-plugin-terminal
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.terminal.gschema.xml
%{_libdir}/gedit/plugins/__pycache__/terminal.*
%{_libdir}/gedit/plugins/terminal.*
%{_metainfodir}/gedit-terminal.metainfo.xml

%files -n gedit-plugin-textsize
%{_libdir}/gedit/plugins/textsize
%{_libdir}/gedit/plugins/textsize.plugin
%{_metainfodir}/gedit-textsize.metainfo.xml

%files -n gedit-plugin-wordcompletion
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.wordcompletion.gschema.xml
%{_libdir}/gedit/plugins/libwordcompletion.so
%{_libdir}/gedit/plugins/wordcompletion.plugin
%{_metainfodir}/gedit-wordcompletion.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 46.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jan 28 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 46.0-1
- Update to 46.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 45.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 18 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 45.0-1
- Update to 45.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 44.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 17 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 44.1-1
- Update to 44.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 27 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1

* Mon Apr 25 2022 David King <amigadave@amigadave.com> - 42.0-2
- Use pkgconfig for BuildRequires

* Mon Apr 04 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0

* Wed Feb 16 2022 David King <amigadave@amigadave.com> - 41.0-1
- Update to 41.0

* Tue Feb 15 2022 David King <amigadave@amigadave.com> - 40.1-5
- Rebuilt for gedit soname change

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Adam Williamson <awilliam@redhat.com> - 40.1-3
- Rebuild for gedit soname bump

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 40.1-1
- Update to 40.1

* Tue Apr 20 2021 Kalev Lember <klember@redhat.com> - 40.0-2
- Avoid depending on tepl as it's unmainained upstream

* Wed Mar 24 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0
- Filter provides for plugin .so files

* Fri Feb 05 2021 Kalev Lember <klember@redhat.com> - 3.38.1-3
- Don't build gedit-plugin-charmap and gedit-plugin-git for RHEL

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Fri Sep 11 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Fri Sep 04 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92
- Explicitly byte-compile python files using py_byte_compile macro
- Fix FTBFS (#1863608)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Adam Williamson <awilliam@redhat.com> - 3.36.2-2
- Rebuild for new libgedit

* Fri Mar 27 2020 Kalev Lember <klember@redhat.com> - 3.36.2-1
- Update to 3.36.2

* Wed Mar 11 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Fri Mar 06 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Feb 04 2020 Kalev Lember <klember@redhat.com> - 3.35.90-1
- Update to 3.35.90
- Remove the zeitgeist plugin

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kalev Lember <klember@redhat.com> - 3.35.1-1
- Update to 3.35.1

* Wed Nov 27 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1
- Re-add synctex plugin

* Wed Sep 11 2019 Kalev Lember <klember@redhat.com> - 3.34.0-2
- Fix building with zeitgeist disabled

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Sun Aug 25 2019 Kalev Lember <klember@redhat.com> - 3.33.90-2
- Spec file cleanups after the meson port

* Thu Aug 08 2019 Phil Wyett <philwyett@kathenas.org> - 3.33.90-1
- Update to 3.33.90.
- This release removes 'synctex' plugin.
- This release adds new 'sessionsaver' plugin.
- Update 'zeitgeist' plugin conditonal. Fedora only, not in RHEL.
- Remove old patches.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.31.90-2
- Rebuilt for gtksourceview4

* Mon Feb 04 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4
- Drop gedit-plugin-dashboard as the plugin is removed upstream

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Thu Sep 06 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.28.1-2
- Rebuilt for Python 3.7

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.1-1
- Update to 3.27.1
- Add new translate plugin

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Ray Strode <rstrode@redhat.com> - 3.22.0-5
- Drop non-functional python2 support

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Don't set group tags
- Use make_install macro
- Update project URLs

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.1-1
- Update to 3.17.1
- Require gucharmap-libs instead of gucharmap

* Fri Jul 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.17.0-4
- Rebuilt for libgit2-0.23.0 and libgit2-glib-0.23

* Sat Jul 04 2015 Kalev Lember <klember@redhat.com> - 3.17.0-3
- Require libpeas-loader-python3 for Python 3 plugin support (#1226879)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.0-1
- Update to 3.17.0
- Include new findinfiles plugin

* Tue Mar 24 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Sat Mar 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.1-1
- Update to 3.15.1
- Use %%license macro for the COPYING file

* Sat Feb 21 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.0-1
- Update to 3.15.0

* Wed Nov 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Wed Nov 05 2014 Debarshi Ray <rishi@fedoraproject.org> - 3.14.0-2
- We need the new VTE API/ABI to run
- Carry an upstream patch to pick up a last-minute VTE API break

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 26 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2

* Thu Jul 24 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.1-1
- Update to 3.13.1

* Wed Jun 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.0-2
- Ship gpdefs in the -data package
- Build the zeitgeist plugin

* Wed Jun 25 2014 Richard Hughes <rhughes@redhat.com> - 3.13.0-1
- Update to 3.13.0

* Fri Jun 13 2014 Richard Hughes <rhughes@redhat.com> - 3.12.1-3
- Split out the plugins into subpackages
- This allows us to add and remove them separately in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Wed Mar 05 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Fri Feb 14 2014 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Wed Jan 15 2014 Richard Hughes <rhughes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Fri Dec 27 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.10.1-1
- Update to 3.10.1

* Tue Sep 24 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.10.0-1
- Update to 3.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.3-1
- Update to 3.8.3

* Sun May 26 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.2-1
- Update to 3.8.2

* Mon May  6 2013 Marek Kasik <mkasik@redhat.com> - 3.8.1-2
- Make building of Zeitgeist plugins and usage of python3 conditional

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-2
- Rebuilt for gtksourceview3 soname bump

* Mon Mar 25 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.0-1
- Update to 3.8.0

* Sun Jan 27 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.7.1-1
- Update to 3.7.1

* Tue Oct 16 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.6.1-1
- Update to 3.6.1

* Mon Sep 24 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.5.2-1
- Update to 3.5.2

* Sat Aug 18 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.5.1-1
- Update to 3.5.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-2
- Silence rpm scriptlet output

* Mon Mar 26 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 07 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.4-1
- Update to 3.3.4

* Sat Feb 25 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.3-1
- Update to 3.3.3

* Tue Feb 07 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.2-1
- Update to 3.3.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 03 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.1-1
- Update to 3.3.1

* Sun Oct 16 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.1-1
- Update to 3.2.1

* Mon Sep 26 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.0-1
- Update to 3.2.0
- Bump pygobject to 3.0

* Tue Sep 20 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.5-1
- Update to 3.1.5

* Tue Sep 06 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.4-1
- Update to 3.1.4

* Thu Sep 01 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.3-1
- Update to 3.1.3

* Tue Jul 05 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.2-1
- Update to 3.1.2

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Wed May 18 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.0.2-2
- Remove useless deps

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Wed Apr 13 2011 Christopher Aillon <caillon@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Wed Apr  6 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Sun Mar 27 2011 Christopher Aillon <caillon@redhat.com> - 2.91.3-1
- Update to 2.91.3

* Tue Mar  8 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.1-1
- Update to 2.91.1

* Mon Feb 28 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-3
- Rebuild against newer libpeas

* Thu Feb 24 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-2
- Add runtime dependencies to make introspection work

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.90-1
- Update to 2.91.90

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.31.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct  7 2010 Matthias Clasen <mclasen@redhat.com> 2.31.6-1
- Rebuild against newer gucharmap

* Thu Sep 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> 2.31.6-1
- Updated to 2.31.6
- FTBFS 599912

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.31.1-2
- recompiling .py files against Python 2.7 (rhbz#623308)

* Wed May 19 2010 Rakesh Pandit <rakesh@fedoraproject.org> 2.31.1-1
- Updated to 2.31.1

* Fri Apr 23 2010 Rakesh Pandit <rakesh@fedoraproject.org> 2.30.0-1
- Updated to 2.30.0

* Wed Jan 27 2010 Rakesh Pandit <rakesh@fedoraproject.org> 2.29.4-1
- Updated to 2.29.4

* Wed Dec 02 2009 Rakesh Pandit <rakesh@fedoraproject.org> 2.29.3-1
- Updated to 2.29.3

* Mon Nov 09 2009 Rakesh Pandit <rakesh@fedoraproject.org> 2.28.0-1
- Updated to 2.28.0

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 2.26.1-3
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Apr 11 2009 Dodji Seketeli <dodji@redhat.org> - 2.26.1-1
- Update to upstream release 2..26.1
- Fixes GNOME bugzilla bug #576766 - Crash when Configuring "Draw Spaces"
- Make sure to remove all *.la files
- Remove BuildRequire libgnomeui-devel as needless now

* Fri Apr 10 2009 Dodji Seketeli <dodji@redhat.org> - 2.26.0-1
- Update to upstream release (2.26.1)
- Add plugin files from %%{_datadir}
- Don't check for vte anymore, the package checks it pkg-config
- Add 'bookmarks' to the plugin set

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.22.3-3
- Rebuild for Python 2.6

* Mon Sep 29 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 2.22.3-2
- Fixed buildrequires

* Mon Sep 29 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 2.22.3-1
- Updated to 2.22.3

* Mon Sep 29 2008 Rakesh Pandit <rakesh@fedoraproject.org> - 2.22.0-2
- rebuild to pick latest gucharmap

* Tue Mar 18 2008 Trond Danielsen <trond.danielsen@gmail.com> - 2.22.0-1
- Updated.

* Mon Apr 30 2007 Trond Danielsen <trond.danielsen@gmail.com> - 2.18.0-2
- Disable buggy session saver plugin.
- Removed static libraries.

* Sun Apr 01 2007 Trond Danielsen <trond.danielsen@gmail.com> - 2.18.0-1
- Initial version.
