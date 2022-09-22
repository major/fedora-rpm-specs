Name:           duktape
Version:        2.6.0
Release:        %autorelease
Summary:        Embeddable Javascript engine
License:        MIT
Url:            http://duktape.org/
Source0:        http://duktape.org/%{name}-%{version}.tar.xz
Source1:        duktape.pc.in
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  make

%description
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description    devel
Embeddable Javascript engine.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%setup -q

sed -e's|@prefix@|%{_prefix}|' \
    -e's|@libdir@|%{_lib}|' \
    -e's|@PACKAGE_VERSION@|%{version}|' \
    < %{SOURCE1} > %{name}.pc.in

%build
sed -e '/^INSTALL_PREFIX/s|[^=]*$|%{_prefix}|' \
    -e '/install\:/a\\tinstall -d $(DESTDIR)$(INSTALL_PREFIX)/%{_lib}\n\tinstall -d $(DESTDIR)$(INSTALL_PREFIX)/include' \
    -e 's/\(\$.INSTALL_PREFIX.\)/$(DESTDIR)\1/g' \
    -e 's/\/lib\b/\/%{_lib}/g' \
     < Makefile.sharedlibrary > Makefile
%make_build

%install
%make_install

install -Dm0644 %{name}.pc.in %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%ldconfig_scriptlets

%files
%license LICENSE.txt
%doc AUTHORS.rst
%{_libdir}/libduktape.so.*
%{_libdir}/libduktaped.so.*

%files devel
%doc examples/ README.rst
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_libdir}/libduktape.so
%{_libdir}/libduktaped.so
%{_libdir}/pkgconfig/duktape.pc

%changelog
%autochangelog
