Summary:      Advanced drum machine for GNU/Linux
Name:         hydrogen
Version:      1.2.7
%global docversion %version
Release:      %autorelease
URL:          http://www.hydrogen-music.org/
# GPL-2.0-or-later
Source0:      https://github.com/hydrogen-music/%{name}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
# GPL-2.0-only AND MIT
Source1:      https://github.com/hydrogen-music/documentation/archive/refs/tags/%{docversion}/%{name}-documentation-%{docversion}.tar.gz
SourceLicense:	GPL-2.0-or-later AND GPL-2.0-only AND MIT
License:      GPL-2.0-or-later

# Fedora-specific, build release with debugging information and don’t use -O3
Patch0:       %{name}-cxxflags.patch

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gcc-c++
# Doesn’t use pkgconfig
BuildRequires: ladspa-devel
BuildRequires: libappstream-glib
# Doesn’t use pkgconfig
BuildRequires: libtar-devel
BuildRequires: make
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(flac)
# Build with traditional JACK headers
BuildRequires: pkgconfig(jack) < 3
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(lrdf)
BuildRequires: pkgconfig(rubberband)
BuildRequires: pkgconfig(sndfile)

Requires:      hicolor-icon-theme

%description
Hydrogen is an advanced drum machine for GNU/Linux. Its main goal is to bring
professional yet simple and intuitive pattern-based drum programming.

%package devel
Summary:    Hydrogen header files
Requires:   %{name}%{_isa} = %{version}-%{release}

%description devel
Header files for the hydrogen drum machine.

%package doc
Summary:	Hydrogen documentation
License:	GPL-2.0-only AND MIT
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation files for the hydrogen drum machine.

%prep
%autosetup -p1 -T -b 0 -a 1
rmdir data/doc
mv documentation-%{docversion} data/doc

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
  -DWANT_ALSA:BOOL=ON \
  -DWANT_CPPUNIT:BOOL=ON \
  -DWANT_DEBUG:BOOL=OFF \
  -DWANT_JACK:BOOL=ON \
  -DWANT_JACKSESSION:BOOL=ON \
  -DWANT_LADSPA:BOOL=ON \
  -DWANT_LASH:BOOL=ON \
  -DWANT_LIBARCHIVE:BOOL=ON \
  -DWANT_LRDF:BOOL=ON \
  -DWANT_NSMSESSION:BOOL=ON \
  -DWANT_OSS:BOOL=OFF \
  -DWANT_PORTAUDIO:BOOL=OFF \
  -DWANT_PORTMIDI:BOOL=OFF \
  -DWANT_PULSEAUDIO:BOOL=ON \
  -DWANT_RUBBERBAND:BOOL=ON \
  -DWANT_SHARED:BOOL=ON \
  -DWANT_QT6:BOOL=ON \
  -DWANT_OSC:BOOL=ON
%cmake_build

%install
%cmake_install

# install hydrogen.desktop properly.
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications   \
  --add-category AudioVideoEditing             \
  --add-category Midi                          \
  --add-category Sequencer                     \
  --add-category X-Drumming                    \
  --add-category X-Jack                        \
  --add-category X-Sound                       \
  --remove-mime-type text/xml                  \
  --delete-original                            \
  %{buildroot}%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop

# Validate desktop hydrogen.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop

# Move the icon to the proper place
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp %{buildroot}%{_datadir}/%{name}/data/img/gray/*.svg \
   %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

# No need to package these (they will not be installed automatically in rc3?):
rm -f %{buildroot}%{_datadir}/%{name}/data/doc/{Makefile,README}* \
      %{buildroot}%{_datadir}/%{name}/data/doc/*.{docbook,po,pot}

# Validate appdata
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.hydrogenmusic.Hydrogen.metainfo.xml

%files
%doc AUTHORS CHANGELOG.md README.md
%license COPYING
%{_bindir}/hydrogen
%{_bindir}/h2cli
%{_bindir}/h2player
%{_datadir}/hydrogen/
%exclude %{_datadir}/%{name}/data/doc
%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_libdir}/libhydrogen-core-1.2.*.so
%{_mandir}/man1/hydrogen.1*
%{_metainfodir}/org.hydrogenmusic.Hydrogen.metainfo.xml

%files devel
%{_includedir}/hydrogen/

%files doc
%doc %{_datadir}/%{name}/data/doc

%changelog
%autochangelog
