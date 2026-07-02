%global        namespace org.rncbc

Summary:       A polyphonic sampler synthesizer with stereo effects
Name:          samplv1
Version:       1.4.2
Release:       %autorelease
License:       GPL-2.0-or-later
URL:           https://%{name}.sourceforge.io/
Source:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch:         %{name}-nostrip.patch

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
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(sndfile)

Requires:      hicolor-icon-theme

%description
%{name} is a polyphonic sampler synthesizer with stereo effects.

%package -n lv2-%{name}
Summary:       An LV2 port of %{name}
Requires:      lv2 >= 1.8.1

%description -n lv2-%{name}
An LV2 plugin of the %{name} synth

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
