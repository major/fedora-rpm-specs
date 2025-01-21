%global _description %{expand:
s2n-tls is a C99 implementation of the TLS/SSL protocols that is
designed to be simple, small, fast, and with security as a priority.}

Name:           s2n-tls
Version:        1.5.10
Release:        2%{?dist}
Summary:        A C99 implementation of the TLS/SSL protocols

License:        Apache-2.0
URL:            https://github.com/aws/s2n-tls
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Install cmake files in 'libdir/cmake/s2n-tls' rather than 'libdir/s2n-tls/cmake'
Patch:          s2n-tls-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
# openssl/engine.h moved into sub-package since f41
# https://src.fedoraproject.org/rpms/openssl/c/e67e9d9c40cd2cb9547e539c658e2b63f2736762?branch=rawhide
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  ninja-build

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# Dependencies like aws-c-common don't support and build on s390x
# Upstream issue: https://github.com/awslabs/aws-c-common/issues/1111
# Fedora bugzilla ticket to be created after package review
ExcludeArch: s390x

%description %{_description}


%package devel
Summary:        %{summary}
Requires:       openssl-devel%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel %{_description}


%package doc
Summary:        %{summary}
BuildArch:      noarch

%description doc %{_description}


%prep
%autosetup -p1


%build
%cmake -GNinja -DBUILD_SHARED_LIBS=ON -DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install
# install documentation
mkdir -p %{buildroot}/%{_docdir}/s2n-tls/docs
mkdir -p %{buildroot}/%{_docdir}/s2n-tls/docs/examples
mkdir -p %{buildroot}/%{_docdir}/s2n-tls/docs/images
install -p -m 644 docs/*.md %{buildroot}/%{_docdir}/s2n-tls/docs/
install -p -m 644 docs/examples/*.c %{buildroot}/%{_docdir}/s2n-tls/docs/examples/
install -p -m 644 docs/images/*.png %{buildroot}/%{_docdir}/s2n-tls/docs/images/
install -p -m 644 docs/images/*.svg %{buildroot}/%{_docdir}/s2n-tls/docs/images/


%check
%ctest


%files
%license LICENSE NOTICE
%doc README.md VERSIONING.rst
%{_libdir}/libs2n.so.1{,.*}


%files devel
%{_libdir}/libs2n.so
%{_includedir}/s2n.h
%{_includedir}/s2n/
%{_libdir}/cmake/s2n/


%files doc
%license LICENSE NOTICE
%dir %{_docdir}/s2n-tls/
%{_docdir}/s2n-tls/docs/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 21 2024 Packit <hello@packit.dev> - 1.5.10-1
- Update to version 1.5.10
- Resolves: rhbz#2332744

* Thu Nov 14 2024 Packit <hello@packit.dev> - 1.5.9-1
- Update to version 1.5.9
- Resolves: rhbz#2316588

* Fri Sep 20 2024 Packit <hello@packit.dev> - 1.5.3-1
- Update to version 1.5.3
- Resolves: rhbz#2307472, rhbz#2304838, rhbz#2304837, rhbz#2304681

* Sun Aug 11 2024 Packit <hello@packit.dev> - 1.5.0-1
- Update to version 1.5.0
- Resolves: rhbz#2299427

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 10 2024 Dominik Wombacher <dominik@wombacher.cc> - 1.4.17-2
- BuildRequires openssl-devel-engine for f41 and above

* Thu Jul 4 2024 Packit <hello@packit.dev> - 1.4.17-1
- Update to version 1.4.17
- Resolves: rhbz#2295720

* Thu Jun 6 2024 Packit <hello@packit.dev> - 1.4.16-1
- Update to version 1.4.16
- Resolves: rhbz#2282290

* Wed May 15 2024 Dominik Wombacher <dominik@wombacher.cc> - 1.4.14-1
- update to 1.4.14

* Tue Sep 26 2023 Benson Muite <benson_muite@emailplus.org> - 1.3.51-1
- Initial packaging
