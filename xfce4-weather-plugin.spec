# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173105

%global minorversion 0.11

%global xfceversion 4.16

Name:           xfce4-weather-plugin
Version:        0.11.1
Release:        %autorelease
Summary:        Weather plugin for the Xfce panel

License:        BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-weather-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  libsoup-devel >= 2.26.0
BuildRequires:  upower-devel >= 0.9.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libxml2-devel >= 2.4.0
Requires:       xfce4-panel >= %{xfceversion}

%description
A weather plugin for the Xfce panel. It shows the current temperature and 
weather condition, using weather data provided by xoap.weather.com.


%prep
%autosetup

%build
%configure
%make_build

%install
%make_install


# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/xfce4/weather


%changelog
%autochangelog
