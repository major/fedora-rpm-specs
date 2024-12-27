# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173544

%global _hardened_build 1
%global minor_version 4.2
%global xfceversion 4.16

Name:           xfce4-genmon-plugin
Version:        4.2.1
Release:        %autorelease
Summary:        Generic monitor plugin for the Xfce panel

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-genmon-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  gettext
Requires:       xfce4-panel >= %{xfceversion}

%description
The GenMon plugin cyclically spawns the indicated script/program,
captures its output and displays it as a string into the panel.


%prep
%autosetup


%build
%configure --disable-static
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
%doc AUTHORS ChangeLog
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/icons/hicolor/*/apps/org.xfce.genmon.*g
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/xfce4/genmon/scripts/*

%changelog
%autochangelog
