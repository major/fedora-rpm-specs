# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173658

%global _hardened_build 1
%global minorversion 1.3
%global xfceversion 4.18

Name:           xfce4-cpugraph-plugin
Version:        1.3.0
Release:        %autorelease
Summary:        CPU monitor for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-cpugraph-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  xfce4-panel-devel
BuildRequires:  meson
Requires:       xfce4-panel >= %{xfceversion}

%description
A CPU monitor plugin for the Xfce panel. It offers multiple display modes 
(LED, gradient, fire, etc...) to show the current CPU load of the system. The 
colors and the size of the plugin are customizable.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%check
%meson_test


%files -f %{name}.lang
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
%autochangelog
