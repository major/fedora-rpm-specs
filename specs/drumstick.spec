%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Summary: C++/Qt6 wrapper around multiple MIDI interfaces
Name:    drumstick
Version: 2.10.0
Release: %autorelease

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL:     https://drumstick.sourceforge.io/
Source0: https://sourceforge.net/projects/drumstick/files/%{version}/drumstick-%{version}.tar.bz2

BuildRequires: gcc-c++
BuildRequires: cmake >= 3.9
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: qt6-qtbase-devel >= 6.2
BuildRequires: qt6-qtsvg-devel
BuildRequires: fluidsynth-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: sonivox-devel >= 3.6.12
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qt5compat-devel
# For building manpages
BuildRequires: docbook-style-xsl
BuildRequires: libxslt
# For building API documents
BuildRequires: doxygen

Obsoletes: aseqmm < %{version}-%{release}
Provides: aseqmm = %{version}-%{release}

%description
The drumstick library is a C++ wrapper around the ALSA library sequencer
interface, using Qt objects, idioms and style. OSS, network and Fluidsynth
interfaces are also supported by this library.

%package devel
Summary: Developer files for %{name}
Requires: %{name} = %{version}-%{release}
# cmake(drumstick-alsa) requires FindALSA
Requires: alsa-lib-devel
Obsoletes: aseqmm-devel < %{version}-%{release}
Provides: aseqmm-devel = %{version}-%{release}
%description devel
%{summary}.

%package examples
Summary: Example programs for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: aseqmm-examples < %{version}-%{release}
Provides: aseqmm-examples = %{version}-%{release}
%description examples
This package contains the test/example programs for %{name}.

%package drumgrid
Summary: Drum Grid application from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description drumgrid
This package contains the drumgrid application.

%package guiplayer
Summary: MIDI player from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description guiplayer
This package contains the guiplayer application.

%package vpiano
Summary: Virtual piano application from %{name}
Requires: %{name}-examples = %{version}-%{release}
%description vpiano
This package contains the vpiano application.

%package dumprmi
Summary: RIFF RMID file support for %{name}
Requires: %{name}-examples = %{version}-%{release}
%description dumprmi
Standard RIFF MIDI File dump program.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake

%cmake_build
doxygen %{_vpath_builddir}/Doxyfile


%install
%cmake_install
for i in $RPM_BUILD_ROOT%{_datadir}/applications/* ; do
  desktop-file-validate $i
done

%check
# Tests require an alsa system, which may not be available within the mock env
#make %{?_smp_mflags} -C %{_vpath_builddir} test

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING TODO
%{_libdir}/libdrumstick-file.so.2*
%{_libdir}/libdrumstick-alsa.so.2*
%{_libdir}/libdrumstick-rt.so.2*
%{_libdir}/libdrumstick-widgets.so.2*
%{_libdir}/drumstick2/
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/%{name}/
%{_qt6_plugindir}/designer/libdrumstick-vpiano-plugin.so

%files devel
%doc doc/html/*
%{_libdir}/libdrumstick-file.so
%{_libdir}/libdrumstick-alsa.so
%{_libdir}/libdrumstick-rt.so
%{_libdir}/libdrumstick-widgets.so
%{_libdir}/pkgconfig/drumstick-file.pc
%{_libdir}/pkgconfig/drumstick-alsa.pc
%{_libdir}/pkgconfig/drumstick-rt.pc
%{_libdir}/pkgconfig/drumstick-widgets.pc
%{_libdir}/cmake/%{name}/
%{_datadir}/%{name}
%{_includedir}/drumstick/
%{_includedir}/drumstick.h

%files examples
%{_bindir}/drumstick-dumpmid
%{_bindir}/drumstick-dumpsmf
%{_bindir}/drumstick-dumpwrk
%{_bindir}/drumstick-metronome
%{_bindir}/drumstick-playsmf
%{_bindir}/drumstick-sysinfo
%{_datadir}/icons/hicolor/16x16/apps/drumstick.png
%{_datadir}/icons/hicolor/32x32/apps/drumstick.png
%{_datadir}/icons/hicolor/48x48/apps/drumstick.png
%{_datadir}/icons/hicolor/64x64/apps/drumstick.png
%{_datadir}/icons/hicolor/scalable/apps/drumstick.svgz
%{_datadir}/man/man1/drumstick-dumpmid.1.gz
%{_datadir}/man/man1/drumstick-dumpsmf.1.gz
%{_datadir}/man/man1/drumstick-dumpwrk.1.gz
%{_datadir}/man/man1/drumstick-metronome.1.gz
%{_datadir}/man/man1/drumstick-playsmf.1.gz
%{_datadir}/man/man1/drumstick-sysinfo.1.gz

%files drumgrid
%{_bindir}/drumstick-drumgrid
%{_datadir}/applications/net.sourceforge.drumstick-drumgrid.desktop
%{_datadir}/man/man1/drumstick-drumgrid.1.gz
%{_datadir}/metainfo/net.sourceforge.drumstick-drumgrid.metainfo.xml

%files guiplayer
%{_bindir}/drumstick-guiplayer
%{_datadir}/applications/net.sourceforge.drumstick-guiplayer.desktop
%{_datadir}/man/man1/drumstick-guiplayer.1.gz
%{_datadir}/metainfo/net.sourceforge.drumstick-guiplayer.metainfo.xml

%files vpiano
%{_bindir}/drumstick-vpiano
%{_datadir}/applications/net.sourceforge.drumstick-vpiano.desktop
%{_datadir}/man/man1/drumstick-vpiano.1.gz
%{_datadir}/metainfo/net.sourceforge.drumstick-vpiano.metainfo.xml

%files dumprmi
%{_bindir}/drumstick-dumprmi
%{_datadir}/man/man1/drumstick-dumprmi.1.gz

%changelog
%autochangelog
