Name: ctk
Version: 0.1
%global soname_version 0.1
Release: %autorelease
Summary: The Commmon Toolkit for biomedical imaging

# The entire source is Apache-2.0; CMake/CMakeFindDependencyMacro.cmake is
# BSD-3-Clause, but does not contribute to the licenses of the binary RPMs.
License: Apache-2.0
URL: https://commontk.org/
Source: https://github.com/commontk/CTK/archive/2018-10-29/CTK-2018-10-29.tar.gz

Patch: ctk-0.1.20171224git71799c2-fix_qreal_cast.patch
Patch: ctk-DCMTK_3.6.4_updated_function.patch

BuildRequires: gcc-c++

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: cmake(dcmtk)
BuildRequires: qt-devel

Obsoletes: ctk-doc < 0.1-45

%global _description %{expand:
The Common Toolkit is a community effort to provide support code for medical
image analysis, surgical navigation, and related projects.}

%description %{_description}

This package contains the CTK Core library.


%package dicom

Summary: Library of high-level classes for querying PACS and local databases

Requires: ctk%{?_isa} = %{version}-%{release}
Requires: ctk-widgets%{?_isa} = %{version}-%{release}

%description dicom %{_description}

DICOM library provides high-level classes supporting query and retrieve
operations from PACS and local databases. It includes Qt widgets to easily
set-up a server connection and to send queries and view the results.


%package plugin-framework

Summary: A dynamic component system for C++

Requires: ctk%{?_isa} = %{version}-%{release}

%description plugin-framework %{_description}

The Plugin Framework is a dynamic component system for C++, modeled after the
OSGi specifications. It enable a development model where applications are
(dynamically) composed of many different (reusable) components following a
service oriented approach.


%package widgets

Summary: A collection of Qt widgets for biomedical imaging applications

Requires: ctk%{?_isa} = %{version}-%{release}

%description widgets %{_description}

The Widgets library is a collection of Qt widgets for usage in biomedical
imaging applications.


%package devel

Summary: Development files for the Common Toolkit

Requires: ctk%{?_isa} = %{version}-%{release}
Requires: ctk-dicom%{?_isa} = %{version}-%{release}
Requires: ctk-plugin-framework%{?_isa} = %{version}-%{release}
Requires: ctk-widgets%{?_isa} = %{version}-%{release}
Requires: dcmtk-devel%{?_isa}
Requires: qt-devel%{?_isa}

%description devel %{_description}

This package contains files for development of CTK applications.


%prep
%autosetup -n CTK-2018-10-29 -p1

%build
%cmake \
    -GNinja \
    -DCMAKE_PREFIX_PATH=%{_libdir}/cmake/InsightToolkit \
    -DCTK_SUPERBUILD=OFF \
    -DCTK_INSTALL_LIB_DIR=%{_libdir} \
    -DCTK_INSTALL_CMAKE_DIR=%{_libdir}/cmake/ctk \
    -DCTK_INSTALL_PLUGIN_DIR=%{_libdir}/ctk/plugins \
    -DCTK_INSTALL_QTPLUGIN_DIR=%{_qt4_plugindir} \
    -DCTK_ENABLE_DICOM=ON \
    -DCTK_ENABLE_PluginFramework=ON \
    -DCTK_ENABLE_Widgets=ON \
    -DDOCUMENTATION_TARGET_IN_ALL=OFF \
    -DBUILD_TESTING:BOOL=OFF
%cmake_build


%install
%cmake_install


# No %%check section here because running tests requires working X server
# and data files that are distributed without any copyright/license info
# (see https://github.com/commontk/CTKData/issues/1).


%files
%doc README.rst
%license NOTICE LICENSE
%{_libdir}/libCTKCore.so.%{soname_version}{,.*}

%files dicom
%{_libdir}/libCTKDICOMCore.so.%{soname_version}{,.*}
%{_libdir}/libCTKDICOMWidgets.so.%{soname_version}{,.*}

%files plugin-framework
%{_libdir}/libCTKPluginFramework.so.%{soname_version}{,.*}

%files widgets
%{_libdir}/libCTKWidgets.so.%{soname_version}{,.*}

%files devel
%{_includedir}/ctk-%{soname_version}/
%{_libdir}/libCTKCore.so
%{_libdir}/libCTKDICOMCore.so
%{_libdir}/libCTKDICOMWidgets.so
%{_libdir}/libCTKPluginFramework.so
%{_libdir}/libCTKWidgets.so
%{_qt4_plugindir}/designer/libCTKDICOMWidgetsPlugins.so
%{_qt4_plugindir}/designer/libCTKWidgetsPlugins.so
%{_libdir}/cmake/ctk/


%changelog
%autochangelog
