%global minorversion 1.1
%global xfceversion 4.16

Name:           xfce4-terminal
Version:        1.1.4
Release:        %autorelease
Summary:        Terminal Emulator for the Xfce Desktop environment

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://docs.xfce.org/apps/terminal/start
Source0:        http://archive.xfce.org/src/apps/xfce4-terminal/%{minorversion}/%{name}-%{version}.tar.bz2


BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  vte291-devel >= 0.38
BuildRequires:  gtk3-devel >= 3.14.0
BuildRequires:  glib2-devel >= 2.26.0

BuildRequires:  desktop-file-utils
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
# require a small monospace font
Requires:       dejavu-sans-mono-fonts
# This package replaces the Terminal package
Provides: Terminal = %{version}-%{release}
Obsoletes: Terminal < 0.4.8-5

%description
Xfce4-terminal is a lightweight and easy to use terminal emulator application 
with many advanced features including drop down, tabs, unlimited scrolling, 
full colors, fonts, transparent backgrounds, and more.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}
desktop-file-install \
  --delete-original \
  --add-category="GTK" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install \
  --delete-original \
  --add-category="GTK" \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}-settings.desktop

rm -rf %{buildroot}%{_datadir}/gnome-control-center

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc ChangeLog NEWS AUTHORS HACKING THANKS
%{_bindir}/xfce4-terminal
%{_datadir}/xfce4/terminal
%{_datadir}/icons/hicolor/*/apps/org.xfce.terminal*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_mandir}/man1/xfce4-terminal.1.*

%changelog
%autochangelog
