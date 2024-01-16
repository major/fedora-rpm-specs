Name:           libpsl
Version:        0.21.5
Release:        %autorelease
Summary:        C library for the Publix Suffix List
License:        MIT
URL:            https://rockdaboot.github.io/libpsl
Source0:        https://github.com/rockdaboot/libpsl/releases/download/%{version}/libpsl-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libicu-devel
BuildRequires:  libidn2-devel
BuildRequires:  libunistring-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  publicsuffix-list
BuildRequires:  python3-devel
Requires:       publicsuffix-list-dafsa

%description
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

Browsers and other web clients can use it to

- Avoid privacy-leaking "supercookies";
- Avoid privacy-leaking "super domain" certificates;
- Domain highlighting parts of the domain in a user interface;
- Sorting domain lists by site;

Libpsl...

- has built-in PSL data for fast access;
- allows to load PSL data from files;
- checks if a given domain is a "public suffix";
- provides immediate cookie domain verification;
- finds the longest public part of a given domain;
- finds the shortest private part of a given domain;
- works with international domains (UTF-8 and IDNA2008 Punycode);
- is thread-safe;
- handles IDNA2008 UTS#46;

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       publicsuffix-list

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%package -n     psl
Summary:        Commandline utility to explore the Public Suffix List

%description -n psl
This package contains a commandline utility to explore the Public Suffix List,
for example it checks if domains are public suffixes, checks if cookie-domain
is acceptable for domains and so on.

%package -n     psl-make-dafsa
Summary:        Compiles the Public Suffix List into DAFSA form
BuildArch:      noarch

%description -n psl-make-dafsa
This script produces C/C++ code or an architecture-independent binary object
which represents a Deterministic Acyclic Finite State Automaton (DAFSA)
from a plain text Public Suffix List.


%prep
%autosetup -p1
rm -frv list
ln -sv %{_datadir}/publicsuffix list
%py3_shebang_fix src/psl-make-dafsa


%build
# Tarballs from github have 2 versions, one is raw files from repo, and
# the other one from CDN contains pre-generated autotools files.
# But makefile hack is not upstreamed yet so we continue reconfiguring these.
# [ -f configure ] || autoreconf -fiv
# autoreconf -fiv

# libicu does allow support for a newer IDN specification (IDN 2008) than
# libidn 1.x (IDN 2003). However, libpsl mostly relies on an internally
# compiled list, which is generated at buildtime and the testsuite thereof
# requires either libidn or libicu only at buildtime; the runtime
# requirement is only for loading external lists, which IIUC neither curl
# nor wget support. libidn2 supports IDN 2008 as well, and is *much* smaller
# than libicu.
#
# curl (as of 7.51.0-1.fc25) and wget (as of 1.19-1.fc26) now depend on libidn2.
# Therefore, we use libidn2 at runtime to help minimize core dependencies.
%configure --disable-silent-rules \
           --disable-static       \
           --enable-man           \
           --enable-gtk-doc       \
           --enable-builtin=libicu \
           --enable-runtime=libidn2 \
           --with-psl-distfile=%{_datadir}/publicsuffix/public_suffix_list.dafsa  \
           --with-psl-file=%{_datadir}/publicsuffix/effective_tld_names.dat       \
           --with-psl-testfile=%{_datadir}/publicsuffix/test_psl.txt

# avoid using rpath
sed -i libtool \
    -e 's|^\(runpath_var=\).*$|\1|' \
    -e 's|^\(hardcode_libdir_flag_spec=\).*$|\1|'

%make_build


%install
%make_install


%check
make check || cat tests/test-suite.log


%files
%license COPYING
%{_libdir}/libpsl.so.5
%{_libdir}/libpsl.so.5.*

%files devel
%doc AUTHORS NEWS
%{_datadir}/gtk-doc/html/libpsl/
%{_includedir}/libpsl.h
%{_libdir}/libpsl.so
%{_libdir}/pkgconfig/libpsl.pc
%{_mandir}/man3/libpsl.3*

%files -n psl
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/psl
%{_mandir}/man1/psl.1*

%files -n psl-make-dafsa
%license COPYING
%{_bindir}/psl-make-dafsa
%{_mandir}/man1/psl-make-dafsa.1*

%changelog
%autochangelog
