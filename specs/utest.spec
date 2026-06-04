%global commit aca9d89481e13f583ce35a715be286c89c9e0161
%global snapdate 20260602

Name:           utest
Version:        0^%{snapdate}.%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Single header unit testing framework for C and C++

License:        Unlicense
URL:            https://github.com/sheredom/utest.h
Source:         %{url}/archive/%{commit}/utest.h-%{commit}.tar.gz

# For tests:
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

# No compiled binaries are installed, so this would be empty.
%global debug_package %{nil}

%global common_description %{expand:
A simple one header solution to unit testing for C/C++.}

%description %{common_description}


%package devel
Summary:        Development files for %{name}

BuildArch:      noarch

# Header-only library
Provides:       %{name}-static = %{version}-%{release}

%description devel %{common_description}

The %{name}-devel package contains header files for developing applications
that use %{name}.


%prep
%autosetup -n utest.h-%{commit}

# -Werror is too strict for distribution packaging:
sed --regexp-extended --in-place 's/-Werror//' test/CMakeLists.txt


%conf
cd test
%cmake


%build
cd test
%cmake_build


%install
install -D --preserve-timestamps --mode=0644 \
    --target='%{buildroot}%{_includedir}' utest.h


%check
cd test
%ctest


%files devel
%license LICENSE
%doc README.md

%{_includedir}/utest.h


%changelog
%autochangelog
