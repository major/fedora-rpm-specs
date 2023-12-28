%global debug_package %{nil}

Name:           functionalplus
Version:        0.2.22
Release:        %autorelease
Summary:        Functional Programming Library for C++

License:        BSL-1.0
URL:            https://github.com/Dobiasd/FunctionalPlus
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

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
%autosetup -n FunctionalPlus-%{version}


%build
%cmake -DFunctionalPlus_INSTALL_CMAKEDIR=%{_datadir}/cmake/FunctionalPlus
%cmake_build
%ifnarch %{ix86}
pushd test
%cmake
%cmake_build
popd
%endif

%install
%cmake_install


%check
%ifnarch %{ix86}
pushd test
%ctest
%endif


%files devel
%license LICENSE
%doc README.md
%{_includedir}/fplus/
%{_datadir}/cmake/FunctionalPlus/


%changelog
%autochangelog
