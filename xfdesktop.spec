%global xfceversion 4.16

Name:           xfdesktop
Version:        4.16.1
Release:        %autorelease
Summary:        Desktop manager for the Xfce Desktop Environment

License:        GPLv2+
URL:            http://www.xfce.org/
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  exo-devel >= 0.12.0
BuildRequires:  libgudev1-devel >= 145
BuildRequires:  Thunar-devel >= 1.8.0
BuildRequires:  dbus-glib-devel >= 0.84
BuildRequires:  garcon-devel >= 0.1.2
BuildRequires:  libwnck3-devel >= 3.14
BuildRequires:  libnotify-devel >= 0.4.0
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  libSM-devel
BuildRequires:  libICE-devel
Requires:       xfwm4 >= %{xfceversion}
Requires:       xfce4-panel >= %{xfceversion}
Requires:       redhat-menus
Requires:       desktop-backgrounds-compat
%if 0%{fedora}>= 37
Requires:       webp-pixbuf-loader%{?_isa}
%endif

%description
This package includes a desktop manager for the Xfce Desktop Environment.

%prep
%setup -q

# change default background for Fedora
%if 0%{fedora} >= 37
sed -i 's|/backgrounds/xfce/xfce-verticals.png|/backgrounds/images/default.webp|' common/xfdesktop-common.h
%else
sed -i 's|/backgrounds/xfce/xfce-verticals.png|/backgrounds/images/default.png|' common/xfdesktop-common.h
%endif

%build
%configure

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/xfce-backdrop-settings.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc TODO ChangeLog NEWS AUTHORS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/*
%{_datadir}/backgrounds/xfce
%{_mandir}/man1/*

%changelog
%autochangelog
