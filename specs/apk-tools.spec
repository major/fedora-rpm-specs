%global somajor 2

%global luaver 5.4

%global makeopts SBINDIR=%{_sbindir} \\\
     LIBDIR=%{_libdir} \\\
     DOCDIR=%{_docdir}/apk-tools \\\
     PKGCONFIGDIR=%{_libdir}/pkgconfig \\\
     LUA=lua LUA_VERSION=%{luaver} LUA_PC=lua LUA_LIBDIR=%{_libdir}/lua/%{luaver} \\\
     %{nil}

# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
%global optflags %optflags -DOPENSSL_NO_ENGINE

Name:           apk-tools
Version:        2.14.1
Release:        4%{?dist}
Summary:        Fast and lightweight package manager originally for Alpine
# libapk AND netbsd-libfetch
SourceLicense:  GPL-2.0-only AND BSD-3-Clause
License:        GPL-2.0-only
URL:            https://gitlab.alpinelinux.org/alpine/apk-tools
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  lua-zlib
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(zlib)

# Provide the user-friendly package name
Provides:       apk = %{version}-%{release}
Provides:       apk%{?_isa} = %{version}-%{release}

Requires:       libapk%{?_isa} = %{version}-%{release}

%description
The Alpine Package Keeper (APK) is a suite of tools to implement the
package management solution made for Alpine Linux.


%files
%license LICENSE
%doc README.md
%{_sbindir}/apk
%{_mandir}/man?/apk*
%dir %{_sysconfdir}/apk
%ghost %{_sysconfdir}/apk/{arch,keys,repositories,world}
%dir %{_localstatedir}/cache/apk

%dnl --------------------------------------------------------------------

%package -n lua-apk
Summary:        Lua module for the Alpine Package Keeper
Requires:       libapk%{?_isa} = %{version}-%{release}

%description -n lua-apk
The lua-apk package contains a Lua module to interface with the Alpine
Package Keeper system.


%files -n lua-apk
%license LICENSE
%{_libdir}/lua/*/apk.so

%dnl --------------------------------------------------------------------

%package -n libapk
Summary:        Core library for the Alpine Package Keeper
# libapk AND netbsd-libfetch
License:        GPL-2.0-only AND BSD-3-Clause
# Modified version of NetBSD libfetch adapted for apk-tools
Provides:       bundled(netbsd-libfetch)

%description -n libapk
The libapk package contains libraries used by applications that leverage
the Alpine Package Keeper system.


%files -n libapk
%license LICENSE
%{_libdir}/libapk.so.%{somajor}{,.*}

%dnl --------------------------------------------------------------------

%package -n libapk-devel
Summary:        Development files for libapk
Requires:       libapk%{?_isa} = %{version}-%{release}

%description -n libapk-devel
The libapk-devel package contains libraries and header files for
developing applications that use libapk.


%files -n libapk-devel
%{_includedir}/apk/
%{_libdir}/libapk.so
%{_libdir}/pkgconfig/apk.pc

%dnl --------------------------------------------------------------------

%prep
%autosetup -n %{name}-v%{version}


%build
%set_build_flags
%make_build %{makeopts}


%install
%make_install %{makeopts}

# Delete static archives
find %{buildroot} -name '*.a' -exec rm -f {} ';'

# Remove pointless exec bit from man pages
find %{buildroot}%{_mandir} -type f -exec chmod -x {} ';'

# Own configuration data locations
mkdir -p %{buildroot}%{_sysconfdir}/apk
touch %{buildroot}%{_sysconfdir}/apk/{arch,keys,repositories,world}

# Own cachedir location
mkdir -p %{buildroot}%{_localstatedir}/cache/apk


%check
%make_build %{makeopts} check


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Michel Lind <salimma@fedoraproject.org> - 2.14.1-3
- Disable deprecated OpenSSL engine support

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.14.1-1
- Initial package
