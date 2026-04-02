%bcond_with devel

# Recent so-version, so we do not bump accidentally.
%global nettle_so_ver 8
%global hogweed_so_ver 6

# * In RHEL nettle is included in the gnutls FIPS module boundary,
#   and HMAC is calculated there with its own tool.
# * In RHEL gmp is statically linked to ensure zeroization of CSP.
%if %{defined rhel}
%bcond_with fipshmac
%bcond_without bundle_gmp
%else
%bcond_without fipshmac
%bcond_with bundle_gmp
%endif

Name:           nettle3.10
Version:        3.10.1
Release:        %{?autorelease}%{!?autorelease:1%{?dist}}
Summary:        Compatibility version of the Nettle library

License:        (LGPL-3.0-or-later OR GPL-2.0-or-later) AND MIT
URL:            http://www.lysator.liu.se/~nisse/nettle/
Source0:	http://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz
Source1:	http://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz.sig
Source2:	nettle-release-keyring.gpg
Patch:		nettle-3.8-zeroize-stack.patch
Patch:		nettle-3.10-hobble-to-configure.patch

%if %{with bundle_gmp}
Source200:	gmp-6.2.1.tar.xz
# Taken from the main gmp package
Source201:	gmp-6.2.1-intel-cet.patch
Source202:	gmp-6.2.1-zeroize-allocator.patch
Source203:	gmp-6.2.1-c23.patch
%endif

BuildRequires: make
BuildRequires:  gcc
%if !%{with bundle_gmp}
BuildRequires:  gmp-devel
%endif
BuildRequires:  m4
BuildRequires:	libtool, automake, autoconf, gettext-devel
%if %{with fipshmac}
BuildRequires:  fipscheck
%endif
BuildRequires:  gnupg2
Conflicts:      nettle < 4.0
Provides:       deprecated()

%if %{with devel}
%package devel
Summary:        Development headers for a low-level cryptographic library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
Conflicts:      nettle-devel
Provides:       deprecated()
%endif

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space. This version of Nettle package contains only the libraries
from the 3.10 version and is provided for compatibility with previous
releases.

%if %{with devel}
%description devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing 
applications with nettle.
%endif


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n nettle-%{version} -Tb 0 -p1

%if %{with bundle_gmp}
mkdir -p bundled_gmp
pushd bundled_gmp
tar --strip-components=1 -xf %{SOURCE200}
patch -p1 < %{SOURCE201}
patch -p1 < %{SOURCE202}
patch -p1 < %{SOURCE203}
popd

# Prevent -lgmp appearing in the compiler command line in dependent components
sed -i '/^Libs.private:/d' hogweed.pc.in
%endif

# Disable -ggdb3 which makes debugedit unhappy
sed s/ggdb3/g/ -i configure

%build
%if %{with bundle_gmp}
pushd bundled_gmp
autoreconf -ifv
%configure --disable-cxx --disable-shared --enable-fat --with-pic
%make_build
popd
%endif

autoreconf -ifv
# For annocheck
export ASM_FLAGS="-Wa,--generate-missing-build-notes=yes"
%configure --enable-shared --enable-fat \
--disable-sm3 --disable-sm4 --disable-ecc-secp192r1 --disable-ecc-secp224r1 \
%if %{with bundle_gmp}
--with-include-path=$PWD/bundled_gmp --with-lib-path=$PWD/bundled_gmp/.libs \
%endif
%{nil}
%make_build

%if %{with fipshmac}
%define fipshmac() \
	fipshmac -d $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_libdir}/%1.* \
	file=`basename $RPM_BUILD_ROOT%{_libdir}/%1.*.hmac` && \
	mv $RPM_BUILD_ROOT%{_libdir}/$file $RPM_BUILD_ROOT%{_libdir}/.$file && \
	ln -s .$file $RPM_BUILD_ROOT%{_libdir}/.%1.hmac

%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	%fipshmac libnettle.so.%{nettle_so_ver} \
	%fipshmac libhogweed.so.%{hogweed_so_ver} \
%{nil}
%endif


%install
%make_install
make install-shared DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{_infodir}
install -p -m 644 nettle.info $RPM_BUILD_ROOT%{_infodir}/
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-lfib-stream
rm -f $RPM_BUILD_ROOT%{_bindir}/pkcs1-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/sexp-conv
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-hash
rm -f $RPM_BUILD_ROOT%{_bindir}/nettle-pbkdf2

chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.%{nettle_so_ver}.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.%{hogweed_so_ver}.*

%if %{without devel}
# Delete devel files
rm -rf $RPM_BUILD_ROOT%{_infodir}/nettle.info
rm -rf $RPM_BUILD_ROOT%{_includedir}/nettle
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig
%endif

%check
make check

%files
%doc AUTHORS NEWS README
%license COPYINGv2 COPYING.LESSERv3
%{_libdir}/libnettle.so.%{nettle_so_ver}
%{_libdir}/libnettle.so.%{nettle_so_ver}.*
%{_libdir}/libhogweed.so.%{hogweed_so_ver}
%{_libdir}/libhogweed.so.%{hogweed_so_ver}.*
%if %{with fipshmac}
%{_libdir}/.libhogweed.so.*.hmac
%{_libdir}/.libnettle.so.*.hmac
%endif

%if %{with devel}
%files devel
%doc descore.README nettle.html nettle.pdf
%{_infodir}/nettle.info.*
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc
%endif

%ldconfig_scriptlets


%changelog
%autochangelog
