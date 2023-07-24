%global somajor 1

Name:           wget2
Version:        2.0.0
Release:        6%{?dist}
Summary:        An advanced file and recursive website downloader

# Documentation is GFDL
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND GFDL-1.3-or-later
URL:            https://gitlab.com/gnuwget/wget2
Source0:        https://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.gz

# Buildsystem build requirements
BuildRequires:  autoconf
BuildRequires:  autogen
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  flex-devel >= 2.5.35
BuildRequires:  gettext >= 0.18.2
BuildRequires:  gcc
BuildRequires:  make

# Documentation build requirements
BuildRequires:  doxygen
BuildRequires:  pandoc

# Wget2 build requirements
BuildRequires:  bzip2-devel
BuildRequires:  python3
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  texinfo
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(libbrotlidec)
## Not available yet
#BuildRequires:  pkgconfig(libhsts)
BuildRequires:  pkgconfig(libidn2) >= 0.14.0
## Not available yet
#BuildRequires:  pkgconfig(liblz)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpsl)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

# Test suite
BuildRequires:  lcov
BuildRequires:  lzip

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
GNU Wget2 is the successor of GNU Wget, a file and recursive website
downloader.

Designed and written from scratch it wraps around libwget, that provides the
basic functions needed by a web client.

Wget2 works multi-threaded and uses many features to allow fast operation.
In many cases Wget2 downloads much faster than Wget1.x due to HTTP2, HTTP
compression, parallel connections and use of If-Modified-Since HTTP header.

%package libs
Summary:        Runtime libraries for GNU Wget2
# There's some gnulib in there :)
Provides:       bundled(gnulib)

%description libs
This package contains the libraries for applications to use
Wget2 functionality.

%package devel
Summary:        Libraries and header files needed for using wget2 libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers needed for building applications to
use functionality from GNU Wget2.

%prep
%autosetup -p1


%build
%configure --disable-static
# Remove RPATH
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
%make_install
%find_lang %{name}

# Purge all libtool archives
find %{buildroot} -type f -name "*.la" -delete -print


%check
%make_build check


%files -f %{name}.lang
%license COPYING*
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}_noinstall
%{_mandir}/man1/*

%files libs
%license COPYING*
%{_libdir}/libwget*.so.%{somajor}{,.*}

%files devel
%{_includedir}/wget.h
%{_includedir}/wgetver.h
%{_libdir}/libwget*.so
%{_libdir}/pkgconfig/libwget.pc
%{_mandir}/man3/*

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Michal Ruprich <mruprich@redhat.com> - 2.0.0-5
- SPDX migration

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 26 2021 Neal Gompa <ngompa@fedoraproject.org> - 2.0.0-1
- Rebase to 2.0.0 final
- Split out libraries into libs subpackage
- Delete unwanted static subpackage

* Wed Apr  1 2020 Anna Khaitovich <akhaitov@redhat.com> - 1.99.2-1
- Initial package

