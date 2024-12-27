# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=187569
%global minorversion 1.3
%global xfceversion 4.16

Name:           xfce4-mailwatch-plugin
Version:        1.3.2
Release:        %autorelease
Summary:        Mail Watcher plugin for the Xfce panel

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-weather-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.7.2
BuildRequires:  gnutls-devel >= 1.2.0
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  gettext
Requires:       xfce4-panel >= %{xfceversion}


%description
Mailwatch is a plugin for the Xfce 4 panel. It is intended to replace the 
current (4.0, 4.2) mail checker plugin in Xfce 4.4. It supports IMAP and POP, 
local mailboxes in Mbox, Maildir and MH-Maildir format as well as Gmail.

%prep
%autosetup
# Fix icon in 'Add new panel item' dialog
sed -i 's|Icon=xfce-mail|Icon=mail-unread|g' panel-plugin/mailwatch.desktop.in


%build
%configure
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
%doc AUTHORS ChangeLog README
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/*/*


%changelog
%autochangelog
