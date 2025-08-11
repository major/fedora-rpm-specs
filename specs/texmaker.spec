Summary:	LaTeX editor
Name:		texmaker
Version:	6.0.1
Release:	%{autorelease}
Epoch:		1
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.xm1math.net/texmaker/
Source:		http://www.xm1math.net/texmaker/texmaker-%{version}.tar.bz2
	
ExclusiveArch: %{qt6_qtwebengine_arches}
	
 
BuildRequires:  make
BuildRequires:	desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:	gettext
BuildRequires:	hunspell-devel
BuildRequires:	qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:	qt6-qtwebengine-devel
BuildRequires:	qt6-qt5compat-devel
BuildRequires:	qtsingleapplication-qt6-devel
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:	lcms2-devel
BuildRequires:	libappstream-glib
BuildRequires:	libjpeg-turbo-devel
# libjpeg-turbo target requires turbojpeg
# https://bugzilla.redhat.com/show_bug.cgi?id=2387454
BuildRequires:  turbojpeg
BuildRequires:	libpng-devel
BuildRequires:	poppler-qt6-devel
BuildRequires:	zlib-devel

Requires:	tetex-latex

# Unbundle packages
Patch0:		%{name}-unbundle.patch

# Always use xdg-open
Patch1:		%{name}-%{version}-viewfiles.patch

# Bundled libraries
Provides: bundled(encodingprober)
Provides: bundled(pdfium)
Provides: bundled(synctex)
#  pdfium/third_party
#   Not packaged
Provides: bundled(agg23)
Provides: bundled(base)
Provides: bundled(bigint)
#   Fedora has openjpeg 2.5 and pdfium uses internal openjpeg functions
Provides: bundled(libopenjpeg) = 2.0


%description
Texmaker is a program, that integrates many tools needed to develop 
documents with LaTeX, in just one application. 
Texmaker runs on unix, macosx and windows systems and is released under the GPL
license

%prep
%setup -q
%patch -P0 -p1 -b .unbundle
%patch -P1 -p0

# remove bundled stuff (hunspell and qtsingleapplication)
# libtiff, pymock appear to be unused by anything
rm -r 3rdparty/{hunspell,singleapp,pdfium/third_party/{lcms,libjpeg,libpng,libtiff,pymock,zlib}*}
# pdfium needs an internal freetype header pstables.h
find 3rdparty/pdfium/third_party/freetype -name pstables.h -o -type f -delete


%build
export CXXFLAGS="%{optflags} -DUSE_SYSTEM_LIBJPEG"
%cmake
%cmake_build

%install
%cmake_install

install -Dp -m 0644 datas/distrib/linux/texmaker16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker22x22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/texmaker.png
install -Dp -m 0644 datas/distrib/linux/texmaker256x256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/texmaker.png

# Don't package these twice
rm -r %{buildroot}%{_datadir}/%{name}/{AUTHORS,COPYING,tex*.png}
rm -f %{buildroot}%{_datadir}/applications/texmaker.desktop

desktop-file-install 		\
	--dir %{buildroot}%{_datadir}/applications	\
	--remove-category Publishing			\
	--remove-category X-SuSE-Core-Office		\
	--remove-category X-Mandriva-Office-Publishing	\
	--remove-category X-Misc			\
	datas/distrib/linux/texmaker.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%files
%license COPYING
%doc AUTHORS datas/doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
%autochangelog
