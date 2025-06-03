# Review: https://bugzilla.redhat.com/show_bug.cgi?id=173657

%global _hardened_build 1
%global minorversion 1.7
%global xfceversion 4.16

Name:           xfce4-clipman-plugin
Version:        1.7.0
Release:        %autorelease
Summary:        Clipboard manager plugin for the Xfce panel

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  exo-devel >= 0.6.0
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  xorg-x11-proto-devel >= 7.0.0
BuildRequires:  libXtst-devel >= 1.0.0
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  qrencode-devel
Requires:       xfce4-panel >= %{xfceversion}

%description
This is a simple cliboard history for Xfce panel. It includes a "Clear 
clipboard" option, and a drag-and-drop paste feature.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --delete-original \
  %{buildroot}%{_datadir}/applications/xfce4-clipman.desktop

desktop-file-install \
  --dir %{buildroot}%{_sysconfdir}/xdg/autostart \
  --delete-original  \
  %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop


%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%config %{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%config(noreplace) %{_sysconfdir}/xdg/xfce4/panel/xfce4-clipman-actions.xml
%{_bindir}/xfce4-clipman
%{_bindir}/xfce4-clipman-history
%{_bindir}/xfce4-clipman-settings
%{_bindir}/xfce4-popup-clipman
%{_bindir}/xfce4-popup-clipman-actions
%{_libdir}/xfce4/panel/plugins/libclipman*
%{_datadir}/applications/xfce4-clipman-settings.desktop
%{_datadir}/applications/xfce4-clipman.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/xfce4/panel/plugins/%{name}.desktop
%{_datadir}/metainfo/xfce4-clipman.appdata.xml
%{_datadir}/icons/hicolor/16x16/apps/clipman-symbolic.svg

%changelog
%autochangelog
