# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=215169

%global minor_version 0.8
%global xfceversion 4.16

Name:           xfce4-dict
Version:        0.8.10
Release:        %autorelease
Summary:        A Dictionary Client for the Xfce desktop environment
Summary(de):    Ein Wörterbuch-Client für die Xfce Desktop-Umgebung

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/apps/xfce4-dict/start
Source0:        https://archive.xfce.org/src/apps/%{name}/%{minor_version}/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel >= %{xfceversion}

Requires:       enchant
Requires:       xdg-utils

%description
Xfce4 Dictionary is a client program to query different dictionaries. It can
query a Dict server (RFC 2229), open online dictionaries in a web browser or
verify the spelling of a word using enchant. This package contains the
stand-alone application, that can be used in different desktop environments
too.

%package        plugin
Summary:        Xfce panel plugin to query a Dict server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       xfce4-panel >= %{xfceversion}

%description    plugin
Xfce4 Dictionary is a client program to query different dictionaries. It can
query a Dict server (RFC 2229), open online dictionaries in a web browser or
verify the spelling of a word using enchant. This package contains the plugin
for the Xfce panel.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# make sure debuginfo is generated properly
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%meson_test

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.Dictionary.png
%{_datadir}/icons/hicolor/scalable/apps/org.xfce.Dictionary.svg
%{_mandir}/man1/%{name}.1*

%files plugin
%{_libdir}/xfce4/panel/plugins/libxfce4dict.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
