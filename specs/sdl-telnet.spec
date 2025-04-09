%global srcname telnet
%global date 20250324
%global commit 384b2542dfc9af67ca078e2bc13487a8fc234a3f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?el8}
# Needed for epel8
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
libtelnet is a library for handling the TELNET protocol for use by the
SDL-Hercules-390 emulator. It includes routines for parsing incoming data from
a remote peer as well as formatting data to be sent to the remote peer.

libtelnet uses a callback-oriented API, allowing application-specific handling
of various events. The callback system is also used for buffering outgoing
protocol data, allowing the application to maintain control of the actual
socket connection.

Features supported include the full TELNET protocol, Q-method option
negotiation, and NEW-ENVIRON.}

Name:           sdl-telnet
Version:        1.0.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Simple RFC-compliant TELNET implementation for SDL-Hercules-390

License:        LicenseRef-Fedora-Public-Domain
URL:            https://github.com/SDL-Hercules-390/%{srcname}
Source:         %{url}/archive/%{commit}/%{srcname}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{commit}
sed -i extra.txt -e 's:DESTINATION .:DESTINATION share/doc/%{name}-devel:g'

%build
%cmake
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-devel/%{srcname}.LICENSE.txt .

%files devel
%license %{srcname}.LICENSE.txt
%doc README.md
%doc %{_docdir}/%{name}-devel/%{srcname}.README.txt
%{_includedir}/*.h
%{_libdir}/lib%{srcname}*.a

%changelog
%autochangelog
