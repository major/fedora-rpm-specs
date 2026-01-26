Name:           docparser
Version:        1.0.25
Release:        %autorelease
Summary:        A document parser library ported from document2html

License:        LGPL-3.0-or-later AND CC-BY-4.0 AND CC0-1.0 AND MIT
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
BuildRequires:  pkgconfig(libmagic)
# test dependencies
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Dtk6Core)

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
sed -i 's|Debug|RelWithDebInfo|' CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_bindir}/{docparser_test,docparser_autotest}

%check
%{_vpath_builddir}/tests/docparser_autotest

%files
%license LICENSES/*
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
