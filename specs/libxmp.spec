%global abi 4

Name: libxmp
Version: 4.6.1
Release: %autorelease
Summary: A multi-format module playback library
Source0: https://downloads.sourceforge.net/project/xmp/libxmp/%{version}/libxmp-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: make
Provides: bundled(md5-plumb)
# most of the files are covered by MIT, except:
# src/depackers/bunzip2.c: 0BSD
# src/depackers/lhasa: ISC
# src/depackers/s404_dec.c: public-domain
# src/depackers/xfnmatch.[ch]: BSD-3-Clause
# src/md5.[ch]: public-domain
# src/mkstemp.c: BSD-3-Clause
License: 0BSD AND BSD-3-Clause AND ISC AND MIT AND LicenseRef-Fedora-Public-Domain
URL: http://xmp.sourceforge.net/

%description
Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker (MOD),
Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse Tracker (IT).

Many compressed module formats are supported, including popular Unix, DOS,
and Amiga file packers including gzip, bzip2, SQSH, Powerpack, etc.

%package devel
Summary: A multi-format module playback library development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake-filesystem

%description devel
Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker (MOD),
Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse Tracker (IT).

Many compressed module formats are supported, including popular Unix, DOS,
and Amiga file packers including gzip, bzip2, SQSH, Powerpack, etc.

This package contains the header and development library.

%prep
%setup -q
for file in docs/Changelog ; do
        iconv -f iso8859-1 -t utf8 -o $file.utf $file && touch -r $file $file.utf && mv $file.utf $file
done

%build
%configure
%make_build

%install
%make_install
install -Dpm644 docs/libxmp.3 %{buildroot}%{_mandir}/man3/libxmp.3
chmod 755 %{buildroot}%{_libdir}/libxmp.so.*

%check
%make_build check

%files
%license docs/COPYING
%doc README docs/Changelog docs/CREDITS
%{_libdir}/libxmp.so.%{abi}{,.*}

%files devel
%doc docs/libxmp.html docs/libxmp.pdf docs/{fixloop,formats}.txt
%{_includedir}/xmp.h
%{_mandir}/man3/libxmp.3*
%{_libdir}/cmake/libxmp/libxmp-config-version.cmake
%{_libdir}/cmake/libxmp/libxmp-config.cmake
%{_libdir}/pkgconfig/libxmp.pc
%{_libdir}/libxmp.so

%changelog
%autochangelog
