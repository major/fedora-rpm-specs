Name:           curlpp
Version:        0.8.1
Release:        %autorelease
Summary:        A C++ wrapper for libcURL
License:        MIT
URL:            http://curlpp.org/
Source0:        https://github.com/jpbarrette/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         curlpp-0.8.1-fix-curloption.patch
Patch1:         curlpp-0.8.1-fix-pkgconfig.patch
Patch2:         curlpp-0.8.1-cmake_minimum.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  make

%description
cURLpp is a C++ wrapper for libcURL.

%package        devel
Summary:        Development files for %{name}
Requires:       boost-devel
Requires:       curl-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

# Convert CRLF line endings to LF in the examples
for file in examples/*.cpp
do
    sed 's/\r//' $file > $file.new && \
    touch -r $file $file.new && \
    mv $file.new $file
done

# remove deps on global.h which in turn pulls in config.h
sed -i '28 d' include/curlpp/Types.hpp

# unexport private build flags
sed -i 's/ @LDFLAGS@//; s/ @CURLPP_CXXFLAGS@//;' \
  extras/curlpp.pc.in \
  extras/curlpp-config.in

%build
%cmake -Wno-dev
%cmake_build

%install
%cmake_install
# Unwanted library files
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

%check
%ctest

%files
%doc doc/AUTHORS doc/TODO
%license doc/LICENSE
%{_libdir}/libcurlpp.so.*

%files devel
%doc examples/*.cpp examples/README doc/guide.*
%{_bindir}/curlpp-config
%{_includedir}/curlpp/
%{_includedir}/utilspp/
%{_libdir}/libcurlpp.so
%{_libdir}/pkgconfig/curlpp.pc

%changelog
%autochangelog
