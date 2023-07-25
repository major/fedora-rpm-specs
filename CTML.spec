%global debug_package %{nil}

%global common_description %{expand:
CTML is a C++ HTML document constructor, that was designed to be simple to use
and implement. Has no dependencies on any other projects, only the C++ standard
library.}

Name:           CTML
Version:        2.0.0
Release:        %autorelease
Summary:        C++ HTML document constructor only depending on the standard library

License:        MIT
URL:            https://github.com/tinfoilboy/CTML
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  catch2-devel

%description
%{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
%{common_description}

%prep
%autosetup
# Replace bundled copy of catch with the packaged one
ln -sf %{_includedir}/catch2/catch.hpp tests

%build
%cmake
%cmake_build

%install
install -Dpm0644 -t %{buildroot}%{_includedir}/%{name} include/ctml.hpp

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}

%changelog
%autochangelog
