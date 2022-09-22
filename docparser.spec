Name:           docparser
Version:        1.0.1
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
License:        GPLv3+ and Boost and MIT and zlib
URL:            https://github.com/linuxdeepin/docparser
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(Qt5Core)

%description
This file content analysis library is provided for the full-text search function
of document management.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
