Name: glui
Version:  2.36
Release:  31%{?dist}
Summary: A GLUT-Based User Interface Library

License: Zlib
URL: http://glui.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
#Upstream only builds a static library, this makes a solib.
Patch0: glui-2.36-solib.patch
BuildRequires:  gcc-c++
BuildRequires: freeglut-devel libXi-devel libXmu-devel
BuildRequires: make

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description
GLUI is a GLUT-based C++ user interface library which provides controls
such as buttons, checkboxes, radio buttons, and spinners to OpenGL applications. 
It is window-system independent, relying on GLUT to handle all system-dependent 
issues, such as window and mouse management. 


%description devel
GLUI is a GLUT-based C++ user interface library which provides controls
such as buttons, checkboxes, radio buttons, and spinners to OpenGL applications. 
It is window-system independent, relying on GLUT to handle all system-dependent 
issues, such as window and mouse management. 

These are the development files.

%prep
%setup -q
%patch -P0 -p1 -b .solib
find -type f -name '*.cpp' | xargs chmod -x
find -type f -name '*.h' | xargs chmod -x

%build
pushd src
%{__make} CPPFLAGS="%{optflags} -I./ -I./include -fPIC" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_includedir}/GL
install -p -m 644 src/include/GL/glui.h %{buildroot}%{_includedir}/GL/
mkdir -p %{buildroot}%{_libdir}
install -p -m 755 src/libglui.so.0.0 %{buildroot}%{_libdir}/
ln -s %{_libdir}/libglui.so.0.0 %{buildroot}%{_libdir}/libglui.so.0
ln -s %{_libdir}/libglui.so.0 %{buildroot}%{_libdir}/libglui.so


%ldconfig_scriptlets


%files
%doc src/LICENSE.txt
%{_libdir}/*.so.*

%files devel
%doc src/doc/ src/example/ www/ 
%{_libdir}/*.so
%{_includedir}/GL/
%{_includedir}/GL/glui.h


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 2.36-26
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Matthew Miller <mattdm@fedoraproject.org> - 2.36-22
- as of 2.36, this is under just the zlib license (see LICENSE.txt, or license.md in newer codebase)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.36-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Jon Ciesla <limb@jcomserv.net> - 2.36-2
- Review fixes. from BZ 845308, comment 1.

* Thu Aug 02 2012 Jon Ciesla <limb@jcomserv.net> - 2.36-1
- create.
