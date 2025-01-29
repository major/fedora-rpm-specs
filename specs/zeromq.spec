#
%bcond_without pgm
%bcond_without unwind

Name:           zeromq
Version:        4.3.5
Release:        %autorelease
Summary:        Software library for fast, message-based applications

License:        MPL-2.0 AND BSD-3-Clause AND MIT
URL:            https://zeromq.org
Source0:        https://github.com/%{name}/libzmq/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         zeromq-configure-c99.patch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  libsodium-devel

%if %{with unwind}
BuildRequires:  libunwind-devel
%endif

%if %{with pgm}
BuildRequires:  openpgm-devel
BuildRequires:  krb5-devel
%endif

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ZeroMQ shared library.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1

# Remove bundled code.
rm -rf external/wepoll

# Fix permissions.
chmod -x src/xsub.hpp


%build
autoreconf -fi
%configure \
%if %{with pgm}
            --with-pgm \
            --with-libgssapi_krb5 \
%endif
            --with-libsodium \
            --enable-drafts \
%if %{with unwind}
            --enable-libunwind \
%endif
            --disable-Werror \
            --disable-static
%make_build


%install
%make_install

# remove *.la
rm %{buildroot}%{_libdir}/libzmq.la


%check
%ifarch s390x
make check V=1 XFAIL_TESTS=tests/test_radio_dish || ( cat test-suite.log && exit 1 )
%endif


%ldconfig_scriptlets


%files
%doc README.md AUTHORS NEWS
%license LICENSE
%{_bindir}/curve_keygen
%{_libdir}/libzmq.so.5*
%{_mandir}/man3/zmq_*
%{_mandir}/man7/zmq_*
%{_mandir}/man7/zmq.*

%files devel
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*.h


%changelog
%autochangelog

