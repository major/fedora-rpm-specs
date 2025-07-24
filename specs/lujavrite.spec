Name:           lujavrite
Version:        1.2.2
Release:        %autorelease
Summary:        Lua library for calling Java code
License:        Apache-2.0
URL:            https://github.com/mizdebsk/lujavrite
ExclusiveArch:  %{java_arches}

Source:         https://github.com/mizdebsk/lujavrite/releases/download/%{version}/lujavrite-%{version}.tar.zst

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  java-25-openjdk-devel

%{?lua_requires}

%description
LuJavRite is a rock-solid Lua library that allows calling Java code
from Lua code.  It does so by launching embedded Java Virtual Machine
and using JNI interface to invoke Java methods.

%prep
%autosetup -p1 -C

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{lua_libdir}/*
%license LICENSE NOTICE
%doc README.md

%changelog
%autochangelog
