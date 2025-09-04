Name:		xrootd-s3-http
Version:	0.5.1
Release:	1%{?dist}
Summary:	S3/HTTP filesystem plugins for XRootD

License:	Apache-2.0
URL:		https://github.com/PelicanPlatform/%{name}
Source0:	%{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	xrootd-server-devel
BuildRequires:	curl-devel
BuildRequires:	json-devel
BuildRequires:	openssl-devel
BuildRequires:	tinyxml2-devel
#		For testing
BuildRequires:	gtest-devel
BuildRequires:	curl
BuildRequires:	hostname
BuildRequires:	openssl
BuildRequires:	procps
BuildRequires:	xrootd-server
Requires:	xrootd-server

%description
These filesystem plugins for XRootD allow you to serve objects from S3
and HTTP backends through an XRootD server.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DXROOTD_EXTERNAL_TINYXML2:BOOL=ON \
       -DXROOTD_PLUGINS_EXTERNAL_GTEST:BOOL=ON \
       -DENABLE_TESTS:BOOL=ON \
       -DEXE_BIN:PATH=/bin/true
%cmake_build

%check
# s3 tests require network (https://s3.us-east-1.amazonaws.com)
# posc tests fail when run in parallel:
# https://github.com/PelicanPlatform/xrootd-s3-http/issues/111
%ctest -- -E 'S3|s3|TestPosc'

%install
%cmake_install

%files
%{_libdir}/libXrdHTTPServer-5.so
%{_libdir}/libXrdOssFilter-5.so
%{_libdir}/libXrdOssGlobus-5.so
%{_libdir}/libXrdOssHttp-5.so
%{_libdir}/libXrdOssS3-5.so
%{_libdir}/libXrdOssPosc-5.so
%{_libdir}/libXrdS3-5.so
%doc README.md
%license LICENSE

%changelog
* Tue Sep 02 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.1-1
- Update to version 0.5.1

* Sun Aug 24 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.5.0-1
- Update to version 0.5.0

* Sat Aug 23 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 0.4.1-4
- Rebuilt for tinyxml2 11.0.0

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jun 08 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.1-2
- Fix broken glob filter

* Sat Jun 07 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.4.1-1
- Update to version 0.4.1

* Sun Mar 09 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.1-2
- Add -DLIB_INSTALL_DIR to cmake command

* Sun Feb 02 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.1-1
- Update to version 0.2.1

* Fri Jan 24 2025 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1.8-3
- Do not hardcode the build type
- Use CMAKE_BUILD_TYPE RelWithDebInfo to avoid -Werror in compiler flags

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1.8-1
- Update to version 0.1.8
- Drop patches accepted upstream
- Run http unit tests

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.1.7-3
- rebuild for tinyxml2

* Fri Nov 01 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1.7-2
- Fix linking error on 32 bit architectures

* Thu Oct 24 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.1.7-1
- Initial package
