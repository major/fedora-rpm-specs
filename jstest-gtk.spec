%global commit 17956d285fedcf476ea753ff850fa7adf51ba07c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20231001

Name:           jstest-gtk
Version:        0.1.0
Release:        %{date}git%{shortcommit}.%autorelease
Summary:        Simple joystick tester based on Gtk+

License:        GPL-3.0-only
URL:            https://github.com/Grumbel/jstest-gtk
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(sigc++-1.2)

Requires:       hicolor-icon-theme

%description
jstest-gtk is a simple joystick tester based on Gtk+. It provides you with a
list of attached joysticks, a way to display which buttons and axis are
pressed, a way to remap axis and buttons and a way to calibrate your joystick.


%prep
%autosetup -n %{name}-%{commit}


%build
%cmake
%cmake_build


%install
%cmake_install


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%doc README.md 
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.svg
%{_libexecdir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/*.xml


%changelog
%autochangelog
