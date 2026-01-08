
%global debug_package %{nil}

%global forgeurl https://github.com/ThePhD/sol2
Version: 3.5.0
Release:        %{autorelease}
%global tag v%{version}


%forgemeta

Name:           sol2
Summary:        a C++ <-> Lua API wrapper with advanced features and top notch performance
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  ninja-build
BuildRequires: lua-devel >= 5.4
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
BuildRequires: python3-breathe


%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:  lua-devel >= 5.4

%description devel
%{summary}.

%package devel-docs
Summary:        API documentation for %{name}-devel
Requires: %{name}-devel = %{version}-%{release}
BuildArch:  noarch

%description devel-docs
%{summary}.

%prep
%{forgesetup}


%build
%cmake -G Ninja \
                -DSOL2_CI=ON \
                -DSOL2_BUILD_LUA=OFF \
                -DSOL2_LUA_VERSION=5.4 \
                -DSOL2_DOCS=ON

%cmake_build

%install
%cmake_install


#diabling tests as package tests require internet connection


%files devel
%{_includedir}/sol/
%{_datadir}/cmake/sol2/
%{_datadir}/pkgconfig/sol2.pc
%doc README.md
%license LICENSE.txt

%files devel-docs
%doc %{_datadir}/doc/sol2/
%exclude %{_datadir}/doc/sol2/sphinx/.*


%changelog
%autochangelog
