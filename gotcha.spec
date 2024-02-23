Name:           gotcha
Version:        1.0.5
Release:        %autorelease
Summary:        A library for wrapping function calls to shared libraries

License:        LGPL-2.1-only
URL:            https://github.com/llnl/gotcha
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  python3dist(sphinx)
# Exclude leaf architecture where build fails
ExcludeArch:    %{ix86}

%description
Gotcha is a library that wraps functions. Tools can use gotcha to install hooks
into other libraries, for example putting a wrapper function around libc's
malloc.  It is similar to LD_PRELOAD, but operates via a programmable API. This
enables easy methods of accomplishing tasks like code instrumentation or
wholesale replacement of mechanisms in programs without disrupting their source
code.

%package devel

Summary:        A library for wrapping function calls to shared libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development header and cmake configuration files for Gotcha.

%prep
%autosetup -n GOTCHA-%{version}
# Use shared library for testing
sed -i 's/libcheck.a/libcheck.so/g' test/unit/CMakeLists.txt
# Use standard optimiztaion levels to enable regular build flags
sed -i 's/-O0 //g' test/hammer/CMakeLists.txt
# Broken test, reported upstream
# https://github.com/LLNL/GOTCHA/issues/136
sed -i '/symver/d' test/CMakeLists.txt

%build
%cmake -DGOTCHA_ENABLE_TESTS=ON -DDEPENDENCIES_PREINSTALLED=TRUE
%cmake_build
# Build Documentation
pushd docs
sphinx-build . -b man man
popd

%install
%cmake_install
# install documentation
mkdir -p %{buildroot}/%{_mandir}/man1
cp -p docs/man/gotcha.1 %{buildroot}/%{_mandir}/man1

%check
ctest

%files
%license COPYRIGHT
%license LGPL
%doc README.md
%{_mandir}/man1/gotcha.1*
%{_libdir}/libgotcha.so.2
%{_libdir}/libgotcha.so.2.*

%files devel
%dir %{_includedir}/gotcha
%{_includedir}/gotcha/gotcha.h
%{_includedir}/gotcha/gotcha_types.h
%dir %{_libdir}/cmake/gotcha
%{_libdir}/cmake/gotcha/*.cmake
%{_libdir}/libgotcha.so

%changelog
%autochangelog
