%global        namespace org.rncbc

Summary:       A 4-oscillator subtractive polyphonic synthesizer
Name:          synthv1
Version:       1.4.2
Release:       %autorelease
URL:           https://%{name}.sourceforge.io/
Source:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Do not strip executables
Patch:         synthv1-nostrip.patch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
Requires:      hicolor-icon-theme

BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
# pipewire-jack can be used at runtime, but is difficult to find at build time
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lv2)

%description
%{name} is a 4-oscillator subtractive polyphonic synthesizer with stereo fx.

%package -n lv2-%{name}
Summary:       An LV2 port of synthv1
Requires:      lv2 >= 1.2.0

%description -n lv2-%{name}
An LV2 plugin of the synthv1 subtractive synthesizer

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
chmod +x %{buildroot}%{_libdir}/lv2/%{name}.lv2/%{name}.so

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{namespace}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{namespace}.%{name}.metainfo.xml

%files
%doc README
%license LICENSE
%{_datadir}/applications/%{namespace}.%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_bindir}/%{name}_jack
%{_datadir}/mime/packages/%{namespace}.%{name}.xml
%{_mandir}/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_metainfodir}/%{namespace}.%{name}.metainfo.xml
%{_datadir}/%{name}

%files -n lv2-%{name}
%doc README
%license LICENSE
%{_libdir}/lv2/%{name}.lv2/

%changelog
%autochangelog
