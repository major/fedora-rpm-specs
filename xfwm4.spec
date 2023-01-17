%global xfceversion 4.16

Name:           xfwm4
Version:        4.16.1
Release:        %autorelease
Summary:        Next generation window manager for Xfce

License:        GPLv2+
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfwm4
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libXext-devel
%if 0%{?fedora}
BuildRequires:  libXpresent-devel
%endif
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  startup-notification-devel >= 0.5
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  desktop-file-utils

Provides:       firstboot(windowmanager) = xfwm4

%description
xfwm4 is a window manager compatible with GNOME, GNOME2, KDE2, KDE3 and Xfce.

%prep
%autosetup -p1


%build
export export CFLAGS="%{optflags} -DSHOW_POSITION"
%configure --disable-static

%make_build

%install
%make_install

%find_lang %{name}

for file in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done

%files -f %{name}.lang
%license COPYING
%doc example.gtkrc-2.0 TODO AUTHORS COMPOSITOR
%{_bindir}/xfwm4
%{_bindir}/xfwm4-settings
%{_bindir}/xfwm4-tweaks-settings
%{_bindir}/xfwm4-workspace-settings
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfwm4
%{_datadir}/themes/*
%dir %{_libdir}/xfce4/xfwm4/
%{_libdir}/xfce4/xfwm4/helper-dialog


%changelog
%autochangelog
