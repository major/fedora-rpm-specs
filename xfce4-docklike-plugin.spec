%global majorversion 0.4
%global xfceversion 4.16

Name:           xfce4-docklike-plugin
Version:        0.4.0
Release:        6%{?dist}
Summary:        A modern, minimalist taskbar for Xfce

License:        GPLv2+ and GPLv3+ and FSFUL
URL:            https://gitlab.xfce.org/panel-plugins/xfce4-docklike-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{majorversion}/%{name}-%{version}.tar.bz2

BuildRequires:	desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gio-qt-devel
BuildRequires:  gtk3-devel
BuildRequires:	intltool
BuildRequires:  libwnck3-devel
BuildRequires:	libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libX11-devel
BuildRequires:  make
BuildRequires:	xfce4-panel-devel >= %{xfceversion}

%description
Docklike Taskbar behaves similarly to many other desktop environments
and operating systems. Wherein all application windows are grouped
together as an icon and can be pinned to act as a launcher when
the application is not running. Commonly referred to as a dock.


%prep
%autosetup

# remove empty files
rm -f ChangeLog README


%build
%configure
%make_build


%install
%make_install

# remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

	
%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS
%{_datadir}/xfce4/panel/plugins/docklike.desktop
%{_libdir}/xfce4/panel/plugins/libdocklike.so


%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.4.0-2
- SPEC file fixes

* Tue Mar 8 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 0.4.0-1
- Initial build for Fedora
