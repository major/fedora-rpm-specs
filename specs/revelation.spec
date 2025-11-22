%global gettext_package revelation
%global glib2_version 2.52.0
%global gtk3_version 3.22

Name:           revelation
Version:        0.5.6
Release:        %autorelease
Summary:        A password manager for the GNOME desktop
License:        GPL-2.0-or-later
URL:            https://revelation.olasagasti.info
Source0:        https://github.com/mikelolasagasti/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-gobject-devel
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  gtk3-devel >= %{gtk3_version}
BuildRequires:  dconf-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  python3dist(pwquality)
BuildRequires:  python3dist(pycryptodomex)
BuildRequires:  python3dist(pwquality)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       python3-gobject
Requires:       python3dist(defusedxml)
Requires:       python3dist(pycryptodomex)
Requires:       python3dist(pwquality)
Requires:       dbus
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas
Requires:       gtk3%{?_isa} >= %{gtk3_version}
Requires:       hicolor-icon-theme

%description
Revelation is a password manager for the GNOME desktop, released under the GNU
GPL license. It stores all your accounts and passwords in a single, secure
place, and gives you access to it through a user-friendly graphical interface. 

%prep
%autosetup -p1

%build
%meson
%define __ninja_common_opts -v
%meson_build

%install
%meson_install
%find_lang %{gettext_package}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/info.olasagasti.revelation.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/info.olasagasti.revelation.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md TODO
%{_bindir}/*
%{_metainfodir}/*.metainfo.xml
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/??x??/mimetypes/gnome-mime-application-x-revelation.png
%{_datadir}/icons/hicolor/*/apps/info.olasagasti.%{name}*.*
%{python3_sitelib}/%{name}/
%{_datadir}/mime/packages/*
%{_datadir}/glib-2.0/schemas/info.olasagasti.revelation.gschema.xml

%changelog
%autochangelog
