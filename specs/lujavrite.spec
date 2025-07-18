Name:           lujavrite
Version:        1.2.1
Release:        %autorelease
Summary:        Lua library for calling Java code
License:        Apache-2.0
URL:            https://github.com/mizdebsk/lujavrite
ExclusiveArch:  %{java_arches}

Source:         https://github.com/mizdebsk/lujavrite/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

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

%build
export LDFLAGS=-llua-5.4
export JAVA_HOME=%{_jvmdir}/jre-25-openjdk
./build.sh

%install
install -D -p -m 0755 lujavrite.so %{buildroot}%{lua_libdir}/%{name}.so

%check
export JAVA_HOME=%{_jvmdir}/jre-25-openjdk
lua test.lua

%files
%{lua_libdir}/*
%license LICENSE NOTICE
%doc README.md

%changelog
%autochangelog
