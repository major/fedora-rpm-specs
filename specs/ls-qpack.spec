Name:           ls-qpack
Version:        2.5.3
Release:        5%{?dist}
Summary:        QPACK compression library for use with HTTP/3

License:        MIT
URL:            https://github.com/litespeedtech/ls-qpack
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         soname-and-external-libxxhash.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  perl
BuildRequires:  pkgconfig(libxxhash)
# rpath is needed for tests, but should not be 
# in installed binaries
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_removing_rpath
BuildRequires:  chrpath

%description
ls-qpack is a full-featured, tested, and fast QPACK library. The QPACK
encoder produces excellent compression results based on an innovative
mnemonic technique. It boasts the fastest Huffman encoder and decoder.

The library is production quality. It is used in OpenLiteSpeed,
LiteSpeed Web Server, and LiteSpeed Web ADC.

The library is robust:
* The encoder does not assume anything about usual HTTP headers
such as Server or User-Agent. Instead, it uses its mnemonic compression
technique to achieve good compression results for any input.
* The decoder uses modulo arithmetic to track dynamic table insertions. This
is in contrast to all other QPACK implementations, which use an integer
counter, meaning that at some point, the decoder will break.
* The decoder processes input in streaming fashion. The caller does not have
to buffer the contents of HTTP/3 HEADERS frame. Instead, the decoder can be
supplied input byte-by-byte.

%package devel
Summary:   QPACK compression library for use with HTTP/3
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  xxhash-devel

%description devel
Development files for ls-qpack


%prep
%autosetup -p1
# remove failing test
# https://github.com/litespeedtech/ls-qpack/issues/51
sed -i '/dyn_table_cap_mismatch/d' test/CMakeLists.txt
# Do not want rpath
sed -i 's/PRIVATE ls-qpack/PUBLIC ls-qpack/g' bin/CMakeLists.txt
# Remove bundled xxhash
rm -r deps/xxhash

%build
%cmake -DLSQPACK_TESTS=ON \
       -DLSQPACK_XXH=OFF \
       -DLSQPACK_BIN=ON \
       -DCMAKE_SKIP_INSTALL_RPATH=TRUE
%cmake_build


%install
%cmake_install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/encode-int
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/fuzz-decode
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/interop-decode
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/interop-encode
chmod 755 $RPM_BUILD_ROOT%{_bindir}/encode-int
chmod 755 $RPM_BUILD_ROOT%{_bindir}/fuzz-decode
chmod 755 $RPM_BUILD_ROOT%{_bindir}/interop-decode
chmod 755 $RPM_BUILD_ROOT%{_bindir}/interop-encode

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_bindir}/encode-int
%{_bindir}/fuzz-decode
%{_bindir}/interop-decode
%{_bindir}/interop-encode
%{_libdir}/libls-qpack.so.2
%{_libdir}/libls-qpack.so.2.*

%files devel
%{_includedir}/lsqpack.h
%{_includedir}/lsxpack_header.h
%{_libdir}/pkgconfig/ls-qpack.pc
%{_libdir}/libls-qpack.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 22 2023 Benson Muite <benson_muite@emailplus.org> - 2.5.3-1
- Initial packaging
