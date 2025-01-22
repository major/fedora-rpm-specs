# Upstream version is 2.0.0 but has no release
%global snapdate 20240426
%global commit d725c816bb26483ac397ce0d19de5ad2972955f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})


Name:           libxeddsa
Version:        2.0.0^%{snapdate}git%{shortcommit}
Release:        7%{?dist}
Summary:        Toolkit around Curve25519 and Ed25519 key pairs

# ref10 library is Public Domain (under ref10/ subdirectory)
License:        MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libsodium-devel
BuildRequires:  libsodium-static
# For docs:
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-breathe

%description
An implementation of XEdDSA, based on ref10 by Daniel J. Bernstein.

XEdDSA is a signature scheme that utilizes the birational maps between
Curve25519 and Ed25519 (defined in RFC 7748 on page 5) to create and
verify digital signatures with Curve25519 keys.

XEdDSA is also specified for Curve448/Ed448, which is not covered by
this library.

This library has a set of functions surrounding Curve25519 and Ed25519
key pairs, to make this library a toolset around both curves instead
of just an implementation of XEdDSA.



%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains HTML documentation for developing
applications that use %{name}.



%prep
%autosetup -n %{name}-%{commit}


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
# results are in redhat-linux-build/
%cmake_build
# Build HTML documentation
pushd docs/
make html  # results are in docs/_build/html/
popd


%install
%cmake_install
# INCLUDE_INSTALL_DIR=/usr/include is not used by the project
install -D -p -m 0644 include/xeddsa.h %{buildroot}%{_includedir}/xeddsa.h
# Install html docs
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -pr docs/_build/html %{buildroot}%{_pkgdocdir}/
# Remove buildinfo sphinx documentation
rm -rf %{buildroot}%{_pkgdocdir}/html/.buildinfo
# Remove static library
rm -f %{buildroot}/%{_libdir}/*.a


%check
%ctest -C Debug



%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.*


%files devel
%{_libdir}/%{name}.so
%{_includedir}/xeddsa.h


%files doc
%{_pkgdocdir}/html/



%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0^20240426gitd725c81-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0^20240426gitd725c81-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 26 2024 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0^20240426gitd725c81-5
- Package Review RHBZ#2227804:
  - Update git snapshot
  - Fix Version field and Release field
  - Fix license

* Thu Aug 24 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0-4^20230824git1140086
- Package Review RHBZ#2227804:
  - Update git snapshot
  - Improve %%description about ref10 library
  - Fix cmake flags in %%build section
  - Cleanup %%install section and remove useless comments
  - Fix filename in %%files section

* Wed Aug 2 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0-3^20230730git8ab957a
- Package Review RHBZ#2227804:
  - Improve file ownership in doc subpackage
  - Add more comments about soname of the library

* Tue Aug 1 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0-2^20230730git8ab957a
- Package Review RHBZ#2227804:
  - Remove %%cmake_install then manually install library file in %%install section

* Mon Jul 31 2023 Matthieu Saulnier <fantom@fedoraproject.org> - 2.0.0-1^20230730git8ab957a
- Package Review RHBZ#2227804:
  - Initial packaging
