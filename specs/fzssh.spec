Name: fzssh
Version: 1.4.0
Release: 1%{?dist}
URL: https://fzssh.filezilla-project.org/
Summary: SSH/SFTP library based on libfilezilla
License: AGPL-3.0-or-later WITH AdditionRef-fzssh AND MIT
# Also putty components under MIT

# Must be downloaded with browser
Source0: https://download.filezilla-project.org/%{name}/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: gmp-devel
BuildRequires: nettle-devel
BuildRequires: libargon2-devel
BuildRequires: libfilezilla-devel
BuildRequires: meson

%description
fzssh is a SSH/SFTP library based on libfilezilla

%package devel
Summary: Development files for fzssh
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
fzssh is a SSH/SFTP library based on libfilezilla

This package contains files needed to compile code using libfilezilla.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license agpl3.txt
%doc NEWS README
%{_libdir}/libfzssh.so.14*
%{_libdir}/libfzssh-client.so.14*
%{_libdir}/libfzssh-crypt.so.14*

%files devel
%{_includedir}/fzssh/
%{_libdir}/libfzssh.so
%{_libdir}/libfzssh-client.so
%{_libdir}/libfzssh-crypt.so
%{_libdir}/pkgconfig/libfzssh-client.pc

%changelog
* Tue Sep 22 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- 1.4.0

* Fri Jul 24 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-1
- 1.3.0

* Tue Apr 14 2026 Gwyn Ciesla <gwync@protonmail.com> - 1.1.10-1
- Initial package.
