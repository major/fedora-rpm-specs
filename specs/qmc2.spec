%global forgeurl https://github.com/qmc2/qmc2-mame-fe/
#global commit 2cc9d99fbff31c03a78c7b9698ced54eae61495c

Version:        0.243

%forgemeta

Name:           qmc2
Release:        %autorelease
Summary:        M.A.M.E. Catalog / Launcher II

#PDF.js is ASL 2.0
#data/js/pdfjs/web/l10n.js is MIT
#everything else is GPLv2
License:        GPLv2 and ASL 2.0 and MIT
URL:            http://qmc2.batcom-it.net
Source0:        %{forgesource}
#Fedora-specific configuration
Patch1:         %{name}-ini.patch
Patch2:         0001-Fix-build-with-minizip-4.0.8.patch
#Fixes and improvements from upstream git
Patch10:        0001-fix-MachineListDatabase-wasn-t-saved-to-qmc2.ini.patch
Patch11:        0001-new-added-a-Brasilian-Portuguese-translation-thanks-.patch
Patch12:        0001-imp-added-Ubuntu-22.04-build-configuration.patch
Patch13:        0001-imp-removed-ancient-build-configs.patch
Patch14:        0001-imp-Added-history.xml-support-and-use-XML-parser-to-.patch
Patch15:        0002-imp-Updated-Fedora-and-Ubuntu-build-configurations.-.patch
Patch16:        0007-imp-Updated-bundled-libraries-to-their-current-upstr.patch
Patch17:        0008-imp-Replaced-custom-XML-parsing-with-QXmlStreamReade.patch
Patch18:        0001-imp-Updated-SDL-to-2.30.3-LZMA-SDK-to-25.06-and-mini.patch

BuildRequires:  desktop-file-utils
BuildRequires:  git
BuildRequires:  libarchive-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  rsync
BuildRequires:  SDL2-devel
Requires:       games-menus
Provides:       bundled(lzma-sdk) = 24.06
Provides:       PDF.js = 3f320f0b

%description
A Qt based multi-platform GUI front-end for MAME.


%package -n qchdman
Summary:        Qt CHDMAN GUI
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Requires:       mame-tools

%description -n qchdman
A stand-alone graphical user interface / front-end to chdman


%package arcade
Summary:        Arcade QMC2 GUI
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only

%description arcade
A QML-based standalone graphical arcade mode binary which utilizes the cached
data of qmc2 to quickly display and launch emulators and get you "straight into
the games"


%prep
%forgeautosetup -p1 -S git
#ensure system minizip and zlib are used
rm -rf src/minizip
rm -rf src/zlib
#fix opening documentation from the menu
sed -i s@doc/html/@doc/@ src/qmc2main.cpp


%build
#https://bugzilla.redhat.com/show_bug.cgi?id=1998742
%make_build DISTCFG=1 CC_FLAGS="$RPM_OPT_FLAGS" CXX_FLAGS="$RPM_OPT_FLAGS" \
    L_FLAGS="$RPM_LD_FLAGS" \
    SYSTEM_MINIZIP=1 \
    SYSTEM_ZLIB=1 LIBARCHIVE=1 GIT_REV=0
%make_build arcade DISTCFG=1 CC_FLAGS="$RPM_OPT_FLAGS" CXX_FLAGS="$RPM_OPT_FLAGS" \
    L_FLAGS="$RPM_LD_FLAGS"  \
    SYSTEM_MINIZIP=1 \
    SYSTEM_ZLIB=1 LIBARCHIVE=1 GIT_REV=0
%make_build qchdman DISTCFG=1 CXX_FLAGS="$RPM_OPT_FLAGS" L_FLAGS="$RPM_LD_FLAGS" \
    GIT_REV=0
%make_build doc DISTCFG=1


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make arcade-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make qchdman-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make doc-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 MAN_DIR=%{_mandir}

#remove docs since we are installing docs in %%doc
pushd $RPM_BUILD_ROOT%{_datadir}/%{name}
rm -fr doc
ln -s %{_docdir}/%{name} doc
popd

#validate the desktop files
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qmc2-sdlmame.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qmc2-arcade.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qchdman.desktop


%files
%doc data/doc/html/*
%license data/doc/html/us/copying.html data/js/pdfjs/LICENSE
%config(noreplace) %{_sysconfdir}/qmc2
%{_bindir}/qmc2
%{_bindir}/qmc2-sdlmame
%{_datadir}/applications/qmc2-sdlmame.desktop
%{_mandir}/man6/qmc2-main-gui.6*
%{_mandir}/man6/qmc2-sdlmame.6*
%{_mandir}/man6/qmc2.6*
%{_datadir}/qmc2

%files arcade
%license data/doc/html/us/copying.html
%{_bindir}/qmc2-arcade
%{_datadir}/applications/qmc2-arcade.desktop
%{_mandir}/man6/qmc2-arcade.6*

%files -n qchdman
%license data/doc/html/us/copying.html
%{_bindir}/qchdman
%{_datadir}/applications/qchdman.desktop
%{_mandir}/man6/qchdman.6*


%changelog
%autochangelog
