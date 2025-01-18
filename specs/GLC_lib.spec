Name:           GLC_lib
Version:        2.5.0
Release:        21%{?dist}
Summary:        C++ class library for OpenGL application based on Qt 4

License:        LGPL-3.0-or-later
URL:            http://www.glc-lib.net/
Source0:        https://github.com/laumaya/GLC_lib/archive/Version_2_5_0.zip
Patch0:         GLC_lib_src_2.5.0-nobundled.patch

BuildRequires:  qt4-devel
BuildRequires:  pkgconfig(lib3ds)
BuildRequires:  pkgconfig(quazip1-qt4)
BuildRequires:  make


%description
GLC_lib is a C++ class library that enables the quick creation of OpenGL
application based on Qt 4. Some GLC_lib features : Camera orbiting, Obj
textured file support, 3D Primitive... And more.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt4-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%setup -q -n GLC_lib-Version_2_5_0/
%patch -P 0 -p1 -b .no3rd

#Fix library Path on lib64
sed -i -e 's|LIB_DIR = /usr/local/lib|LIB_DIR = %{buildroot}%{_libdir}|' install.pri
sed -i -e 's|/usr/local/include.*|%{buildroot}%{_includedir}/%{name}|' install.pri

# Remove bundled libraries
rm -rf src/3rdparty


%build
%{qmake_qt4} -recursive
%make_build


%install
%make_install


%ldconfig_scriptlets


%files
%license LICENSE.LGPL
%{_libdir}/*.so.*

%files devel
%{_includedir}/GLC_lib/
%{_libdir}/*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.0-19
- convert license to SPDX

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 04 2023 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-14
- rebuilt

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 18 2022 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-11
- Rebuilt for quazip 1.3

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 2.5.0-9
- Rebuild (quazip)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.5.0-1
- Update to 2.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-13
- use %%qmake_qt4 macro to ensure proper build flags

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-11
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 21 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-5
- Remove spurious direct use of minizip

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 21 2011 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-3
- Fix with gcc46

* Mon Jul 25 2011 Nicolas Chauvet <kwizart@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Tue Mar 15 2011 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Thu Dec 09 2010 Nicolas Chauvet <kwizart@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 23 2009 kwizart < kwizart at gmail.com > - 1.1.0-1
- Update to 1.1.0

* Thu Aug 14 2008 kwizart < kwizart at gmail.com > - 1.0.0-1
- Update to 1.0.0

* Wed May 28 2008 kwizart < kwizart at gmail.com > - 0.9.9-1
- Update to 0.9.9

* Sat May 17 2008 kwizart < kwizart at gmail.com > - 0.9.8-2
- Fix COPYING end-of-line encoding

* Mon Feb 11 2008 kwizart < kwizart at gmail.com > - 0.9.8-1
- Initial spec file

