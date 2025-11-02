# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           accerciser
Version:        3.48.0
Release:        %autorelease
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
%autochangelog
