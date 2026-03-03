%bcond check 1

Name: coeurl
Version: 0.3.2
Release: %autorelease

License: MIT
URL: https://nheko.im/nheko-reborn/%{name}
Summary: Simple async wrapper around CURL for C++
Source0: %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

%if %{with check}
BuildRequires: cmake
BuildRequires: doctest-devel
BuildRequires: openssl
BuildRequires: python3dist(flask)
%endif

BuildRequires: fmt-devel
BuildRequires: libcurl-devel
BuildRequires: libevent-devel
BuildRequires: spdlog-devel

BuildRequires: gcc-c++
BuildRequires: meson
BuildRequires: ninja-build

%description
Simple library to do http requests asynchronously via CURL in C++.

Based on the CURL-libevent example.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson \
    -Dwerror=false \
%if %{with check}
    -Dtests=true \
%else
    -Dtests=false \
%endif
    -Dexamples=false
%meson_build

%install
%meson_install

%if %{with check}
%check
scripts/run_testserver.sh &
scripts/run_tls_testserver.sh &
# self-signed cert generation takes a few seconds
sleep 5
%meson_test
%endif

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/lib%{name}.so.0.3

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
