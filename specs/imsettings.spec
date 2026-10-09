Name:		imsettings
Version:	1.8.12
Release:	%autorelease
License:	LGPL-2.0-or-later
URL:		https://gitlab.com/tagoh/%{name}/
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	libtool automake autoconf autoconf-archive
BuildRequires:	glib2-devel >= 2.32.0, gobject-introspection-devel, gtk3-devel >= 3.3.3, gtk-doc
BuildRequires:	libnotify-devel
BuildRequires:	libX11-devel
%if !0%{?rhel}
BuildRequires:	xfconf-devel, libgxim-devel >= 0.5.0
%endif
BuildRequires: make
Source0:	https://gitlab.com/tagoh/%{name}/-/releases/%{version}/downloads/%{name}-%{version}.tar.bz2
## Fedora specific: run IM for certain languages only
Patch0:		%{name}-constraint-of-language.patch
## Fedora specific: Disable XIM support
Patch1:		%{name}-disable-xim.patch
## Fedora specific: Enable xcompose for certain languages
Patch2:		%{name}-xinput-xcompose.patch
%if 0%{?rhel}
Patch4:		%{name}-glib.patch
## backport
Patch5:		%{name}-disable-kde.patch
%endif

Summary:	Delivery framework for general Input Method configuration
Requires:	xorg-x11-xinit >= 1.0.2-22.fc8
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-desktop-module%{?_isa} = %{version}-%{release}
Requires(post):	systemd %{_sbindir}/alternatives
Requires(postun):	systemd %{_sbindir}/alternatives
Requires:	/bin/bash
Suggests:	%{name}-gsettings

%description
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the core DBus services and some utilities.

%package	libs
Summary:	Libraries for imsettings

%description	libs
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the shared library for imsettings.

%package	devel
Summary:	Development files for imsettings
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
Requires:	glib2-devel >= 2.32.0

%description	devel
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains the development files to make any
applications with imsettings.

%package	gsettings
Summary:	GSettings support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	dconf
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}
Provides:	%{name}-gnome = %{version}-%{release}
Obsoletes:	%{name}-gnome < 1.5.1-3
Provides:	%{name}-systemd = %{version}-%{release}
Obsoletes:	%{name}-systemd < 1.8.3-6
Provides:	%{name}-cinnamon = %{version}-%{release}
Obsoletes:	%{name}-cinnamon < 1.8.10-4

%description	gsettings
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on
GNOME and Cinnamon which requires GSettings in their
own XSETTINGS daemons.

%package	qt
Summary:	Qt support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	qt
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Qt
applications.

%package	plasma
Summary:	Plasma Workspace support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser
Requires:	kf5-filesystem
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	plasma
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains Plasma Workspace support on
imsettings.

%package	mate
Summary:	MATE support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
# need to keep more deps for similar reason to https://bugzilla.redhat.com/show_bug.cgi?id=693809
Requires:	mate-settings-daemon >= 1.5.0
Requires:	mate-session-manager
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	mate
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on MATE.

%if !0%{?rhel}
%package	xim
Summary:	XIM support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser

%description	xim
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working with XIM.

%package	xfce
Summary:	Xfce support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	im-chooser-xfce
Requires:	xfce4-settings >= 4.5.99.1-2
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	xfce
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on Xfce.

%package	lxde
Summary:	LXDE support on imsettings
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	lxde-settings-daemon
# Hack for upgrades: see https://bugzilla.redhat.com/show_bug.cgi?id=693809
Requires:	lxsession
Requires:	/usr/bin/lxsession
Requires:	im-chooser
Provides:	imsettings-desktop-module%{?_isa} = %{version}-%{release}

%description	lxde
IMSettings is a framework that delivers Input Method
settings and applies the changes so they take effect
immediately without any need to restart applications
or the desktop.

This package contains a module to get this working on LXDE.
%endif

%prep
%autosetup -p1
autoreconf -i

%build
%configure	\
	--with-xinputsh=50-xinput.sh \
	--disable-static \
	--disable-schemas-install

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

# change the file attributes
chmod 0755 $RPM_BUILD_ROOT%{_libexecdir}/imsettings-target-checker.sh
chmod 0755 $RPM_BUILD_ROOT%{_libexecdir}/xinputinfo.sh
chmod 0755 $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh

install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/plasma-workspace/env
ln -sf $(realpath --relative-to=$RPM_BUILD_ROOT%{_sysconfdir}/xdg/plasma-workspace/env/ $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/)/50-xinput.sh $RPM_BUILD_ROOT%{_sysconfdir}/xdg/plasma-workspace/env/xinput.sh

# clean up the unnecessary files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/libimsettings-{cinnamon-gsettings,gconf,mateconf,systemd-gtk,systemd-qt}.so
%if 0%{?rhel}
rm -f $RPM_BUILD_ROOT%{_libdir}/imsettings/libimsettings-{lxde,xfce,xim}.so
%endif

desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/imsettings-start.desktop

%find_lang %{name}


#%%check
## Disable it because it requires DBus session
# make check

%post
alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/none.conf 10
alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/xcompose.conf 20
alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/xim.conf 30
systemctl reload dbus.service 2>&1 || :

%postun
if [ "$1" = 0 ]; then
	alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/none.conf
	alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/xcompose.conf
	alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/xim.conf
	systemctl reload dbus.service 2>&1 || :
fi

%ldconfig_scriptlets	libs

%files	-f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/imsettings
%{_bindir}/imsettings-info
%{_bindir}/imsettings-list
%{_bindir}/imsettings-reload
%{_bindir}/imsettings-switch
%{_bindir}/imsettings-boot.sh
%{_libexecdir}/imsettings-check
%{_libexecdir}/imsettings-daemon
%{_libexecdir}/xinputinfo.sh
%{_libexecdir}/imsettings-functions
%{_libexecdir}/imsettings-target-checker.sh
%{_datadir}/dbus-1/services/*.service
%{_datadir}/pixmaps/*.png
%{_sysconfdir}/X11/xinit/xinitrc.d/50-xinput.sh
%{_sysconfdir}/X11/xinit/xinput.d
%{_sysconfdir}/xdg/autostart/imsettings-start.desktop
%{_mandir}/man1/imsettings-*.1*

%files	libs
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libimsettings.so.5*

%files	devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/imsettings
%{_libdir}/libimsettings.so
%{_libdir}/pkgconfig/imsettings.pc
%{_libdir}/girepository-*/IMSettings-*.typelib
%{_datadir}/gir-*/IMSettings-*.gir
%{_datadir}/gtk-doc/html/imsettings

%files	gsettings
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-gsettings.so

%files	qt
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-qt.so

%files	plasma
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/xdg/plasma-workspace/env/xinput.sh

%files	mate
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-mate-gsettings.so

%if !0%{?rhel}
%files	xim
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/imsettings-xim
%{_libdir}/imsettings/libimsettings-xim.so

%files	xfce
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-xfce.so

%files	lxde
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/imsettings/libimsettings-lxde.so
%endif

%changelog
%autochangelog
