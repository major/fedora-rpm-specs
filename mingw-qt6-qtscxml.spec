%{?mingw_package_header}

%global qt_module qtscxml

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt6-%{qt_module}
Version:        6.6.1
Release:        %autorelease
Summary:        Qt6 for Windows - QtScxml component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  qt6-qtscxml-devel >= %{version}

# for ninja
BuildRequires:  mingw32-filesystem >= 104
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase >= %{version}
BuildRequires:  mingw32-qt6-qtdeclarative >= %{version}

# for ninja
BuildRequires:  mingw64-filesystem >= 104
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase >= %{version}
BuildRequires:  mingw64-qt6-qtdeclarative >= %{version}


%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtScxml component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtScxml component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.


%{?mingw_debug_package}

%prep
%autosetup -p1 -n %{source_folder}

%build
export MINGW32_CFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CFLAGS="%{mingw64_cflags} -msse2"
export MINGW32_CXXFLAGS="${mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="${mingw64_cflags} -msse2"
%mingw_cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja

%install
%mingw_ninja_install


# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6Scxml.dll
%{mingw32_bindir}/Qt6StateMachine.dll
%{mingw32_bindir}/Qt6ScxmlQml.dll
%{mingw32_bindir}/Qt6StateMachineQml.dll
%{mingw32_includedir}/qt6/QtScxml/
%{mingw32_includedir}/qt6/QtStateMachine/
%{mingw32_includedir}/qt6/QtScxmlQml/
%{mingw32_includedir}/qt6/QtStateMachineQml/
%dir %{mingw32_libdir}/qt6/plugins/scxmldatamodel
%{mingw32_libdir}/qt6/plugins/scxmldatamodel/qscxmlecmascriptdatamodel.dll
%{mingw32_libdir}/qt6/metatypes/*.json
%{mingw32_libdir}/qt6/modules/*.json
%{mingw32_libdir}/qt6/qml
%{mingw32_libdir}/qt6/mkspecs
%{mingw32_libdir}/cmake/Qt6Scxml/
%{mingw32_libdir}/cmake/Qt6StateMachine/
%{mingw32_libdir}/cmake/Qt6StateMachineQml/
%{mingw32_libdir}/cmake/Qt6BuildInternals/
%{mingw32_libdir}/cmake/Qt6Qml/
%{mingw32_libdir}/cmake/Qt6ScxmlQml/
%{mingw32_libdir}/cmake/Qt6/
%{mingw32_libdir}/libQt6Scxml.dll.a
%{mingw32_libdir}/pkgconfig/*.pc
%{mingw32_libdir}/libQt6StateMachine.dll.a
%{mingw32_libdir}/libQt6ScxmlQml.dll.a
%{mingw32_libdir}/libQt6StateMachineQml.dll.a
%{mingw32_libdir}/*.prl

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Scxml.dll
%{mingw64_bindir}/Qt6StateMachine.dll
%{mingw64_bindir}/Qt6ScxmlQml.dll
%{mingw64_bindir}/Qt6StateMachineQml.dll
%{mingw64_includedir}/qt6/QtScxml/
%{mingw64_includedir}/qt6/QtStateMachine/
%{mingw64_includedir}/qt6/QtScxmlQml/
%{mingw64_includedir}/qt6/QtStateMachineQml/
%dir %{mingw64_libdir}/qt6/plugins/scxmldatamodel
%{mingw64_libdir}/qt6/plugins/scxmldatamodel/qscxmlecmascriptdatamodel.dll
%{mingw64_libdir}/qt6/metatypes/*.json
%{mingw64_libdir}/qt6/modules/*.json
%{mingw64_libdir}/qt6/qml
%{mingw64_libdir}/qt6/mkspecs
%{mingw64_libdir}/cmake/Qt6Scxml/
%{mingw64_libdir}/cmake/Qt6StateMachine/
%{mingw64_libdir}/cmake/Qt6StateMachineQml/
%{mingw64_libdir}/cmake/Qt6BuildInternals/
%{mingw64_libdir}/cmake/Qt6Qml/
%{mingw64_libdir}/cmake/Qt6ScxmlQml/
%{mingw64_libdir}/cmake/Qt6/
%{mingw64_libdir}/libQt6Scxml.dll.a
%{mingw64_libdir}/pkgconfig/*.pc
%{mingw64_libdir}/libQt6StateMachine.dll.a
%{mingw64_libdir}/libQt6ScxmlQml.dll.a
%{mingw64_libdir}/libQt6StateMachineQml.dll.a
%{mingw64_libdir}/*.prl

%changelog
%autochangelog
