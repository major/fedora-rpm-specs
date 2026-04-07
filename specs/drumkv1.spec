%global        namespace org.rncbc

Summary:       An old-school drum-kit sampler
Name:          drumkv1
Version:       1.4.1
Release:       %autorelease
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://%{name}.sourceforge.io
Source0:       https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Do not strip executables
Patch0:        drumkv1-nostrip.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(sndfile)
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: jack-audio-connection-kit-devel
Requires:      hicolor-icon-theme

%description
%{name} is an old-school all-digital drum-kit sampler synthesizer with
stereo fx.

%package -n lv2-%{name}
Summary:       An LV2 port of %{name}
Requires:      lv2

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
%ctest

%files
%doc README
%license LICENSE
%{_bindir}/%{name}_jack
%{_datadir}/applications/%{namespace}.%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/%{namespace}.%{name}.xml
%{_mandir}/man1/%{name}.1*
%{_mandir}/fr/man1/%{name}.1*
%{_metainfodir}/%{namespace}.%{name}.metainfo.xml

%files -n lv2-%{name}
%doc README
%license LICENSE
%{_libdir}/lv2/%{name}.lv2/

%changelog
%autochangelog
