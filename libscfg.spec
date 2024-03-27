%global abi_ver 1

Name:           libscfg
Version:        0.1.1
Release:        %autorelease
Summary:        C library for a simple configuration file format

License:        MIT
URL:            https://sr.ht/~emersion/libscfg/
%global forgeurl https://git.sr.ht/~emersion/libscfg
Source0:        %{forgeurl}/refs/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{forgeurl}/refs/download/v%{version}/%{name}-%{version}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

Patch:          %{forgeurl}/commit/3bdba8c2.patch#/libscfg-0.1.1-build-set-library-version-and-soversion.patch

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license LICENSE
%doc README.md
%{_libdir}/libscfg.so.%{abi_ver}
%{_libdir}/libscfg.so.%{version}

%files devel
%{_includedir}/scfg.h
%{_libdir}/libscfg.so
%{_libdir}/pkgconfig/scfg.pc


%changelog
%autochangelog
