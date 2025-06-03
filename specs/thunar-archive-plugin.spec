# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=215241

%global minor_version 0.6
%global thunar_version 4.20.0
%global xfceversion 4.20

Name:           thunar-archive-plugin
Version:        0.6.0
Release:        %autorelease
Summary:        Archive plugin for the Thunar file manager

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:        http://archive.xfce.org/src/thunar-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.xz
#VCS:           git:git://git.xfce.org/thunar-plugins/thunar-archive-plugin

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  exo >= 0.12.0
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  Thunar-devel >= %{thunar_version}
BuildRequires:  libxml2-devel
BuildRequires:  meson
Requires:       Thunar >= %{thunar_version}

%description
The Thunar Archive Plugin allows you to create and extract archive files using 
the file context menus in the Thunar file manager. Starting with version 0.2.0, 
the plugin provides a generic scripting interface for archive managers. 


%prep
%setup -q


%build
%meson
%meson_build

%install
%meson_install


%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS THANKS NEWS
%doc scripts/template.tap
%{_libdir}/thunarx-*/thunar-archive-plugin.so
%{_libexecdir}/thunar-archive-plugin/
%{_datadir}/icons/hicolor/*/*/*


%changelog
%autochangelog
