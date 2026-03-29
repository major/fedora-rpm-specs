%global forgeurl      https://github.com/cisco/mlspp
%global commit        61e4d76dbe6628cbe36ffb9cab684f3bee390d05
%forgemeta

Name:           mlspp
Version:        0.1.0
Release:        %{autorelease}
Summary:        Implementation of Messaging Layer Security

License:        BSD-2-Clause
URL:            %{forgeurl}
Source:         %{forgesource}
Patch:          soname.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  openssl-devel
# Tests
BuildRequires:  catch-devel
BuildRequires:  doctest-devel

%description
Implementation of the proposed Messaging Layer Security protocol in C++.
Depends on C++17, STL for data structures, and OpenSSL or BoringSSL for
crypto.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n mlspp-%{commit}


%build
# Not all tested ciphers are enabled on Fedora
%cmake -DTESTING=OFF

%cmake_build


%install
%cmake_install
# Package separately as license file
rm %{buildroot}%{_datadir}/mlspp/copyright
rm -r  %{buildroot}%{_datadir}/mlspp/

%check
# No-op
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libbytes.so.{,0*}
%{_libdir}/libhpke.so.{,0*}
%{_libdir}/libmls_ds.so.{,0*}
%{_libdir}/libmls_vectors.so.{,0*}
%{_libdir}/libmlspp.so.{,0*}
%{_libdir}/libtls_syntax.so.{,0*}

%files devel
%{_includedir}/mlspp/
%{_libdir}/libbytes.so
%{_libdir}/libhpke.so
%{_libdir}/libmls_ds.so
%{_libdir}/libmls_vectors.so
%{_libdir}/libmlspp.so
%{_libdir}/libtls_syntax.so
%{_datadir}/MLSPP/

%changelog
%autochangelog
