# CVS   https://gitlab.xfce.org/panel-plugins/xfce4-timer-plugin
%global minorver 1.8

Name:           xfce4-timer-plugin
Version:        1.8.0
Release:        %autorelease
Summary:        Timer for the Xfce panel
License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/panel-plugins/xfce4-timer-plugin/start
Source0:        https://archive.xfce.org/src/panel-plugins/xfce4-timer-plugin/%{minorver}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libxfce4ui-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel

Requires:       xfce4-panel

%description
A timer for the Xfce panel. It supports countdown periods and alarms at 
certain times.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

# Rename non-standard hye locale to hy
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_libdir}/xfce4/panel/plugins/libxfcetimer.so
%{_datadir}/xfce4/panel/plugins/xfce4-timer-plugin.desktop
%{_datadir}/icons/hicolor/*/apps/xfce4-timer-plugin.*g


%changelog
%autochangelog
