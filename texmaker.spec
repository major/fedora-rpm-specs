Summary:	LaTeX editor
Name:		texmaker
Version:	5.1.3
Release:	%{autorelease}
Epoch:		1
License:	GPLv2+
URL:		http://www.xm1math.net/texmaker/
Source:		http://www.xm1math.net/texmaker/texmaker-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)

BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	qt5-qtscript-devel
BuildRequires:	qt5-qtwebengine-devel
BuildRequires:	qtsingleapplication-qt5-devel
BuildRequires:	poppler-qt5-devel
BuildRequires:	hunspell-devel
BuildRequires:	zlib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	libappstream-glib

Requires:	tetex-latex
Requires:	tetex-dvipost

# setup the .pro file to unbundle qtsingleapplication and hunspell
# also fixes a single header file to use system singleapp
Patch0:		%{name}-%{version}-unbundle-qtsingleapp.patch

# fix header files to use system hunspell
Patch1:		%{name}-%{version}-unbundle-hunspell.patch

# use system pdf viewers instead of hardcoded evince
Patch2:		%{name}-%{version}-viewfiles.patch

# Excldue arches where qtwebengine-devel is missing
ExcludeArch: ppc64 ppc64le s390x


%description
Texmaker is a program, that integrates many tools needed to develop 
documents with LaTeX, in just one application. 
Texmaker runs on unix, macosx and windows systems and is released under the GPL
license

%prep
%setup -q
%patch0
%patch1
%patch2

# get rid of zero-length space
sed -i 's/\xe2\x80\x8b//g' utilities/%{name}.metainfo.xml

# remove bundled stuff (hunspell and qtsingleapplication)
rm -fr hunspell singleapp


%build
# Disable LTO for now
# /usr/bin/ld: .obj/gzlib.o (symbol from plugin): undefined reference to symbol 'gzbuffer@@ZLIB_1.2.3.5'
# /usr/bin/ld: /usr/lib64/libz.so.1: error adding symbols: DSO missing from command line
# collect2: error: ld returned 1 exit status
# https://koji.fedoraproject.org/koji/buildinfo?buildID=1644664
%define _lto_cflags %{nil}
%{qmake_qt5} texmaker.pro
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
