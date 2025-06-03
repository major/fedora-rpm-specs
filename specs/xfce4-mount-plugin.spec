# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173549

%global _hardened_build 1
%global minorversion 1.2
%global xfceversion 4.20

Name:           xfce4-mount-plugin
Version:        1.2.0
Release:        %autorelease
Summary:        Mount/unmount utility for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-diskperf-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  meson
Requires:       xfce4-panel >= %{xfceversion}

%description
Mount and unmount filesystems from the Xfce panel.

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


%files -f %{name}.lang
%doc AUTHORS README
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/xfce-mount.svg

%changelog
%autochangelog
