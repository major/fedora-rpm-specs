%global uuid    com.github.lainsce.%{name}

Name:           coin
Version:        1.3.0
Release:        %autorelease
Summary:        Track the virtual currencies in real world currency value

License:        GPLv3+
URL:            https://github.com/lainsce/coin
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)

Requires:       hicolor-icon-theme

%description
Track the virtual currencies in real world currency value with this handy
applet.

- Choose which currency and virtual currency to use for tracking
- Quit anytime with the shortcut Ctrl + Q
- Move the applet by dragging it from anywhere in the window
- Stays out of your way in the desktop


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.appdata.xml


%changelog
%autochangelog
