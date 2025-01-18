Name:           asio-grpc
Version:        2.8.0
Release:        5%{?dist}
Summary:        Asynchronous gRPC with Asio/unified executors
License:        Apache-2.0
URL:            https://github.com/Tradias/asio-grpc
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# This is a header-only package
BuildArch:      noarch
BuildRequires:  cmake
# It checks for this but doesn't actually use it.
BuildRequires:  gcc-c++
# These are for the test suite, which uh, doesn't actually build sanely.
# BuildRequires:  zlib-devel
# BuildRequires:  c-ares-devel
# BuildRequires:  openssl-devel
# BuildRequires:  protobuf-devel
# BuildRequires:  re2-devel
# BuildRequires:  boost-devel
# BuildRequires:  liburing-devel
# BuildRequires:  git
# BuildRequires:  doxygen
# BuildRequires:  graphviz
# BuildRequires:  doctest-devel
# BuildRequires:  asio-devel

%description
An Executor, Networking TS and std::execution interface to
grpc::CompletionQueue for writing asynchronous gRPC clients and servers using
C++20 coroutines, Boost.Coroutines, Asio's stackless coroutines, callbacks,
sender/receiver and more.

%package        devel
Summary:        Development files for asio-grpc
Requires:       boost-devel, asio-devel, liburing-devel

%description    devel
The asio-grpc-devel package contains libraries and header files for
developing applications that use asio-grpc.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install

# move cmake files out of an arch specific dir
mkdir -p %{buildroot}%{_datadir}/cmake
mv %{buildroot}/usr/lib*/cmake/asio-grpc %{buildroot}%{_datadir}/cmake/

%check

# %%files

%files devel
%license LICENSE
%doc README.md
%{_datadir}/cmake/asio-grpc/
%{_includedir}/agrpc/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 22 2023 Tom Callaway <spot@fedoraproject.org> - 2.8.0-1
- update to 2.8.0

* Wed Nov 22 2023 Tom Callaway <spot@fedoraproject.org> - 2.7.0-1
- Initial packaging
