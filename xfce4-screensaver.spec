%global majorver 4.18

Name:           xfce4-screensaver
Version:        4.18.1
Release:        %autorelease
Summary:        Screensaver application for Xfce Desktop

License:        GPLv2 and LGPLv2
URL:            https://git.xfce.org/apps/xfce4-screensaver/
Source0:        https://archive.xfce.org/src/apps/%{name}/%{majorver}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(garcon-gtk3-1)
BuildRequires:  libwnck3-devel
BuildRequires:  systemd-devel
BuildRequires:  pam-devel
BuildRequires:  desktop-file-utils

Requires:       xfdesktop
Requires:       xfconf
Requires:       xfce4-session

%description
Xfce Screensaver is a port of MATE Screensaver, itself a port of GNOME 
Screensaver. It has been tightly integrated with the Xfce desktop, utilizing 
Xfce libraries and the Xfconf configuration backend.


%prep
%autosetup


%build
%configure --with-systemd --enable-pam --enable-locking

%make_build

%install
%make_install

# conflict between systemd service and autostart
# remove systemd file
# https://bugzilla.redhat.com/show_bug.cgi?id=2055507
rm -f %{buildroot}%{_datadir}/dbus-1/services/org.xfce.ScreenSaver.service


for file in %{buildroot}%{_datadir}/applications/screensavers/*.desktop ; do
     desktop-file-install \
         --add-category="X-XFCE" \
         --delete-original \
         --dir=%{buildroot}%{_datadir}/applications/screensavers \
         $file
done

desktop-file-install \
      --add-category="X-XFCE" \
      --delete-original \
      --dir=%{buildroot}%{_datadir}/applications \
      %{buildroot}%{_datadir}/applications/%{name}-preferences.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING COPYING.LGPL
%{_sysconfdir}/pam.d/xfce4-screensaver
%{_sysconfdir}/xdg/autostart/xfce4-screensaver.desktop
%{_sysconfdir}/xdg/menus/xfce4-screensavers.menu
%{_bindir}/%{name}
%{_bindir}/xfce4-screensaver-command
%{_bindir}/xfce4-screensaver-configure
%{_bindir}/xfce4-screensaver-preferences
%{_libexecdir}/xfce4-screensaver-dialog
%{_libexecdir}/xfce4-screensaver-gl-helper
%{_datadir}/icons/hicolor/*/apps/org.xfce.ScreenSaver.*
%{_datadir}/applications/screensavers/xfce-personal-slideshow.desktop
%{_datadir}/applications/screensavers/xfce-popsquares.desktop
%{_datadir}/applications/screensavers/xfce-floaters.desktop
%{_datadir}/applications/xfce4-screensaver-preferences.desktop
%{_datadir}/desktop-directories/xfce4-screensaver.directory
%{_mandir}/man1/xfce4-screensaver-command.1.*
%{_mandir}/man1/xfce4-screensaver-preferences.1.*
%{_mandir}/man1/xfce4-screensaver.1.*
%{_datadir}/pixmaps/xfce-logo-white.svg
%{_libexecdir}/%{name}

%changelog
%autochangelog
