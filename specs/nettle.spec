# Recent so-version, so we do not bump accidentally.
%global nettle_so_ver 8
%global hogweed_so_ver 6

# Set to 1 when building a bootstrap for a bumped so-name.
%global bootstrap 0

%if 0%{?bootstrap}
%global version_old 3.5.1
%global nettle_so_ver_old 7
%global hogweed_so_ver_old 5
%endif

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

Name:           nettle
Version:        3.10.1
Release:        %{?autorelease}%{!?autorelease:1%{?dist}}
Summary:        A low-level cryptographic library

License:        LGPL-3.0-or-later OR GPL-2.0-or-later
URL:            http://www.lysator.liu.se/~nisse/nettle/
Source0:	http://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz
Source1:	http://www.lysator.liu.se/~nisse/archive/%{name}-%{version}.tar.gz.sig
Source2:	nettle-release-keyring.gpg
%if 0%{?bootstrap}
Source100:	%{name}-%{version_old}-hobbled.tar.xz
Source101:	nettle-3.5-remove-ecc-testsuite.patch
%endif
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

%package devel
Summary:        Development headers for a low-level cryptographic library
Requires:       %{name} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}

%description
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.

%description devel
Nettle is a cryptographic library that is designed to fit easily in more
or less any context: In crypto toolkits for object-oriented languages
(C++, Python, Pike, ...), in applications like LSH or GNUPG, or even in
kernel space.  This package contains the files needed for developing 
applications with nettle.


%prep
%autosetup -Tb 0 -p1

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

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

%if 0%{?bootstrap}
mkdir -p bootstrap_ver
pushd bootstrap_ver
tar --strip-components=1 -xf %{SOURCE100}
patch -p1 < %{SOURCE101}

# Disable -ggdb3 which makes debugedit unhappy
sed s/ggdb3/g/ -i configure
sed 's/ecc-192.c//g' -i Makefile.in
sed 's/ecc-224.c//g' -i Makefile.in
popd
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

%if 0%{?bootstrap}
pushd bootstrap_ver
autoconf
%configure --with-tests
%make_build
popd
%endif

%if %{with fipshmac}
%define fipshmac() \
	fipshmac -d $RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_libdir}/%1.* \
	file=`basename $RPM_BUILD_ROOT%{_libdir}/%1.*.hmac` && \
	mv $RPM_BUILD_ROOT%{_libdir}/$file $RPM_BUILD_ROOT%{_libdir}/.$file && \
	ln -s .$file $RPM_BUILD_ROOT%{_libdir}/.%1.hmac

%if 0%{?bootstrap}
%define bootstrap_fips 1
%endif

%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	%fipshmac libnettle.so.%{nettle_so_ver} \
	%fipshmac libhogweed.so.%{hogweed_so_ver} \
	%{?bootstrap_fips:%fipshmac libnettle.so.%{nettle_so_ver_old}} \
	%{?bootstrap_fips:%fipshmac libhogweed.so.%{hogweed_so_ver_old}} \
%{nil}
%endif


%install
%if 0%{?bootstrap}
make -C bootstrap_ver install-shared-nettle DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
make -C bootstrap_ver install-shared-hogweed DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libnettle.so.%{nettle_so_ver_old}.*
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/libhogweed.so.%{hogweed_so_ver_old}.*
%endif

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

%check
make check

%files
%doc AUTHORS NEWS README
%license COPYINGv2 COPYING.LESSERv3
%{_infodir}/nettle.info.*
%{_libdir}/libnettle.so.%{nettle_so_ver}
%{_libdir}/libnettle.so.%{nettle_so_ver}.*
%{_libdir}/libhogweed.so.%{hogweed_so_ver}
%{_libdir}/libhogweed.so.%{hogweed_so_ver}.*
%if 0%{?bootstrap}
%{_libdir}/libnettle.so.%{nettle_so_ver_old}
%{_libdir}/libnettle.so.%{nettle_so_ver_old}.*
%{_libdir}/libhogweed.so.%{hogweed_so_ver_old}
%{_libdir}/libhogweed.so.%{hogweed_so_ver_old}.*
%endif
%if %{with fipshmac}
%{_libdir}/.libhogweed.so.*.hmac
%{_libdir}/.libnettle.so.*.hmac
%endif

%files devel
%doc descore.README nettle.html nettle.pdf
%{_includedir}/nettle
%{_libdir}/libnettle.so
%{_libdir}/libhogweed.so
%{_libdir}/pkgconfig/hogweed.pc
%{_libdir}/pkgconfig/nettle.pc

%ldconfig_scriptlets


%changelog
%autochangelog
