%global commitdate 20241222
%global commit 24b5e7a8b27f42fa16b96fc70aade9106cf7102f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global debug_package %{nil}

Name:		rapidjson
Version:	1.1.0^%{commitdate}git%{shortcommit}
Release:	%autorelease
Summary:	Fast JSON parser and generator for C++

# Most files are MIT, rapidjson/msinttypes/{stdint,inttypes}.h are BSD
License:	MIT AND BSD-3-Clause
URL:		https://rapidjson.org/
Source0:	https://github.com/Tencent/rapidjson/archive/%{commit}/%{name}-%{commit}.tar.gz
# https://github.com/Tencent/rapidjson/pull/2340
Patch:          0001-CMake-improvements.patch
# https://github.com/Tencent/rapidjson/pull/2337
Patch:          0002-CMakeLists-fix-add_custom_command-warning.patch

BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	gtest-devel
%ifarch %{valgrind_arches}
BuildRequires:	valgrind
%endif
BuildRequires:	doxygen

%description
RapidJSON is a fast JSON parser and generator for C++.  It was		
inspired by RapidXml.							
									
  RapidJSON is small but complete.  It supports both SAX and DOM style	
  API. The SAX parser is only a half thousand lines of code.		
									
  RapidJSON is fast.  Its performance can be comparable to strlen().	
  It also optionally supports SSE2/SSE4.1 for acceleration.		
									
  RapidJSON is self-contained.  It does not depend on external		
  libraries such as BOOST.  It even does not depend on STL.		
									
  RapidJSON is memory friendly.  Each JSON value occupies exactly	
  16/20 bytes for most 32/64-bit machines (excluding text string).  By	
  default it uses a fast memory allocator, and the parser allocates	
  memory compactly during parsing.					
									
  RapidJSON is Unicode friendly.  It supports UTF-8, UTF-16, UTF-32	
  (LE & BE), and their detection, validation and transcoding		
  internally.  For example, you can read a UTF-8 file and let RapidJSON	
  transcode the JSON strings into UTF-16 in the DOM.  It also supports	
  surrogates and "\u0000" (null character).				
									
JSON(JavaScript Object Notation) is a light-weight data exchange	
format.  RapidJSON should be in fully compliance with RFC4627/ECMA-404.


%package devel
Summary:        %{summary}
Provides:	%{name}%{?_isa} = %{version}-%{release}
Provides:	%{name}-static = %{version}-%{release}

%description devel
%{description}


%package doc
Summary:	Documentation-files for %{name}
BuildArch:	noarch

%description doc
This package contains the documentation-files for %{name}.


%prep
%autosetup -p 1 -n %{name}-%{commit}

# Remove bundled code
rm -rf thirdparty

# Convert DOS line endings to unix
for file in "license.txt" $(find example -type f -name *.c*)
do
  sed -e "s/\r$//g" < ${file} > ${file}.new && \
    touch -r ${file} ${file}.new && \
    mv -f ${file}.new ${file}
done

# Remove -march=native and -Werror from compile commands
find . -type f -name CMakeLists.txt -print0 | \
  xargs -0r sed -i -e "s/-march=native/ /g" -e "s/-Werror//g"


%build
%cmake \
    -DDOC_INSTALL_DIR:PATH=%{_pkgdocdir} \
    -DRAPIDJSON_BUILD_CXX11:BOOL=OFF \
    -DGTESTSRC_FOUND:BOOL=ON \
    -DGTEST_SOURCE_DIR:PATH=.
%cmake_build


%install
%cmake_install
install -pm 644 CHANGELOG.md readme*.md %{buildroot}%{_pkgdocdir}/
find %{buildroot} -type f -name 'CMake*.txt' -delete


%check
%ctest


%files devel
%license license.txt
%dir %{_pkgdocdir}
%{_pkgdocdir}/CHANGELOG.md
%{_pkgdocdir}/readme*.md
%{_libdir}/cmake/RapidJSON/
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/


%files doc
%license license.txt
%{_pkgdocdir}/


%changelog
%autochangelog
