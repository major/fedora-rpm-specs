# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173105
%global _hardened_build 1

%global minorversion 1.2
%global xfceversion 4.20

Name:           xfce4-battery-plugin
Version:        1.2.0
Release:        %autorelease
Summary:        Battery monitor for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-battery-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  meson
Requires:       xfce4-panel >= %{xfceversion}

%description
A battery monitor plugin for the Xfce panel, compatible with APM and ACPI.


%prep
%autosetup

%build
%meson
%meson_build


%install
%meson_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS COPYING.LIB README.md
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*


%changelog
%autochangelog
