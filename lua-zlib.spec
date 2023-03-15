%global forgeurl https://github.com/brimworks/lua-zlib
%global tag v%{version}

Name:      lua-zlib
Version:   1.2
Release:   1%{?dist}
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
* Tue Nov 15 2022 Jonny Heggheim <hegjon@gmail.com> - 1.2-1
- Initial package
