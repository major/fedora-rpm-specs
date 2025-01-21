Name:           simspark
Version:        0.3.5
Release:        10%{?dist}
Summary:        Spark physical simulation system

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://simspark.sourceforge.net
Source0:        http://downloads.sourceforge.net/simspark/%{name}-%{version}.tar.xz
Patch0:         %{name}-confscript-mlibfix.patch
# https://gitlab.com/robocup-sim/SimSpark/-/merge_requests/53
Patch1:         %{name}-pr53-cxx-header-include.patch


BuildRequires: make
BuildRequires:  gcc gcc-c++ cmake boost-devel ruby ruby-devel SDL-devel tex(latex)
BuildRequires:  ode-devel libGL-devel DevIL-devel freetype-devel libGLU-devel
BuildRequires:  ImageMagick tex(titlesec.sty) tex(wrapfig.sty)
BuildRequires:  tex(subfigure.sty) qt5-qtbase-devel git
Conflicts:      rcssserver3d < 0.6.1
Requires:       ruby ruby(release)
Requires:       dejavu-sans-mono-fonts

%description
Spark is a physical simulation system. The primary purpose of this system is
to provide a *generic* simulator for different kinds of simulations.
In these simulations, agents can participate as external processes. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa} ruby-devel%{?_isa} ode-devel%{?_isa}
Requires:       DevIL-devel%{?_isa} libGL-devel libGLU-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -S git

%build
mkdir build
cd build
export CXXFLAGS="${CXXFLAGS:-%optflags} -std=gnu++98"
export CFLAGS="${CFLAGS:-%optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIBDIR:PATH=%{_lib} -DODE_CONFIG_EXEC=ode-double-config .. \
  -DRUBY_INCLUDE_PATH=`ruby -e 'puts File.join(RbConfig::CONFIG[%q(includedir)], RbConfig::CONFIG[%q(sitearch)])'`
make VERBOSE=1 %{?_smp_mflags}
make pdf
cp doc/devel/manual.pdf ../doc/devel/

%install
make -C build install DESTDIR=%{buildroot}

ln -fs %{_datadir}/fonts/dejavu/DejaVuSansMono.ttf \
      %{buildroot}/%{_datadir}/%{name}/fonts/VeraMono.ttf
rm -rf %{buildroot}/%{_datadir}/%{name}/*.h

mkdir package_docs
mv %{buildroot}/%{_datadir}/doc/%{name}/* package_docs/
rm -rf %{buildroot}/%{_datadir}/doc

%files
%doc package_docs/*
%dir %{_libdir}/%{name}
# Notice: the package needs .so files for running so
# they can't be moved to -devel package
%{_libdir}/%{name}/[^l]*.so*
%{_libdir}/%{name}/lib*.so.*
%{_libdir}/gui*/*.so
%{_datadir}/%{name}
%{_datadir}/carbon

%files devel
%{_bindir}/*
%{_includedir}/%{name}
%{_includedir}/gui*
%{_libdir}/%{name}/lib*.so
%doc doc/devel/manual.pdf

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.5-9
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.5-8
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.5-6
- Add additional header, fix FTBFS with g++14

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 0.3.5-4
- Rebuilt for Boost 1.83

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.5-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.3.5-1
- Update to latest upstream version with small fixes

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 0.3.3-7
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.3-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Thu Aug 18 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.3.3-4
- Fix Ruby 3 compatibility, closes rhbz#1997693

* Sun Jul 24 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.3-3
- Rebuilt for Ode soname bump

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.3.3-1
- Update to latest upstream version: 0.3.3

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 0.3.2-6
- Rebuilt for Boost 1.78

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.2-5
- F-36: rebuild against ruby31

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.3.2-3
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 11 2021 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.3.2-1
- Update to version 0.3.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-21
- Rebuilt for Boost 1.75

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-20
- F-34: rebuild against ruby 3.0

* Sat Oct 17 2020 Jeff Law <law@redhat.com> - 0.3.0-19
- Fix missing #include for gcc-11

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-17
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-15
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-12
- Rebuilt for Boost 1.69

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-11
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.3.0-9
- Add gcc-c++ build dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-7
- Rebuilt for Boost 1.66

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-6
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-3
- Rebuilt for s390x binutils bug

* Tue Jul 04 2017 Jonathan Wakely <jwakely@redhat.com> - 0.3.0-2
- Rebuilt for Boost 1.64

* Fri Mar 24 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.3.0-1
- New upstream version with Carbon: a gui & simulation framework

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 0.2.4-23
- Rebuilt for Boost 1.63

* Fri Jan 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.4-22
- F-26: rebuild for ruby24

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 0.2.4-21
- Rebuilt for linker errors in boost (#1331983)

* Thu Mar 03 2016 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.4-20
- Fix compilation on GCC 6.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 0.2.4-18
- Rebuilt for Boost 1.60

* Wed Jan 13 2016 Vít Ondruch <vondruch@redhat.com> - 0.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.2.4-16
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.2.4-14
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.2.4-12
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 0.2.4-11
- Rebuild for boost 1.57.0

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.4-10
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Thu Oct 30 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.4-9
- Rebuild due to new ODE version (so version bump)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.2.4-6
- Rebuild for boost 1.55.0

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.2.4-3
- Rebuild for boost 1.54.0

* Sun Jul 21 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.4-2
- Fix update path from f17/f18

* Tue Jun 18 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.4-1
- Update to new upstream release: 0.2.4

* Wed Mar 27 2013 Vít Ondruch <vondruch@redhat.com> - 0.2.3-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.3-5
- Fixed compilation with boost 1.53
- Fix TeXLive dependencies for Fedora 19

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.2.3-4
- Rebuild for Boost-1.53.0

* Wed Aug 15 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.3-3
- Rebuild for Boost 1.50

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.3-1
- Update to new upstream version 0.2.3
- Remove some old .spec stuff (e.g. defattr's)
- Fix bug #704861

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-9
- Rebuilt for c++ ABI breakage

* Thu Feb 16 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.2-8
- Fix compilation under gcc 4.7

* Wed Feb 08 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.2.2-7
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.2-5
- Rebuild for Boost 1.48

* Fri Jul 22 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.2-4
- Rebuild for boost 1.47

* Sat Apr 30 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.2-3
- Added an upstream patch on the log viewer to fix a crash in logviewer
- Make -devel dependencies arch specific, and also base package dependency
- Cleanup: clean section, buildroot tag

* Wed Apr 27 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.2-2
- Link against the correct ode library

* Wed Apr 27 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.2-1
- Updated to latest release 0.2.2

* Sun Apr 17 2011 Kalev Lember <kalev@smartlink.ee> - 0.2.1-5
- Rebuilt for boost 1.46.1 soname bump

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.2.1-3
- Rebuilt to fix crashing in multi-threaded mode
- Replacing an old address in changelog comments

* Wed Aug 04 2010 Hedayat Vatankhah <hedayat@grad.com> - 0.2.1-2
- Rebuild for the new boost
- Fixed multilib conflict in config scripts (rh #507983)

* Wed Jun 09 2010 Hedayat Vatankhah <hedayat@grad.com> - 0.2.1-1
- New upstream version 0.2.1
- Removed conditional for F10 and before

* Tue Jan 19 2010 Hedayat Vatankhah <hedayat@grad.com> 0.2-1
- Updated to latest upstream release 0.2

* Mon Aug 10 2009 Hedayat Vatankhah <hedayat@grad.com> 0.1.2-1
- Updated to latest upstream release 0.1.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 08 2009 Hedayat Vatanlhah <hedayat@grad.com> 0.1-4
- Rebuild for boost 1.39

* Wed Mar 18 2009 Hedayat Vatankhah <hedayat@grad.com> 0.1-3
- fixed lib directory variable for cmake

* Tue Mar 17 2009 Hedayat Vatankhah <hedayat@grad.com> 0.1-2
- Added cmake and DevIL patches
- Removed redundant gcc-c++ requirement
- Add verbose output for make
- Added CXXFLAGS
- Font package name fix for different distros

* Thu Feb 19 2009 Hedayat Vatankhah <hedayat@grad.com> 0.1-1
- Some cleanup
- fixed package documentation installation
- added tex(latex) and ImageMagic as a build requirement

* Fri Feb 13 2009 Hedayat Vatankhah <hedayat@grad.com> 0.1-1
- Initial version
