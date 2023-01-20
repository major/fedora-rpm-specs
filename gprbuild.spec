%undefine _hardened_build
### global bootstrap_arch  %{GPRbuild_arches}
%global bootstrap_arch  no_bootstraping

# When bootstrapping GPRbuild for a new architecture, set bootstrap_arch to the
# name of that architecture and add a tarball with binaries as Source100.
# When not bootstrapping bootstrap_arch must have a nonempty value that isn't
# an architecture name, as this spec would be syntactically invalid otherwise.
#
# Bootstrapping exception: https://fedorahosted.org/fpc/ticket/605
%ifarch %{bootstrap_arch}
%global debug_package %{nil}
%endif
# Stripping out debugging information isn't important when bootstrapping, and
# skipping this allows one to avoid unnecessary efforts to produce unstripped
# binaries to bootstrap with.
%ifnarch %{bootstrap_arch}
%define with_libgpr 1
%else
%define with_libgpr 0
%endif
%global _python_bytecompile_extra 0

Name:       gprbuild
Version:    2020
Release:    12%{?dist}
Summary:    Ada project builder
License:    GPLv3+
URL:        http://libre.adacore.com
## Direct download is not available
Source0:    gprbuild-2020-20200429-19BD2-src.tar.gz
# target patterns for Fedora's architectures:
Source2:    fedora_arches.xml
Source3:    gprbuild-sanity.tar.gz
Patch2:     %{name}-2016-gcc5.patch
# This usrmove patch works for this package. Upstream a different solution
# would be needed to handle other possible setups.
Patch3:     %{name}-2016-usrmove.patch
Patch6:       %{name}-2017-fedora_compilers.patch
# Adaptation to a change in GCC's version numbering:
Patch8:     %{name}-2016-gcc7.patch

Patch11:    gprbuild-2017-libsubdir.patch
Patch10:    gprbuild-drop_exe_prefix.patch
Patch4:     gprbuild-symlinked_dirs.patch
# GPRbuild and Google's GRPC both want the filename "libgpr.so". This patch
# renames the library to "libgnatprj.so" to resolve the conflict. The name is
# chosen for consistency with Debian.
Patch12:    gprbuild-2020-resolve_libgpr_conflict.patch
# Resolve collisions between Ada.Characters.Handling.To_Lower and
# GNAT.Case_Util.To_Lower (already fixed upstream):
Patch13:    gprbuild-2020-case_util_conflicts.patch


%ifarch %{bootstrap_arch}
BuildRequires:  xmlada-sources
%else
# xmlada devel must be explicitly specified for first build
# after bootstrap.
BuildRequires: xmlada-devel > 2018-6
BuildRequires: xmlada-static > 2018-6
%endif

%ifnarch %{bootstrap_arch}
BuildRequires: gprbuild
%endif

BuildRequires:  gcc-gnat > 5.1
BuildRequires:  libgnat-static >= 6.1
BuildRequires:  fedora-gnat-project-common >= 2
BuildRequires: make

## for make doc
## FIXME ??? XXXX
## Doc build is broken
###BuildRequires:  python3-sphinx texinfo doxygen

Requires:       fedora-gnat-project-common >= 2
Requires:       gnat-srpm-macros
%ifnarch %{bootsrap_arch}
# Build only on architectures where GPRbuild is already available, plus the
# architecture being bootstrapped, if any:
ExclusiveArch:  %{GPRbuild_arches} %{bootstrap_arch}
%endif

%description
GPRbuild is an advanced software tool designed to help automate
the construction of multi-language systems.
It removes complexity from multi-language development by allowing
developers to quickly and easily compile and link software written
in a combination of languages including Ada, Assembler, C, C++, and Fortran.
Easily extendable by users to cover new toolchains and languages
it is primarily aimed at projects of all sizes organized into subsystems
and libraries and is particularly well-suited for compiled languages.

%ifnarch %{bootstrap_arch}
%package doc
Summary:        Documentation for GPRbuild
License:        GPLv3+
Requires:       %{name} = %{version}-%{release}

%description doc
%{summary}
%endif

%if %{with_libgpr}
%package -n libgpr
# The source file headers indicate that its name is "GPR Project Manager".
Summary:        GPR Project Manager library
License:        GPLv3+
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n libgpr
The GPR Project Manager is an Ada library for handling GNAT project files. It is
part of GPRbuild.

This is not the libgpr that is part of GRPC from Google.

%package -n libgpr-devel
Summary:        Development files for the GPR Project Manager
License:        GPLv3+
Requires:       libgpr%{?_isa} = %{version}-%{release}

%description -n libgpr-devel
The GPR Project Manager is an Ada library for handling GNAT project files. It is
part of GPRbuild.

The libgpr-devel package contains source code and linking information for
developing applications that use the GPR Project Manager.

This is not the libgpr that is part of GRPC from Google.
%endif

%prep
%setup -q -n gprbuild-2020-20200429-19BD2-src
#%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .symlinked
%patch6 -p1
###%patch7 -p1
%patch8 -p0
%patch10 -p1 -b .exe
%patch11 -p1 -b .libusr
%patch12 -p1
%patch13 -p1


%build
%ifarch %{bootstrap_arch}
## Some useful output
gcc -v
gcc -dumpmachine
gcc -dumpversion
gnatls -v --version
##
export GNATMAKEFLAGS="%{Gnatmake_optflags}"
./bootstrap.sh --with-xmlada=%{_includedir}/xmlada/sources/ --prefix=%{buildroot}/%{_prefix}/ build
cp %{SOURCE2} %{buildroot}/%{_datarootdir}/gprconfig/
%else
make prefix=%{buildroot}/%{_prefix} setup BUILD=debug
XMLADA_BUILD=shared make BUILDER="gprbuild -v %{GPRbuild_optflags}" all BUILD=debug
%if %{with_libgpr}
XMLADA_BUILD=shared make BUILDER="gprbuild -v %{GPRbuild_optflags}" libgpr.build.shared BUILD=debug
%endif
%endif

%ifarch %{bootstrap_arch}
%check
tar -xvf %{SOURCE3}
PATH="%{buildroot}/%{_bindir}:$PATH" gprbuild -P ./gprbuild-tests/tests_shared.gpr
%endif

%install
%{?filter_setup:
%filter_requires_in %{_libdir}
%filter_requires_in %{_bindir}
%filter_setup
}
%ifarch %{bootstrap_arch}
bash -x ./bootstrap.sh --with-xmlada=%{_includedir}/xmlada/sources/ --prefix=%{buildroot}/%{_prefix}/ install
# Add target patterns for Fedora's architectures.
cp %{SOURCE2} %{buildroot}%{_datadir}/gprconfig/
exit 0
%endif
rm -rf %{buildroot}
%ifarch %{bootstrap_arch}
export PATH="$PWD/bin/:${PATH}"
export INSTALLER="$PWD/bin/gprinstall"
%endif

make install DESTDIR=%{buildroot} BUILD=debug
%if %{with_libgpr}
make install DESTDIR=%{buildroot} libgpr.install.shared BUILD=debug LIB_DIR=%{buildroot}/%{_libdir}
%endif
%if %{with_libgpr}
cd %{buildroot}/%{_libdir} && find . -name '*.so' -exec ln -rs {} \; && cd - 
%endif
find %{buildroot}%{_datadir}/gprconfig -type f -name "*.xml" -exec chmod -x {} \;
# Add target patterns for Fedora's architectures.
cp %{SOURCE2} %{buildroot}%{_datadir}/gprconfig/

# Install the Info version of the manual where Info files belong.
mv --no-target-directory %{buildroot}%{_pkgdocdir}/info %{buildroot}%{_infodir}

mkdir __doc
mv  %{buildroot}/%{_datadir}/doc/%{name}/* __doc
mv %{buildroot}/%{_datadir}/examples __doc
rm -rf %{buildroot}/%{_datadir}/doc/%{name} 
##%%find __doc/examples -type f -exec chmod -x {} \;
rm -f %{buildroot}/%{_prefix}/doinstall
rm -rf %{buildroot}%{_GNAT_project_dir}/manifests


%files
%doc README.md COPYING* CHANGE*
%ifnarch %{bootstrap_arch}
%doc __doc/*
%{_infodir}/*
%endif
%{_bindir}/gpr*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gpr*
%{_datadir}/gprconfig
%_GNAT_project_dir/_default.gpr

%if %{with_libgpr}
%files -n libgpr
%dir %{_libdir}/gpr
%dir %{_libdir}/gpr/relocatable
%dir %{_libdir}/gpr/relocatable/gpr
%{_libdir}/libgnatprj.so
%{_libdir}/gpr/relocatable/gpr/libgnatprj.so

%files -n libgpr-devel
%{_includedir}/gpr
%{_libdir}/gpr/relocatable/gpr/*.ali
%_GNAT_project_dir/gpr.gpr
%endif

%ifnarch %{bootstrap_arch}
%files doc
%doc doc/*
%endif

%changelog
* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2020-12
- Rebuilt with GCC 13.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 05 2022 Björn Persson <Bjorn@Rombobjörn.se> - 2020-10
- Fixed the location of the Info file.

* Wed Feb 02 2022 Björn Persson <Bjorn@Rombobjörn.se> - 2020-9
- Added workarounds to be able to build with GCC 12 prerelease.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2020-6
- rebuilt with gcc-11.0.1-0.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-4
- Workaround for possible gcc bug 

* Tue Dec  8 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-3
- Fix builds of symlinked projects

* Mon Dec  7 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-1
- New version 2020. Rebuild with new gnat

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb  3 2020 Pavel Zhukov <pzhukov@redhat.com> - 2018-16
- rebuild grpuild

* Mon Feb  3 2020 Pavel Zhukov <pzhukov@redhat.com> - 2018-15
- Bootstrap with gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-12
- Normal build (non bootstrap'ed)

* Sun Feb 10 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-11
- Fix target for armv7hl

* Sat Feb  9 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-9
- Rebuild with new gnat-srpm-macros
- Enable sanity tests for bootstrap arches

* Tue Feb  5 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-7
- Add simple tests
- Build with fedora flags
- Add canonical names for targetsets

* Tue Feb  5 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-3
- Bootstrap for all arches

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Pavel Zhukov <pzhukov@redhat.com> - 2017-14
- Do not byte-compile python

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017-13
- Escape macros in %%changelog

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2017-12
- rebuilt

* Tue Aug  1 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-11
- Specify Ada is default language.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-8
- Enable libgpr. Add subpackage.
- Move gpr.gpr to libgpr-devel
- Move ALIs to devel

* Sat Jul 15 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-6
- Disable bootstrap for all arches

* Sat Jul 15 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-5
- Use upstream bootstrap
- Enable bootstrap for all %%{GPRbuild_arches}

* Fri Jul 14 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-2
- New version 2017
- Drop dev suffix

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2016-7
- Rebuild due to bug in RPM (RHBZ #1468476)

* Thu Feb 16 2017 Björn Persson <Bjorn@Rombobjörn.se> - 2016-6
- Reverted the temporary workaround.

* Mon Feb 13 2017 Björn Persson <Bjorn@Rombobjörn.se> - 2016-5
- Patched the GPRconfig knowledge base to adapt to a change in GCC's version numbering.
- Made a temporary workaround to rebuild with GCC 7 prerelease.

* Sun Feb  5 2017 Pavel Zhukov <pavel@zhukoff.net> - 2016-3
- Rebuild with new gnat

* Wed Nov 02 2016 Maxim Reznik <reznikmm@gmail.com> - 2016-3
- Fix mingw32 targets to match one from fedora packages
- Fix mingw patch conflict

* Sun Aug 07 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2016-1
- Upgraded to the 2016 release.
- The license has changed to GPLv3+.

* Sun Apr 17 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2015-13
- Added target patterns to make GPRconfig recognize the native GCC on Fedora's
  secondary architectures.
- Re-bootstrapped on ppc64.
- Bootstrapped on ppc64le.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2015-8
- Re-bootstrapped on ARM.

* Tue Jan 19 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2015-6
- GPRbuild no longer requires XMLada as it's statically linked in.

* Tue Jan 19 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2015-5
- Build only on x86 and x86-64.

* Wed Dec 23 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2015-4
- Changed to static linking.

* Thu Jun 25 2015  Pavel Zhukov  <landgraf@fedoraproject.org> - 2015-3
- Remove disabling of autorequires 

* Thu Jun 25 2015  Pavel Zhukov  <landgraf@fedoraproject.org> - 2015-2
- Add xmlada to requires. Missed by disable autorequires

* Thu Jun 25 2015  Pavel Zhukov  <landgraf@fedoraproject.org> - 2015-1
- New Release (#2015)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Pavel Zhukov  <landgraf@fedoraproject.org> - 2014-8
- Modify usrmove patch

* Sun May 24 2015 Pavel Zhukov  <landgraf@fedoraproject.org> - 2014-7
- Ship gnat 5.1 headers

* Mon May  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2014-6
- Don't build ADA hardened

* Sat May 02 2015 Björn Persson <bjorn@rombobjörn.se> - 2014-5
- Fixed a bug that threw away GCC options that begin with "-m".

* Sun Mar 29 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2014-4
- New release (2014)
- Fix library version 

* Sun Feb 15 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-16
- Remove OpenVMS from supported OS

* Sat Feb 14 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-15
- Rebuild with new gcc 5.0

* Mon Nov 10 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2013-14
- Update config.sub and config.guess for new architectures

* Sat Oct 11 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-13
- Add gnat-srpm-macros as dependency
 
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 09 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-11
- Add arm to compillers list

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2013-8
- Use GNAT_arches rather than an explicit list

* Wed May  7 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-7
- Rebuild with new libgnat

* Mon Nov 18 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-6
- Add fedora-gnat-project-common to the requires list

* Wed Sep 04 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-5
- changed http://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2013-2
- rebuild with Fedora optflags (#984721)

* Sat Jul 13 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2013-1
- New release (2013)

* Fri Jan 25 2013   Pavel Zhukov <landgraf@fedoraproject.org> - 2012-4
- Rebuild with GCC 4.8 

* Tue Dec 18 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2012-3
- Rebuild for new xmlada

* Mon Dec 17 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2012-2
- Update to gprbuild 2012

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Julian Leyh <julian@vgai.de> - 2011-4
- Remove rpath from default configuration
- Make parsing of gcc version locale-independant

* Sun Mar 04 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-3
- Updated to 2011 (#722704)
- Add unreference patch

* Mon Feb 27 2012 Björn Persson <bjorn@rombobjörn.se> - 2011-1
- Patched to resolve the link /bin → /usr/bin.
- Removed a superfluous explicit dependency on xmlada.

* Sun Jul 17 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2010-10
- Rebuld for xmlada 2011

* Thu Mar 24 2011 Dan Horák <dan[at]danny.cz> - 2010-8
- updated the supported arch list
