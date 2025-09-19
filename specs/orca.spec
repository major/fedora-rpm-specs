%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           orca
Version:        49.0
Release:        %autorelease
Summary:        Assistive technology for people with visual impairments

License:        LGPL-2.1-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Projects/Orca
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{tarball_version}.tar.xz

BuildArch:      noarch

BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(liblouis)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  brlapi-devel
BuildRequires:  brltty
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  python3-brlapi
BuildRequires:  python3-dasbus
BuildRequires:  python3-devel
BuildRequires:  python3-louis
BuildRequires:  python3-pyatspi
BuildRequires:  python3-speechd
BuildRequires:  /usr/bin/desktop-file-validate

Requires:       libwnck3
Requires:       python3-brlapi
Requires:       python3-dasbus
Requires:       python3-louis
Requires:       python3-pyatspi
Requires:       python3-speechd
Requires:       speech-dispatcher

%description
Orca is a screen reader that provides access to the graphical desktop via
user-customizable combinations of speech and/or braille. Orca works with
applications and toolkits that support the assistive technology service
provider interface (AT-SPI), e.g. the GNOME desktop.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate %{buildroot}%{_sysconfdir}/xdg/autostart/orca-autostart.desktop


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/orca
%{python3_sitelib}/orca/
%{_datadir}/icons/hicolor/*/apps/orca.png
%{_datadir}/icons/hicolor/scalable/apps/orca.svg
%{_datadir}/icons/hicolor/symbolic/apps/orca-symbolic.svg
%{_datadir}/orca
%{_sysconfdir}/xdg/autostart/orca-autostart.desktop
%{_mandir}/man1/orca.1*
%{_userunitdir}/orca.service


%changelog
%autochangelog
