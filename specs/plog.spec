# This is a header only library
%global debug_package %{nil}

Name:           plog
Version:        1.1.10
Release:        5%{?dist}
Summary:        Portable, simple and extensible C++ logging library

License:        MIT
URL:            https://github.com/SergiusTheBest/plog
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%global _description %{expand:
Plog is a C++ logging library that is designed to be as simple,
small and flexible as possible. It is created as an alternative
to existing large libraries and provides some unique features
as CSV log format and wide string support.}

%description %{_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel %{_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%cmake -DPLOG_BUILD_TESTS=ON
%cmake_build


%install
%cmake_install

# Delete wrongly installed doc content, we'll docify later
rm -rv %{buildroot}%{_datadir}/doc/%{name}


%check
%ctest


%files devel
%license LICENSE
%doc README.md doc
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 10 2023 Neal Gompa <ngompa@fedoraproject.org> - 1.1.10-1
- Initial package
