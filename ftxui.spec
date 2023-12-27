%global forgeurl https://github.com/ArthurSonzogni/FTXUI
Version:        5.0.0
%forgemeta

Name:           ftxui
Release:        %autorelease
Summary:        A simple cross-platform C++ library for terminal based user interfaces

License:        MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
%if 0%{?fedora}
# testing dependencies
BuildRequires:  cmake(gtest)
BuildRequires:  cmake(benchmark)
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
%if 0%{?fedora}
    -DFTXUI_BUILD_TESTS=ON \
%else
    -DFTXUI_BUILD_TESTS=OFF \
%endif

%cmake_build

%install
%cmake_install

%check
%if 0%{?fedora}
%ctest
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/libftxui-*.so.%{version}

%files devel
%{_includedir}/ftxui/
%{_libdir}/cmake/ftxui/
%{_libdir}/pkgconfig/ftxui.pc
%{_libdir}/libftxui-*.so

%changelog
%autochangelog
