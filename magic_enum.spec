%global debug_package %{nil}

%global common_description %{expand:
Magic Enum is a header-only C++17 library that provides static reflection for
enums, working with any enum type without any macro or boilerplate code.}

Name:           magic_enum
Version:        0.9.5
Release:        %autorelease
Summary:        Static reflection for enums for modern C++

License:        MIT
URL:            https://github.com/Neargye/magic_enum
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  catch2-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description    %{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

%prep
%autosetup -p1

# Replace bundled copy of Catch2 with the system one
ln -sf %{_includedir}/catch2/catch.hpp test/3rdparty/Catch2/include/catch2/

%build
%cmake
%cmake_build

%install
%cmake_install

# This is meant for use with ROS and isn't actually useful
rm %{buildroot}%{_datadir}/%{name}/package.xml

%check
%ctest

%files devel
%license LICENSE
%doc README.md doc
%{_includedir}/%{name}*.hpp
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
