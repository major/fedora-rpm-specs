# Exclude privlibs
%global __provides_exclude_from ^%{_libdir}/gnome-builder
%global privlibs .*-private|libide|libgnome-builder-plugins
%global __requires_exclude ^(%{privlibs}).*\\.so.*

%global tarball_version %%(echo %{version} | tr '~' '.')

%global glib2_version 2.75.0
%global gtk4_version 4.15.5
%global json_glib_version 1.2.0
%global jsonrpc_glib_version 3.43.0
%global libadwaita_version 1.6~alpha
%global libdex_version 0.2
%global libpeas_version 1.99.0
%global libspelling_version 0.3.0
%global libgit2_glib_version 1.1.0
%global template_glib_version 3.36.1

Name:           gnome-builder
Version:        49.0
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
# Automatically converted from old format: GPLv3+ and GPLv2+ and LGPLv3+ and LGPLv2+ and MIT and CC-BY-SA and CC0 - review is highly recommended.
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY-SA AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Builder
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{tarball_version}.tar.xz

BuildRequires:  clang-devel
BuildRequires:  ctags
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  llvm-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:  pkgconfig(jsonrpc-glib-1.0) >= %{jsonrpc_glib_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libdex-1) >= %{libdex_version}
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= %{libgit2_glib_version}
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(libpeas-2) >= %{libpeas_version}
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libspelling-1) >= %{libspelling_version}
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(template-glib-1.0) >= %{template_glib_version}
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  /usr/bin/appstream-util

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk4%{?_isa} >= %{gtk4_version}
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       jsonrpc-glib%{?_isa} >= %{jsonrpc_glib_version}
Requires:       libadwaita%{?_isa} >= %{libadwaita_version}
Requires:       libdex%{?_isa} >= %{libdex_version}
Requires:       libgit2-glib%{?_isa} >= %{libgit2_glib_version}
Requires:       libpeas%{?_isa} >= %{libpeas_version}
Requires:       libpeas-loader-gjs%{?_isa} >= %{libpeas_version}
Requires:       libspelling%{?_isa} >= %{libspelling_version}
Requires:       template-glib%{?_isa} >= %{template_glib_version}

Requires:       flatpak-builder
Recommends:     clang
Recommends:     clang-tools-extra
Recommends:     ctags
Recommends:     meson
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
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Builder.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Builder.desktop

%files -f gnome-builder.lang
%doc NEWS README.md
%license COPYING
%{_bindir}/gnome-builder
%{_libdir}/gnome-builder/
%{_libexecdir}/gnome-builder-clang
%{_libexecdir}/gnome-builder-flatpak
%{_libexecdir}/gnome-builder-git
%{_datadir}/applications/org.gnome.Builder.desktop
%{_datadir}/dbus-1/services/org.gnome.Builder.service
%{_datadir}/glib-2.0/schemas/org.gnome.builder*.gschema.xml
%exclude %{_datadir}/gnome-builder/gir-1.0/
%{_datadir}/gnome-builder/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Builder*.svg
%{_metainfodir}/org.gnome.Builder.metainfo.xml
%lang(en) %{_datadir}/doc/gnome-builder/en/

%files devel
%{_includedir}/gnome-builder*/
%{_libdir}/pkgconfig/gnome-builder-*.pc
%{_datadir}/gnome-builder/gir-1.0/

%changelog
%autochangelog
