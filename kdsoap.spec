Name:           kdsoap
Version:        2.2.0
Release:        %autorelease
Summary:        A Qt-based client-side and server-side SOAP component

# Note that this project requires the 3rd party 'libkode' submodule
# that is licensed separately with LGPL-2.0-or-later; however, libkode
# is used for code-generation only and the resulting code can be made
# available under any license.
# 
# Various other freely distributable files are contained in the unittests
# and are not used in the library code itself.
License:        MIT
URL:            https://github.com/KDAB/KDSoap
Source0:        https://github.com/KDAB/KDSoap/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/KDAB/KDSoap/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz.asc
Source2:        https://www.kdab.com/kdab-products.asc

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  qt6-rpm-macros
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  gnupg2
# for doc generation
BuildRequires:  doxygen
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  qt6-doc-devel

%global _description %{expand:
KDSoap can be used to create client applications for web services
and also provides the means to create web services without the need
for any further component such as a dedicated web server.}

%description %{_description}

For more information, see
https://www.kdab.com/development-resources/qt-tools/kd-soap/

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel-common%{?_isa} = %{version}-%{release}
%description    devel
This package contains header files and associated tools and libraries to
develop programs which need to access web services using the SOAP protocol.

%package     -n kdsoap6
Summary:        Qt 6 version of %{name}
%description -n kdsoap6
%{_description}

%package     -n kdsoap6-devel
Summary:        Development files for kdsoap6
Requires:       kdsoap6%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel-common%{?_isa} = %{version}-%{release}
%description -n kdsoap6-devel
This package contains header files and associated tools and libraries to
develop programs which need to access web services using the SOAP protocol.

%package        devel-common
Summary:        Header files and other common development files for kdsoap and kdsoap6
%description    devel-common
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DKDSoap_EXAMPLES=false -DKDSoap_QT6=OFF
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
# qhelpgenerator needs to be in $PATH to be detected
export PATH=%{_qt6_libexecdir}:$PATH
%cmake -DKDSoap_EXAMPLES=false -DKDSoap_QT6=ON -DKDSoap_DOCS=ON
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
mkdir -p %{buildroot}%{_qt6_docdir}
mv %{buildroot}%{_docdir}/KDSoap-qt6/*.qch %{buildroot}%{_qt6_docdir}/
mv %{buildroot}%{_docdir}/KDSoap-qt6/*.tags %{buildroot}%{_qt6_docdir}/
rm -rf %{buildroot}%{_datarootdir}/doc/KDSoap{,-qt6}

%check
%global _vpath_builddir %{_target_platform}-qt5
%ctest
%global _vpath_builddir %{_target_platform}-qt6
%ctest


%files
%doc README.md
%license LICENSES/MIT.txt
%{_libdir}/libkdsoap-server.so.2*
%{_libdir}/libkdsoap.so.2*

%files -n kdsoap6
%doc README.md
%license LICENSES/MIT.txt
%{_libdir}/libkdsoap-server-qt6.so.2*
%{_libdir}/libkdsoap-qt6.so.2*

%files devel
%doc kdsoap.pri kdwsdl2cpp.pri
%{_libdir}/libkdsoap-server.so
%{_libdir}/libkdsoap.so
%{_bindir}/kdwsdl2cpp
%{_libdir}/cmake/KDSoap/
%{_libdir}/qt5/mkspecs/modules/*
%{_includedir}/KDSoapClient/
%{_includedir}/KDSoapServer/

%files -n kdsoap6-devel
%doc kdsoap.pri kdwsdl2cpp.pri
%{_libdir}/libkdsoap-server-qt6.so
%{_libdir}/libkdsoap-qt6.so
%{_bindir}/kdwsdl2cpp-qt6
%{_libdir}/cmake/KDSoap-qt6/
%{_libdir}/qt6/mkspecs/modules/*
%{_includedir}/KDSoapClient-Qt6/
%{_includedir}/KDSoapServer-Qt6/
%{_qt6_docdir}/kdsoap.tags

%files devel-common
%dir %{_datadir}/mkspecs
%dir %{_datadir}/mkspecs/features
%{_datadir}/mkspecs/features/kdsoap.prf


%files doc
%doc docs/CHANGES* docs/manual
%{_qt6_docdir}/kdsoap-api.qch

%changelog
%autochangelog
