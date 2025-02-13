Name:           docparser
Version:        1.0.16
Release:        %autorelease
Summary:        A document parser library ported from document2html

# The entire source code is GPLv2+ except
# src/utils/getoptpp.* which are Boost,
# src/utils/json.hpp,
# src/utils/miniz.c,
# src/utils/pugiconfig.hpp,
# src/utils/pugixml.cpp and
# src/utils/pugixml.hpp
# which are MIT,
# /src/utils/lodepng.* which are zlib
# Automatically converted from old format: GPLv3+ and Boost and MIT and zlib - review is highly recommended.
License:        GPL-3.0-or-later AND BSL-1.0 AND LicenseRef-Callaway-MIT AND Zlib
URL:            https://github.com/linuxdeepin/docparser
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(tinyxml2)

%description
This file content analysis library is provided for the full-text search function
of document management.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files and libraries for %{name}.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
