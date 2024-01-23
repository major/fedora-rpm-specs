Name:           padthv1
Version:        0.9.23
Release:        6%{?dist}
Summary:        An old-school polyphonic additive synthesizer

License:        GPLv2+
URL:            https://%{name}.sourceforge.io/
Source0:        https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Patch requested upstream https://sourceforge.net/p/padthv1/tickets/1/
Patch0:         %{name}-nostrip.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  jack-audio-connection-kit-devel >= 1.9.12
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist
BuildRequires:  lv2-devel >= 1.8.1
BuildRequires:  desktop-file-utils
BuildRequires:  libsndfile-devel
BuildRequires:  liblo-devel
BuildRequires:  fftw-devel
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme

%description
%{name} is an old-school polyphonic additive synthesizer with stereo effects.
%{name} is based on the PADsynth algorithm by Paul Nasca,
as a special variant of additive synthesis.
This is the standalone Jack version.

%package -n     lv2-%{name}
Summary:        LV2 port of an old-school polyphonic additive synthesizer
Requires:       lv2 >= 1.8.1

%description -n lv2-%{name}
%{name} is an old-school polyphonic additive synthesizer with stereo effects.
%{name} is based on the PADsynth algorithm by Paul Nasca,
as a special variant of additive synthesis.
This is the LV2 version.

%prep
%autosetup -p1

# Remove cruft from appdata file
# https://sourceforge.net/p/padthv1/tickets/2/
pushd src/appdata
iconv -f utf-8 -t ascii//IGNORE -o tmpfile %{name}.appdata.xml 2>/dev/null || :
mv -f tmpfile %{name}.appdata.xml
popd

%build
%cmake
%cmake_build

%install
%cmake_install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%license COPYING
%doc README AUTHORS
%{_bindir}/%{name}_jack
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-%{name}-preset.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml

%files -n       lv2-%{name}
%license COPYING
%doc README AUTHORS
%{_libdir}/lv2/%{name}.lv2/

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.23-1
- Update to 0.9.23
- Switch build system to cmake

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 21 2021 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.21-1
- Update to 0.9.21

* Mon Feb 15 2021 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.20-1
- Update to 0.9.20

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 12:22:11 CET 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.19-1
- Update to 0.9.19

* Mon Sep 14 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.17-1
- Update to 0.9.17

* Fri Aug 28 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.16-1
- Update to 0.9.16

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.15-1
- Update to 0.9.15
- Do not own hicolor dir entirely

* Sun May 24 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.14-1
- Update to 0.9.14

* Sun Apr 19 2020 Guido Aulisi <guido.aulisi@gmail.com> - 0.9.13-1
- Initial build
