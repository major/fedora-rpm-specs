Name:		rply
Version:	1.1.4
Release:	%autorelease
Summary:	A library to read and write PLY files
License:	MIT
URL:		https://www.tecgraf.puc-rio.br/~diego/professional/rply/
Source0:	https://www.tecgraf.puc-rio.br/~diego/professional/rply/%{name}-%{version}.tar.gz
Source1:	rply_CMakeLists.txt
Source2:	RPLYConfig.cmake.in
Source3:	rply_cmake_export_cmakelists.txt
BuildRequires:  cmake >= 2.6.0
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
RPly is a library that lets applications read and write PLY files.
The PLY file format is widely used to store geometric information, such as 3D
models, but is general enough to be useful for other purposes.

RPly is easy to use, well documented, small, free, open-source, ANSI C,
efficient, and well tested. The highlights are:

* A callback mechanism that makes PLY file input straightforward;
* Support for the full range of numeric formats;
* Binary (big and little endian) and text modes are fully supported;
* Input and output are buffered for efficiency;
* Available under the MIT license for added freedom.

%package	devel
Summary:	Libraries and headers for rply
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Rply Library Header Files and Link Libraries

%prep
%autosetup -p1

# Add CMakeLists.txt file
cp %{SOURCE1} CMakeLists.txt

# Add CMake detection modules
mkdir -p CMake/export
mkdir -p CMake/Modules
cp %{SOURCE2} CMake/Modules/
cp %{SOURCE3} CMake/export/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
       -DCMAKE_VERBOSE_MAKEFILE=ON

%cmake_build

iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE

%install
%cmake_install

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/rplyConfig.cmake

%files
%license LICENSE
%doc manual/*
%{_libdir}/*.so.*
%{_bindir}/*

%files devel
%license LICENSE
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*
%{_libdir}/*.so
%dir %{_datadir}/%{name}/

%changelog
%autochangelog
