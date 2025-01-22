Summary:	Gnome Partition Editor
Name:		gparted
Version:	1.6.0
Release:	%autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://gparted.org
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

# Backporting patches to fix reading exfat filesystems
# https://gitlab.gnome.org/GNOME/gparted/-/issues/275
Patch0:		35baa44e2f174504a20b22424285458d501dcda4.diff
Patch1:		344e03439e1a79776b9cc7e6f65fccf3e6f656dd.diff

BuildRequires:	gtkmm30-devel
BuildRequires:	parted-devel
BuildRequires:	libuuid-devel
BuildRequires:	gettext
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel, polkit
BuildRequires:	libappstream-glib
BuildRequires:	itstool
BuildRequires:	gcc-c++
BuildRequires:	make

Requires:	PolicyKit-authentication-agent

%description
GParted stands for Gnome Partition Editor and is a graphical frontend to
libparted. Among other features it supports creating, resizing, moving
and copying of partitions. Also several (optional) filesystem tools provide
support for filesystems not included in libparted. These optional packages
will be detected at runtime and don't require a rebuild of GParted

%prep
%autosetup -p1

%build
%configure --enable-libparted-dmraid --enable-online-resize --enable-xhost-root
%make_build

%install
%make_install

sed -i 's#_X-GNOME-FullName#X-GNOME-FullName#' %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's#sbin#bin#' %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --delete-original			\
	--dir %{buildroot}%{_datadir}/applications	\
	--mode 0644					\
	--add-category X-Fedora				\
	--add-category GTK				\
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# install appdata file
mkdir -p %{buildroot}%{_datadir}/metainfo
%{__install} -p -m755 %{name}.appdata.xml %{buildroot}%{_datadir}/metainfo

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README
%{_libexecdir}/gpartedbin
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/gparted.*
%{_datadir}/polkit-1/actions/org.gnome.gparted.policy
%{_datadir}/help/*/gparted/*
%{_mandir}/man8/gparted.*

%changelog
%autochangelog
