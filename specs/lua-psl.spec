%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}

%global luapkgname psl

Name:           lua-%{luapkgname}
Version:        0.3
Release:        16%{?dist}
Summary:        Lua bindings to Public Suffix List library

License:        MIT
URL:            https://github.com/daurnimator/lua-psl
Source0:        https://github.com/daurnimator/lua-psl/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig
BuildRequires:  gcc
BuildRequires:  libpsl-devel
BuildRequires:  lua
BuildRequires:  lua-devel

%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
%endif

Requires:       lua(abi) = %{luaver}

%description
Lua bindings to libpsl, a C library that handles the Public Suffix List (PSL).

The PSL is a list of domains where there may be sub-domains outside of the
administrator's control. e.g. the administrator of '.com' does not manage
'github.com'.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        Lua %{luacompatver} bindings to Public Suffix List library
Requires:       lua(abi) = %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
Lua %{luacompatver} bindings to libpsl, a C library that handles the Public
Suffix List (PSL).

The PSL is a list of domains where there may be sub-domains outside of the
administrator's control. e.g. the administrator of '.com' does not manage
'github.com'.
%endif

%prep
%setup -q -n %{name}-%{version}

%build
gcc -fPIC %{?optflags} $(pkg-config --cflags lua libpsl) -o psl/psl.o -c psl/psl.c
gcc -shared %{?build_ldflags} -o psl.so psl/psl.o $(pkg-config --libs lua libpsl)

%if 0%{?fedora} || 0%{?rhel} > 7
gcc -fPIC %{?optflags} $(pkg-config --cflags lua-%{luacompatver} libpsl) -o psl/psl.o -c psl/psl.c
gcc -shared %{?build_ldflags} -o psl-%{luacompatver}.so psl/psl.o $(pkg-config --libs lua-%{luacompatver} libpsl)
%endif

%install
install -d -m 0755 %{buildroot}%{lualibdir}
install -p -m 0755 psl.so %{buildroot}%{lualibdir}/psl.so
%if 0%{?fedora} || 0%{?rhel} > 7
install -d -m 0755 %{buildroot}%{luacompatlibdir}
install -p -m 0755 psl-%{luacompatver}.so %{buildroot}%{luacompatlibdir}/psl.so
%endif

%files
%license LICENSE
%{lualibdir}/psl.so

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%license LICENSE
%{luacompatlibdir}/psl.so
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3-5
- Rebuilt for Lua 5.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.3-2
- Make LDFLAGS order comaptible with -Wl,--as-needed (F30+)

* Wed Jul 17 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.3-1
- Initial package for F29+ and EPEL7
