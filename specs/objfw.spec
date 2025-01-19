%global toolchain clang
# LTO makes configure's double endianess test fail.
%global _lto_cflags %nil

Name:          objfw
Version:       1.2.3
Release:       2%{?dist}
Summary:       Portable, lightweight framework for the Objective-C language

License:       LGPL-3.0-only
URL:           https://objfw.nil.im
Source0:       https://objfw.nil.im/downloads/objfw-%{version}.tar.gz
Source1:       https://objfw.nil.im/downloads/objfw-%{version}.tar.gz.sig
# gpg2 --export --export-options export-minimal DC43171B6BE93978D09AD8B2C601EE21773E7C8F >gpgkey-objfw.gpg
Source2:       gpgkey-%{name}.gpg

Patch0:        utils-pie.patch

BuildRequires: clang
BuildRequires: make
BuildRequires: pkgconfig(gnutls)
BuildRequires: gnupg2
BuildRequires: doxygen
BuildRequires: lksctp-tools-devel
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
Requires:      libobjfwhid-devel%{_isa} = %{version}-%{release}

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

%package -n libobjfwhid
Summary:       HID support for ObjFW

%description -n libobjfwhid
The libobjfwhid package contains HID support for ObjFW.

%package -n libobjfwhid-devel
Summary:       Header files and libraries for libobjfwhid
Requires:      libobjfwhid%{_isa} = %{version}-%{release}
Requires:      libobjfw-devel%{_isa} = %{version}-%{release}
Requires:      libobjfwrt-devel%{_isa} = %{version}-%{release}

%description -n libobjfwhid-devel
The libobjfwhid-devel package contains header files and libraries for HID
support for ObjFW.

%package -n ofarc
Summary:       Utility for handling ZIP, Tar, LHA and Zoo archives

%description -n ofarc
ofarc is a multi-format archive utility that allows creating, listing,
extracting and modifying ZIP, Tar, LHA and Zoo archives using ObjFW's classes
for various archive types.

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
%license COPYING
%license COPYING.LESSER

%files -n libobjfw
%license COPYING
%license COPYING.LESSER
%{_libdir}/libobjfw.so.1{,.*}

%files -n libobjfw-devel
%license COPYING
%license COPYING.LESSER
%{_bindir}/objfw-compile
%{_bindir}/objfw-config
%{_bindir}/objfw-embed
%{_bindir}/objfw-new
%{_includedir}/ObjFW
%{_includedir}/ObjFWTest
%{_libdir}/libobjfw.so
%{_libdir}/libobjfwtest.a
%{_libdir}/objfw-config/ObjFWTest.oc
%{_mandir}/man1/objfw-compile.1.gz
%{_mandir}/man1/objfw-config.1.gz
%{_mandir}/man1/objfw-embed.1.gz
%{_mandir}/man1/objfw-new.1.gz

%files -n libobjfwrt
%license COPYING
%license COPYING.LESSER
%{_libdir}/libobjfwrt.so.1{,.*}

%files -n libobjfwrt-devel
%license COPYING
%license COPYING.LESSER
%{_includedir}/ObjFWRT
%{_libdir}/libobjfwrt.so

%files -n libobjfwtls
%license COPYING
%license COPYING.LESSER
%{_libdir}/libobjfwtls.so.1{,.*}

%files -n libobjfwtls-devel
%license COPYING
%license COPYING.LESSER
%{_includedir}/ObjFWTLS
%{_libdir}/libobjfwtls.so
%{_libdir}/objfw-config/ObjFWTLS.oc

%files -n libobjfwhid
%license COPYING
%license COPYING.LESSER
%{_libdir}/libobjfwhid.so.1{,.*}

%files -n libobjfwhid-devel
%license COPYING
%license COPYING.LESSER
%{_includedir}/ObjFWHID
%{_libdir}/libobjfwhid.so
%{_libdir}/objfw-config/ObjFWHID.oc

%files -n ofarc
%license COPYING
%license COPYING.LESSER
%{_bindir}/ofarc
%{_datadir}/ofarc
%{_mandir}/man1/ofarc.1.gz

%files -n ofdns
%license COPYING
%license COPYING.LESSER
%{_bindir}/ofdns
%{_datadir}/ofdns
%{_mandir}/man1/ofdns.1.gz

%files -n ofhash
%license COPYING
%license COPYING.LESSER
%{_bindir}/ofhash
%{_datadir}/ofhash
%{_mandir}/man1/ofhash.1.gz

%files -n ofhttp
%license COPYING
%license COPYING.LESSER
%{_bindir}/ofhttp
%{_datadir}/ofhttp
%{_mandir}/man1/ofhttp.1.gz

%files doc
%license COPYING
%license COPYING.LESSER
%{_docdir}/objfw

%autochangelog
