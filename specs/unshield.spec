Name:          unshield
Version:       1.6.2
Release:       %autorelease
Summary:       Extract CAB files from InstallShield installers
SourceLicense: MIT and LicenseRef-RSA
License:       MIT
URL:           https://github.com/twogood/unshield
VCS:           git:%{url}.git
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: zlib-devel

%description
This tool allows the extraction of InstallShield format cabinet files (which
are different from Microsoft cabinet files). It was initially developed as a
part of the SynCE project to aid with installing applications for Pocket PC
devices, which were often contained in InstallShield installers, but these days
that is rather less likely to be the primary use case.

%package devel
Summary:       Files needed for software development with %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the files needed for development with
%{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DUSE_OUR_OWN_MD5=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/unshield
%{_libdir}/libunshield.so.1
%{_libdir}/libunshield.so.1.6.2
%{_mandir}/man1/unshield.1.*

%files devel
%{_includedir}/libunshield.h
%{_libdir}/cmake/%{name}/
%{_libdir}/libunshield.so
%{_libdir}/pkgconfig/libunshield.pc

%changelog
%autochangelog
