%global commit 1f1f6c2efc893eed31323caf3469dfe603e85243
%global snapdate 20260620

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

# The file test/subprocess.h is a vendored copy of
# https://github.com/sheredom/subprocess.h, but it is used only for testing and
# does not contribute to the binary RPMs, so we do not treat it as a bundled
# dependency.

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
