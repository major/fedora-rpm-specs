Name:           TeXmacs
Version:        2.1.4
Release:        %autorelease
Summary:        Structured WYSIWYG scientific text editor
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.texmacs.org
Source:         http://www.texmacs.org/Download/ftp/tmftp/source/TeXmacs-%{version}-src.tar.gz
# Make plugins/mathematica/bin/realpath.py Python 3 compatible
Patch0:         https://github.com/texmacs/texmacs/pull/73.patch
# Changes for C++20
Patch1:         https://github.com/texmacs/texmacs/pull/107.patch
Patch2:         https://github.com/texmacs/texmacs/pull/109.patch
Requires:       ghostscript
Requires:       texmacs-fedora-fonts = %{version}-%{release}
BuildRequires:  cmake
BuildRequires:  cmake(Qt5)
BuildRequires:  compat-guile18-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl-generators
BuildRequires:  freetype-devel
BuildRequires:  libICE-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  sqlite-devel
BuildRequires:  zlib-devel
BuildRequires:  qt5-qtsvg-devel
# For pathfix
BuildRequires:  python3-devel
Provides:       texmacs = %{version}-%{release}
Requires:       fig2ps

%description
GNU TeXmacs is a free scientific text editor, which was both inspired
by TeX and GNU Emacs. The editor allows you to write structured
documents via a WYSIWYG (what-you-see-is-what-you-get) and user
friendly interface.  New styles may be created by the user. The
program implements high-quality typesetting algorithms and TeX fonts,
which help you to produce professionally looking documents.

The high typesetting quality still goes through for automatically
generated formulas, which makes TeXmacs suitable as an interface for
computer algebra systems. TeXmacs also supports the Guile/Scheme
extension language, so that you may customize the interface and write
your own extensions to the editor.

In the future, TeXmacs is planned to evolve towards a complete
scientific office suite, with spreadsheet capacities, a technical
drawing editor and a presentation mode.


%package devel
Summary:        Development files for TeXmacs
Requires:       %{name} = %{version}-%{release}

%description devel
Development files required to create TeXmacs plugins.

%package -n texmacs-fedora-fonts
Summary:        Fonts for TeXmacs
Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel
BuildArch:      noarch

%description -n texmacs-fedora-fonts
TeXmacs font.

%prep
%autosetup -p1 -n TeXmacs
%{py3_shebang_fix} plugins/mathematica/bin/realpath.py

%build
%cmake
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/texmacs.desktop

rm -f %{buildroot}%{_bindir}/fig2ps
rm -f %{buildroot}%{_mandir}/man*/fig2ps*

# link installed fonts with Fedora
install -d -m 0755 %{buildroot}%{_fontdir}
pushd %{buildroot}%{_datadir}/TeXmacs/fonts/type1/ec/
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/ec/$i
done
cd ../la
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/la/$i
done
cd ../math
for i in `ls *.pfb`; do
        mv $i %{buildroot}%{_fontdir}
        ln -s ../../../../fonts/TeXmacs/$i %{buildroot}%{_datadir}/TeXmacs/fonts/type1/math/$i
done
popd
rm -f %{buildroot}%{_datadir}/icons/gnome/icon-theme.cache
find %{buildroot}%{_datadir}/mime/ -type f -maxdepth 1 -print | xargs rm -f


%files
%license LICENSE
%doc COPYING TeXmacs/README TeXmacs/TEX_FONTS
%{_bindir}/*
%{_mandir}/man*/*
%{_prefix}/lib/texmacs/
%{_datadir}/TeXmacs
%exclude %{_datadir}/TeXmacs/examples/plugins
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/128x128/apps/TeXmacs.png
%{_datadir}/icons/hicolor/16x16/apps/TeXmacs.png
%{_datadir}/icons/hicolor/22x22/apps/TeXmacs.png
%{_datadir}/icons/hicolor/24x24/apps/TeXmacs.png
%{_datadir}/icons/hicolor/256x256/apps/TeXmacs.png
%{_datadir}/icons/hicolor/32x32/apps/TeXmacs.png
%{_datadir}/icons/hicolor/48x48/apps/TeXmacs.png
%{_datadir}/icons/hicolor/512x512/apps/TeXmacs.png
%{_datadir}/icons/hicolor/64x64/apps/TeXmacs.png
%{_datadir}/icons/hicolor/scalable/apps/TeXmacs.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/text-x-texmacs.svg

%files devel
%{_includedir}/*
%{_datadir}/TeXmacs/examples/plugins

%_font_pkg -n fedora *


%changelog
%autochangelog
