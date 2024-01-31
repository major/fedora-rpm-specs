Name:		3Depict
Version:	0.0.22
Release:	22%{?dist}
Summary:	Valued 3D point cloud visualization and analysis


License:	GPLv3+
URL:		http://threedepict.sourceforge.net
Source0:	http://downloads.sourceforge.net/threedepict/%{name}-%{version}.tar.gz


#Mathgl for plotting
BuildRequires:	gcc-c++
BuildRequires:	mathgl-devel 
#Mesa for GLU
BuildRequires:	libGL-devel 
#Libxml2 for file parsing
BuildRequires:	libxml2-devel 
#FTGL for 3d fonts
BuildRequires:	ftgl-devel 
#libpng for textures
BuildRequires: libpng-devel
#Desktop file utils for installing desktop file
BuildRequires: desktop-file-utils
#WX widgets
BuildRequires: wxGTK-devel
#Vigra, for voxelisation
BuildRequires: vigra-devel

#PDF latex build
#BuildRequires: tex(latex)

#Required for surface removal algorithms 
BuildRequires: qhull-devel
BuildRequires: make

#Fedora specific PDF dir.
Patch0: %{name}-%{version}-manual-pdf-loc.patch
#Fedora specific font dir
Patch1: %{name}-%{version}-font-path.patch
#Qhull dir has changed 
Patch2: %{name}-%{version}-qhull.patch
#Fix for PPC64 arch
Patch3: %{name}-%{version}-qhull_ppc64le.patch

#wxGLCanvas not supported under wayland.
# wx bug 17702
Patch4: %{name}-%{version}-wayland.patch
# Fixes for wxWidgets 3.2 compatibility
Patch5: %{name}-%{version}-wx3.2.patch
%description
This software is designed to help users visualize and analyze 3D point clouds
with an associated real value, in a fast and flexible fashion. It is 
specifically targeted to atom probe tomography applications, but may be 
useful for general scalar valued point data purposes.

%prep

%setup -q 

%patch0
%patch1
%patch2
%patch3
%patch4
%patch5 -p1

%if 0%{?fedora} > 24
# Installation directory has changed
sed -i -e 's,qhull/qhull_a.h,libqhull/qhull_a.h,' \
  src/backend/filters/filterCommon.h \
  src/backend/filters/algorithms/spatial.cpp \
  configure configure.ac
# Avoid rerunning the autotools
touch -r aclocal.m4 configure configure.ac
%endif

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%configure --disable-debug-checks --enable-openmp-parallel 
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Install the textures
mkdir -p %{buildroot}%{_datadir}/%{name}/textures
cp -p data/textures/*png %{buildroot}%{_datadir}/%{name}/textures/


#Install the manpage
install -Dp -m 644 packaging/manpage/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

desktop-file-install \
		--dir %{buildroot}%{_datadir}/applications \
		packaging/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -Dp -m 644 data/textures/tex-source/%{name}-icon.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

#install language files
#--
#Remap locale names
mv locales/de_DE/ locales/de/

mkdir -p %{buildroot}/%{_datadir}/locale/
cp -R locales/* %{buildroot}/%{_datadir}/locale/

#Restore the internal build's locale naming
mv locales/de/ locales/de_DE/
#--


#Move the documentation such that it is picked up by the doc macro
mv docs/manual-latex/manual.pdf %{name}-%{version}-manual.pdf

#Locale stuff
%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc ChangeLog.txt README %{name}-%{version}-manual.pdf
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/textures
%{_datadir}/%{name}/textures/*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/*.svg


%changelog
* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 10 2023 Tom Callaway <spot@fedoraproject.org> - 0.0.22-18
- rebuild for new qhull

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Orion Poplawski <orion@nwra.com> - 0.0.22-15
- Rebuild with mathgl 8.0.1

* Mon Sep 12 2022 Scott Talbert <swt@techie.net> - 0.0.22-14
- Rebuild with wxWidgets 3.2

* Tue Aug 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.22-13
- Rebuild for gsl-2.7.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 0.0.22-8
- Force C++14 as this code is not C++17 ready

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.0.22-5
- Rebuilt for GSL 2.6.

* Sun Aug 11 2019 D Haley <mycae(a!t)gmx.com> - 0.0.22-4
- Add workaround for crash under wayland (wx bug 17702)

* Sun Aug 11 2019 D Haley <mycae(a!t)gmx.com> - 0.0.22-3
- Fix for PPC64LE qhull include bug (#1735406)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 05 2019 D Haley <mycae(a!t)gmx.com> - 0.0.22-1
- Update to 0.0.22

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 D Haley <mycae(a!t)gmx.com> - 0.0.21-1
- Update to 0.0.21

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018  D Haley <mycae(a!t)gmx.com> - 0.0.20-6
- Bump for MGL rebuild

* Thu Oct 12 2017  D Haley <mycae(a!t)gmx.com> - 0.0.20-5
- Bump for GSL rebuild
- Add fixes for s390/ppc64

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sun Feb 05 2017 D Haley <mycae(a!t)gmx.com> - 0.0.20-1
- Update to 0.0.20
- Do not specify wx-config-3.0 (bug in wx, 1077718, fixed)
=======
* Sat Jan 14 2017 D Haley <mycae(a!t)gmx.com> - 0.0.19-2
- Rebuild for libmgl bump

* Wed Jun 01 2016 D Haley <mycae(a!t)gmx.com> - 0.0.19-1
- Update to 0.0.19
- Remove gcc patch, fixed upstream
- Add upstream patch

* Fri Apr 29 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.0.18-7
- Rebuild for qhull-2015.2-1.
- Reflect qhull_a.h's location having changed.

* Tue Mar 8 2016 Orion Poplawski <orion@cora.nwra.com> - 0.0.18-6
- Add patch for fix compilation with gcc 6

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.0.18-5
- Rebuild for gsl 2.1
- Cleanup spec

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Kalev Lember <klember@redhat.com> - 0.0.18-3
- Rebuilt for libmgl soname bump

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 D Haley <mycae(a!t)gmx.com> - 0.0.18-1
- Update to 0.0.18

* Sat Oct 11 2014 D Haley <mycae(a!t)gmx.com> - 0.0.17-2
- Rebuild for mathgl 2.3

* Sun Sep 28 2014 D Haley <mycae(a!t)gmx.com> - 0.0.17-1
- Update to 0.0.17

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 D Haley <mycae(a!t)gmx.com> - 0.0.16-1
- Update to 0.0.16

* Wed Feb 12 2014 D Haley <mycae(a!t)gmx.com> - 0.0.15-4
- Rebuild for mgl

* Wed Feb 05 2014 D Haley <mycae(a!t)gmx.com> - 0.0.15-3
- Rebuild for new mgl
- Add upstream patches 

* Sun Jan 26 2014 D Haley <mycae(a!t)gmx.com> - 0.0.15-2
- Rebuild for new mgl

* Sun Dec 01 2013 D Haley <mycae(a!t)gmx.com> - 0.0.15-1
- Update to 0.0.15

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 D Haley <mycae(a!t)gmx.com> - 0.0.14-1
- Update to 0.0.14

* Tue Jun 25 2013 D Haley <mycae(a!t)gmx.com> - 0.0.13-2
- Enable mathgl2

* Fri Apr 12 2013 D Haley <mycae(a!t)gmx.com> - 0.0.13-1
- Update to 0.0.13

* Sat Mar 23 2013 D Haley <mycae(a!t)gmx.com> - 0.0.12-4
- Add aarch 64 patch for bug 924960, until next version

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 9 2012 D Haley <mycae(a!t)yahoo.com> - 0.0.12-2
- Import bugfixes from upstream for plot UI and crash fixes

* Sun Nov 25 2012 D Haley <mycae(a!t)yahoo.com> - 0.0.12-1
- Update to 0.0.12

* Mon Apr 2 2012 D Haley <mycae(a!t)yahoo.com> - 0.0.10-1
- Update to 0.0.10

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 D Haley <mycae(a!t)yahoo.com> - 0.0.9-3
- Patch to fix FTFBS for gcc 4.7

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 17 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.9-1
- Update to 0.0.9

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.0.8-3
- Rebuild for new libpng

* Sat Oct 29 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.8-2
- Post release fixes for various crash bugs

* Sun Oct 23 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.8-1
- Update to 0.0.8

* Sun Aug 14 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.7-1
- Update to 0.0.7

* Fri May 20 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.6-1
- Update to 0.0.6

* Sun Mar 27 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.5-1
- New upstream release

* Sun Mar 13 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.4-3
- Patch opengl startup code -- peek at gl context. Possible fix for bug 684390

* Sat Feb 12 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.4-2
- Fix bug 677016 - 3Depict no built with rpm opt flags

* Sat Jan 22 2011 D Haley <mycae(a!t)yahoo.com> - 0.0.4-1
- Update to 0.0.4

* Fri Nov 26 2010 D Haley <mycae(a!t)yahoo.com> - 0.0.3-1
- Update to 0.0.3

* Tue Oct 5 2010 D Haley <mycae(a!t)yahoo.com> - 0.0.2-3
- Use tex(latex) virtual package in preference to texlive-latex

* Mon Oct 4 2010 D Haley <mycae(a!t)yahoo.com> - 0.0.2-2
- Add latex build for manual

* Sat Sep 25 2010 D Haley <mycae(a!t)yahoo.com> - 0.0.2-1
- Update to 0.0.2
- Address comments in package review 

* Sun Aug 08 2010 D Haley <mycae(a!t)yahoo.com> - 0.0.1-1
- Initial package

