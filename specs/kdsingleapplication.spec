%if %{defined rhel}
# EPEL
%bcond qt5 %[%{rhel} <  10]
%bcond qt6 %[%{rhel} >= 10]
%else
# Fedora
%bcond qt5 1
%bcond qt6 1
%endif
# Docs are not needed in the flatpak build and would require
# additional fixes.
%bcond docs %{undefined flatpak}
%bcond test 1

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
%if %{with docs}
BuildRequires:  cmake(Qt5DocTools)
%endif
%endif
%if %{with qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
%if %{with docs}
BuildRequires:  cmake(Qt6ToolsTools)
%endif
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
# qhelpgenerator needs to be in $PATH to be detected
PATH=%{_qt5_libexecdir}":$PATH" %cmake %cmake_args \
    -DECM_MKSPECS_INSTALL_DIR:PATH=%{_qt5_archdatadir}/mkspecs/modules
%cmake_build
%endif

%if %{with qt6}
%global _vpath_builddir build-qt6
# qhelpgenerator needs to be in $PATH to be detected
PATH=%{_qt6_libexecdir}":$PATH" %cmake %cmake_args -DKDSingleApplication_QT6=true \
    -DECM_MKSPECS_INSTALL_DIR:PATH=%{_qt6_archdatadir}/mkspecs/modules
%cmake_build
%endif

%install
%if %{with qt5}
%global _vpath_builddir build-qt5
%cmake_install

%if %{with docs}
# add symlinks into _qt5_docdir so that IDEs can find the doc files
install -d %{buildroot}%{_qt5_docdir}
pushd %{buildroot}%{_docdir}
for file in KDSingleApplication/*.{qch,tags}; do
    ln -s "../$file" %{buildroot}%{_qt5_docdir}
done
popd
%endif
%endif

%if %{with qt6}
%global _vpath_builddir build-qt6
%cmake_install

%if %{with docs}
# add symlinks into _qt6_docdir so that IDEs can find the doc files
install -d %{buildroot}%{_qt6_docdir}
pushd %{buildroot}%{_docdir}
for file in KDSingleApplication-qt6/*.{qch,tags}; do
    ln -s "../$file" %{buildroot}%{_qt6_docdir}
done
popd
%endif
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
%{_docdir}/KDSingleApplication/LICENSES/
%{_docdir}/KDSingleApplication/LICENSE.txt
%{_docdir}/KDSingleApplication/README.md


%package qt5-devel
Summary:      Development files for %{name}-qt5
Requires:     %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:     cmake(Qt5Core)
Requires:     cmake(Qt5Network)
Requires:     cmake(Qt5Widgets)
%if %{with docs}
Recommends:   %{name}-qt5-doc
%endif

%description qt5-devel
The %{name}-qt5-devel package contains libraries, header files and
documentation for developing applications that use %{name}-qt5.

%files qt5-devel
%license LICENSES/MIT.txt
%{_libdir}/libkdsingleapplication.so
%{_libdir}/cmake/KDSingleApplication/
%{_qt5_archdatadir}/mkspecs/modules/*
%{_includedir}/kdsingleapplication/


%if %{with docs}
%package qt5-doc
Summary:      Developer Documentation files for %{name}-qt5
BuildArch:    noarch

%description qt5-doc
Developer Documentation files for %{name}-qt5 for use
with KDevelop or QtCreator.

%files qt5-doc
%{_docdir}/KDSingleApplication/*.{qch,tags}
%{_qt5_docdir}/
%endif
%endif

%if %{with qt6}
%package qt6
Summary:      KDAB's helper class for single-instance policy applications (Qt6)

%description qt6 %_description

%files qt6
%license LICENSES/MIT.txt
%{_libdir}/libkdsingleapplication-qt6.so.%{soversion}
%{_libdir}/libkdsingleapplication-qt6.so.%{version}
%{_docdir}/KDSingleApplication-qt6/LICENSES/
%{_docdir}/KDSingleApplication-qt6/LICENSE.txt
%{_docdir}/KDSingleApplication-qt6/README.md


%package qt6-devel
Summary:      Development files for %{name}-qt6
Requires:     %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:     cmake(Qt6Core)
Requires:     cmake(Qt6Network)
Requires:     cmake(Qt6Widgets)
%if %{with docs}
Recommends:   %{name}-qt6-doc
%endif

%description qt6-devel
The %{name}-qt6-devel package contains libraries, header files and
documentation for developing applications that use %{name}-qt6.

%files qt6-devel
%license LICENSES/MIT.txt
%{_libdir}/libkdsingleapplication-qt6.so
%{_libdir}/cmake/KDSingleApplication-qt6/
%{_qt6_mkspecsdir}/modules/*
%{_includedir}/kdsingleapplication-qt6/


%if %{with docs}
%package qt6-doc
Summary:      Developer Documentation files for %{name}-qt6
BuildArch:    noarch

%description qt6-doc
Developer Documentation files for %{name}-qt6 for use
with KDevelop or QtCreator.

%files qt6-doc
%{_docdir}/KDSingleApplication-qt6/*.{qch,tags}
%{_qt6_docdir}/
%endif
%endif

%changelog
%autochangelog
