%global forgeurl https://github.com/brimworks/lua-zlib
%global tag v%{version}

Name:      lua-zlib
Version:   1.2
Release:   6%{?dist}
Summary:   Simple streaming interface to zlib for Lua
License:   MIT
URL:       %{forgeurl}

%forgemeta
Source:    %{forgesource}

BuildRequires: lua-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: zlib-devel


%description
%{summary}.


%prep
%forgesetup


%build
%make_build linux \
  LUAPATH=%{lua_pkgdir} \
  LUACPATH=%{lua_libdir} \
  INCDIR="-I%{_includedir}" \
  CFLAGS="$CFLAGS -fPIC" \
  LDFLAGS="$LDFLAGS -shared -fPIC"

%install
install -dD %{buildroot}%{lua_libdir}
%make_install LUACPATH=%{buildroot}%{lua_libdir}


%check
lua test.lua


%files
%license README
%doc README
%{lua_libdir}/zlib.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Nov 15 2022 Jonny Heggheim <hegjon@gmail.com> - 1.2-1
- Initial package
