%bcond_without qt5
%bcond_without qt6
# currently broken
%bcond_with docs
%bcond_without test

%global forgeurl https://github.com/KDAB/KDSingleApplication/
# bumping this requires rebuild of dependent pkgs!
%global soversion 1.1

%global cmake_args -DKDSingleApplication_TESTS=true
%if %{with docs}
%global cmake_args %cmake_args -DKDSingleApplication_DOCS=true
%endif

Name:           kdsingleapplication
Version:        1.1.0
Release:        %autorelease
Summary:        KDAB's helper class for single-instance policy applications
%forgemeta
URL:            %{forgeurl}
Source:         %{forgesource}
License:        MIT

BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with qt5}
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
%endif
%if %{with qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
%endif
%if %{with docs}
BuildRequires:  doxygen
%endif

%global _description %{expand:
KDSingleApplication is a helper class for single-instance policy applications
written by KDAB.}

%description %_description

%prep
%forgeautosetup -p1

%build
%if %{with qt5}
%global _vpath_builddir build-qt5
%cmake %cmake_args
%cmake_build
%endif

%if %{with qt6}
%global _vpath_builddir build-qt6
%cmake %cmake_args -DKDSingleApplication_QT6=true
%cmake_build
%endif

%install
%if %{with qt5}
%global _vpath_builddir build-qt5
%cmake_install
%endif

%if %{with qt6}
%global _vpath_builddir build-qt6
%cmake_install
%endif

%if %{with test}
%check
%if %{with qt5}
%global _vpath_builddir build-qt5
%ctest
%endif

%if %{with qt6}
%global _vpath_builddir build-qt6
%ctest
%endif
%endif

%if %{with qt5}
%package qt5
Summary:      KDAB's helper class for single-instance policy applications (Qt5)

%description qt5 %_description

%files qt5
%license LICENSES/MIT.txt
%{_libdir}/libkdsingleapplication.so.%{soversion}
%{_libdir}/libkdsingleapplication.so.%{version}
%{_docdir}/KDSingleApplication

%package qt5-devel
Summary:      Development files for %{name}-qt5
Requires:     %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:     cmake(Qt5Core)
Requires:     cmake(Qt5Network)
Requires:     cmake(Qt5Widgets)

%description qt5-devel
The %{name}-qt5-devel package contains libraries, header files and
documentation for developing applications that use %{name}-qt5.

%files qt5-devel
%license LICENSES/MIT.txt
%{_libdir}/libkdsingleapplication.so
%{_libdir}/cmake/KDSingleApplication/
%{_libdir}/qt5/mkspecs/modules/*
%{_includedir}/kdsingleapplication/
%endif

%if %{with qt6}
%package qt6
Summary:      KDAB's helper class for single-instance policy applications (Qt6)

%description qt6 %_description

%files qt6
%license LICENSES/MIT.txt
%{_libdir}/libkdsingleapplication-qt6.so.%{soversion}
%{_libdir}/libkdsingleapplication-qt6.so.%{version}
%{_docdir}/KDSingleApplication-qt6

%package qt6-devel
Summary:      Development files for %{name}-qt6
Requires:     %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:     cmake(Qt6Core)
Requires:     cmake(Qt6Network)
Requires:     cmake(Qt6Widgets)

%description qt6-devel
The %{name}-qt6-devel package contains libraries, header files and
documentation for developing applications that use %{name}-qt6.

%files qt6-devel
%license LICENSES/MIT.txt
%{_libdir}/libkdsingleapplication-qt6.so
%{_libdir}/cmake/KDSingleApplication-qt6/
%{_libdir}/qt6/mkspecs/modules/*
%{_includedir}/kdsingleapplication-qt6/
%endif

%changelog
%autochangelog
