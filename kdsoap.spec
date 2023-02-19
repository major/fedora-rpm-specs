Name:           kdsoap
Version:        2.1.1
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
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires: gnupg2

%description
KDSoap can be used to create client applications for web services
and also provides the means to create web services without the need
for any further component such as a dedicated web server.

For more information, see 
https://www.kdab.com/development-resources/qt-tools/kd-soap/

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains header files and associated tools and libraries to
develop programs which need to access web services using the SOAP protocol.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
Documentation for %{name}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
%cmake -DCMAKE_BUILD_TYPE=Release -DKDSoap_EXAMPLES=false
%cmake_build


%install
%cmake_install
rm -rf $RPM_BUILD_ROOT/%{_datarootdir}/doc/KDSoap


%check
%ctest


%files
%{_libdir}/libkdsoap-server.so.2*
%{_libdir}/libkdsoap.so.2*
%doc README.md
%license LICENSES/MIT.txt

%files devel
%doc kdsoap.pri kdwsdl2cpp.pri
%dir %{_datadir}/mkspecs
%dir %{_datadir}/mkspecs/features
%{_datadir}/mkspecs/features/kdsoap.prf
%{_includedir}/KDSoapClient/
%{_includedir}/KDSoapServer/
%{_libdir}/libkdsoap-server.so
%{_libdir}/libkdsoap.so
%{_bindir}/kdwsdl2cpp
%{_libdir}/cmake/KDSoap/
%{_libdir}/qt5/mkspecs/modules/

%files doc
%doc docs


%changelog
%autochangelog
