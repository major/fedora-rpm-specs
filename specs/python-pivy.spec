%global realname pivy
%global githash 46ddb2c
%global gitdate 20191108

Name:           python-pivy
Version:        0.6.9
Release:        4%{?dist}
Summary:        Python binding for Coin

License:        ISC
URL:            https://github.com/FreeCAD/pivy

Source0:        https://github.com/coin3d/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz


BuildRequires:  gcc gcc-c++ cmake swig
BuildRequires:  qt5-qtbase-devel
BuildRequires:  python3-devel
BuildRequires:  Coin4-devel
BuildRequires:  SoQt-devel
BuildRequires:  SIMVoleon-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libEGL-devel


%global _description\
Pivy is a Coin binding for Python. Coin is a high-level 3D graphics library with\
a C++ Application Programming Interface. Coin uses scene-graph data structures\
to render real-time graphics suitable for mostly all kinds of scientific and\
engineering visualization applications.\

%description %_description


%package -n python3-pivy
Summary: %summary
%{?python_provide:%python_provide python3-pivy}

%description -n python3-pivy %_description


%package examples
Summary: Pivy example files

%description examples
%{summary}

%prep
%autosetup -p1 -n %{realname}-%{version}

# Examples in the docs folder should not be set executable.
find ./docs -name "*.py" -exec chmod -x {} \;


%build
%cmake
%cmake_build


%install
%cmake_install

chmod +x %{buildroot}%{python3_sitearch}/pivy/sogui.py

find %{buildroot}%{python3_sitearch} -name "*.py" -exec sed -i "s|#!/usr/bin/env python|#!%{__python3}|" {} \;

 
%files -n python3-pivy
%license LICENSE
%doc AUTHORS NEWS README.md THANKS docs/* HACKING
%{python3_sitearch}/pivy/

%files examples
%doc examples


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 0.6.9-3
- Rebuilt for Python 3.14

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 25 2024 Richard Shaw <hobbes1069@gmail.com> - 0.6.9-1
- Update to 0.6.9.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 14 2024 Richard Shaw <hobbes1069@gmail.com> - 0.6.8-9
- Add upstream commits for Python 3.12+ compatibility.

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.6.8-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 Richard Shaw <hobbes1069@gmail.com> - 0.6.8-5
- Rebuild for Coin4.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.6.8-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Richard Shaw <hobbes1069@gmail.com> - 0.6.8-1
- Update to 0.6.8.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.6.7-2
- Rebuilt for Python 3.11

* Thu Apr 28 2022 Richard Shaw <hobbes1069@gmail.com> - 0.6.7-1
- Update to 0.6.7.

* Mon Jan 24 2022 Richard Shaw <hobbes1069@gmail.com> - 0.6.6-1
- Update to 0.6.6.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.6.5-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.5-3
- Rebuilt for Python 3.9

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 0.6.5-2
- Fix string quoting for rpm >= 4.16

* Wed Feb 05 2020 Richard Shaw <hobbes1069@gmail.com> - 0.6.5-1
- Update to 0.6.5.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-0.7.20191108git46ddb2c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.5-0.6.20191108git46ddb2c
- Move to FreeCAD fork of pivy.

* Wed Oct 09 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.5-0.5
- Update for Coin4 and dependencies.
- Move to FreeCAD fork since it is supported.
- Move examples to a subpackage.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.5-0.4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.5-0.3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Richard Shaw <hobbes1069@gmail.com> - 0.6.5-0.1
- Update to 0.6.5a0.

* Sun Feb 03 2019 Richard Shaw <hobbes1069@gmail.com> - 0.5.0-24.db2e64a4a880
- Update to newer upstream checkout.
- Change to Python 3.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-23.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Richard Shaw <hobbes1069@gmail.com> - 0.5.0-22.hg609
- Fix ambiguous python shebang.

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.5.0-21.hg609
- Rebuild with fixed binutils

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-20.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-19.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-18.hg609
- Python 2 binary package renamed to python2-pivy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-17.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-16.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.5.0-15.hg609
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-13.hg609
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-11.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.0-10.hg609
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 28 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.5.0-9.hg609
- Use Coin3.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-7.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4.hg609
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Richard Shaw <hobbes1069@gmail.com> - 0.5.0-3.hg609
- Change name to python-pivy to meet package naming guidelines.
- Change to correct license in spec file. (BSD->ISC)

* Tue Nov 01 2011 Richard Shaw <hobbes1069@gmail.com> - 0.5.0-1
- Inital release.
