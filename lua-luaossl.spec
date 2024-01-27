%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname luaossl

Name:           lua-%{luapkgname}
Version:        20200709
Release:        6%{?dist}
Summary:        Most comprehensive OpenSSL module in the Lua universe

License:        MIT
URL:            https://github.com/wahern/%{luapkgname}
Source0:        https://github.com/wahern/%{luapkgname}/archive/rel-%{version}/%{name}-%{version}.tar.gz

Patch1:         openssl-3-compat.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  lua
BuildRequires:  lua-devel

%if 0%{?fedora} || 0%{?rhel} > 7
# BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
%endif

Requires:       lua(abi) = %{luaver}

%description
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        Most comprehensive OpenSSL module in the Lua universe
Requires:       lua(abi) = %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
luaossl is a comprehensive binding to OpenSSL for Lua 5.1, 5.2, and later.
%endif

%package doc
Summary:        Documentation for OpenSSL Lua module
BuildArch:      noarch
Requires:       %{name} = %{version}
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       lua%{luacompatver}-%{luapkgname} = %{version}
%endif

%description doc
Documentation for the Stackable Continuation Queues library
for the Lua Programming Language

%prep
%setup -q -n %{luapkgname}-rel-%{version}

%patch1 -p1

%build
export CFLAGS="%{?optflags} -fPIC"
export LDFLAGS="%{?build_ldflags}"
make LUA_APIS="%{luaver}" %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir}

%if 0%{?fedora} || 0%{?rhel} > 7
make LUA_APIS="%{luacompatver}" %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir} CFLAGS="$CFLAGS -I%{_includedir}/lua-%{luacompatver}"
%endif

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install%{luaver}
install -d -m 0755 %{buildroot}%{_pkgdocdir}
install -p -m 0644 doc/luaossl.pdf %{buildroot}%{_pkgdocdir}/luaossl.pdf

%if 0%{?fedora} || 0%{?rhel} > 7
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install%{luacompatver}
%endif

%files
%{luapkgdir}/openssl
%{luapkgdir}/openssl.lua
%{lualibdir}/_openssl.so
%license LICENSE

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%{luacompatpkgdir}/openssl
%{luacompatpkgdir}/openssl.lua
%{luacompatlibdir}/_openssl.so
%license LICENSE
%endif

%files doc
%{_pkgdocdir}

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200709-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20200709-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200709-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20200709-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20200709-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 02 2022 Jakub Ružička <jakub.ruzicka@nic.cz> - 20200709-1
- Update to latest version 20200709
- Include upstream patch for OpenSSL 3.0.0
- Drop lua 5.4 compat patch included upstream
- Drop HAVE_EVP_KDF_CTX patch which is no longer needed
- Remove redundant doc files entry

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20190731-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 20190731-8
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190731-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20190731-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190731-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Tom Callaway <spot@fedoraproject.org> - 20190731-4
- fix for lua 5.4

* Tue Jun 30 2020 Björn Esser <besser82@fedoraproject.org> - 20190731-3
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20190731-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Tomas Krizek <tomas.krizek@nic.cz> - 20190805-1
- New upstream release https://github.com/wahern/luaossl/releases/tag/rel-20190731
- Use more portable way of passing build flags

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181207-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Tomas Krizek <tomas.krizek@nic.cz> - 20181207-1
- Initial package for F28+ and EPEL 7+
