%global longver 2024-02-01
%global shortver %(echo %{longver}|sed 's|-||g')

Name:           re2
Version:        %{shortver}
Epoch:          1
Release:        1%{?dist}
Summary:        C++ fast alternative to backtracking RE engines
License:        BSD
URL:            http://github.com/google/re2/
Source0:        https://github.com/google/re2/archive/%{longver}/re2-%{longver}.tar.gz

BuildRequires: cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconf
BuildRequires:  abseil-cpp-devel
BuildRequires:  gtest-devel

%description
RE2 is a C++ library providing a fast, safe, thread-friendly alternative to
backtracking regular expression engines like those used in PCRE, Perl, and
Python.

Backtracking engines are typically full of features and convenient syntactic
sugar but can be forced into taking exponential amounts of time on even small
inputs.

In contrast, RE2 uses automata theory to guarantee that regular expression
searches run in time linear in the size of the input, at the expense of some
missing features (e.g back references and generalized assertions).

%package        devel
Summary:        C++ header files and library symbolic links for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{name}-%{longver}

%build
# The RPM macro for the linker flags does not exist on EPEL
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}

%cmake . \
    -DOVERRIDE_INSTALL_PREFIX=/usr \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DINSTALL_LIBDIR:PATH=%{_libdir} \
    "-GUnix Makefiles"

%cmake_build

%install
%cmake_install

# Suppress the static library
rm -fv %{buildroot}%{_libdir}/libre2.a

%check
%make_build shared-test

%ldconfig_scriptlets

%files
%license LICENSE
%doc README *.md
%{_libdir}/libre2.so.11*

%files devel
%{_includedir}/re2/
%{_libdir}/libre2.so
%{_libdir}/pkgconfig/re2.pc
%{_libdir}/cmake/re2/*.cmake

%changelog
%autochangelog
