Name:		expatpp
Version:	0
Release:	%autorelease -p -s 20120624svn6
Summary:	C++ layer for expat
# Automatically converted from old format: MPLv1.1 - review is highly recommended.
License:	MPL-1.1
URL:		http://sourceforge.net/projects/expatpp/
# svn export -r 6 https://svn.code.sf.net/p/expatpp/code/trunk/src_pp/ expatpp
# tar cjf  expatpp.tar.bz2 expatpp
Source0:	expatpp.tar.bz2
Patch:		0001-Added-CMake-config-file.patch
Patch:		0002-Fix-case-of-required-arg.patch
Patch:		0003-Include-string-header.patch
Patch:		0004-Converted-to-lib-standalone-program-layout.patch
Patch:		0005-Added-test-code.patch
Patch:		0006-Build-testexpatpp1.patch
Patch:		0007-Fix-subdir-command.patch
Patch:		0008-Added-cPack.patch
Patch:		0009-Install-library.patch
Patch:		0010-Use-lib-or-lib64-automatically.patch
Patch:		0011-added-soname-info.patch
Patch:		0012-Fixed-missing-api-version.patch
Patch:		0013-Install-header-file.patch
Patch:		0014-Removed-windows-static-lib-header.patch
Patch:		0015-Reworked-documentation.patch
Patch:		0016-Quick-fix-for-FTBFS.patch
Patch:		0017-PATCH-Modernize-CMake-build-system-for-CMake-4-compa.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	expat-devel


%description
Expatpp is a simple C++ layer to make using the open source expat XML parsing
library vastly easier for complex schemas. It has been used widely in industry
including the Valve Steam project.


%package	devel
Summary:	Headers and development libraries for expatpp
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description devel
You should install this package if you would like to
develop code based on expatpp.


%prep
%autosetup -p1 -n %{name}


%build
%{cmake} -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" .
%{cmake_build}


%install
%{cmake_install}


%check
%{ctest}


%files
%doc CHANGELOG EXTEND TODO
%{_libdir}/*.so.*


%files devel
%{_includedir}/%{name}.h
%{_libdir}/*.so


%changelog
%autochangelog
