%global xfceversion 4.20

Name:           xfce4-settings
Version:        4.20.5
Release:        %autorelease
Summary:        Settings Manager for Xfce

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.xfce.org/
#VCS git:git://git.xfce.org/xfce/xfce4-settings
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2
# Use Fedora theme and font settings
Patch10:        xfce4-settings-%{xfceversion}-fedora.patch

BuildRequires:  colord-devel
BuildRequires:  desktop-file-utils >= 0.7
BuildRequires:  exo-devel >= 0.5.0
BuildRequires:  garcon-devel >= %{xfceversion}
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  intltool
BuildRequires:  libXrandr-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libnotify-devel
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  libxklavier-devel
BuildRequires:  make
BuildRequires:  xfconf-devel >= %{xfceversion}
%ifnarch s390 s390x
BuildRequires:  xorg-x11-drv-libinput-devel
%endif

Requires:       xfconf
%if 0%{?rhel} <= 7
Requires:       gnome-icon-theme
%endif

%description
This package includes the settings manager applications for the Xfce desktop. 

%prep
%autosetup -p0

%build
%configure --enable-sound-settings --enable-xorg-libinput
%make_build

%install
%make_install

# Remove invalid locale directory to silence rpmlint
rm -rf %{buildroot}%{_datadir}/locale/hye

for file in %{buildroot}%{_datadir}/applications/*.desktop ; do
    desktop-file-install \
        --add-category="X-XFCE" \
        --remove-category="XFCE" \
        --delete-original \
        --dir=%{buildroot}%{_datadir}/applications \
        $file
done

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%config(noreplace) %{_sysconfdir}/xdg/autostart/xfsettingsd.desktop
%config(noreplace) %{_sysconfdir}/xdg/menus/xfce-settings-manager.menu
%config(noreplace) %{_sysconfdir}/xdg/xfce4/helpers.rc
%{_bindir}/xfce4-mime-helper
%{_bindir}/xfce4-*-settings
%{_bindir}/xfce4-settings-editor
%{_bindir}/xfce4-settings-manager
%{_bindir}/xfsettingsd
%{_bindir}/xfce4-find-cursor
%{_datadir}/applications/xfce*.desktop
%{_libdir}/xfce4
%{_libdir}/gtk-3.0/modules/libxfsettingsd-gtk-settings-sync.so
%{_datadir}/icons/hicolor/*/*/*xfce*
%{_datadir}/xfce4/helpers/*.desktop

%changelog
%autochangelog
