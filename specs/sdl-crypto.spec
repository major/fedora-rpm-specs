%global srcname crypto
%global date 20250324
%global commit 9ac58405c2b91fb7cd230aed474dc7059f0fcad9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?el8}
# Needed for epel8
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}

%global common_description %{expand:
Crypto provides a simple implementation of the Rijndael (now AES) and DES
encryption algorithms as well as the SHA1 and SHA2 hashing algorithms. The
library is almost a verbatim copy of the code from OpenBSD and PuTTY for use by
the SDL-Hercules-390 emulator.}

Name:           sdl-crypto
Version:        1.0.0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Simple AES/DES encryption and SHA1/SHA2 hashing library

# The Public Domain declarations are under review:
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/550
# https://gitlab.com/fedora/legal/fedora-license-data/-/issues/551
License:        LicenseRef-Fedora-Public-Domain AND MIT AND BSD-3-Clause
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
# both packages install /usr/include/sha2.h
Conflicts:      sha2-devel
# Renamed from crypto, remove once f40 and el8 are EOL
Provides:       crypto-devel%{?_isa} = %{version}-%{release}
Obsoletes:      crypto-devel < 1.0.0-11
Provides:       crypto-static%{?_isa} = %{version}-%{release}
Obsoletes:      crypto-static < 1.0.0-11

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
