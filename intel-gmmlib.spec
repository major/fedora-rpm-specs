Name:           intel-gmmlib
Version:        22.3.3
Release:        2%{?dist}
Summary:        Intel Graphics Memory Management Library

License:        MIT and BSD
URL:            https://github.com/intel/gmmlib
Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# This package relies on intel asm
ExclusiveArch:  x86_64 i686

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
The Intel Graphics Memory Management Library provides device specific
and buffer management for the Intel Graphics Compute Runtime for OpenCL
and the Intel Media Driver for VAAPI.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n gmmlib-intel-gmmlib-%{version}
# Fix license perm
chmod -x LICENSE.md README.rst
# Fix source code perm
find Source -name "*.cpp" -exec chmod -x {} ';'
find Source -name "*.h" -exec chmod -x {} ';'


%build
%cmake \
  -DRUN_TEST_SUITE:BOOL=False

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets


%files
%license LICENSE.md
%doc README.rst
%{_libdir}/libigdgmm.so.12*

%files devel
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Nicolas Chauvet <kwizart@gmail.com> - 22.3.3-1
- Update to 22.3.3

* Wed Dec 28 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.3.2-1
- Update to 22.3.2

* Fri Oct 14 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.2.1-1
- Update to 22.2.1

* Wed Aug 10 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.1.7-1
- Update to 22.1.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.1.4-1
- Update to 22.1.4

* Sun May 15 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.1.3-1
- Update to 22.1.3

* Wed Mar 30 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.1.2-1
- Update to 22.1.2

* Tue Mar 15 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.1.0-1
- Update to 22.1.0

* Fri Mar 04 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.0.3-1
- Update to 22.0.3

* Wed Jan 26 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.0.2-1
- Update to 22.0.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Nicolas Chauvet <kwizart@gmail.com> - 22.0.1-1
- Update to 22.0.1

* Fri Dec 17 2021 Nicolas Chauvet <kwizart@gmail.com> - 22.0.0-1
- Update to 22.0.0

* Fri Dec 17 2021 Nicolas Chauvet <kwizart@gmail.com> - 21.3.5-1
- Update to 21.3.5

* Fri Dec 10 2021 Nicolas Chauvet <kwizart@gmail.com> - 21.3.4-1
- Update to 21.3.4

* Thu Nov 04 2021 Nicolas Chauvet <kwizart@gmail.com> - 21.3.2-1
- Update to 21.3.2

* Sun Oct 03 2021 Nicolas Chauvet <nchauvet@linagora.com> - 21.3.1-1
- Update to 21.3.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Nicolas Chauvet <kwizart@gmail.com> - 21.2.1-1
- Update to 21.2.1

* Tue May 04 2021 Nicolas Chauvet <kwizart@gmail.com> - 21.1.3-1
- Update to 21.1.3

* Mon Apr 26 2021 Nicolas Chauvet <kwizart@gmail.com> - 21.1.2-1
- Update to 21.1.2

* Thu Apr 01 2021 Nicolas Chauvet <kwizart@gmail.com> - 21.1.1-1
- Update to 21.1.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.4.1-1
- Update to 20.4.1

* Fri Oct 30 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.3.3-1
- Update to 20.3.3

* Fri Sep 25 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.3.2-1
- Update to 20.3.2

* Mon Sep 14 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.3.1-1
- Update to 20.3.1

* Sun Sep 13 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.2.5-2
- rebuilt

* Tue Sep 01 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.2.5-1
- Update to 20.2.5

* Thu Aug 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - Update to 20.2.4-1
- Update to 20.2.4

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.2.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.2.3-1
- Update to 20.2.3

* Wed Jun 24 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.2.2-1
- Update to 20.2.2

* Thu Mar 26 2020 Nicolas Chauvet <kwizart@gmail.com> - 20.1.1-1
- Update to 20.1.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 19.4.1-1
- Update to 19.4.1

* Thu Dec 19 2019 Nicolas Chauvet <kwizart@gmail.com> - 19.3.4-1
- Update to 19.3.4

* Thu Sep 19 2019 Nicolas Chauvet <kwizart@gmail.com> - 19.3.2-1
- Update to 19.3.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Nicolas Chauvet <kwizart@gmail.com> - 19.2.3-1
- Update to 19.2.3

* Fri May 10 2019 Nicolas Chauvet <kwizart@gmail.com> - 19.1.2-1
- Update to 19.1.2

* Sat Apr 06 2019 Nicolas Chauvet <kwizart@gmail.com> - 19.1.1-1
- Update to 19.1.1

* Thu Feb 14 2019 Nicolas Chauvet <kwizart@gmail.com> - 18.4.1-1
- Update to 18.4.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 18.3.0-1
- Initial spec file
