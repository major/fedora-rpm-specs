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
Release:        %autorelease
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

# https://gitlab.gnome.org/GNOME/gnome-builder/-/merge_requests/679
Patch0:         webkitgtk-2.39.5.patch

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
%autochangelog
