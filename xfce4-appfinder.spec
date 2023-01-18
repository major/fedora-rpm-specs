%global xfceversion 4.18

Name:           xfce4-appfinder
Version:        4.18.0
Release:        %autorelease
Summary:        Appfinder for the Xfce4 Desktop Environment

License:        GPLv2+
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfce4-appfinder
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(dbus-glib-1) >= 0.84
BuildRequires:  pkgconfig(garcon-1) >= 0.1.7
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfceversion}
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfceversion}
BuildRequires:  startup-notification-devel
BuildRequires:  gettext 
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
xfce-appfinder shows system wide installed applications.


%prep
%setup -q

# fix icon problems - GTK-3.10+
sed -i 's/gtk-find/edit-find/g' data/xfce4-appfinder.desktop.in
sed -i 's/gtk-execute/system-run/g' data/xfce4-run.desktop.in

%build
%configure

%make_build

%install
%make_install


desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/xfce4-run.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.xfce.%{name}.appdata.xml

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc TODO ChangeLog AUTHORS
%{_bindir}/xfce4-appfinder
%{_bindir}/xfrun4
%{_datadir}/applications/xfce4-*.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.appfinder*
%{_metainfodir}/org.xfce.%{name}.appdata.xml

%changelog
%autochangelog
