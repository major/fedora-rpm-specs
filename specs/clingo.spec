Name:       clingo
Version:    5.8.0
Release:    %autorelease
Summary:    A grounder and solver for logic programs

License:    MIT
URL:        https://potassco.org/clingo/
Source0:    https://github.com/potassco/clingo/archive/v%{version}/%{name}-%{version}.tar.gz
# Disable gcc warning no-class-memaccess, which is intended use in this case
Patch0:     clingo.clasp-disable-class-memaccess-warning.patch

BuildRequires: bison
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3-setuptools
BuildRequires: re2c

%description
Clingo is part of the Potassco project for Answer Set Programming
(ASP). ASP offers a simple and powerful modeling language to describe
combinatorial problems as logic programs. The clingo system then takes
such a logic program and computes answer sets representing solutions
to the given problem.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n lua-%{name}
Summary:        Lua bindings for Clingo
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  lua-devel

%description -n lua-%{name}
Lua bindings for Clingo, a grounder and solver for logic programs.

Detailed information (including a User's manual), source code, and pre-compiled
binaries are available at: http://potassco.org/

%package -n python3-%{name}
Summary:        Python 3 bindings for Clingo
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python3, python3-devel
BuildRequires:  python3-cffi
BuildRequires:  make
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This module provides functions and classes to work with ground terms and to
control the instantiation process. In clingo builts, additional functions to
control and inspect the solving process are available.

Functions defined in a python script block are callable during the
instantiation process using @-syntax. The default grounding/solving process can
be customized if a main function is provided.

Detailed information (including a User's manual), source code, and pre-compiled
binaries are available at: http://potassco.org/


%prep
%autosetup -p1


%build
%cmake \
  -DCLINGO_MANAGE_RPATH:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DCLINGO_BUILD_APPS:BOOL=ON \
  -DPython_EXECUTABLE=%{__python3} \
  -DCLINGO_BUILD_SHARED:BOOL=ON \
  -DCLINGO_BUILD_WITH_PYTHON:BOOL=ON \
  -DLUACLINGO_INSTALL_DIR:PATH=%{lua_libdir}

%cmake_build


%install
%cmake_install

%files
%doc README.md INSTALL.md
%license LICENSE.md
%{_libdir}/libclingo.so.4*
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Clingo

%files -n lua-%{name}
%{lua_libdir}/%{name}.so

%files -n python3-%{name}
%{python3_sitearch}/%{name}*

%changelog
%autochangelog
