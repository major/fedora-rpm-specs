Name:           algobox
Version:        1.1.1
Release:        %autorelease
Summary:        Algorithmic software
Summary(fr):    Logiciel d'algorithmique

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.xm1math.net/algobox
Source0:        %{url}/algobox-%{version}.tar.bz2

# Because qtwebengine is not always available
ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel >= 5.7
BuildRequires:  qt5-qtwebengine-devel

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires: make

%description
Algobox is an initiation to algorithmic software at high school level.

%description -l fr
Algobox est un logiciel d'initiation à l'algorithmique au niveau lycée.


%prep
%autosetup -p1
chmod -x license.txt


%build

%{qmake_qt5}

%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


%check
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/algobox.desktop

appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license license.txt
%doc utilities/AUTHORS utilities/CHANGELOG.txt
%{_bindir}/algobox
%{_datadir}/algobox
%{_datadir}/applications/algobox.desktop
%{_datadir}/mime/packages/x-algobox.xml
%{_datadir}/pixmaps/algobox.png
%{_datadir}/metainfo/algobox.metainfo.xml


%changelog
%autochangelog
