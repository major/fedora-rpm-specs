%global gittag rel_2_13_0

Name:           asdcplib
Version:        2.13.0
Release:        4%{?dist}
Summary:        AS-DCP file access libraries
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.cinecert.com/asdcplib/

Source0:        https://github.com/cinecert/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
Source1:        %{name}.pc

ExcludeArch:    %{ix86} %{arm}

BuildRequires:  cmake
BuildRequires:  gcc-c++
# https://fedoraproject.org/wiki/Licensing:FAQ#What.27s_the_deal_with_the_OpenSSL_license.3F
BuildRequires:  openssl-devel
BuildRequires:  xerces-c-devel

%description
Open source implementation of SMPTE and the MXF Interop “Sound & Picture Track
File” format. It was originally developed with support from DCI. Development
is currently supported by CineCert and other d-cinema manufacturers.

It supports reading and writing MXF files containing sound (PCM), picture (JPEG
2000 or MPEG-2) and timed-text (XML) essence. plain text and cipher text are
both supported using OpenSSL for cryptographic support.

%package        tools
Summary:        AS-DCP file access libraries tools

%description    tools
Open source implementation of SMPTE and the MXF Interop “Sound & Picture Track
File” format. It was originally developed with support from DCI. Development
is currently supported by CineCert and other d-cinema manufacturers.

It supports reading and writing MXF files containing sound (PCM), picture (JPEG
2000 or MPEG-2) and timed-text (XML) essence. plain text and cipher text are
both supported using OpenSSL for cryptographic support.

This package contains tools and testing programs for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{gittag}
sed -i -e 's/DESTINATION lib/DESTINATION %{_lib}/g' src/CMakeLists.txt

# rpmlint fixes
find . -name "*.h" -exec chmod 644 {} \;
find . -name "*.cpp" -exec chmod 644 {} \;
chmod 644 README.md

%build
%cmake -DCMAKE_SKIP_RPATH=True
%cmake_build

%install
%cmake_install

install -p -D -m 644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
sed -i \
    -e 's|PREFIX|%{_prefix}|g' \
    -e 's|LIBDIR|%{_libdir}|g' \
    -e 's|INCLUDEDIR|%{_includedir}|g' \
    -e 's|VERSION|%{version}|g' \
    %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

find %{buildroot} -name '*.la' -delete
rm -fr  %{buildroot}%{_prefix}/targets

%files
%license COPYING
%doc README.md
%{_libdir}/libas02.so.2
%{_libdir}/libas02.so.2.*
%{_libdir}/libasdcp.so.2
%{_libdir}/libasdcp.so.2.*
%{_libdir}/libkumu.so.2
%{_libdir}/libkumu.so.2.*

%files devel
%{_includedir}/*
%{_libdir}/libas02.so
%{_libdir}/libasdcp.so
%{_libdir}/libkumu.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/as-02-info
%{_bindir}/as-02-unwrap
%{_bindir}/as-02-wrap
%{_bindir}/as-02-wrap-iab
%{_bindir}/asdcp-info
%{_bindir}/asdcp-test
%{_bindir}/asdcp-unwrap
%{_bindir}/asdcp-util
%{_bindir}/asdcp-wrap
%{_bindir}/blackwave
%{_bindir}/j2c-test
%{_bindir}/klvwalk
%{_bindir}/kmfilegen
%{_bindir}/kmrandgen
%{_bindir}/kmuuidgen
%{_bindir}/wavesplit

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Pete Walter <pwalter@fedoraproject.org> - 2.13.0-3
- Rebuild for xerces-c 3.3

* Fri Oct 18 2024 Pete Walter <pwalter@fedoraproject.org> - 2.13.0-2
- Rebuild for xerces-c 3.3

* Thu Aug 29 2024 Simone Caronni <negativo17@gmail.com> - 2.13.0-1
- Update to 2.13.0.
- Trim changelog.

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12.3-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Simone Caronni <negativo17@gmail.com> - 2.12.3-1
- Update to 2.12.3.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 25 2022 Simone Caronni <negativo17@gmail.com> - 2.12.2-1
- Update to 2.12.2.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
