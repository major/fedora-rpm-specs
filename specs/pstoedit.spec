Name:           pstoedit
Version:        4.02
Release:        %autorelease
Summary:        Translates PostScript and PDF graphics into other vector formats
License:        GPL-2.0-or-later
URL:            http://www.pstoedit.net
Source0:        https://sourceforge.net/projects/pstoedit/files/pstoedit/%{version}/pstoedit-%{version}.tar.gz

# Fix cflags of the pkg-config file
Patch0:         pstoedit-pkglibdir.patch

# drvpptx.cpp:68:1: note: 'std::unique_ptr' is defined in header '<memory>'; did you forget to '#include <memory>'?
Patch1:         pstoedit-fix-gcc12.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gd-devel
BuildRequires:  dos2unix
BuildRequires:  ghostscript
BuildRequires:  plotutils-devel
BuildRequires:  %{?dts}gcc-c++, %{?dts}gcc
BuildRequires:  libzip-devel
%if ! (0%{?rhel} >= 8)
BuildRequires:  ImageMagick-c++-devel
%endif
BuildRequires:  libEMF-devel
Requires:       ghostscript%{?_isa}

%description
Pstoedit converts PostScript and PDF files to various vector graphic
formats. The resulting files can be edited or imported into various
drawing packages. Pstoedit comes with a large set of integrated format
drivers


%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files needed for developing %{name}
applications


%prep
%autosetup -N

%patch -P 0 -p1
%if 0%{?fedora} || 0%{?rhel} > 9
%patch -P 1 -p1
%endif

dos2unix doc/*.htm doc/readme.txt

%build
autoreconf -fiv
%configure --disable-static --enable-docs=no --with-libzip-include=%{_includedir} \
           --with-magick --with-libplot
%make_build

%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm 644 doc/pstoedit.1 $RPM_BUILD_ROOT%{_mandir}/man1/
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%files
%doc doc/readme.txt doc/pstoedit.htm doc/changelog.htm doc/pstoedit.pdf
%license copying
%{_datadir}/pstoedit/
%{_mandir}/man1/*
%{_bindir}/pstoedit
%{_libdir}/libpstoedit.so.0.0.0
%{_libdir}/libpstoedit.so.0
%{_libdir}/pstoedit/

%files devel
%doc doc/changelog.htm
%{_includedir}/pstoedit/
%{_libdir}/libpstoedit.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4


%changelog
%autochangelog
