%global basever 3.0.0
%global prerel rc4
%global commit 3abcd400bdbfc61a2f53f7cf7b240130169154b2
%global shortcommit %{sub %{commit} 1 7}
%global snapdate 20250324

%global somajor 3.0

%global luaver 5.4

# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
%global optflags %optflags -DOPENSSL_NO_ENGINE

Name:           apk-tools
Version:        %{basever}%{?prerel:~%{prerel}}%{?snapdate:^git%{snapdate}.%{shortcommit}}
Release:        1%{?dist}
Summary:        Fast and lightweight package manager originally for Alpine
# libapk AND netbsd-libfetch
SourceLicense:  GPL-2.0-only AND BSD-3-Clause
License:        GPL-2.0-only
URL:            https://gitlab.alpinelinux.org/alpine/apk-tools
%dnl Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

# From: https://gitlab.alpinelinux.org/alpine/apk-tools/-/merge_requests/302
## Fix how meson builds and installs the Python module
Patch0001:      0001-meson-Build-Python-module-using-standard-Meson-pytho.patch
## Fix how meson finds Lua
Patch0002:      0001-meson-Allow-overriding-the-names-of-the-Lua-binary-a.patch

BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  lua-zlib
BuildRequires:  meson
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
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

%package -n python3-apk
Summary:        Python 3 module for the Alpine Package Keeper
Requires:       libapk%{?_isa} = %{version}-%{release}

%description -n python3-apk
The python3-apk package contains a Python 3 module to interface with the
Alpine Package Keeper system.


%files -n python3-apk
%license LICENSE
%{python3_sitearch}/apk*.so

%dnl --------------------------------------------------------------------

%package -n lua-apk
Summary:        Lua module for the Alpine Package Keeper
Requires:       libapk%{?_isa} = %{version}-%{release}

%description -n lua-apk
The lua-apk package contains a Lua module to interface with the Alpine
Package Keeper system.


%files -n lua-apk
%license LICENSE
%{_libdir}/lua/%{luaver}/apk.so

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
%dnl %autosetup -n %{name}-v%{version} -S git_am
%autosetup -n %{name}-%{commit} -S git_am


%conf
%meson -Dlua_version="%{luaver}" -Dlua_bin="lua" -Dlua_pc="lua"


%build
%meson_build


%install
%meson_install

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
%meson_test


%changelog
* Sat Mar 29 2025 Neal Gompa <ngompa@fedoraproject.org> - 3.0.0~rc4^git20250324.3abcd40-1
- Update to post-release git snapshot on 3.0.0~rc4

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Michel Lind <salimma@fedoraproject.org> - 2.14.1-3
- Disable deprecated OpenSSL engine support

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.14.1-1
- Initial package
