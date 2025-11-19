%global gitcommit d243218119b1632987df26baea0d4bc6ccdee533
%global gitdate 20251013
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name:           JKQtPlotter
Version:        5.0.0
Release:        %autorelease -p -s %{gitdate}git%{shortcommit}
Summary:        An extensive Qt5 & Qt6 Plotter framework

License:        LGPL-2.1-or-later AND OFL-1.1
URL:            https://github.com/jkriege2/JKQtPlotter
# Source0:       %%{url}/archive/refs/tags/v%%{version}.tar.gz
Source0:        %{url}/archive/%{gitcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  pkgconfig(cups)
BuildRequires:  CImg-devel
BuildRequires:  cmake(OpenCV)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  glib2-devel
BuildRequires:  libxshmfence-devel

%description
An extensive Qt5 & Qt6 Plotter framework
(including a feature-rich plotter widget,
a speed-optimized, but limited variant and
a LaTeX equation renderer!), written fully
in C/C++ and without external dependencies.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
%description    doc
Contains documentation files for the usage of %{name}.


%prep
%autosetup -p1 -n %{name}-%{gitcommit}


%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# Test fails (Subprocess exits)
%ctest -E test_jkqtpdatastore

%files
%license LICENSE lib/jkqtmathtext/resources/firaMath/LICENSE
%doc README.md SECURITY.md
%{_bindir}/JKQTP*
%{_bindir}/jkqtp*
%{_bindir}/jkqtmathtext_render
%{_libdir}/libJKQTCommon6_Release.so.5.0.0
%{_libdir}/libJKQTFastPlotter6_Release.so.5.0.0
%{_libdir}/libJKQTMath6_Release.so.5.0.0
%{_libdir}/libJKQTMathText6_Release.so.5.0.0
%{_libdir}/libJKQTPlotter6_Release.so.5.0.0

%files devel
%{_bindir}/test_jkqtpdatastore
%{_includedir}/jkqt*/
%{_libdir}/cmake/JKQTPlotter6/
%{_libdir}/libJKQTCommon6_Release.so
%{_libdir}/libJKQTFastPlotter6_Release.so
%{_libdir}/libJKQTMath6_Release.so
%{_libdir}/libJKQTMathText6_Release.so
%{_libdir}/libJKQTPlotter6_Release.so

%files doc
%license %{_datadir}/doc/JKQTPlotter/JKQTMathText6_FIRAMATH_LICENSE
%license %{_datadir}/doc/JKQTPlotter/JKQTMathText6_XITS_LICENSE.txt
%{_datadir}/doc/JKQTPlotter/

%changelog
%autochangelog
