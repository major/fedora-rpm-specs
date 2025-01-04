%global app_name br.app.pw3270

Name:           pw3270
Version:        5.5.0
Release:        %autorelease
Summary:        IBM 3270 Terminal emulator for GTK

License:        LGPL-3.0-only
URL:            https://github.com/PerryWerneck/pw3270
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-scour

BuildRequires:  gettext-devel
BuildRequires:  libv3270-devel

Requires:       hicolor-icon-theme
Suggests:       font(ibm3270)

%description
GTK-based IBM 3270 terminal emulator with many advanced features. It can be
used to communicate with any IBM host that supports 3270-style connections
over TELNET.

Based on the original x3270 code, pw3270 was originally created for Banco do
Brasil, and is now used worldwide.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

mkdir -p %{buildroot}%{_libdir}/%{name}/5.5/plugins/

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_name}.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{app_name}.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/5.5/plugins/
%{_datadir}/%{name}/*
%{_datadir}/applications/%{app_name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{app_name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{app_name}-symbolic.svg
%{_metainfodir}/%{app_name}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{name}*.gschema.xml
%{_datadir}/mime/packages/%{name}.xml

%changelog
%autochangelog
