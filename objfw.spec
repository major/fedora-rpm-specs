%global toolchain clang
# LTO makes configure's double endianess test fail.
%global _lto_cflags %nil

Name:          objfw
Version:       1.0.4
Release:       1%{?dist}
Summary:       Portable, lightweight framework for the Objective-C language

License:       QPL-1.0 OR GPL-3.0-only OR GPL-2.0-only
URL:           https://objfw.nil.im
Source0:       https://objfw.nil.im/downloads/objfw-%{version}.tar.gz
Source1:       https://objfw.nil.im/downloads/objfw-%{version}.tar.gz.sig
# gpg2 --export --export-options export-minimal 6D1EC2269BC0B5459C8BA920CFDAB41F8292CEEE >gpgkey-objfw.gpg
Source2:       gpgkey-%{name}.gpg

Patch0:        utils-pie.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: clang
BuildRequires: make
BuildRequires: pkgconfig(gnutls)
BuildRequires: gnupg2
BuildRequires: doxygen
Requires:      libobjfw%{_isa} = %{version}-%{release}
Requires:      libobjfw-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwrt%{_isa} = %{version}-%{release}
Requires:      libobjfwrt-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwtls%{_isa} = %{version}-%{release}
Requires:      libobjfwtls-devel%{_isa} = %{version}-%{release}
Requires:      ofarc%{_isa} = %{version}-%{release}
Requires:      ofdns%{_isa} = %{version}-%{release}
Requires:      ofhash%{_isa} = %{version}-%{release}
Requires:      ofhttp%{_isa} = %{version}-%{release}

%description
ObjFW is a portable, lightweight framework for the Objective-C language. It
enables you to write an application in Objective-C that will run on any
platform supported by ObjFW without having to worry about differences between
operating systems or various frameworks you would otherwise need if you want to
be portable.

It supports all modern Objective-C features when using Clang, but is also
compatible with GCC ≥ 4.6 to allow maximum portability.

ObjFW also comes with its own lightweight and extremely fast Objective-C
runtime, which in real world use cases was found to be significantly faster
than both GNU's and Apple's runtime.

%package -n libobjfw
Summary:       ObjFW library
Requires:      libobjfwrt%{_isa} = %{version}-%{release}

%description -n libobjfw
The libobjfw package contains the library needed by programs using ObjFW.

%package -n libobjfw-devel
Summary:       Header files, libraries and tools for libobjfw
Requires:      libobjfw%{_isa} = %{version}-%{release}
Requires:      libobjfwrt-devel%{_isa} = %{version}-%{release}

%description -n libobjfw-devel
The libobjfw-devel package contains the header files, libraries and tools to
develop programs using ObjFW.

%package -n libobjfwrt
Summary:       ObjFW Objective-C runtime library

%description -n libobjfwrt
The libobjfwrt package contains ObjFW's Objective-C runtime library.

%package -n libobjfwrt-devel
Summary:       Header files and libraries for libobjfwrt
Requires:      libobjfwrt%{_isa} = %{version}-%{release}

%description -n libobjfwrt-devel
The libobjfwrt-devel package contains header files and libraries for ObjFW's
Objective-C runtime library.

%package -n libobjfwtls
Summary:       TLS support for ObjFW

%description -n libobjfwtls
The libobjfwtls package contains TLS support for ObjFW.

%package -n libobjfwtls-devel
Summary:       Header files and libraries for libobjfwtls
Requires:      libobjfwtls%{_isa} = %{version}-%{release}
Requires:      libobjfw-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwrt-devel%{_isa} = %{version}-%{release}

%description -n libobjfwtls-devel
The libobjfwtls-devel package contains header files and libraries for TLS
support for ObjFW.

%package -n ofarc
Summary:       Utility for handling ZIP, Tar and LHA archives

%description -n ofarc
ofarc is a multi-format archive utility that allows creating, listing,
extracting and modifying ZIP, Tar and LHA archives using ObjFW's classes for
various archive types.

%package -n ofdns
Summary:       Utility for performing DNS requests on the command line

%description -n ofdns
ofdns is an utility for performing DNS requests on the command line using
ObjFW's DNS resolver.

%package -n ofhash
Summary:       Utility to hash files with various cryptographic hash functions

%description -n ofhash
ofhash is an utility to hash files with various cryptographic hash functions
(even using different algorithms at once) using ObjFW's classes for various
cryptographic hashes.

%package -n ofhttp
Summary:       Command line downloader for HTTP(S)

%description -n ofhttp
ofhttp is a command line downloader for HTTP and HTTPS using ObjFW's
OFHTTPClient class. It supports all features one would expect from a modern
command line downloader such as resuming of downloads, using a SOCKS5 proxy, a
modern terminal-based UI, etc.

%package doc
Summary:       Documentation for ObjFW
BuildArch:     noarch

%description doc
Documentation for ObjFW.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p0

%build
%configure OBJC=clang             \
           OBJCFLAGS="$CFLAGS"    \
           --with-tls=gnutls      \
           --disable-rpath        \
           --disable-silent-rules
%make_build
make docs

%install
%make_install
mkdir -p %{buildroot}%{_docdir}
cp -r docs %{buildroot}%{_docdir}/objfw

%check
make check

%files
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL

%files -n libobjfw
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_libdir}/libobjfw.so.1{,.*}

%files -n libobjfw-devel
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_bindir}/objfw-compile
%{_bindir}/objfw-config
%{_bindir}/objfw-embed
%{_bindir}/objfw-new
%{_includedir}/ObjFW
%{_libdir}/libobjfw.so

%files -n libobjfwrt
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_libdir}/libobjfwrt.so.1{,.*}

%files -n libobjfwrt-devel
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_includedir}/ObjFWRT
%{_libdir}/libobjfwrt.so

%files -n libobjfwtls
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_libdir}/libobjfwtls.so.1{,.*}

%files -n libobjfwtls-devel
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_includedir}/ObjFWTLS
%{_libdir}/libobjfwtls.so

%files -n ofarc
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_bindir}/ofarc
%{_datadir}/ofarc

%files -n ofdns
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_bindir}/ofdns
%{_datadir}/ofdns

%files -n ofhash
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_bindir}/ofhash
%{_datadir}/ofhash

%files -n ofhttp
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_bindir}/ofhttp
%{_datadir}/ofhttp

%files doc
%license LICENSE.GPLv2
%license LICENSE.GPLv3
%license LICENSE.QPL
%{_docdir}/objfw

%autochangelog
