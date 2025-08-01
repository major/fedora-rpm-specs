Summary:      Advanced drum machine for GNU/Linux
Name:         hydrogen
Version:      1.2.6
Release:      %autorelease
URL:          http://www.hydrogen-music.org/
Source0:      https://github.com/hydrogen-music/%{name}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
License:      GPL-2.0-or-later

Patch0:       %{name}-cxxflags.patch

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: flac-devel 
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: ladspa-devel
BuildRequires: libsndfile-devel
BuildRequires: libarchive-devel
BuildRequires: liblo-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtxmlpatterns-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtsvg-devel
BuildRequires: cmake
BuildRequires: cppunit-devel
BuildRequires: make
BuildRequires: doxygen
BuildRequires: libappstream-glib

Requires:      hicolor-icon-theme

%description
Hydrogen is an advanced drum machine for GNU/Linux. It's main goal is to bring 
professional yet simple and intuitive pattern-based drum programming.

%package devel
Summary:    Hydrogen header files
Requires:   %{name}%{_isa} = %{version}-%{release}
Obsoletes:  devel <= 0.9.7-9

%description devel
Header files for the hydrogen drum machine.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DWANT_DEBUG=OFF -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_SKIP_INSTALL_RPATH=ON
%cmake_build

%install
%cmake_install

# install hydrogen.desktop properly.
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications   \
  --add-category X-Drumming                    \
  --add-category Midi                          \
  --add-category X-Jack                        \
  --add-category AudioVideoEditing             \
  --remove-mime-type text/xml                  \
  --delete-original                            \
  %{buildroot}%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop

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
%{_bindir}/h2*
%{_datadir}/hydrogen/
%{_datadir}/applications/org.hydrogenmusic.Hydrogen.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_libdir}/libhydrogen-core-1.2.*.so
%{_mandir}/man1/hydrogen.1*
%{_metainfodir}/org.hydrogenmusic.Hydrogen.metainfo.xml

%files devel
%{_includedir}/hydrogen/

%changelog
%autochangelog
