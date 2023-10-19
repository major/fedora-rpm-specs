%global debug_package %{nil}
%global ver 0.2.20

Name:           functionalplus
Version:        %{ver}.p0
Release:        %autorelease
Summary:        Functional Programming Library for C++

License:        BSL-1.0
URL:            https://github.com/Dobiasd/FunctionalPlus
Source:         %{url}/archive/v%{ver}-p0/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Functional Programming Library for C++. Write concise and readable C++ code.


%package        devel
Summary:        Header files for %{name}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{summary}.


%prep
%autosetup -n FunctionalPlus-%{ver}-p0


%build
%cmake -DFunctionalPlus_INSTALL_CMAKEDIR=%{_datadir}/cmake/FunctionalPlus
%cmake_build
pushd test
%cmake
%cmake_build
popd


%install
%cmake_install


%check
pushd test
%ctest


%files devel
%license LICENSE
%doc README.md
%{_includedir}/fplus/
%{_datadir}/cmake/FunctionalPlus/


%changelog
%autochangelog
