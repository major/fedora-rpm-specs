Summary: Software version control visualization
Name: gource
Version: 0.55
Release: 3%{?dist}
URL: http://gource.io/
Source: https://github.com/acaudwell/Gource/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
ExcludeArch: ppc64le

License: GPL-3.0-or-later

BuildRequires: gcc-c++
BuildRequires: SDL2_image-devel
BuildRequires: SDL2-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: pcre2-devel
BuildRequires: libX11-devel
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: glew-devel
BuildRequires: freetype-devel
BuildRequires: glm-devel
BuildRequires: boost-devel
BuildRequires: tinyxml-devel
BuildRequires: make

Requires: gnu-free-sans-fonts

%description

OpenGL-based 3D visualization tool for source control repositories.
The repository is displayed as a tree where the root of the repository is
the centre, directories are branches and files are leaves. Contributors
to the source code appear and disappear as they contribute to specific
files and directories.

%prep
%setup -q
#%%patch1 -p0
sed -i.cp -e 's|cp |cp -p |' Makefile.in
rm -r src/tinyxml

%build
%configure --enable-ttf-font-dir=%{_datadir}/fonts/gnu-free/ --with-tinyxml
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/%{_datadir}/%{name}/fonts

%files
%{_bindir}/gource
%{_mandir}/man1/gource.1.gz
%license COPYING
%doc README.md THANKS ChangeLog

%dir %{_datadir}/gource
%{_datadir}/gource/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Gwyn Ciesla <gwync@protonmail.com> - 0.55-1
- 0.55

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.54-5
- Rebuilt for Boost 1.83

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 28 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.54-3
- migrated to SPDX license

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.54-2
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.54-1
- 0.54

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.53-4
- Move to pcre2.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.53-2
- Rebuilt for Boost 1.78

* Mon May 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.53-1
- 0.53

* Tue Apr 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.52-1
- 0.52

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 0.51-10
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 0.51-8
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.51-5
- Rebuilt for Boost 1.75

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.51-3
- Rebuilt for Boost 1.73

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.51-1
- 0.51

* Thu Nov 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.50-1
- 0.50

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.49-4
- Rebuilt for Boost 1.69

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.49-3
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.49-1
- 0.49

* Tue Feb 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.48-1
- 0.48

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.47-2
- Rebuilt for Boost 1.66

* Mon Sep 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.47-1
- 0.47

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.43-14
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 0.43-13
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.43-11
- Rebuilt for Boost 1.63

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 0.43-10
- Rebuild for glew 2.0.0

* Thu Feb 25 2016 Jon Ciesla <limburgher@gmail.com> - 0.43-9
- Fix FTBFS.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.43-7
- Rebuilt for Boost 1.60

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 0.43-6
- Rebuild for glew 1.13

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.43-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.43-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.43-1
- Update to 0.43

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.42-4
- Rebuild for boost 1.57.0

* Thu Nov 06 2014 Jon Ciesla <limburgher@gmail.com> - 0.42-3
- Use SDL2, BZ 1161101.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.42-1
- New upstream 0.42

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.40-4
- Rebuild for boost 1.55.0

* Sat Mar 15 2014 Ville Skyttä <ville.skytta@iki.fi> - 0.40-3
- Build with system tinyxml

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 0.40-2
- rebuilt for GLEW 1.10

* Fri Oct 18 2013 Jon Ciesla <limburgher@gmail.com> - 0.40-1
- Latest upstream, BZ 1020688.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.38-5
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.38-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.38-3
- Rebuild for Boost-1.53.0

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 0.38-2
- Rebuild for glew 1.9.0

* Mon Sep  3 2012 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.38-1
- New upstream 0.38

* Sun Jul 29 2012 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.37-6
- Rebuild for broken dep on libGLEW.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.37-4
- Rebuild against PCRE 8.30

* Tue Jan 17 2012 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.37-3
- Fix build failure with gcc-4.7

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.37-1
- New upstream 0.37
- Clean up spec to match current guidelines

* Sat Jul 30 2011 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.35-1
- New upstream 0.35

* Mon Jun 20 2011 ajax@redhat.com - 0.29-2
- Rebuild for new glew soname

* Fri Feb 11 2011 Siddhesh Poyarekar <siddhesh@redhat.com> - 0.29-1
- New upstream 0.29

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Aug 28 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.28-1
- New upstream 0.28

* Fri Aug 06 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.27-2
- Fixed missing dist in the Release value
- Fixed dates in the changelog

* Thu Aug 05 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.27-1
- Rebase to upstream version 0.27

* Sat Jul 10 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.27-0.1.beta.20100710
- Rebase to new upstream version
- Added new BuildRequires libGLEW

* Fri Apr 16 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.24-3
- BZ #582781 Randomize name for files created in /tmp

* Sun Feb 28 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.24-2
- BZ #567559: Flip images in software for PPM output since hardware flipping
  fails on some video cards

* Thu Feb 18 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.24-1
- New upstream release
- Added COPYING, README, THANKS and ChangeLog in docs

* Sun Jan 17 2010 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.23-2
- Modified Makefile.in in %%prep section to preserve timestamps
- Require gnu-free-sans-fonts and use the --enable-ttf-font-dir configure option
- Updated %%files section in spec file based on suggestions in review request

* Tue Dec 29 2009 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.23-1
- Rebase to new upstream release version 0.23
- Spec file updates: use parallel make and %%global instead of %%define

* Sat Dec 05 2009 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.18-3
- Fixed unowned directory in .spec files section
- Dropped package version patch since it's not really breaking anything
- Replace RPM_BUILD_ROOT with buildroot to maintain consistency
- Removed unnecessary Requires from spec
- Removed unnecessary --prefix in configure section
- Preserve timestamps during install
- Added freetype-devel as a build dependency
- Fixed BuildRoot
- Clean buildroot in the install section

* Wed Dec 02 2009 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.18-2
- Fixed spec and rpm warnings from rpmlint

* Wed Dec 02 2009 Siddhesh Poyarekar <spoyarek@redhat.com> - 0.18-1
- New package
- Fixed version number in configure.ac to reflect the released version

