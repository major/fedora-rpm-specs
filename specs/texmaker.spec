Summary:	LaTeX editor
Name:		texmaker
Version:	5.1.4
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
BuildRequires:	lcms2-devel
BuildRequires:	libappstream-glib
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	poppler-qt6-devel
BuildRequires:	zlib-devel

Requires:	tetex-latex

# setup the .pro file to unbundle qtsingleapplication and hunspell
# also fixes a single header file to use system singleapp
Patch0:		%{name}-%{version}-unbundle-qtsingleapp.patch

# fix header files to use system hunspell
Patch1:		%{name}-%{version}-unbundle-hunspell.patch

# use system pdf viewers instead of hardcoded evince
Patch2:		%{name}-%{version}-viewfiles.patch

# Use system libraries
Patch3: texmaker-zlib.patch
Patch4: texmaker-lcms.patch
Patch5: texmaker-libpng.patch

# Bundled libraries
Provides: bundled(pdfium)
#  pdfium/third_party
#   Not packaged
Provides: bundled(agg23)
Provides: bundled(base)
Provides: bundled(bigint)
#   Fedora has openjpeg 2.5
Provides: bundled(libopenjpeg) = 2.0


%description
Texmaker is a program, that integrates many tools needed to develop 
documents with LaTeX, in just one application. 
Texmaker runs on unix, macosx and windows systems and is released under the GPL
license

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p1 -b .zlib
%patch -P4 -p1 -b .lcms
%patch -P5 -p1 -b .libpng

# get rid of zero-length space
sed -i 's/\xe2\x80\x8b//g' utilities/%{name}.metainfo.xml

# remove bundled stuff (hunspell and qtsingleapplication)
# libtiff, pymock appear to be unused by anything
rm -fr hunspell singleapp pdfium/third_party/{lcms,libjpeg,libpng,libtiff,pymock,zlib}*
# pdfium needs an internal freetype header pstables.h
find pdfium/third_party/freetype -name pstables.h -o -type f -delete
# Use system libraries
sed -i -e '1iPKGCONFIG += freetype2 lcms2 libjpeg libpng zlib' -e '/third_party\/\(freetype\|lcms\|libjpeg\|libpng\)/d' texmaker.pro


%build
export CXXFLAGS="%{optflags} -DUSE_SYSTEM_LIBJPEG"
%{qmake_qt6} texmaker.pro
%make_build

%install
# cannot use make_install macro - inappropriate
make INSTALL_ROOT=%{buildroot} install INSTALL="install -p"

install -Dp -m 0644 utilities/texmaker16x16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker22x22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker32x32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker48x48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/texmaker.png
install -Dp -m 0644 utilities/texmaker128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/texmaker.png

# Don't package these twice
rm -rf %{buildroot}%{_datadir}/%{name}/{AUTHORS,COPYING,*.desktop,tex*.png}
rm -f %{buildroot}%{_datadir}/applications/texmaker.desktop

desktop-file-install 		\
	--dir %{buildroot}%{_datadir}/applications	\
	--remove-category Publishing			\
	--remove-category X-SuSE-Core-Office		\
	--remove-category X-Mandriva-Office-Publishing	\
	--remove-category X-Misc			\
	utilities/texmaker.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.metainfo.xml

%ldconfig_scriptlets

%files
%license utilities/COPYING
%doc utilities/AUTHORS doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
%autochangelog
