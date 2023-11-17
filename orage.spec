%global xfceversion 4.18

Name:           orage
Version:        4.18.0
Release:        %autorelease
Summary:        A calendar application

License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
Source:         http://archive.xfce.org/src/apps/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfce4ui-2)

Requires:       hicolor-icon-theme
Requires:       dbus-common

%description
Orage is a fast and easy to use graphical time-managing application for the
Xfce Desktop Environment. It uses portable ical format and includes common
calendar features like repeating appointments and multiple alarming
possibilities. Orage does not have group calendar features, but can
only be used for single user.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%doc README.md AUTHORS
%{_bindir}/%{name}
%dir %{_datadir}/locale/hy_AM
%dir %{_datadir}/locale/hy_AM/LC_MESSAGES
%{_datadir}/applications/org.xfce.%{name}*desktop
%{_datadir}/dbus-1/services/org.xfce.%{name}.service
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/%{name}/
%{_metainfodir}/org.xfce.%{name}.appdata.xml


%changelog
%autochangelog
