# Tests require access to an actual smartcard to work
%bcond_with check

%global date 20230418
%global commit 2cbe462c62bacf537b9a9a427a1c053d8c2e4760
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pkcs11test
Version:        0~%{date}git%{shortcommit}
Release:        %autorelease
Summary:        PKCS#11 Test Suite

# pkcs11test itself is Apache-2.0, the PKCS#11 headers are RSA
License:        Apache-2.0 AND LicenseRef-RSA
URL:            https://github.com/google/pkcs11test
Source:         %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# Add missing #include for GCC 15
# https://github.com/google/pkcs11test/pull/74
Patch:          %{url}/pull/74.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  sed

BuildRequires:  gtest-devel
%if %{with check}
BuildRequires:  opencryptoki-libs
%endif

# Originally imported in f5b35ef94742a86ad6c87587a9270a11e65da3fd
Provides:       bundled(pkcs11-headers) = 1.4

%description
This package provides a test suite for PKCS#11.

%prep
%autosetup -n %{name}-%{commit} -p1

# Build system fixes
# * Replace bundled gtest with the system one
# * Switch to C++14 as now required by the system gtest package
# * Fix library path for opencryptoki
rm -r gtest-1.10.0
sed -i makefile \
  -e 's:libgtest.a::' \
  -e 's:-std=c++0x:-std=c++14:' \
  -e 's:-lpthread:-lpthread -lgtest %{build_ldflags}:' \
  -e 's:/usr/lib/opencryptoki:%{_libdir}/opencryptoki:g'

# Rename license for bundled pkcs11 headers
mv third_party/pkcs11/LICENSE third_party/pkcs11/LICENSE.pkcs11

%build
%if 0%{?el9}
%set_build_flags
%endif
%make_build \
  GTEST_INC="-isystem %{_includedir}/gtest" \
  GTEST_DIR="%{_includedir}/gtest"

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}

%if %{with check}
%check
%make_build test_opencryptoki
%endif

%files
%license LICENSE third_party/pkcs11/LICENSE.pkcs11
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
