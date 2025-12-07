%global gitcommit d243218119b1632987df26baea0d4bc6ccdee533
%global gitdate 20251013
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})

%bcond_without qt5

Name:           JKQtPlotter
Version:        5.0.0
Release:        %autorelease -p -s %{gitdate}git%{shortcommit}
Summary:        An extensive Qt6 Plotter framework
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
Requires:       %{name}-doc = %{version}-%{release}

%description
Extensive Qt6 Plotter framework
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

%if %{with qt5}
%package        -n %{name}-qt5
Summary:        An extensive Qt5 Plotter framework
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Svg)
Requires:       %{name}-doc = %{version}-%{release}

%description    -n %{name}-qt5
Extensive Qt5 Plotter framework
(including a feature-rich plotter widget,
a speed-optimized, but limited variant and
a LaTeX equation renderer!), written fully
in C/C++ and without external dependencies.

%package        -n %{name}-qt5-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}

%description    -n %{name}-qt5-devel
The %{name}-qt5-devel package contains libraries and header files for
developing applications that use %{name}-qt5.
%endif

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
Contains documentation files for the usage of %{name}.


%prep
%setup -qc

%if %{with qt5}
cp -a %{name}-%{gitcommit} %{name}-qt5-%{gitcommit}
cp -p %{name}-%{gitcommit}/lib/jkqtmathtext/resources/firaMath/LICENSE \
      %{name}-%{gitcommit}/lib/jkqtmathtext/resources/firaMath/LICENSE-firaMath
%endif

%build
pushd %{name}-%{gitcommit}
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release \
       -DCMAKE_PREFIX_PATH:PATH=/usr/%{_lib}/cmake/Qt6 \
       -DJKQtPlotter_BUILD_DECORATE_LIBNAMES_WITH_BUILDTYPE:BOOL=OFF
%cmake_build
popd

%if %{with qt5}
pushd %{name}-qt5-%{gitcommit}
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON -DCMAKE_BUILD_TYPE:STRING=Release \
       -DCMAKE_PREFIX_PATH:PATH=/usr/%{_lib}/cmake/Qt5 \
       -DJKQtPlotter_BUILD_DECORATE_LIBNAMES_WITH_BUILDTYPE:BOOL=OFF
%cmake_build
popd
%endif

%install
pushd %{name}-%{gitcommit}
%cmake_install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}/
rm -rf %{buildroot}%{_bindir}
popd

%if %{with qt5}
pushd %{name}-qt5-%{gitcommit}
%cmake_install
mkdir -p %{buildroot}%{_libexecdir}/%{name}-qt5
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libexecdir}/%{name}-qt5/
rm -rf %{buildroot}%{_bindir}
popd
%endif

%check
pushd %{name}-%{gitcommit}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest -V -E test_jkqtpdatastore
popd

%if %{with qt5}
pushd %{name}-qt5-%{gitcommit}
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest -V -E test_jkqtpdatastore
popd
%endif

%files
%{_libdir}/libJKQTCommon6.so.5.0.0
%{_libdir}/libJKQTFastPlotter6.so.5.0.0
%{_libdir}/libJKQTMath6.so.5.0.0
%{_libdir}/libJKQTMathText6.so.5.0.0
%{_libdir}/libJKQTPlotter6.so.5.0.0

%files devel
%{_includedir}/jkqt*/
%{_libdir}/cmake/JKQTPlotter6/
%{_libdir}/libJKQTCommon6.so
%{_libdir}/libJKQTFastPlotter6.so
%{_libdir}/libJKQTMath6.so
%{_libdir}/libJKQTMathText6.so
%{_libdir}/libJKQTPlotter6.so
%{_libexecdir}/%{name}/

%if %{with qt5}
%files -n %{name}-qt5
%{_libdir}/libJKQTCommon5.so.5.0.0
%{_libdir}/libJKQTFastPlotter5.so.5.0.0
%{_libdir}/libJKQTMath5.so.5.0.0
%{_libdir}/libJKQTMathText5.so.5.0.0
%{_libdir}/libJKQTPlotter5.so.5.0.0

%files -n %{name}-qt5-devel
%{_includedir}/jkqt*/
%{_libdir}/cmake/JKQTPlotter5/
%{_libdir}/libJKQTCommon5.so
%{_libdir}/libJKQTFastPlotter5.so
%{_libdir}/libJKQTMath5.so
%{_libdir}/libJKQTMathText5.so
%{_libdir}/libJKQTPlotter5.so
%{_libexecdir}/%{name}-qt5/
%endif

%files doc
%doc %{name}-%{gitcommit}/README.md %{name}-%{gitcommit}/SECURITY.md
%license %{name}-%{gitcommit}/LICENSE %{name}-%{gitcommit}/lib/jkqtmathtext/resources/firaMath/LICENSE-firaMath
%{_datadir}/doc/JKQTPlotter/

%changelog
%autochangelog
