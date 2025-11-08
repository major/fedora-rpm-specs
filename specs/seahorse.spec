%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           seahorse
Version:        47.0.1
Release:        %autorelease
Summary:        A GNOME application for managing encryption keys

# seahorse is GPLv2+
# libcryptui is LGPLv2+
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Seahorse
Source:         https://download.gnome.org/sources/%{name}/47/%{name}-%{tarball_version}.tar.xz

# https://gitlab.gnome.org/GNOME/seahorse/-/merge_requests/248
Patch1:         seahorse-47.0.1-allow-build-with-gpgme2.patch

BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gck-1)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsecret-unstable)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gpgme-devel >= 1.0
BuildRequires:  gnupg2
BuildRequires:  itstool
BuildRequires:  libSM-devel
BuildRequires:  meson
BuildRequires:  openldap-devel
BuildRequires:  openssh-clients
BuildRequires:  vala
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

# https://bugzilla.redhat.com/show_bug.cgi?id=474419
# https://bugzilla.redhat.com/show_bug.cgi?id=587328
Requires:       pinentry-gui

%description
Seahorse is a graphical interface for managing and using encryption keys.
It also integrates with nautilus, gedit and other places for encryption
operations.  It is a keyring manager.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson -Dmanpage=true
%meson_build

%install
%meson_install

%find_lang seahorse --with-gnome --all-name

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_metainfodir}/org.gnome.seahorse.Application.appdata.xml
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/org.gnome.seahorse.Application.desktop

%files -f %{name}.lang
%license COPYING*
%doc NEWS README.md
%{_bindir}/seahorse
%{_libexecdir}/seahorse/
%{_datadir}/applications/org.gnome.seahorse.Application.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.seahorse.Application.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.seahorse.Application.svg
%{_datadir}/dbus-1/services/org.gnome.seahorse.Application.service
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse*.gschema.xml
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers/
%{_datadir}/gnome-shell/search-providers/seahorse-search-provider.ini
%{_datadir}/seahorse/
%{_mandir}/man1/seahorse.1*
%{_metainfodir}/org.gnome.seahorse.Application.appdata.xml

%changelog
%autochangelog
