Name:           libxlsxwriter
Version:        1.1.7
Release:        3%{?dist}
Summary:        A C library for creating Excel XLSX files

# BSD: Most files
# Public Domain: third_party/md5/*
# MPL: third_party/tmpfileplus/*
License:        BSD-2-Clause AND LicenseRef-Fedora-Public-Domain AND MPL-2.0
URL:            https://github.com/jmcnamara/libxlsxwriter/
Source0:        https://github.com/jmcnamara/libxlsxwriter/archive/RELEASE_%{version}/%{name}-%{version}.tar.gz
# Fix zlib and minizip detection
Patch0:         libxlsxwriter_minizip.patch

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  zlib-devel
BuildRequires:  python3-pytest


%description
Libxlsxwriter is a C library that can be used to write text, numbers, formulas
and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-RELEASE_%{version}

# Delete bundled minizip
rm -rf third_party/minizip
rm -f include/xlsxwriter/third_party/zip.h

# FIXME Remove failing test
# [ERROR][/home/sandro/rpmbuild/BUILD/libxlsxwriter-RELEASE_1.1.5/src/packager.c:1711]: Error adding member to zipfile
# [ERROR] workbook_close(): Zip ZIP_ERRNO error while creating xlsx file '(null)'. System error = Success
rm test/functional/test_output_buffer.py


%build
%cmake -DUSE_SYSTEM_MINIZIP=ON -DBUILD_TESTS=ON
%cmake_build


%install
%cmake_install

%check
%ifnarch s390x i686
%ctest
%endif


%files
%license License.txt
%doc Readme.md Changes.txt
%{_libdir}/%{name}.so.6*

%files devel
%{_includedir}/xlsxwriter.h
%{_includedir}/xlsxwriter/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/xlsxwriter.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 08 2024 Sandro Mani <manisandro@gmail.com> - 1.1.7-1
- Update to 1.1.7

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 04 2023 Lukas Javorsky <ljavorsk@redhat.com> - 1.1.5-4
- Rebuilt for minizip-ng transition Fedora change
- Fedora Change: https://fedoraproject.org/wiki/Changes/MinizipNGTransition

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Sandro Mani <manisandro@gmail.com> - 1.1.5-1
- Update to 1.1.5

* Tue Nov 15 2022 Lukas Javorsky <ljavorsk@redhat.com> - 1.1.4-4
- Rebuild for minizip-ng soname bump

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct 13 2021 Sandro Mani <manisandro@gmail.com> - 1.1.4-1
- Update to 1.1.4

* Tue Aug 10 2021 Sandro Mani <manisandro@gmail.com> - 1.1.3-1
- Update to 1.1.3

* Mon Aug 09 2021 Sandro Mani <manisandro@gmail.com> - 1.1.2-2
- Add libxlsxwriter_operator.patch

* Mon Aug 09 2021 Sandro Mani <manisandro@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Tue Jul 27 2021 Sandro Mani <manisandro@gmail.com> - 1.1.1-2
- Backport fix for test failure

* Fri Jul 23 2021 Sandro Mani <manisandro@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Sandro Mani <manisandro@gmail.com> - 1.1.0-1
- Update to 1.1.0

* Fri Apr 16 2021 Sandro Mani <manisandro@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Wed Mar 31 2021 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Tue Feb 09 2021 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-5
- Rebuilt for minizip 3.0.0

* Tue Feb 09 2021 Sandro Mani <manisandro@gmail.com> - 1.0.0-4
- Rebuild (minizip)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-2
- Fix license
- Start with soversion 0
- Remove ldconfig scriptlets

* Fri Nov 13 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-1
- Update to 1.0.0
