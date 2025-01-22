Name:   ibus-speech-to-text
Version:  0.4.0
Release:  2%{?dist}
Summary:  A speech to text IBus Input Method using VOSK
BuildArch:  noarch
License:  GPL-3.0-or-later
URL:     https://github.com/PhilippeRo/IBus-Speech-To-Text
Source0: https://github.com/PhilippeRo/IBus-Speech-To-Text/archive/refs/tags/%{version}.tar.gz
# Adjust Locale.number_symbols changes in Babel 2.14 
# https://github.com/python-babel/babel/releases/tag/v2.14.0
Patch0: babel.patch
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  ibus-devel >= 1.5.3
BuildRequires:  libadwaita-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

Requires:    ibus >= 1.5.3
Requires:    python3-dbus
Requires:    python3-babel
Requires:    gstreamer1
Requires:    gobject-introspection
Requires:    gst-vosk >= 0.3.0
Requires:    gtk4
Requires:    dconf

%description
A speech to text IBus Input Method using VOSK, 
which can be used to dictate text to any application

%prep
%setup -q -n IBus-Speech-To-Text-%{version}
%patch 0 -p1 -b .orig~

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-stt.desktop
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}
%find_lang ibus-stt

%files -f ibus-stt.lang
%license COPYING
%doc AUTHORS README.md
%{_libexecdir}/ibus-engine-stt
%{_libexecdir}/ibus-setup-stt
%{_datadir}/ibus-stt
%{_datadir}/ibus/component/stt.xml
%{_datadir}/applications/ibus-setup-stt.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.stt.gschema.xml

%changelog
* Wed Jan 15 2025 Manish Tiwari <matiwari@redhat.com> 0.4.0-2
- Added desktop-file-validate to ensure .desktop file compliance

* Wed Sep 04 2024 Manish Tiwari <matiwari@redhat.com> 0.4.0-1
- Initial version of the package
