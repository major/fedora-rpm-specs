%global app_id io.github.wxmaxima_developers.wxMaxima

Summary: Graphical user interface for Maxima
Name:    wxMaxima
Version: 26.01.0
Release: %autorelease

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://wxmaxima-developers.github.io/wxmaxima/
Source0: https://github.com/wxMaxima-developers/wxmaxima/archive/Version-%{version}.tar.gz

## upstream patches
# none at this time

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: dos2unix
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gettext
BuildRequires: ImageMagick
BuildRequires: libappstream-glib
BuildRequires: libxml2-devel
BuildRequires: wxGTK-devel

Provides: wxmaxima = %{version}-%{release}

Requires: jsmath-fonts
Requires: maxima >= 5.30

%description
A Graphical user interface for the computer algebra system
Maxima using wxWidgets.


%prep
%autosetup -n wxmaxima-Version-%{version} -p1

dos2unix data/%{app_id}.desktop


%build
%cmake
%cmake_build


%install
%cmake_install

# app icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{scalable,48x48,64x64,128x128}/apps/
cp -alf \
  %{buildroot}%{_datadir}/pixmaps/%{app_id}.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp -alf \
  %{buildroot}%{_datadir}/pixmaps/%{app_id}.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
convert -resize 64x64 \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{app_id}.png \
  %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{app_id}.png
convert -resize 48x48 \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{app_id}.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{app_id}.png

# mime icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/
cp -alf  %{buildroot}%{_datadir}/pixmaps/text-x-wx*.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/

%find_lang wxMaxima
%find_lang wxmaxima --with-man

# Unpackaged files
rm -fv %{buildroot}%{_datadir}/wxmaxima/{COPYING,README,README.md}
rm -rfv %{buildroot}%{_datadir}/pixmaps/
rm -rfv %{buildroot}%{_datadir}/menu


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop


%files -f wxMaxima.lang -f wxmaxima.lang
%doc AUTHORS.md ChangeLog NEWS.md README.md
%license COPYING
%{_bindir}/wxmaxima
%{_datadir}/wxMaxima/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/%{app_id}.desktop
%{_metainfodir}/%{app_id}.appdata.xml
%{_datadir}/bash-completion/completions/wxmaxima
%{_datadir}/mime/packages/x-wxmathml.xml
%{_datadir}/mime/packages/x-wxmaxima-batch.xml
%{_docdir}/wxmaxima/
%{_mandir}/man1/wxmaxima.1*


%changelog
%autochangelog
