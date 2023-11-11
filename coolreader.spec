%global forgeurl https://github.com/buggins/coolreader

Name:           coolreader
Version:        3.2.59
Release:        %autorelease
Summary:        Cross platform open source e-book reader
%global tag cr%{version}
%forgemeta
License:        GPL-2.0-or-later
URL:            %forgeurl
Source0:        %forgesource
Source1:        cr3.appdata.xml

# libunibreak dropped i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libunibreak)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  utf8proc-devel
BuildRequires:  libzstd-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
CoolReader is fast and small cross-platform XML/CSS based eBook reader for
desktops and handheld devices. Supported formats: FB2, TXT, RTF, DOC, TCR,
HTML, EPUB, CHM, PDB, MOBI.


%prep
%forgeautosetup -p1


%build
mkdir -p %{_vpath_builddir}
%cmake \
  -DGUI=QT5 \
  -DCMAKE_BUILD_TYPE=Release \
  -DMAX_IMAGE_SCALE_MUL=2 \
  -DDOC_DATA_COMPRESSION_LEVEL=3 \
  -DDOC_BUFFER_SIZE=0x1400000 \
  -D CMAKE_INSTALL_PREFIX=/usr \
  .

%cmake_build


%install
%cmake_install
install -D -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/cr3.appdata.xml

# gather locale files
%find_lang cr3 --with-qt --without-mo


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/cr3.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/cr3.appdata.xml


%files -f cr3.lang
%license LICENSE
%{_bindir}/cr3
%{_datadir}/applications/cr3.desktop
%dir %{_datadir}/cr3
%{_datadir}/cr3/*.css
%{_datadir}/cr3/backgrounds/
%{_datadir}/cr3/hyph/
%{_datadir}/cr3/textures/
%{_datadir}/pixmaps/cr3.*
%{_metainfodir}/cr3.appdata.xml
%{_mandir}/man1/cr3.1*
%doc %{_docdir}/cr3
%doc README.md


%changelog
%autochangelog
