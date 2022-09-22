Name:           gloox
Epoch:          1
Version:        1.0.23
Release:        %autorelease
Summary:        A rock-solid, full-featured Jabber/XMPP client C++ library
License:        GPLv3
URL:            https://camaya.net/gloox
Source0:        https://camaya.net/download/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  gnutls-devel >= 1.2
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel >= 0.5
BuildRequires:  zlib-devel >= 1.2.3
BuildRequires: make

%description
gloox is a rock-solid, full-featured Jabber/XMPP client library written in
C++. It makes writing spec-compliant clients easy and allows for hassle-free
integration of Jabber/XMPP functionality into existing applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnutls-devel%{?_isa}
Requires:       libidn-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{name}-%{version}%{?prerel}
# recode to UTF
mv -f AUTHORS AUTHORS.old
iconv -f iso8859-1 -t UTF-8 AUTHORS.old > AUTHORS
sed -i 's|sys/time.h>|sys/time.h>\n#include <time.h>|' src/tests/*/*perf.cpp
sed -e '1 i #include <time.h>' -i src/examples/*pp

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%check
# Tests are broken since F27, needs bugreport
make check

%ldconfig_scriptlets

%files
%license LICENSE
%{_libdir}/libgloox.so.17*

%files devel
%doc AUTHORS ChangeLog TODO UPGRADING
%{_bindir}/%{name}-config
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libgloox.so

%changelog
%autochangelog
