Name:           pstoedit
Version:        4.3
Release:        %autorelease
Summary:        Translates PostScript and PDF graphics into other vector formats
License:        GPL-2.0-or-later
URL:            http://www.pstoedit.net
Source0:        https://github.com/woglu/pstoedit/archive/refs/tags/%{version}/pstoedit-%{version}.tar.gz

# Fix cflags of the pkg-config file
Patch0:         %{name}-pkglibdir.patch

# drvpptx.cpp:68:1: note: 'std::unique_ptr' is defined in header '<memory>'; did you forget to '#include <memory>'?
Patch1:         %{name}-fix-gcc12.patch

# Force qmake to use optflags and to get debuginfo files
Patch2:         %{name}-force_CXXFLAGS.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  chrpath
BuildRequires:  make
BuildRequires:  texlive-latex
BuildRequires:  texlive-babel
BuildRequires:  texlive-babel-english
BuildRequires:  texlive-texlive-scripts
BuildRequires:  texlive-fancyhdr
BuildRequires:  texlive-scheme-basic
BuildRequires:  texlive-latex-base-dev
BuildRequires:  gd-devel
BuildRequires:  dos2unix
BuildRequires:  ghostscript
BuildRequires:  plotutils-devel
BuildRequires:  libEMF-devel
BuildRequires:  libzip-devel
BuildRequires:  ImageMagick-c++-devel
Requires:       ghostscript%{?_isa}

%description
Pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of integrated format
drivers.

%package gui
Summary:        Qt GUI of %{name}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  desktop-file-utils
Requires:       %{name}%{?_isa} = 0:%{version}-%{release}

%description gui
PstoeditQtGui provides an alternative to the command driven operation. The
GUI provides access to almost all options and features that are supported by
pstoedit. In addition it supports the conversion of multiple files in one job
and also provides some shortcuts to some of Ghostscript’s high level
output devices.

%package devel
Summary:        Files for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = 0:%{version}-%{release}

%description devel
This package contains libraries and header files needed for
developing %{name} applications.


%prep
%autosetup -p1 -n pstoedit-%{version}

dos2unix doc/*.htm

%build
autoreconf -if --warnings=all

# Force qmake to use optflags
export OPTFLAGS="%{optflags}"
%configure --disable-static --enable-docs=yes \
           --with-magick --with-libplot --with-emf --with-gui
%make_build

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 doc/pstoedit.1 $RPM_BUILD_ROOT%{_mandir}/man1/
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

chrpath -d $RPM_BUILD_ROOT%{_bindir}/pstoedit
chrpath -d $RPM_BUILD_ROOT%{_bindir}/PstoeditQtGui

# Leave just one main category
desktop-file-edit --remove-category=Utility $RPM_BUILD_ROOT%{_datadir}/applications/PstoeditQtGui.desktop

%files
%doc README.md doc/pstoedit.htm doc/changelog.htm doc/pstoedit.pdf
%license LICENSE
%{_bindir}/pstoedit
%{_libdir}/libpstoedit.so.0.0.0
%{_libdir}/libpstoedit.so.0
%{_libdir}/pstoedit/
%{_datadir}/pstoedit/
%{_mandir}/man1/*

%files gui
%{_bindir}/PstoeditQtGui
%{_datadir}/icons/hicolor/256x256/apps/pstoedit.png
%{_datadir}/applications/PstoeditQtGui.desktop

%files devel
%doc doc/changelog.htm
%{_includedir}/pstoedit/
%{_libdir}/libpstoedit.so
%{_libdir}/pkgconfig/*.pc


%changelog
%autochangelog
