Name:			PerceptualDiff
Version:		2.1
Release:		12%{?dist}
Summary:		An image comparison utility

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:		GPL-2.0-or-later
URL:			https://github.com/myint/perceptualdiff
Source:		%{url}/archive/v%{version}/perceptualdiff-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: cmake
BuildRequires: freeimage-devel
BuildRequires: libtiff-devel
BuildRequires: libpng-devel

Provides: perceptualdiff = %{version}-%{release}


%description
PerceptualDiff is an image comparison utility that makes use of a 
computational model of the human visual system to compare two images.

This software is released under the GNU General Public License.

%prep
%autosetup -p1 -n perceptualdiff-%{version}


%build
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}

%cmake_build


%install
%cmake_install

mkdir -p %{buildroot}%{_libdir}
find . -name libpdiff.so -exec mv {} %{buildroot}%{_libdir}/libpdiff.so ';'

%files
%doc README.rst
%license LICENSE
%{_bindir}/perceptualdiff
# TODO: fix SONAME
%{_libdir}/libpdiff.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Nicolas Chauvet <kwizart@gmail.com> - 2.1-1
- Switch upstream perceptualdiff

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-27
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.1-15
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 20 2009 kwizart < kwizart at gmail.com > - 1.1.1-1
- Update to 1.1.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 kwizart < kwizart at gmail.com > - 1.0.2-4
- Fix and Rebuild for gcc44

* Mon Sep  1 2008 kwizart < kwizart at gmail.com > - 1.0.2-3
- Re-introduce gcc43 patch

* Mon Sep  1 2008 kwizart < kwizart at gmail.com > - 1.0.2-2
- Add Missing BR freeimage-devel

* Mon Sep  1 2008 kwizart < kwizart at gmail.com > - 1.0.2-1
- Update to 1.0.2

* Sat Feb  9 2008 kwizart < kwizart at gmail.com > - 1.0.1-8
- Rebuild for gcc43

* Fri Jan  4 2008 kwizart < kwizart at gmail.com > - 1.0.1-7
- Fix gcc43

* Tue Aug 14 2007 kwizart < kwizart at gmail.com > - 1.0.1-6
- Update the license field to GPLv2

* Tue Apr 17 2007 kwizart < kwizart at gmail.com > - 1.0.1-5
- Removed cflags calls at cmake step.

* Tue Apr 17 2007 kwizart < kwizart at gmail.com > - 1.0.1-4
- Fix CXXFLAGS
- Fix wrong-script-end-of-line-encoding and spurious-executable-perm

* Tue Apr 17 2007 kwizart < kwizart at gmail.com > - 1.0.1-3
- Fix RPATHs from cmake build from:
  http://fedoraproject.org/wiki/PackagingDrafts/cmake
- Make VERBOSE=1

* Sat Apr 14 2007 kwizart < kwizart at gmail.com > - 1.0.1-2
- Minor fixes wip

* Wed Apr 11 2007 kwizart < kwizart at gmail.com > - 1.0.1-1
- Update to 1.0.1
- Fix RPATHs
- Removed Exclude x86_64

* Sun Jan 21 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.0-2
- BuildRequires fixed
- Excluded x86_64

* Thu Jan 18 2007 Tobias Sauerwein <tsauerwein@aqsis.org> 1.0-1
- Update to 1.0

* Mon Dec 11 2006 Tobias Sauerwein <tsauerwein@aqsis.org> 0.9
- Initial RPM/SPEC
