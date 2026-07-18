Name:           gpgmepp
Summary:        C++ bindings/wrapper for GPGME
Version:        2.0.0
Release:        2%{?dist}
Epoch:          1

License:        LGPL-2.0-or-later
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.xz
Source1:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://gnupg.org/signature_key.asc

Requires:       gpgme%{?_isa} >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gpgme) >= %{version}
BuildRequires:  pkgconfig(gpg-error) >= 1.47
BuildRequires:  gpgverify

%description
%{summary}. GnuPG Made Easy (GPGME) is a library designed
to make access to GnuPG easier for applications.  It provides 
a high-level crypto API for encryption, decryption, signing,
signature verification and key management.

%package devel
Summary:        Development libraries and header files for %{name}
Provides:       gpgme-pp-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gpgme-devel%{?_isa} >= %{version}

%description devel
%{summary}.

%prep
# verify sources
%{gpgverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -p1 -S gendiff

%build
%cmake -DENABLE_SHARED=yes -DENABLE_STATIC=no
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS NEWS README ChangeLog
%license COPYING*
%{_libdir}/lib%{name}.so.7*

%files devel
%{_includedir}/gpgme++/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/Gpgmepp/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Mon May 04 2026 Michal Hlavinka <mhlavink@redhat.com> - 1:2.0.0-1
- initial build after split from gpgme
