%global _hardened_build 1

%bcond_without python3
%bcond_without  perl
%bcond_without  ecdsa
%bcond_without  eddsa
%bcond_without  dane_ta
# GOST is not allowed in Fedora/RHEL due to legal reasons (not NIST ECC)
%bcond_with     gost

%if %{with python3}
%{?filter_setup:
%global _ldns_internal_filter /^_ldns[.]so.*/d;
%filter_from_requires %{_ldns_internal_filter}
%filter_from_provides %{_ldns_internal_filter}
%filter_setup
}
%global _ldns_internal _ldns[.]so[.].*
%global __requires_exclude ^(%{_ldns_internal})$
%global __provides_exclude ^(%{_ldns_internal})$
%endif

%if %{with perl}
%{?perl_default_filter}
%endif

%global forgeurl https://github.com/NLnetLabs/%{name}
%global downloadurl https://www.nlnetlabs.nl/downloads/%{name}

Summary: Low-level DNS(SEC) library with API
Name: ldns
Version: 1.9.2
Release: %autorelease

License: BSD-3-Clause
Url: https://www.nlnetlabs.nl/ldns/
Vcs: git:%{forgeurl}
Source0: %{downloadurl}/%{name}-%{version}.tar.gz
Source1: %{downloadurl}/%{name}-%{version}.tar.gz.asc
# https://nlnetlabs.nl/downloads/keys/releases-g2.asc
Source2: nlnetlabs2026-g2.asc
Patch1: ldns-1.7.0-multilib.patch

# https://github.com/NLnetLabs/ldns/pull/288
Patch8: ldns-1.9-std23-bool.patch

BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: autoconf-archive

BuildRequires: gcc, make
BuildRequires: libpcap-devel
BuildRequires: openssl-devel >= 1.1.0
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: gnupg2

%if %{with python3}
BuildRequires: python3-devel, swig
%endif
%if %{with perl}
BuildRequires: perl-devel
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: perl-generators
BuildRequires: perl(Devel::CheckLib)
# workaround for koji / perl bug
BuildRequires: perl-interpreter
%endif
Requires: ca-certificates

%description
ldns is a library with the aim to simplify DNS programming in C. All
low-level DNS/DNSSEC operations are supported. We also define a higher
level API which allows a programmer to (for instance) create or sign
packets.

%package devel
Summary: Development package that includes the ldns header files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig openssl-devel

%description devel
The devel package contains the ldns library and the include files

%package utils
Summary: DNS(SEC) utilities for querying dns
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Collection of tools to get, check or alter DNS(SEC) data.


%if %{with python3}
%package -n python3-ldns
Summary: Python3 extensions for ldns
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-ldns}

%description -n python3-ldns
Python3 extensions for ldns
%endif


%if %{with perl}
%package -n perl-ldns
Summary: Perl extensions for ldns
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n perl-ldns
Perl extensions for ldns
%endif

%package doc
Summary: Documentation for the ldns library
BuildArch: noarch

%description doc
This package contains documentation for the ldns library

%prep
%{?extra_version:%global pkgname %{name}-%{version}%{extra_version}}%{!?extra_version:%global pkgname %{name}-%{version}}
%if 0%{?fedora}
%gpgverify -d 0 -s 1 -k 2
%endif

%autosetup -n %{pkgname} -p1

rm -f config.guess config.sub ltmain.sh
# Use ax_python_devel from autoconf-archive
cp -p %{_datadir}/aclocal/{ax_python_devel,ax_pkg_swig}.m4 .
aclocal
libtoolize -c --install
autoreconf --install

# copy common doc files - after here, since it may be patched
cp -p contrib/ldnsx/LICENSE LICENSE.ldnsx
cp -p contrib/ldnsx/README README.ldnsx


%build
CFLAGS="%{optflags} -fPIC -fno-strict-aliasing -DOPENSSL_NO_ENGINE"
CXXFLAGS="%{optflags} -fPIC -fno-strict-aliasing -DOPENSSL_NO_ENGINE"
LDFLAGS="$RPM_LD_FLAGS -Wl,-z,now -pie"
export CFLAGS CXXFLAGS LDFLAGS

%if %{with gost}
  %global enable_gost --enable-gost
%else
  %global enable_gost --disable-gost
%endif

%if %{with ecdsa}
  %global enable_ecdsa --enable-ecdsa
%else
  %global enable_ecdsa --disable-ecdsa
%endif

%if %{with eddsa}
  %global enable_eddsa --enable-ed25519 --enable-ed448
%else
  %global enable_eddsa --disable-ed25519 --disable-ed448
%endif

%if ! %{with dane_ta}
  %global disable_dane_ta --disable-dane-ta-usage
%endif

%global common_args \\\
  --disable-rpath \\\
  %{enable_gost} %{enable_ecdsa} %{enable_eddsa} %{?disable_dane_ta} \\\
  --with-ca-file=/etc/pki/tls/certs/ca-bundle.trust.crt \\\
  --with-ca-path=/etc/pki/tls/certs/ \\\
  --with-trust-anchor=%{_sharedstatedir}/unbound/root.key \\\
  --disable-static \\\

%configure \
  %{common_args} \
  --with-examples \
  --with-drill \
%if %{with python3}
  --with-pyldns PYTHON=%{__python3}
%endif

# Using 'make' instead of 'make_build' macro to prevent build from failing
make
%make_build doc

# Multilib conflict avoidance
sed -e "s,-L%{_libdir},," -i packaging/ldns-config

# We cannot use the built-in --with-p5-dns-ldns
%if %{with perl}
  pushd contrib/DNS-LDNS
  LD_LIBRARY_PATH="../../lib:$LD_LIBRARY_PATH" perl \
      Makefile.PL INSTALLDIRS=vendor  INC="-I. -I../.." LIBS="-L../../lib"
  %make_build -j1
  popd
%endif

# specfic hardening options should not end up in ldns-config
sed -i "s~$RPM_LD_FLAGS~~" packaging/ldns-config



%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
%make_install

# remove .la files
rm -rf %{buildroot}%{_libdir}/*.la
%if %{with python3}
rm -rf %{buildroot}%{python3_sitearch}/*.la
%endif

%if %{with perl}
  %make_install -j1 -C contrib/DNS-LDNS pure_install
  chmod 755 %{buildroot}%{perl_vendorarch}/auto/DNS/LDNS/LDNS.so
  rm -f %{buildroot}%{perl_vendorarch}/auto/DNS/LDNS/{.packlist,LDNS.bs}
  rm -f %{buildroot}%{perl_archlib}/perllocal.pod
%endif

# don't package xml files
rm doc/*.xml
# don't package building script for install-doc in doc section
rm doc/doxyparse.pl
# remove double set of man pages
rm -rf doc/man

%ldconfig_scriptlets

%files
%doc README
%license LICENSE
%{_libdir}/libldns.so.3*

%files utils
%{_bindir}/drill
%{_bindir}/ldnsd
%{_bindir}/ldns-chaos
%{_bindir}/ldns-compare-zones
%{_bindir}/ldns-[d-z]*
%{_mandir}/man1/drill*
%{_mandir}/man1/%{name}*

%files devel
%doc Changelog README.git
%{_libdir}/libldns.so
%{_libdir}/pkgconfig/ldns.pc
%{_bindir}/ldns-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_mandir}/man3/%{name}*.3*

%if %{with python3}
%files -n python3-ldns
%doc contrib/python/Changelog README.ldnsx
%license LICENSE.ldnsx
%pycached %{python3_sitearch}/%{name}.py
%pycached %{python3_sitearch}/%{name}x.py
%{python3_sitearch}/_%{name}.so*
%endif

%if %{with perl}
%files -n perl-ldns
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/DNS::LDNS*.3pm.gz
%endif

%files doc
%doc doc/dns-lib-implementations
%doc doc/TODO
%doc doc/*.css
%doc doc/images/
%doc doc/html/
%doc doc/*.dox

%changelog
%autochangelog
