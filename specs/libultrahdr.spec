%global gitdate       20251202
%global commit        8cbc983d2f6c2171af5cbcdb8801102f83fe92ab
%global short_commit  %(c="%{commit}"; echo ${c:0:7})

Name:           libultrahdr
Version:        1.4.0^%{gitdate}git%{short_commit}
Release:        %autorelease
Summary:        Reference codec for the Ultra HDR format
# main library is licensed under Apache-2.0
# bundled image_io library is licensed under Apache-2.0, except:
# third_party/image_io/src/modp_b64: BSD-3-Clause
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/google/libultrahdr
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch1:         https://github.com/google/libultrahdr/pull/383.patch#/remove-platform-and-architecture-detection-logic.patch
Patch2:         https://github.com/google/libultrahdr/pull/381.patch#/use-system-gtest.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  gtest-devel
BuildRequires:  gmock-devel

Provides:       bundled(image_io)

%description
libultrahdr is an image compression library that uses gain map technology to
store and distribute HDR images. Conceptually on the encoding side, the library
accepts SDR and HDR rendition of an image and from these a Gain Map (quotient
between the two renditions) is computed. The library then uses backward
compatible means to store the base image (SDR), gain map image and some
associated metadata. Legacy readers that do not support handling the gain map
image and/or metadata, will display the base image. Readers that support the
format combine the base image with the gain map and render a high dynamic range
image on compatible displays.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -p1 -C
# Rename license
mv third_party/image_io/src/modp_b64/LICENSE third_party/image_io/src/modp_b64/LICENSE.BSD-3-Clause

%build
%cmake -DUHDR_BUILD_TESTS=ON -DUHDR_ENABLE_SYSTEM_GTEST=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/libuhdr.a

%check
# https://github.com/google/libultrahdr/issues/382
%ifnarch s390x
%ctest
%endif

%files
%license LICENSE third_party/image_io/src/modp_b64/LICENSE.BSD-3-Clause
%doc README.md
%{_libdir}/libuhdr.so.1{,.*}

%files devel
%{_bindir}/ultrahdr_app
%{_includedir}/ultrahdr_api.h
%{_libdir}/libuhdr.so
%{_libdir}/pkgconfig/libuhdr.pc

%changelog
%autochangelog
