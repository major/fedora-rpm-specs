%global svnversion 16

Name:           opencl-utils
Version:        1
Release:        17.svn%{svnversion}%{?dist}
Summary:        Useful OpenCL tools and utilities

License:        MIT
Url:            http://code.google.com/p/%{name}
###Commands to grab source from svn:
#svn co -r 16 http://opencl-utils.googlecode.com/svn/trunk/ opencl-utils
#tar -Jcv --exclude-vcs -f opencl-utils.tar.xz opencl-utils
#rm -f -r opencl-utils
Source0:         %{name}.tar.xz
Source1:         %{name}.pc
#Based on dolphin-emu, updates to opencl 1.2:
#https://github.com/dolphin-emu/dolphin/commit/0bd218ea8eb1094c8f86fa4c7efbd8aece355138
#Also disabled autogeneration via perl, as opencl 1.2 breaks it
Patch0:         %{name}-opencl12.patch
#This patch does three things:
#-Reformats the MAKEFILE to be more helpful
#-clrun as a system library rather than local
#-Use system opencl headers instead of bundled
Patch1:         %{name}-sharedcl.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  opencl-headers

%package        devel
Summary:        Devel files for OpenCL Utils
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       opencl-headers

%description
#Modified from the homepage
OpenCL Utils is a project that aims to create various tools and utilities to
make the use of OpenCL more useful and efficient, such as: useful functions,
optimization hints and common kernel templates. This package currently only
contains CLRun, which allows for dynamic loading of OpenCL.

%description devel
This package includes the headers and development files for OpenCL Utils.
OpenCL Utils is a project that aims to create various tools and utilities to
make the use of OpenCL more useful and efficient, such as: useful functions,
optimization hints and common kernel templates.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
#Fix example2.cpp encoding
sed -i 's/\r//' examples/clrun-example/example2.cpp
#To avoid copying a windows build file later on
rm -f examples/OCLUtilsExamples.vcproj
#Remove bundled opencl headers
rm -rf src/include/CL

%build
cd src/clrun/
env CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
cd src/clrun/
make DESTDIR=%{buildroot} \
     LIBDIR=%{_libdir} \
     INCLUDEDIR=%{_includedir} \
     install
install -m 0644 -D %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%files
%{_libdir}/*.so.*

%files devel
%doc examples/*
%{_libdir}/*.so
%{_includedir}/clrun.h
%{_libdir}/pkgconfig/*.pc

%ldconfig_scriptlets

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-17.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-16.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-15.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-14.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-13.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-12.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-11.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-10.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-9.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 1-8.svn16
- BuildRequires: gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-7.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-6.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-5.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-4.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-3.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1-2.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 8 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 1-1.svn16
- Patch code to work with OpenCL 1.2 (based on dolphin-emu)
- Rework previous patches (also bump so to 1.16 to avoid 1.2 api breaking)
- Cleanup, tweaks and fixes based on rpmlint output

* Sun Oct 25 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 0-16.svn16
- Unbundle OpenCL headers, add requires for opencl-headers

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-15.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-14.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-13.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-12.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0-11.svn16
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-10.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-9.svn16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 0-8.svn16
- Fixed a typo (creates a redundant empty folders)
- Fixed missing source devel files
- Added missing buildrequire perl

* Sun Jun 24 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 0-7.svn16
- Reverted reorganizing of source files due to compilation problems

* Sun Jun 24 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 0-6.svn16
- Silenced an rpmlint mixed-use-of-spaces-and-tabs warning
- Implimented reserving timestamps
- Renamed README source file with prefix
- Added bug report for patch0

* Sun Jun 24 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 0-5.svn16
- Various simplications and fixes of the package structure
- Added cleaning of generated files to prep
- Reorganizing of source files
- Added compiling README and added examples as documentation
- Fixed up examples, included packagecfg

* Sun Apr 8 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 0-4.svn16
- Removed all non headers from devel excluding examples
- More tweaks to the makefile (clrun)
- Various improvements/cleanups
- OpenCLpointers patch dropped due to compiling issues (functions fine without)
- trimwhitespace patch dropped due to little purpose

* Thu Apr 5 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 0-3.svn16
- Fixed soname/ldconfig issue
- Typo in the date of the last changelog

* Thu Apr 5 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 0-2.svn16
- Changed sub-packages to something more suitable
- Patched the makefile a little more
- Fixed requirements

* Sun Mar 25 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 0-1.svn16
- Initial package SPEC created

