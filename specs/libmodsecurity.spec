Name: libmodsecurity
Version: 3.0.14
Release: %autorelease
Summary: A library that loads/interprets rules written in the ModSecurity SecRules

License: Apache-2.0
URL: https://github.com/owasp-modsecurity/ModSecurity

Source0: https://github.com/owasp-modsecurity/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1: https://github.com/owasp-modsecurity/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz.sig
# Key 0B2BA1924065B44691202A2AD286E022149F0F6E
Source2: OWASP_ModSecurity.asc

BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: git-core
# for gpg verification
BuildRequires: gnupg2
BuildRequires: make
BuildRequires: pkgconfig(libcurl)
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: pkgconfig(libmaxminddb)
%else
BuildRequires: pkgconfig(geoip)
%endif
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(lmdb)
BuildRequires: pkgconfig(yajl)
BuildRequires: ssdeep-devel

# libinjection is supposed to be bundled (same as with mod_security 2.x)
# See: https://github.com/client9/libinjection#embedding
Provides: bundled(libinjection) = 3.9.2

%description
Libmodsecurity is one component of the ModSecurity v3 project.
The library codebase serves as an interface to ModSecurity Connectors
taking in web traffic and applying traditional ModSecurity processing.
In general, it provides the capability to load/interpret rules written
in the ModSecurity SecRules format and apply them to HTTP content provided
by your application via Connectors.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package static
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static libraries for developing
applications that use %{name}.



%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n modsecurity-v%{version} -S git


%build
%configure --libdir=%{_libdir} --with-lmdb --with-pcre2 --without-pcre
%make_build


%install
%make_install

# Clean out files that should not be part of the rpm.
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets


%files
%doc README.md AUTHORS
%{_libdir}/*.so.*
%{_bindir}/*
%license LICENSE

%files devel
%doc README.md AUTHORS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig
%license LICENSE

%files static
%{_libdir}/*.a


%changelog
%autochangelog
