# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173105
# VCS   https://gitlab.xfce.org/panel-plugins/xfce4-weather-plugin

%global minorversion 0.12

%global xfceversion 4.20

Name:           xfce4-weather-plugin
Version:        0.12.0
Release:        %autorelease
Summary:        Weather plugin for the Xfce panel
License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/panel-plugins/xfce4-weather-plugin/start
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  json-c-devel
BuildRequires:  libsoup3-devel
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  libxml2-devel >= 2.4.0
BuildRequires:  meson
BuildRequires:  upower-devel >= 0.9.0
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}

Requires:       xfce4-panel >= %{xfceversion}

%description
A weather plugin for the Xfce panel. It shows the current temperature and 
weather condition, using weather data provided by xoap.weather.com.


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

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%check
%meson_test


%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/weather


%changelog
%autochangelog
