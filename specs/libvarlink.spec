%global _hardened_build 1

Name:           libvarlink
Version:        24
Release:        %autorelease
Summary:        Varlink C Library
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/varlink/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glibc-langpack-de

%description
Varlink C Library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        util
Summary:        Varlink command line tools

%description    util
The %{name}-util package contains varlink command line tools.

%prep
%autosetup

%build
%meson
%meson_build

%check
export LC_CTYPE=C.utf8
# https://github.com/varlink/libvarlink/issues/63
%ifarch ppc64le
test_list=$(%meson_test --list) 2> /dev/null
test_list=${test_list//test-symbols}
%meson_test $test_list
%else
%meson_test
%endif

%install
%meson_install

%files
%license LICENSE
%{_libdir}/libvarlink.so.*

%files util
%{_bindir}/varlink
%{_datadir}/bash-completion/completions/varlink
%{_datadir}/vim/vimfiles/after/*

%files devel
%{_includedir}/varlink.h
%{_libdir}/libvarlink.so
%{_libdir}/pkgconfig/libvarlink.pc

%changelog
%autochangelog
