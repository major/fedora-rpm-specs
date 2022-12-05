# Exclude privlibs
%global __provides_exclude_from ^%{_libdir}/gnome-builder
%global privlibs .*-private|libide|libgnome-builder-plugins
%global __requires_exclude ^(%{privlibs}).*\\.so.*

%global tarball_version %%(echo %{version} | tr '~' '.')

%global glib2_version 2.73.3
%global gtk4_version 4.7.1
%global json_glib_version 1.2.0
%global jsonrpc_glib_version 3.42.0
%global libpeas_version 1.34.0
%global template_glib_version 3.36.0
%global libgit2_glib_version 1.1.0
%global sysprof_version 3.46.0

Name:           gnome-builder
Version:        43.4
Release:        1%{?dist}
Summary:        IDE for writing GNOME-based software

# Note: Checked as of 3.20.2
#
# Most of GNOME Builder is licensed under the GPLv3+.
#
# Others are easy to identify
#
# The following files are MIT licensed:
#     - src/resources/css/markdown.css
#     - src/resources/js/marked.js
#
# The following files are licensed under the CC-BY-SA license:
#     - data/icons/
#
# The following files are licensed under the CC0 license:
#     - data/org.gnome.Builder.appdata.xml
#     - data/html-preview.png
License:        GPLv3+ and GPLv2+ and LGPLv3+ and LGPLv2+ and MIT and CC-BY-SA and CC0
URL:            https://wiki.gnome.org/Apps/Builder
Source0:        https://download.gnome.org/sources/%{name}/43/%{name}-%{tarball_version}.tar.xz

BuildRequires:  clang-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(dspy-1)
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= %{jsonrpc_glib_version}
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= %{libgit2_glib_version}
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(libpeas-1.0) >= %{libpeas_version}
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(sysprof-4) >= %{sysprof_version}
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(sysprof-ui-5) >= %{sysprof_version}
BuildRequires:  pkgconfig(template-glib-1.0) >= %{template_glib_version}
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  /usr/bin/appstream-util

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       jsonrpc-glib%{?_isa} >= %{jsonrpc_glib_version}
Requires:       libgit2-glib%{?_isa} >= %{libgit2_glib_version}
Requires:       libpeas%{?_isa} >= %{libpeas_version}
Requires:       libpeas-loader-python3%{?_isa} >= %{libpeas_version}
Requires:       libsysprof-ui%{?_isa} >= %{sysprof_version}
Requires:       template-glib%{?_isa} >= %{template_glib_version}

Requires:       flatpak-builder
Recommends:     clang
Recommends:     gnome-code-assistance
Recommends:     meson
Recommends:     python3-jedi
Recommends:     sysprof-agent

%description
Builder attempts to be an IDE for writing software for GNOME. It does not try
to be a generic IDE, but one specialized for writing GNOME software.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Dhelp=true
%meson_build

%install
%meson_install

%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gnome-builder/plugins/

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Builder.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Builder.desktop

%files -f gnome-builder.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-builder
%{_libdir}/gnome-builder/
%{_libexecdir}/gnome-builder-clang
%{_libexecdir}/gnome-builder-flatpak
%{_libexecdir}/gnome-builder-git
%{python3_sitelib}/gi/
%{_datadir}/applications/org.gnome.Builder.desktop
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder*.gschema.xml
%exclude %{_datadir}/gnome-builder/gir-1.0/
%{_datadir}/gnome-builder/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Builder*.svg
%{_metainfodir}/org.gnome.Builder.appdata.xml
%lang(en) %{_datadir}/doc/gnome-builder/en/

%files devel
%{_includedir}/gnome-builder*/
%{_libdir}/pkgconfig/gnome-builder-*.pc
%{_datadir}/gnome-builder/gir-1.0/

%changelog
* Thu Dec 01 2022 David King <amigadave@amigadave.com> - 43.4-1
- Update to 43.4 (#2149807)

* Wed Nov 23 2022 David King <amigadave@amigadave.com> - 43.3-1
- Update to 43.3

* Sat Oct 29 2022 David King <amigadave@amigadave.com> - 43.2-2
- Rebuild against vte

* Fri Oct 07 2022 Kalev Lember <klember@redhat.com> - 43.2-1
- Update to 43.2

* Tue Sep 27 2022 Kalev Lember <klember@redhat.com> - 43.1-1
- Update to 43.1

* Thu Sep 22 2022 Kalev Lember <klember@redhat.com> - 43.0-1
- Update to 43.0

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43~rc-2
- Enable d-spy support

* Tue Sep 20 2022 Kalev Lember <klember@redhat.com> - 43~rc-1
- Update to 43.rc

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 43~alpha1-2
- Re-enable webkit support

* Mon Aug 08 2022 Kalev Lember <klember@redhat.com> - 43~alpha1-1
- Update to 43.alpha1
- Switch to gtk4 and libsoup3
- Disable webkit support as we don't have gtk4-enabled webkitgtk yet

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 42.1-2
- Rebuilt for Python 3.11

* Thu Apr 21 2022 David King <amigadave@amigadave.com> - 42.1-1
- Update to 42.1 (#2077298)

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 42.0-1
- Update to 42.0 (#2061582)

* Tue Mar 08 2022 David King <amigadave@amigadave.com> - 42~rc1-1
- Update to 42.rc1

* Wed Feb 23 2022 David King <amigadave@amigadave.com> - 42~beta1-1
- Update to 42.beta1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42~alpha1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jan 08 2022 David King <amigadave@amigadave.com> - 42~alpha1-1
- Update to 42.alpha1

* Tue Dec 07 2021 Kalev Lember <klember@redhat.com> - 41.3-1
- Update to 41.3

* Sun Nov 28 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 41.1-3
- Rebuild for libgit2 1.3.x

* Thu Oct 07 2021 Tom Stellard <tstellar@redhat.com> - 41.1-2
- Rebuild for llvm-13.0.0

* Thu Sep 23 2021 Kalev Lember <klember@redhat.com> - 41.1-1
- Update to 41.1

* Wed Sep 08 2021 Kalev Lember <klember@redhat.com> - 41.0-1
- Update to 41.0

* Wed Aug 04 2021 Kalev Lember <klember@redhat.com> - 41~alpha1-1
- Update to 41.alpha1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.40.2-2
- Rebuilt for Python 3.10

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 3.40.2-1
- Update to 3.40.2

* Wed May 05 2021 Kalev Lember <klember@redhat.com> - 3.40.1-1
- Update to 3.40.1

* Fri Mar 26 2021 Kalev Lember <klember@redhat.com> - 3.40.0-2
- Rebuild to fix sysprof-capture symbols leaking into libraries consuming it

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 3.40.0-1
- Update to 3.40.0
- Don't disable python bytecompile errors
- Explicitly byte compile plugins python files

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 3.39.99-1
- Update to 3.39.99

* Fri Mar 05 2021 Kalev Lember <klember@redhat.com> - 3.39.92-2
- Rebuild

* Fri Mar 05 2021 Kalev Lember <klember@redhat.com> - 3.39.92-1
- Update to 3.39.92

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 3.39.90-1
- Update to 3.39.90

* Tue Feb 02 2021 Kalev Lember <klember@redhat.com> - 3.38.2-1
- Update to 3.38.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.38.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Tom Stellard <tstellar@redhat.com> - 3.38.1-3
- Rebuild for clang-11.1.0

* Tue Dec 29 09:15:46 CET 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.38.1-2
- Rebuild for libgit2 1.1.x

* Fri Oct 16 2020 Kalev Lember <klember@redhat.com> - 3.38.1-1
- Update to 3.38.1

* Sun Sep 13 2020 Kalev Lember <klember@redhat.com> - 3.38.0-2
- Rebuilt for libgladeui soname bump

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 3.38.0-1
- Update to 3.38.0

* Mon Sep 07 2020 Kalev Lember <klember@redhat.com> - 3.37.92-1
- Update to 3.37.92

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.37.90-1
- Update to 3.37.90

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.36.0-4
- Rebuilt for Python 3.9

* Fri May 22 2020 Kalev Lember <klember@redhat.com> - 3.36.0-3
- Rebuilt for libgladeui soname bump

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.36.0-2
- Rebuild for libgit2 1.0.0

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Tue Mar 03 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.35.91-2
- Rebuild for libgit2 0.99

* Mon Feb 17 2020 Kalev Lember <klember@redhat.com> - 3.35.91-1
- Update to 3.35.91

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.35.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Kalev Lember <klember@redhat.com> - 3.35.3-2
- Rebuilt for vala 0.48

* Tue Jan 07 2020 Kalev Lember <klember@redhat.com> - 3.35.3-1
- Update to 3.35.3

* Mon Oct 07 2019 Kalev Lember <klember@redhat.com> - 3.34.1-1
- Update to 3.34.1

* Sun Sep 29 2019 Kalev Lember <klember@redhat.com> - 3.34.0-2
- Rebuild for llvm 9.0

* Tue Sep 10 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Thu Sep 05 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Mon Aug 26 2019 Kalev Lember <klember@redhat.com> - 3.33.90-1
- Update to 3.33.90

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.33.3-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Kalev Lember <klember@redhat.com> - 3.33.3-1
- Update to 3.33.3

* Tue Jul 16 2019 Kalev Lember <klember@redhat.com> - 3.32.4-1
- Update to 3.32.4

* Wed Jun 12 2019 Kalev Lember <klember@redhat.com> - 3.32.3-1
- Update to 3.32.3

* Tue May 07 2019 Kalev Lember <klember@redhat.com> - 3.32.2-1
- Update to 3.32.2

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-4
- Buildrequires python3-sphinx_rtd_theme (fix build on Rawhide)

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 3.32.1-3
- Rebuild with Meson fix for #1699099

* Mon Apr 15 2019 Kalev Lember <klember@redhat.com> - 3.32.1-2
- appdata: Keep the app ID same as was in 3.30

* Thu Apr 11 2019 Kalev Lember <klember@redhat.com> - 3.32.1-1
- Update to 3.32.1

* Wed Mar 13 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-2
- Rebuilt against fixed atk (#1626575)

* Tue Feb 19 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Thu Feb 07 2019 Kalev Lember <klember@redhat.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Kalev Lember <klember@redhat.com> - 3.31.4-2
- Require libpeas-loader-python3 (#1671093)

* Thu Jan 10 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4
- Re-enable libide gtk-doc building
- Re-enable help building

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 3.31.1-2
- Rebuilt for vala 0.44

* Wed Oct 31 2018 Kalev Lember <klember@redhat.com> - 3.31.1-1
- Update to 3.31.1

* Wed Oct 31 2018 Kalev Lember <klember@redhat.com> - 3.30.2-1
- Update to 3.30.2
- Co-own gtksourceview styles directories

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Sat Sep 08 2018 Kalev Lember <klember@redhat.com> - 3.30.0-2
- Rebuilt against fixed atk (#1626575)

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.30.0-1
- Update to 3.30.0

* Mon Aug 06 2018 Kalev Lember <klember@redhat.com> - 3.28.4-3
- Rebuilt for vala 0.42

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.28.4-2
- Rebuild with fixed binutils

* Sat Jul 28 2018 Kalev Lember <klember@redhat.com> - 3.28.4-1
- Update to 3.28.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 3.28.3-2
- Rebuilt for Python 3.7

* Tue Jun 26 2018 Kalev Lember <klember@redhat.com> - 3.28.3-1
- Update to 3.28.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.28.2-2
- Rebuilt for Python 3.7

* Tue May 29 2018 Kalev Lember <klember@redhat.com> - 3.28.2-1
- Update to 3.28.2

* Tue Apr 10 2018 Kalev Lember <klember@redhat.com> - 3.28.1-1
- Update to 3.28.1

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Sun Mar 11 2018 Kalev Lember <klember@redhat.com> - 3.27.92-2
- Rebuilt for gspell 1.8

* Mon Mar 05 2018 Kalev Lember <klember@redhat.com> - 3.27.92-1
- Update to 3.27.92

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Kalev Lember <klember@redhat.com> - 3.27.90-1
- Update to 3.27.90

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.3-4
- Remove obsolete scriptlets

* Wed Dec 20 2017 Kalev Lember <klember@redhat.com> - 3.27.3-3
- Rebuilt for vala 0.40

* Tue Dec 19 2017 Kalev Lember <klember@redhat.com> - 3.27.3-2
- Filter private libgnome-builder-plugins.so from gnome-builder requires

* Tue Dec 19 2017 Kalev Lember <klember@redhat.com> - 3.27.3-1
- Update to 3.27.3

* Fri Nov 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.2-2
- Rebuild for LLVM5

* Wed Nov 01 2017 Kalev Lember <klember@redhat.com> - 3.26.2-1
- Update to 3.26.2

* Tue Oct 24 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.26.1-2
- Rebuild for LLVM 5.0

* Sun Oct 08 2017 Kalev Lember <klember@redhat.com> - 3.26.1-1
- Update to 3.26.1

* Wed Sep 13 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.25.92-1
- Update to 3.25.92

* Sun Aug 27 2017 Kalev Lember <klember@redhat.com> - 3.25.91-1
- Update to 3.25.91

* Fri Aug 25 2017 Kalev Lember <klember@redhat.com> - 3.25.90-3
- Rebuilt for libdevhelp soname bump

* Mon Aug 21 2017 Kalev Lember <klember@redhat.com> - 3.25.90-2
- Rebuilt for vala 0.38

* Tue Aug 15 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 3.25.5-1
- Update to 3.25.5

* Wed Jul 19 2017 Kalev Lember <klember@redhat.com> - 3.25.4-1
- Update to 3.25.4

* Tue Jul 18 2017 Kalev Lember <klember@redhat.com> - 3.25.3-1
- Update to 3.25.3
- Switch to meson build system
- Set minimum versions for various required libraries

* Sat Jul 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.25.2-3
- Rebuild for libgit2 0.26.x

* Tue Jun 13 2017 Kalev Lember <klember@redhat.com> - 3.25.2-2
- Filter private libraries, thanks to Yanko Kaneti for the patch

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 3.25.2-1
- Update to 3.25.2

* Thu May 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.24.2-2
- Rebuild clang/llvm-4

* Tue May 09 2017 Kalev Lember <klember@redhat.com> - 3.24.2-1
- Update to 3.24.2

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Fri Mar 24 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.24.0-3
- Rebuild for LLVM4

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-2
- Rebuilt for libdevhelp soname bump

* Mon Mar 20 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Fri Mar 17 2017 Kalev Lember <klember@redhat.com> - 3.23.92-1
- Update to 3.23.92
- Add Recommends: flatpak-builder for flatpak building

* Tue Feb 28 2017 Richard Hughes <rhughes@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Mon Feb 13 2017 Kalev Lember <klember@redhat.com> - 3.22.4-3
- Rebuilt for vala 0.36

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 3.22.4-2
- Rebuilt for libgit2 soname bump

* Thu Dec 22 2016 Kalev Lember <klember@redhat.com> - 3.22.4-1
- Update to 3.22.4

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.22.3-3
- Rebuild for Python 3.6

* Thu Dec 01 2016 Kalev Lember <klember@redhat.com> - 3.22.3-2
- Enable flatpak support

* Tue Nov 29 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.22.3-1
- Update to 3.22.3

* Wed Nov 02 2016 Kalev Lember <klember@redhat.com> - 3.22.2-1
- Update to 3.22.2

* Wed Oct 12 2016 Kalev Lember <klember@redhat.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 26 2016 Dan Horák <dan[at]danny.cz> - 3.22.0-3
- add missing BR

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-2
- Rebuilt for vala 0.34

* Tue Sep 20 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0
- Don't set group tags

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 3.21.91-1
- Update to 3.21.91

* Tue Aug 23 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.21.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 3.21.1-1
- Update to 3.21.1

* Thu Apr 28 2016 Igor Gnatenko <ignatenko@redhat.com> - 3.20.2-1
- Update to 3.20.2

* Thu Mar 24 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.20.0-1
- Update to 3.20.0

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.19.90-3
- Rebuilt for libgit2 0.24.0

* Mon Mar 07 2016 Kalev Lember <klember@redhat.com> - 3.19.90-2
- Rebuilt for vala 0.32

* Mon Feb 29 2016 Richard Hughes <rhughes@redhat.com> - 3.19.90-1
- Update to 3.19.90

* Fri Feb 19 2016 David King <amigadave@amigadave.com> - 3.19.4-5
- Rebuilt for libclang bump

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Adam Jackson <ajax@redhat.com> 3.19.4-3
- Rebuild for llvm 3.7.1 library split

* Wed Jan 27 2016 David King <amigadave@amigadave.com> - 3.19.4-2
- Fix build against pygobject3

* Wed Jan 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.19.4-1
- Update to 3.19.4

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 17 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.18.1-2
- Backport patches from upstream

* Thu Oct 15 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.18.1-1
- Update to 3.18.1

* Wed Sep 23 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.18.0-2
- Add python3-jedi to Recommends

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Thu Sep 17 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Sat Aug 29 2015 Kalev Lember <klember@redhat.com> - 3.16.3-7
- Backport more fixes for libgit2-glib API changes

* Sat Aug 29 2015 Kalev Lember <klember@redhat.com> - 3.16.3-6
- Drop unneeded uncrustify dependency
- Use make_install macro

* Thu Jul 30 2015 Igor Gnatenko <ignatenko@src.gnome.org> - 3.16.3-5
- Adopt to new API in libgit2-glib (0.23.0)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 13 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.16.3-3
- Remove ineffective local storage crash patch.
- Add patch to increase the max number of files.

* Mon Jun 01 2015 Michael Catanzaro <mcatanzaro@gnome.org> - 3.16.3-2
- Disable HTML5 local storage to avoid a crash.

* Mon May 18 2015  Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.16.3-1
- Update to 3.16.3

* Fri Apr 17 2015 David King <amigadave@amigadave.com> - 3.16.2-2
- Require a recent enough libgit2-glib (#1212804)

* Thu Apr 16 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.2-1
- Update to 3.16.2

* Tue Apr 14 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Tue Mar 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Thu Jan 29 2015 David King <amigadave@amigadave.com> - 3.15.4.1-2
- Add uncrustify Requires

* Fri Jan 23 2015 David King <amigadave@amigadave.com> - 3.15.4.1-1
- Initial packaging (#1185301)
