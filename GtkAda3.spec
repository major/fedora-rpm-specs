Name:           GtkAda3
Version:        2020
Release:        7%{?dist}
Summary:        GTKada 3, an Ada binding to GTK+ 3
Summary(sv):    GTKada 3, en adabindning till GTK+ 3

# Pass "--without opengl" to RPMbuild to disable the -gl subpackage.
%bcond_without opengl

# The GPS plug-in is excluded because GPS isn't packaged.
# Pass "--with gps" to RPMbuild to include it.
%bcond_with gps

License:        GPLv3+ with exceptions
URL:            https://github.com/AdaCore/gtkada
Source:         https://community.download.adacore.com/v1/35a07c29543ba779a96e690ea10db866fa1e92e3?filename=gtkada-2020-20200814-19A6C-src.tar.gz#/gtkada-2020-20200814-19A6C-src.tar.gz
# The long hexadecimal number is what identifies the file on the server.
# Don't forget to update it!
# The latest known address of the download page is:
# https://www.adacore.com/download/more
Source2:        testgtk_Makefile
Source3:        testgtk.gpr
Source4:        gtkada.gpr
Source5:        gtkada_gl.gpr

# GNU-specific patch to avoid link bloat:
Patch1:         gtkada-3.14.2-libs.patch
# Workaround for name collisions with stuff that was added to GTK+:
Patch3:         gtkada-2017-namespace.patch
# Port the binding generator to Python 3:
# https://github.com/AdaCore/gtkada/pull/23
Patch4:         gtkada-2020-python3.patch

BuildRequires:  gcc-gnat gprbuild fedora-gnat-project-common
BuildRequires:  python3
BuildRequires:  gtk3-devel
%if %{with opengl}
BuildRequires:  libGL-devel libGLU-devel
%endif
BuildRequires:  make diffutils recode
%if %{with gps}
BuildRequires:  sed
%endif
# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
GTKada is an Ada binding to the graphical toolkit GTK+. It allows you to \
develop graphical user interfaces in Ada using GTK+.

%global common_description_sv \
GTKada är en adabindning till den grafiska verktygslådan GTK+. Med GTKada \
kan du utveckla grafiska användargränssnitt i ada baserade på GTK+.

%description %{common_description_en}

%description -l sv %{common_description_sv}


%package devel
Summary:        Development files for GTKada 3
Summary(sv):    Filer för programmering med GTKada 3
Requires:       fedora-gnat-project-common
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with opengl}
Requires:       %{name}-gl%{?_isa} = %{version}-%{release}
%endif
Recommends:     %{name}-doc
Conflicts:      GtkAda-devel < 3

# Unlike GTK+, GTKada has no support for installing two versions side by side,
# other than dumping the entire directory tree under some nonstandard prefix
# and requiring users to mess with various environment variables. Despite the
# API incompatibilities, both versions use the filename "gtkada.gpr" and
# directories named "gtkada".
#
# Hacking the build system to change various filenames from "gtkada" to
# "gtkada3" would be more trouble than it's worth, and would make Fedora
# incompatible with everything that uses GTKada. Both developers and packagers
# would have to do special things to select the right version of the library.
#
# Therefore GtkAda-devel and GtkAda3-devel are allowed to conflict.

%description devel %{common_description_en}

The %{name}-devel package contains source code and linking information for
developing applications that use GTKada 3.x.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder GTKada 3.x.


%package gl
Summary:        GTKada 3 binding to OpenGL
Summary(sv):    GTKada 3:s bindning till OpenGL
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description gl %{common_description_en}

The %{name}-gl package contains the GTKada binding to the OpenGL interface.

%description gl -l sv %{common_description_sv}

Paketet %{name}-gl innehåller GTKadas bindning till OpenGL-gränssnittet.


%package doc
Summary:        Documentation for GTKada 3
Summary(sv):    Dokumentation till GTKada 3
BuildArch:      noarch

%description doc %{common_description_en}

The %{name}-doc package contains the documentation for GTKada 3.x.

%description doc -l sv %{common_description_sv}

Paketet %{name}-doc innehåller dokumentationen till GTKada 3.x.


# The hardening hack needs to be disabled because of gtkada-dialog and the demo
# programs, until someone figures out how to make it work for Ada.
# https://bugzilla.redhat.com/show_bug.cgi?id=1197501
%undefine _hardened_build


%prep
%autosetup -n gtkada-2020-20200814-19A6C-src -p0

# Transcode the author's name in comments in some source files.
recode ISO-8859-1..UTF-8 src/opengl/{gdkgl,gtkglarea}.[hc] testgtk/opengl/lw.[hc]

# Remove bogus executable bits.
chmod a-x testgtk/*.ad[sb]


%build
# This package triggers a GCC failure when building with LTO.  Disable
# LTO for now.  fld_incomplete_type_of, at tree.c:5371
%define _lto_cflags %{nil}

%{configure} --disable-static --disable-static-pic %{!?with_opengl:--with-GL=no}

# Regenerate the generated Ada packages to verify that they can be regenerated.
# Use the included GIR files, because binding.py is only expected to work with
# those specific files.
mv src/generated src/pre-generated
mkdir src/generated
make generate PYTHON=python3

# Compare the generated packages to the pre-generated ones to verify that the
# code being compiled is the same as what the developers upstream have reviewed
# and tested. Ignore differences in comment lines.
rm src/generated/tmp.ada
diff --recursive --ignore-matching-lines='^-- ' src/pre-generated src/generated >&2

# Build the library, and also perform configuration of the demo source code.
# Allow it to also build the demo programs. It has some value as a smoke test.
make GPRBUILD_FULL="gprbuild %{GPRbuild_optflags}"

# The documentation is not regenerated because that requires GPS and would
# cause a dependency loop.


%install
%global demodir %{_pkgdocdir}/examples/testgtk
%global inst install --mode=u=rw,go=r,a-s --preserve-timestamps

%{make_install} PRJDIR=%{buildroot}%{_GNAT_project_dir} exampledir=%{demodir}

# Move the binary libraries into place and fix the links.
if test lib != '%{_lib}' ; then
    mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
fi
pushd %{buildroot}%{_libdir}
mv gtkada/*/gtkada/libgtkada*.so.* .
rm libgtkada*.so gtkada/*/gtkada/libgtkada*.so
ln -s libgtkada.so.* libgtkada.so
ln -s libgtkada_gl.so.* libgtkada_gl.so
popd

# It's much easier to install our own multilib-compatible usage project files
# than to patch the ones that GPRinstall generated.
%{inst} %{SOURCE4} %{SOURCE5} --target-directory=%{buildroot}%{_GNAT_project_dir}

# GPRinstall's manifest files are architecture-specific because they contain
# what seems to be checksums of architecture-specific files, so they must not
# be under _datadir. Their function is apparently undocumented, but my crystal
# ball tells me that they're used when GPRinstall uninstalls or upgrades
# packages. The manifest file is therefore irrelevant in this RPM package, so
# delete it.
rm -rf %{buildroot}%{_GNAT_project_dir}/manifests

# Exclude the compiled demo programs from the documentation directory.
rm %{buildroot}%{demodir}/test{gtk,_rtree}

# Move the manuals and demo source code into place.
mv %{buildroot}%{_prefix}/share/doc/gtkada/* --target-directory=%{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_prefix}/share/examples/gtkada/testgtk/* --target-directory=%{buildroot}%{demodir}

# Add missing TestGTK sources.
mkdir --parents %{buildroot}%{demodir}/opengl %{buildroot}%{demodir}/task_project/src
%{inst} testgtk/opengl/*.{h,c,ads,adb,gpb} --target-directory=%{buildroot}%{demodir}/opengl
%{inst} testgtk/task_project/src/*.ad? --target-directory=%{buildroot}%{demodir}/task_project/src

# Add a standalone build system for the demo programs so that users can build
# them and link them to the packaged libraries.
%{inst} --no-target-directory %{SOURCE2} %{buildroot}%{demodir}/Makefile
%{inst} %{SOURCE3} --target-directory=%{buildroot}%{demodir}

%if %{with gps}
# Adjust the documentation directory in the GPS plug-in, and change its
# filename to avoid a conflict between GtkAda3-doc and GtkAda-doc.
sed --in-place --expression=s:share/doc/gtkada:share/doc/GtkAda3:g %{buildroot}%{_datadir}/gps/plug-ins/gtkada.xml
mv %{buildroot}%{_datadir}/gps/plug-ins/gtkada.xml %{buildroot}%{_datadir}/gps/plug-ins/gtkada3.xml
%else
rm -rf %{buildroot}%{_datadir}/gps
%endif

# These files that Sphinx generates aren't needed in the package.
rm %{buildroot}%{_pkgdocdir}/gtkada_ug/{.buildinfo,objects.inv}

# This preprocessor input file isn't needed in the package.
rm %{buildroot}%{_pkgdocdir}/gtkada_rm/index.html.in

# Include these license and documentation files.
mkdir --parents %{buildroot}%{_licensedir}/%{name}
%{inst} COPYING* --target-directory=%{buildroot}%{_licensedir}/%{name}
%{inst} AUTHORS README.md features* known-problems* --target-directory=%{buildroot}%{_pkgdocdir}


%files
%{_libdir}/libgtkada.so.*
%license %{_licensedir}/%{name}
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README.md


%if %{with opengl}
%files gl
%{_libdir}/libgtkada_gl.so.*
%endif


%files devel
%{_bindir}/*
%{_includedir}/gtkada
%{_libdir}/gtkada
%{_GNAT_project_dir}/*
%{_libdir}/lib*.so


%files doc
# features and known-problems belong with the documentation for developers.
# The license, the list of authors and the directories need to be replicated in
# the doc subpackage as it doesn't depend on the main package.
%license %{_licensedir}/%{name}
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/features*
%{_pkgdocdir}/known-problems*
%{_pkgdocdir}/gtkada_ug
%{_pkgdocdir}/gtkada_rm
%{_pkgdocdir}/examples
%if %{with gps}
%{_datadir}/gps
%endif


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2020-4
- rebuilt with gcc-11.0.1-0.3

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Björn Persson <Bjorn@Rombobjörn.se> - 2020-2
- Rebuilt with GCC 11.

* Fri Sep 25 2020 Björn Persson <Bjorn@Rombobjörn.se> - 2020-1
- Upgraded to the 2020 release.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jeff Law <law@redhat.com> - 2017-11
- Disable LTO

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Björn Persson <Bjorn@Rombobjörn.se> - 2017-8
- Built for x86.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2017-5
- rebuilt

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Björn Persson <Bjorn@Rombobjörn.se> - 2017-1
- Upgraded to the 2017 release.
- This release doesn't seem to have a traditional version number, so the year
  is now used as the version.
- Added a version number in gtkada.gpr that GPS's configuration script wants.

* Sat Apr 22 2017 Björn Persson <Bjorn@Rombobjörn.se> - 3.14.2-3
- Adapted pathnames in the project files.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 05 2016 Björn Persson <Bjorn@Rombobjörn.se> - 3.14.2-1
- Upgraded to 3.14.2.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 3.8.3-2
- Rebuilt with GCC 6 prerelease.

* Tue Jul 21 2015 Björn Persson <bjorn@rombobjörn.se> - 3.8.3-1
- Upgraded to 3.8.3.
- The demo source code in GtkAda3-doc is now buildable out of the box.

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 22 2015 Björn Persson <bjorn@rombobjörn.se> - 3.8.2-5
- Changed the pseudo-namespace of some identifiers to work around name
  collisions with stuff that was added to GTK+.

* Mon Mar 16 2015 Than Ngo <than@redhat.com> - 3.8.2-4
- bump release and rebuild so that koji-shadow can rebuild it
  against new gcc on secondary arch

* Sat Feb 07 2015 Björn Persson <bjorn@rombobjörn.se> - 3.8.2-3
- Rebuilt with GCC 5.0.0.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Björn Persson <bjorn@rombobjörn.se> - 3.8.2-1
- Upgraded to 3.8.2.
- Enabled the OpenGL bindings.
- Excluded the GPS plug-in.

* Sat May 10 2014 Björn Persson <bjorn@rombobjörn.se> - 3.4.2-3
- Build the demo programs in the check phase instead of the build phase.

* Tue Feb 04 2014 Björn Persson <bjorn@rombobjörn.se> - 3.4.2-2
- Verify that the generated Ada code is the same as what the developers
  upstream have reviewed and tested.

* Tue Jan 28 2014 Björn Persson <bjorn@rombobjörn.se> - 3.4.2-1
- New package for GTKada 3.x, partly based on the existing package GtkAda.
