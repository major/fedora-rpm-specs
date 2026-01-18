%global debug_package %{nil}
Name:   ibus-speech-to-text
Version:  0.7.0
Release:  2%{?dist}
Summary:  A speech to text IBus Input Method using VOSK
ExcludeArch: %{ix86}
License:  GPL-3.0-or-later
URL:     https://github.com/Manish7093/IBus-Speech-To-Text
Source0: https://github.com/Manish7093/IBus-Speech-To-Text/archive/refs/tags/%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  ibus-devel >= 1.5.3
BuildRequires:  libadwaita-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python3-pywhispercpp

Requires:    ibus >= 1.5.3
Requires:    python3-dbus
Requires:    python3-babel
Requires:    gstreamer1
Requires:    gobject-introspection
Requires:    gst-vosk >= 0.3.0
Requires:    gtk4
Requires:    dconf
Requires:    python3-pywhispercpp

%description
A speech to text IBus Input Method using VOSK and WhisperCpp
which can be used to dictate text to any application

%prep
%setup -q -n IBus-Speech-To-Text-%{version}

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
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jan 7 2026 Manish Tiwari <matiwari@redhat.com> 0.7.0-1
- Update to release 0.7.0
- Add support for WhisperCpp

* Sun Sep 7 2025 Manish Tiwari <matiwari@redhat.com> 0.6.0-1
- Update to 0.6.0 release

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon May 5 2025 Manish Tiwari <matiwari@redhat.com> 0.5.0-1
- Update to 0.5.0 release
- Remove babel.patch

* Wed Jan 15 2025 Manish Tiwari <matiwari@redhat.com> 0.4.0-2
- Added desktop-file-validate to ensure .desktop file compliance

* Wed Sep 04 2024 Manish Tiwari <matiwari@redhat.com> 0.4.0-1
- Initial version of the package
