%global         namespace org.rncbc

Name:           padthv1
Version:        1.4.2
Release:        %autorelease
Summary:        An old-school polyphonic additive synthesizer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://%{name}.sourceforge.io/
Source:         https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Patch requested upstream https://sourceforge.net/p/padthv1/tickets/1/
Patch:          %{name}-nostrip.patch

BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
# pipewire-jack can be used at runtime, but is difficult to find at build time
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(lv2)

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

%build
%cmake
%cmake_build

%install
%cmake_install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so

# Create symlinks for binary-name matching manpages to satisfy rpmlint
ln -s %{name}.1 %{buildroot}%{_mandir}/man1/%{name}_jack.1
ln -s %{name}.1 %{buildroot}%{_mandir}/fr/man1/%{name}_jack.1

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{namespace}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{namespace}.%{name}.metainfo.xml

%files
%license LICENSE
%doc README
%{_bindir}/%{name}_jack
%{_datadir}/applications/%{namespace}.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{namespace}.%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/%{namespace}.%{name}.application-x-%{name}-preset.*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}_jack.1*
%{_mandir}/fr/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}_jack.1*
%{_metainfodir}/%{namespace}.%{name}.metainfo.xml
%{_datadir}/mime/packages/%{namespace}.%{name}.xml
%{_datadir}/%{name}

%files -n       lv2-%{name}
%license LICENSE
%doc README
%{_libdir}/lv2/%{name}.lv2/

%changelog
%autochangelog
