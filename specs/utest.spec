%global commit fb622dc480a56cc53ac9562a4436281bef91c989
%global snapdate 20250831

Name:           utest
Version:        0^%{snapdate}.%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Single header unit testing framework for C and C++

License:        Unlicense
URL:            https://github.com/sheredom/utest.h
Source:         %{url}/archive/%{commit}/utest.h-%{commit}.tar.gz

# For tests:
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

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
sed -r -i 's/-Werror//' test/CMakeLists.txt


%conf
cd test
%cmake


%build
cd test
%cmake_build


%install
install -t '%{buildroot}%{_includedir}' -D -p -m 0644 utest.h


%check
cd test
# Note that utest_cmdline.filter_with_list only works if the current working
# directory contains the test executable.
cd %{_vpath_builddir}
for testbin in utest_test*
do
  printf '\n==== %s ====\n\n' "${testbin}" 1>&2
  "./${testbin}"
done


%files devel
%license LICENSE
%doc README.md

%{_includedir}/utest.h


%changelog
%autochangelog
