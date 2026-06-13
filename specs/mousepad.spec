# the shortcuts plugin uses libxfce4kbd-private
%bcond xfce4kbd %{undefined flatpak}

%global minorversion 0.7

Name:           mousepad
Version:        0.7.0
Release:        %autorelease
Summary:        Simple text editor for Xfce desktop environment

License:        GPL-2.0-or-later
URL:            https://gitlab.xfce.org/apps/mousepad
Source:         https://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gspell-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  xfce4-dev-tools
%if %{with xfce4kbd}
BuildRequires:  libxfce4ui-devel
%endif

%description
Mousepad aims to be an easy-to-use and fast editor. It's target is an editor for
quickly editing text files, not a development environment or an editor with a
huge bunch of plugins.

Mousepad is based on Leafpad. The initial reason for Mousepad was to provide
printing support, which would have been difficult for Leafpad for various
reasons.

Although some features are under development, currently Mousepad has following
features:

    * Complete support for UTF-8 text
    * Cut/Copy/Paste and Select All text
    * Search and Replace
    * Font selection
    * Word Wrap
    * Character coding selection
    * Auto character coding detection (UTF-8 and some codesets)
    * Manual codeset setting
    * Infinite Undo/Redo by word
    * Auto Indent
    * Multi-line Indent
    * Display line numbers
    * Drag and Drop
    * Printing

%package -n libmousepad0
Summary:        Mousepad plugin provider
Requires:       %{name} >= %{version}

%description -n libmousepad0
A plugin provider for the Mousepad text editor


%package devel
Summary:        Development files for Mousepad
Requires:       libmousepad0 = %{version}-%{release}

%description devel
Development files for Mousepad plugin development

%prep
%autosetup

%build
%meson %{!?with_xfce4kbd:-Dshortcuts-plugin=disabled}
%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-edit --remove-category="Application" %{buildroot}%{_datadir}/applications/org.xfce.%{name}.desktop
desktop-file-edit --remove-category="Application" %{buildroot}%{_datadir}/applications/org.xfce.%{name}-settings.desktop

%check
%meson_test
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/mousepad 
%{_metainfodir}/org.xfce.%{name}.appdata.xml
%{_datadir}/applications/org.xfce.%{name}.desktop
%{_datadir}/applications/org.xfce.%{name}-settings.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.%{name}.*.xml
%{_datadir}/polkit-1/actions/org.xfce.mousepad.policy
%{_datadir}/icons/hicolor/*/*/*.%{name}*
%{_libdir}/%{name}/plugins

%files -n libmousepad0
%{_libdir}/libmousepad.so.*

%files devel
%{_libdir}/libmousepad.so

%changelog
%autochangelog
