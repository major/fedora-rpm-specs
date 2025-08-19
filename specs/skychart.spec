%global svnversion 4974
%global date 20250303
%global maj_ver 4.3

Name:       skychart
Version:    %{maj_ver}^%{date}.svn%{svnversion}
Release:    %autorelease
Summary:    Planetarium software for the advanced amateur astronomer
# bgrabitmap code is licensed LGPL-3.0-only WITH LGPL-3.0-linking-exception
License:    GPL-2.0-or-later AND LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:        http://www.ap-i.net/skychart/
# Upstream sources are modified to:
# - Remove pre-built software (iridflare.exe, quicksat.exe, dll files)
# - Remove unneeded Windows and MacOS stuff
# - Remove libraries provided by libpasastro package
#   (they still are in sources only for compiling the Windows version)
# To do this we use the generate-tarball.sh script
# Download upstream tarball from
# https://sourceforge.net/projects/skychart/files/0-beta/
# in the same directory of the script and run:
# ./generate-tarball.sh 4.3-4974
Source0:    %{name}-%{maj_ver}-%{svnversion}-src-nopatents.tar.xz
Source1:    generate-tarball.sh
# Base source data
Source2:    http://sourceforge.net/projects/skychart/files/4-source_data/data_spicesun.tgz
# Source data for skychart-data-stars
Source3:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gcvs.tgz
Source4:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_tycho2.tgz
Source5:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_wds.tgz
Source6:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_idx.tgz
# Source data for skychart-data-dso
Source7:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_leda.tgz
Source8:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_barnard.tgz
Source9:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gcm.tgz
Source10:    http://sourceforge.net/projects/skychart/files/4-source_data/catalog_gpn.tgz
Source11:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_lbn.tgz
Source12:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_ocl.tgz
Source13:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_sh2.tgz
Source14:   http://sourceforge.net/projects/skychart/files/4-source_data/catalog_vdb.tgz


# Avoid stripping debuginfo from executables
# This is Fedora specific and not reported upstream
Patch:      skychart-4.3-nostrip.patch

# Disable wget in install script
# This is Fedora specific and not reported upstream
Patch:      skychart-4.1-wgetdata.patch

# Notify the user that artificial satellites calculation
# has been disabled in Fedora RPMs due to Fedora policies
# This is Fedora specific and not reported upstream
Patch:      skychart-4.3-satmessage.patch

# Disable software update menu item
# This feature was asked upstream specifically for Fedora
Patch:      skychart-4.3-noupdatemenu.patch

# Fix build with FPC 3.2.4
Patch:      skychart-4.3-fpc-3.2.4.patch

ExclusiveArch: %{fpc_arches}
ExcludeArch: %{ix86}


BuildRequires: make
BuildRequires: fpc
BuildRequires:  fpc-src
BuildRequires:  lazarus-lcl-nogui
BuildRequires:  lazarus-lcl-qt5
BuildRequires:  lazarus-tools
BuildRequires: desktop-file-utils
BuildRequires: dos2unix
BuildRequires: gtk2-devel
BuildRequires: ImageMagick
BuildRequires: libappstream-glib

Requires: libpasastro
Requires: tzdata
Requires: xdg-utils
Requires: xplanet

Recommends: openssl-libs
# Used for binary planetary ephemeris files
Recommends: calceph-libs
# Used for Gaia catalog
Recommends: chealpix

# Weak dependency on catgen
Recommends: skychart-catgen = %{version}-%{release}


%description
This program enables you to draw sky charts, making use of the data in 16
catalogs of stars and nebulae. In addition the position of planets,
asteroids and comets are shown.

The purpose of this program is to prepare different sky maps for a
particular observation. A large number of parameters help you to choose
specifically or automatically which catalogs to use, the colour and the
dimension of stars and nebulae, the representation of planets, the display
of labels and coordinate grids, the superposition of pictures, the
condition of visibility and more. All these features make this celestial
atlas more complete than a conventional planetarium.

%package doc
Summary:        Documentation files for Skychart
License:        CC-BY-SA-3.0 OR GFDL-1.3-no-invariants-or-later
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation files from the official Skychart wiki provided
within the program as an offline copy.

%package data-stars
Summary:        Additional star catalogs for Skychart
License:        LicenseRef-Fedora-Public-Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data-stars
Additional star catalogs for Skychart. This package install all the standard
stars catalog down to magnitude 12, variable and double stars:
Tycho 2; General Catalogue of Variable Stars; Washington Double Stars.

%package data-dso
Summary:        Additional Deep Sky Object catalogs for Skychart
License:        LicenseRef-Fedora-Public-Domain
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data-dso
Additional DSO catalogs for Skychart. This package install all the standard
nebulae catalogs: LEDA Catalogue; Lynds Bright Nebulae; Open Cluster Data;
Globular Clusters in the Milky Way; Galactic Planetary Nebulae;
Barnard Catalogue of Dark Nebulae; Sharpless Catalog.

%package catgen
Summary:        Custom catalog builder for Skychart
License:        GPL-2.0-or-later
Provides:       catgen = %{version}-%{release}

%description catgen
Custom catalog builder for Skychart.

%prep
%setup -q -n %{name}-%{maj_ver}-%{svnversion}-src

%autopatch -p1

# Fix executable bit set on sources
find skychart -type f -print0 | xargs -0 chmod -x

# Put additional catalogs files where are required for installation

cp -p %SOURCE2 ./BaseData
cp -p %SOURCE3 ./BaseData
cp -p %SOURCE4 ./BaseData
cp -p %SOURCE5 ./BaseData
cp -p %SOURCE6 ./BaseData
cp -p %SOURCE7 ./BaseData
cp -p %SOURCE8 ./BaseData
cp -p %SOURCE9 ./BaseData
cp -p %SOURCE10 ./BaseData
cp -p %SOURCE11 ./BaseData
cp -p %SOURCE12 ./BaseData
cp -p %SOURCE13 ./BaseData
cp -p %SOURCE14 ./BaseData


%build
./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}

# Skychart doesn't like parallel building so we don't use macro.
# We pass the following options to fpc compiler:
# - O2 for code optimization level
# - gw4 for generating dwarf 4 debug symbols
# - Cg to generate PIC code
make fpcopts="-O2 -gw4 -Cg"


%install
# Install main program
make install PREFIX=%{buildroot}%{_prefix}

# Install catalogs, translations and data files
make install install_data PREFIX=%{buildroot}%{_prefix}

# Install wiki documentation
make install install_doc PREFIX=%{buildroot}%{_prefix}

# Install additional catalogs
make install install_cat1 PREFIX=%{buildroot}%{_prefix}
make install install_cat2 PREFIX=%{buildroot}%{_prefix}


%check
# Menu entry
desktop-file-validate %{buildroot}%{_datadir}/applications/net.ap_i.*.desktop

# Appdata file check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml


%files
%license skychart/gpl.txt
%doc %{_datadir}/doc/skychart/changelog
%doc %{_datadir}/doc/skychart/copyright
%{_bindir}/%{name}
%{_bindir}/cdcicon
%{_bindir}/varobs
%{_datadir}/applications/net.ap_i.%{name}.desktop
%{_datadir}/applications/net.ap_i.varobs.desktop
%{_datadir}/metainfo/net.ap_i.%{name}.metainfo.xml
%{_datadir}/metainfo/net.ap_i.varobs.metainfo.xml
%{_datadir}/mime/packages/net.ap_i.%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/varobs.png
%{_datadir}/icons/*/*/*/%{name}.png
%{_datadir}/icons/*/*/*/varobs.png
%{_datadir}/icons/*/*/*/%{name}.svg
%{_datadir}/icons/*/*/*/varobs.svg
%dir %{_datadir}/skychart
%{_datadir}/skychart/data
%dir %{_datadir}/skychart/cat
%{_datadir}/skychart/cat/DSoutlines
%{_datadir}/skychart/cat/milkyway
%{_datadir}/skychart/cat/openngc
%{_datadir}/skychart/cat/RealSky
%{_datadir}/skychart/cat/xhip
%dir %{_datadir}/skychart/doc
%{_datadir}/skychart/doc/html_doc
%{_datadir}/skychart/doc/releasenotes*.txt
%{_datadir}/skychart/doc/varobs

%files doc
%doc %{_datadir}/skychart/doc/wiki_doc

%files data-stars
%{_datadir}/skychart/cat/gcvs
%{_datadir}/skychart/cat/tycho2
%{_datadir}/skychart/cat/wds
%{_datadir}/skychart/cat/bsc5
%{_datadir}/metainfo/net.ap_i.%{name}.%{name}_data_stars.metainfo.xml

%files data-dso
%{_datadir}/skychart/cat/leda
%{_datadir}/skychart/cat/lbn
%{_datadir}/skychart/cat/ocl
%{_datadir}/skychart/cat/gcm
%{_datadir}/skychart/cat/gpn
%{_datadir}/skychart/cat/barnard
%{_datadir}/skychart/cat/sh2
%{_datadir}/skychart/cat/vdb
%{_datadir}/metainfo/net.ap_i.%{name}.%{name}_data_dso.metainfo.xml

%files catgen
%{_bindir}/catgen
%{_datadir}/applications/net.ap_i.catgen.desktop
%{_datadir}/metainfo/net.ap_i.catgen.metainfo.xml
%{_datadir}/pixmaps/catgen.png
%{_datadir}/icons/*/*/*/catgen.png
%{_datadir}/icons/*/*/*/catgen.svg


%changelog
%autochangelog
