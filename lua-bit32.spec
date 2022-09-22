# see https://luarocks.org/modules/siffiejoe/bit32/5.3.5-1
%global srcname lua-compat-5.3
%global srcver 0.10

%global lua_pkg_name bit32

%global lua51_version 5.1
%global lua51_libdir %{_libdir}/lua/%{lua51_version}
%global lua51_pkgdir %{_datadir}/lua/%{lua51_version}
%global lua51_builddir %{_builddir}/lua%{lua51_version}-%{lua_pkg_name}-%{version}-%{release}

Name:           lua-%{lua_pkg_name}
Version:        5.3.5.1
Release:        %autorelease
Summary:        Lua bit manipulation library

License:        MIT
URL:            https://luarocks.org/modules/siffiejoe/bit32
Source0:        https://github.com/keplerproject/%{srcname}/archive/v%{srcver}.tar.gz#/%{srcname}-%{srcver}.tar.gz

BuildRequires:  gcc
BuildRequires:  lua-devel >= 5.1
BuildRequires:  compat-lua-devel >= %{lua51_version}

%if 0%{?rhel} < 9
Requires:       lua(abi) = %{lua_version}
%endif

%global _description %{expand:
bit32 is a bit manipulation library, in the version from Lua
5.3; it is compatible with Lua 5.1 to 5.4.}

%description %{_description}

%package -n lua%{lua51_version}-%{lua_pkg_name}
Summary:        Lua 5.2 bit manipulation library
Provides:       compat-%{name}
Requires:       lua(abi) = %{lua51_version}

%description -n lua%{lua51_version}-%{lua_pkg_name} %{_description}


%prep
%autosetup -n %{srcname}-%{srcver}


%build
gcc %{optflags} $(pkg-config --cflags lua) -I./c-api -DLUA_COMPAT_BITLIB \
    lbitlib.c \
    -shared -fPIC -o lua-bit32.so $(pkg-config --libs lua)

gcc %{optflags} $(pkg-config --cflags lua-5.1) -I./c-api -DLUA_COMPAT_BITLIB \
    lbitlib.c \
    -shared -fPIC -o compat-lua-bit32.so $(pkg-config --libs lua-5.1)


%install
install -d -m 0755 %{buildroot}%{lua_libdir}
install -m 0755 lua-bit32.so %{buildroot}%{lua_libdir}/bit32.so

install -d -m 0755 %{buildroot}%{lua51_libdir}
install -m 0755 compat-lua-bit32.so %{buildroot}%{lua51_libdir}/bit32.so


%files
%license LICENSE
# README.md doesn't mention bit32
%{lua_libdir}/bit32.so

%files -n lua%{lua51_version}-%{lua_pkg_name}
%{lua51_libdir}/bit32.so


%changelog
%autochangelog
