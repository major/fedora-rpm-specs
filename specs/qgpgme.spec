# No Qt5 on RHEL 10 and higher
%bcond qt5 %[ 0%{?rhel} < 10 ]
%bcond qt6 1

Name:           qgpgme
Summary:        Qt API bindings/wrapper for GPGME
Epoch:          1
Version:        2.0.0
Release:        3%{?dist}

License:        GPL-2.0-or-later
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.xz
Source1:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://gnupg.org/signature_key.asc

# prevent soname .so.15 conflict for qgpgme with compat-qgpgme124-qt{5,6}
Patch1:         qgpgme-2.0.1-soname2.patch
# for qgpgme <= 2.0.0, rhbz#2464335
# https://github.com/gpg/gpgmeqt/commit/150b23c105f3ea7034e6f106e60686aea4e4a13e
Patch2:         qgpgme-2.0-fixdnparsing.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gpgme) >= %{version}
BuildRequires:  pkgconfig(gpgmepp) >= %{version}
BuildRequires:  pkgconfig(gpg-error) >= 1.47

# to remove RPATH
BuildRequires:  chrpath

%description
%{summary}. GnuPG Made Easy (GPGME) is a library
designed to make access to GnuPG easier for applications.  It provides
a high-level crypto API for encryption, decryption, signing, signature
verification and key management.

%if %{with qt5}
%package -n %{name}-qt5
Summary:        Qt5 API bindings/wrapper for GPGME
Requires:       gpgmepp%{?_isa} >= %{version}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)

%description -n %{name}-qt5
%{summary}.
%endif

%if %{with qt6}
%package -n %{name}-qt6
Summary:        Qt6 API bindings/wrapper for GPGME
Requires:       gpgmepp%{?_isa} >= %{version}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Test)

%description -n %{name}-qt6
%{summary}.
%endif

%if %{with qt5}
%package -n %{name}-qt5-devel
Summary:        Development libraries and header files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
# for fedora 39
Obsoletes:      %{name}-devel < 1.20.0

%description -n %{name}-qt5-devel
%{summary}.
%endif

%if %{with qt6}
%package -n %{name}-qt6-devel
Summary:        Development libraries and header files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{name}-qt6-devel
%{summary}.
%endif

%prep
# verify sources
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p1 -S gendiff


%build
# build qt5/6 bindings qgpgme
%cmake -DENABLE_SHARED=yes -DENABLE_STATIC=no -DBUILD_WITH_QT5=%[%{with qt5}?"ON":"OFF"] -DBUILD_WITH_QT6=%[%{with qt6}]?:"ON":"OFF"]
%cmake_build

%install
%cmake_install

%if %{with qt5}
chrpath -d %{buildroot}%{_libdir}/lib%{name}.so*
%endif
%if %{with qt6}
chrpath -d %{buildroot}%{_libdir}/lib%{name}qt6.so*
%endif

%check
%ctest

%if %{with qt5}
%files -n %{name}-qt5
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib%{name}.so.15*
%endif

%if %{with qt6}
%files -n %{name}-qt6
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib%{name}qt6.so.15*
%endif

%if %{with qt5}
%files -n %{name}-qt5-devel
%{_includedir}/%{name}-qt5/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/QGpgme/
%endif

%if %{with qt6}
%files -n %{name}-qt6-devel
%{_includedir}/%{name}-qt6/
%{_libdir}/lib%{name}qt6.so
%{_libdir}/cmake/QGpgmeQt6/
%endif

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon May 04 2026 Michal Hlavinka <mhlavink@redhat.com> - 1:2.0.0-2
- fix parsing DNs that end with a hex string (rhbz#2464335)

* Wed Feb 04 2026 Michal Hlavinka <mhlavink@redhat.com> - 1:2.0.0-1
- initial build after gpgme split
