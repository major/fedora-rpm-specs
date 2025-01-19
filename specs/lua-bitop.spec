%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global lualibdir %{_libdir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatlibdir %{_libdir}/lua/%{luacompatver}

%if 0%{?fedora} || 0%{?rhel} > 7
%global lualib lua-%{luacompatver}
%else
%global lualib lua
%endif

%global luapkgname bitop

Name:           lua-%{luapkgname}
Version:        1.0.2
Release:        17%{?dist}
Summary:        C extension module for Lua which adds bit-wise operations on numbers

License:        MIT
URL:            http://bitop.luajit.org/
Source0:        http://bitop.luajit.org/download/LuaBitOp-%{version}.tar.gz

BuildRequires: make
BuildRequires:  pkgconfig
BuildRequires:  gcc
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  compat-lua
BuildRequires:  compat-lua-devel
%else
BuildRequires:  lua
BuildRequires:  lua-devel
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       lua
%endif

%description
Lua BitOp is a C extension module for Lua 5.1/5.2 which adds bit-wise
operations on numbers.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        C extension module for Lua %{luacompatver} which adds bit-wise operations on numbers
Requires:       lua(abi) = %{luacompatver}

%description -n lua%{luacompatver}-%{luapkgname}
Lua BitOp is a C extension module for Lua 5.1/5.2 which adds bit-wise
operations on numbers.
%endif

%prep
%setup -q  -n LuaBitOp-%{version}

%build
CFLAGS="%{optflags} -fPIC $(pkg-config --cflags %{lualib})"
LDFLAGS="%{build_ldflags} $(pkg-config --libs %{lualib})"
%make_build CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS"

%install
%if 0%{?fedora} || 0%{?rhel} > 7
install -d -m 0755 %{buildroot}%{luacompatlibdir}
install -p -m 0755 bit.so %{buildroot}%{luacompatlibdir}/bit.so
%else
install -d -m 0755 %{buildroot}%{lualibdir}
install -p -m 0755 bit.so %{buildroot}%{lualibdir}/bit.so
%endif

%if 0%{?rhel} && 0%{?rhel} <= 7
%files
%doc README
%{lualibdir}/bit.so
%endif

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%doc README
%{luacompatlibdir}/bit.so
%endif

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 Tomas Krizek <tomas.krizek@nic.cz> - 1.0.2-4
- Bring the package to F28+ for compat-lua
- Unify spec for Fedora and EPEL
- Remove obsolete Group tag

* Mon Aug 4 2014 - Orion Poplawski <orion@cora.nwra.com> - 1.0.2-3
- Fix install location

* Tue Jul 29 2014 - Orion Poplawski <orion@cora.nwra.com> - 1.0.2-2
- Drop BuildRoot
- Wrap description

* Thu Jun 26 2014 - Orion Poplawski <orion@cora.nwra.com> - 1.0.2-1
- Initial package
