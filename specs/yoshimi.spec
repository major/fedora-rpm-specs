%global _vpath_srcdir src

Name:		yoshimi
Version:	2.3.6.1
Release:	%autorelease
Summary:	Rewrite of ZynAddSubFx aiming for better JACK support

License:	GPL-2.0-or-later
URL:		https://sourceforge.net/projects/%{name}
Source0:	https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-cflags.patch

BuildRequires:	gcc-c++
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	cmake 
BuildRequires:	zlib-devel 
BuildRequires:	fontconfig-devel
BuildRequires:	fltk1.3-devel 
BuildRequires:	fltk1.3-fluid 
BuildRequires:	fftw3-devel
BuildRequires:	mxml-devel 
BuildRequires:	alsa-lib-devel 
BuildRequires:	libsndfile-devel
BuildRequires:	desktop-file-utils 
BuildRequires:	boost-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	cairo-devel
BuildRequires:	lv2-devel
BuildRequires:	readline-devel
BuildRequires:	libappstream-glib

%description

Yoshimi is a rewrite of ZynAddSubFx to improve its compatibility with
the Jack Audio Connection Kit.

ZynAddSubFX is an open source software synthesizer capable of making a
countless number of instrument sounds. It is microtonal, and the instruments
made by it sound like those from professional keyboards. The program has
effects like Reverb, Echo, Chorus, Phaser...

%prep
%autosetup -p1 -n home/will/%{name}-%{version}
sed -i '/<icon/d' desktop/metainfo/yoshimi.metainfo.xml


%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DFLTK_INCLUDE_DIR=%{_includedir}/Fl
%cmake_build


%install
%cmake_install

# Remove duplicate examples directory from doc folder
rm -rf %{buildroot}%{_datadir}/doc/%{name}/examples

# Copy main documentation files to the doc directory
cp -p Changelog README.md %{buildroot}%{_datadir}/doc/%{name}/

# Fix directory and file permissions
find %{buildroot}%{_datadir}/%{name} -type d -exec chmod 0755 {} +
find %{buildroot}%{_datadir}/%{name} -type f -exec chmod 0644 {} +
find %{buildroot}%{_datadir}/doc/%{name} -type d -exec chmod 0755 {} +
find %{buildroot}%{_datadir}/doc/%{name} -type f -exec chmod 0644 {} +


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%license COPYING
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}_alt.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml
%{_libdir}/lv2/%{name}.lv2/
%{_mandir}/man1/yoshimi.1*

%changelog
%autochangelog
