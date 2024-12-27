# review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173661

%global _hardened_build 1
%global minorversion 1.1
%global xfceversion 4.16

Name:           xfce4-fsguard-plugin
Version:        1.1.4
Release:        %autorelease
Summary:        Filesystem-Guard plugin for the Xfce panel

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-fsguard-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
A little Xfce plugin, which checks the free space on the chosen mountpoint 
frequently. It displays 4 different icons and a message box, depending on the
free space. The amount of free disk space is visible in a tooltip. If you 
left-click on its icon, it opens the mountpoint directory in the file manager.


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
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%changelog
%autochangelog
