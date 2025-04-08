%global minorversion 0.6

Name:           mousepad
Version:        0.6.5
Release:        %autorelease
Summary:        Simple text editor for Xfce desktop environment

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://git.xfce.org/apps/mousepad/about/
Source0:        http://archive.xfce.org/src/apps/%{name}/%{minorversion}/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  xfce4-dev-tools
BuildRequires:  gettext 
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  gtksourceview4-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  glib2-devel
BuildRequires:  libappstream-glib
BuildRequires:  gspell-devel
BuildRequires:  polkit-devel
BuildRequires:  libxfce4ui-devel

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
    * Font selecton
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
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libmousepad0
A plugin provider for the Mousepad text editor


%package devel
Summary:        Development files for Mousepad
Group:          Development/Libraries
Requires:       libmousepad0 >= %{version}

%Description devel
Development files for Mousepad plugin development

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

desktop-file-install \
    --remove-category="Application" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/org.xfce.%{name}.desktop

desktop-file-install \
    --remove-category="Application" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/org.xfce.%{name}-settings.desktop

mkdir -p %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.appdata.xml

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%if 0%{?el7}
%post
update-desktop-database &> /dev/null ||:
 
%postun
update-desktop-database &> /dev/null ||:
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%post -n libmousepad0 -p /sbin/ldconfig

%postun -n libmousepad0 -p /sbin/ldconfig

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
%endif

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
%{_libdir}/libmousepad.*

%files devel
%{_libdir}/libmousepad.so

%changelog
%autochangelog
