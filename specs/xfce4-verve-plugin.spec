# Review at https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=238348
%global _hardened_build 1
%global minor_version 2.0

Name:		xfce4-verve-plugin
Version:	2.0.4
Release:	%autorelease
Summary:	Comfortable command line plugin for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{minor_version}/%{name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	xfce4-panel-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	exo-devel >= 0.5.0
BuildRequires:	pcre-devel >= 5.0
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	libxml2-devel, gettext, intltool, perl(XML::Parser)

Requires:	xfce4-panel
Provides:	verve-plugin = %{version}
# Retire xfce4-minicmd-plugin
Provides:	xfce4-minicmd-plugin = 0.4-9
Obsoletes:	xfce4-minicmd-plugin =< 0.4-8.fc9


%description
This plugin is like the (quite old) xfce4-minicmd-plugin, except that it ships 
more cool features, such as:
* Command history
* Auto-completion (including command history)
* Open URLs and eMail addresses in your favourite applications
* Focus grabbing via D-BUS (so you can bind a shortcut to it)
* Custom input field width


%prep
%autosetup

%build
%configure --disable-static --enable-dbus
%make_build

%install
%make_install

rm -f %{buildroot}/%{_libdir}/xfce4/panel/plugins/libverve.la
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog THANKS
%{_libdir}/xfce4/panel/plugins/libverve.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
