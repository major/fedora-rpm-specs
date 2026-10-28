Name:		rply
Version:	1.1.4
Release:	%autorelease
Summary:	A library to read and write PLY files
License:	MIT
URL:		https://w3.impa.br/~diego/software/rply/
Source0:	%{url}/%{name}-%{version}.tar.gz
Source1:	rply_CMakeLists.txt
Patch:		11.patch
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

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
       -DCMAKE_VERBOSE_MAKEFILE=ON

%cmake_build

iconv -f iso8859-1 -t utf-8 LICENSE > LICENSE.conv && mv -f LICENSE.conv LICENSE

%install
%cmake_install

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

%changelog
%autochangelog
