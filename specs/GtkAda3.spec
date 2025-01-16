# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     gtkada
%global upstream_version  25.0.0
%global upstream_gittag   v%{upstream_version}

Name:           GtkAda3
Epoch:          2
Version:        %{upstream_version}
Release:        2%{?dist}
Summary:        GTKada, an Ada binding to GTK+ 3
Summary(sv):    GTKada, en adabindning till GTK+ 3

# The GNAT Studio plug-in is excluded because GNAT Studio isn't packaged.
# Pass "--with gps" to RPMbuild to include it.
%bcond_with gps

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNAT-exception
# The license is GPLv3+ with the GCC runtime exception, except for:
# - src/misc.c          : GPLv2+ with GNAT runtime exception
# - src/misc_osx.h      : GPLv2+ with GNAT runtime exception
# - src/misc_osx.m      : GPLv2+ with GNAT runtime exception
# - src/gtkada-intl.gpb : GPLv2+ with GNAT runtime exception

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

Source2:        testgtk_Makefile
Source3:        testgtk.gpr
Source4:        gtkada.gpr.in

# [Fedora-specific] Don't rebuild the library when building gtkada-dialog.
Patch:          %{name}-enable-a-staged-build.patch
# [Fedora-specific] GNAT Studio plugin: remove shortcut to the GtkAda RM.
Patch:          %{name}-gps-plugin-remove-gtkada-rm.patch
# Don't raise Constraint_Error instead of displaying an iconless custom dialog:
# https://github.com/AdaCore/gtkada/issues/56
Patch:          gtkada-dialog-constraint_error.patch

BuildRequires:  gcc-gnat gprbuild make
# A fedora-gnat-project-common that contains GPRbuild_flags is needed.
BuildRequires:  fedora-gnat-project-common >= 3.17

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk

BuildRequires:  python3
BuildRequires:  gtk3-devel
BuildRequires:  diffutils
BuildRequires:  sed
BuildRequires:  findutils

# Build only on architectures where GPRbuild is available:
ExclusiveArch:  %{GPRbuild_arches}

# GTK.GLarea is now included in the main library so GtkAda3-gl is gone. Let
# upgrades remove the subpackage:
Obsoletes:      GtkAda3-gl < 2:23

%global common_description_en \
GTKada is an Ada binding to the graphical toolkit GTK+. It allows you to \
develop graphical user interfaces in Ada using GTK+.

%global common_description_sv \
GTKada är en adabindning till den grafiska verktygslådan GTK+. Med GTKada \
kan du utveckla grafiska användargränssnitt i ada baserade på GTK+.

%description %{common_description_en}

This version of GTKada binds to GTK+ 3.x.

%description -l sv %{common_description_sv}

Denna versionen av GTKada binder till GTK+ 3.x.


#################
## Subpackages ##
#################

%package devel
Summary:        Development files for GTKada for GTK+ 3
Summary(sv):    Filer för programmering med GTKada för GTK+ 3
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(glib-2.0)
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
developing applications that use GTKada to bind to GTK+ 3.x.

%description devel -l sv %{common_description_sv}

Paketet %{name}-devel innehåller källkod och länkningsinformation som behövs
för att utveckla program som använder GTKada för att binda till GTK+ 3.x.


%package doc
Summary:        Documentation for GTKada for GTK+ 3
Summary(sv):    Dokumentation till GTKada för GTK+ 3
BuildArch:      noarch
License:        GFDL-1.1-no-invariants-or-later AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1
# The documents have a GFDL 1.1 license with no invariants. Some Javascript and
# CSS files that Sphinx includes with the documentation are BSD 2-Clause and MIT
# licensed. The example code is licensed under GPLv3+ with the GCC runtime
# exception.

%description doc %{common_description_en}

The %{name}-doc package contains the documentation for GTKada for GTK+ 3.x.

%description doc -l sv %{common_description_sv}

Paketet %{name}-doc innehåller dokumentationen till GTKada för GTK+ 3.x.


#############
## Prepare ##
#############

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -p1

# The substitutions below are scoped to specific lines to increase the chance of
# detecting code changes at this point. Sed should exit with exit code 0 if the
# substitution succeeded (using `t`, jump to end of script) or exit with a non-
# zero exit code if the substitution failed (using `q1`, quit with exit code 1).

# Change the name of the target directory of the documentation to avoid a
# conflict between GtkAda3-doc and GtkAda-doc.
sed --in-place \
    --expression='83 { s,share/doc/gtkada,share/doc/GtkAda3, ; t; q1 }' \
    --expression='86 { s,share/doc/gtkada,share/doc/GtkAda3, ; t; q1 }' \
    src/gtkada.gpr

# Adjust the documentation directory in the GPS plug-in as-well.
sed --in-place \
    --expression='4 { s,share/doc/gtkada,share/doc/GtkAda3, ; t; q1 }' \
    xml/gtkada.xml

# Set the target directory of the artifacts of the `testgtk` application to be
# relative to the prefix argument of GPRinstall, and don't treat the Ada source
# code as artifacts.
sed --in-place \
    --expression='45 { s,share/examples/gtkada/testgtk,\./, ; t; q1 }' \
    --expression='46 { s|"\*\.ad\*", ||                     ; t; q1 }' \
    testgtk/testgtk.gpr

# Update the package version (also in configure.ac, as this is the source for
# the version shown in the documentation; see also `docs/gtkada_ug/conf.py`).
sed --in-place \
    --expression='1   { s,18.0w,%{version}, ; t; q1 }' \
    ./configure.ac
sed --in-place \
    --expression='582 { s,18.0w,%{version}, ; t; q1 }' \
    --expression='583 { s,18.0w,%{version}, ; t; q1 }' \
    ./configure

# Remove VCS files. Some interfere with the code generation check at the
# beginning of the build section.
find -name ".cvsignore" -type f -delete
find -name ".gitignore" -type f -delete

# Remove bogus executable bits.
chmod a-x testgtk/*.ad[sb]


###########
## Build ##
###########

%build
# This package triggers a GCC failure when building with LTO.  Disable
# LTO for now.  fld_incomplete_type_of, at ipa-free-lang-data.cc:257
%define _lto_cflags %{nil}

%{configure} --disable-static --disable-static-pic

# NOTE FOR v23.0.0: The re-generated code does not match the pre-generated code
# in the tarball: upstream made manual changes to the pre-generated code:
#
#    gtk-list_store.adb : upstream commit 99dafa9, near line 536
#    gtk-list_store.adb : upstream commit e9c0e98, near line 536
#    gtk-tree_model.adb : upstream commit 6ae5622, near line 1110
#
# We'll disable the regeneration for now and continue to use the pre-generated
# code with the manual changes.

%if 0

# Regenerate the generated Ada packages to verify that they can be regenerated.
# Use the included GIR files, because binding.py is only expected to work with
# those specific files.
mv src/generated src/pre-generated
mkdir src/generated
make generate PYTHON='%{python3}'

# Compare the generated packages to the pre-generated ones to verify that the
# code being compiled is the same as what the developers upstream have reviewed
# and tested. Ignore differences in comment lines.
rm src/generated/tmp.ada
diff --recursive --ignore-matching-lines='^-- ' src/pre-generated src/generated >&2

%endif

# In order to build gtkada-dialog with hardening switches and dynamically link
# it with the GTKada library, we need to build the library first and then stage
# it.
mkdir stage  # without --parents to avoid clobbering any existing directory

# Build the library.
%{make_build} relocatable GPRBUILD_OPTIONS='%{GPRbuild_flags} -largs -lm -gargs'

# Build the documentation (user's guide only as the reference guide requires
# Gnatdoc; a tool that has not been packaged yet). We build the documentation
# now as it's installed with gtkada.gpr (see `Artifacts` package in gtkada.gpr).
make -C docs/gtkada_ug html latexpdf

# Stage the library and documentation. Use GPRinstall directly instead of the
# Makefile rule to have full control over what is installed where.
%{GPRinstall -d stage -s gtkada -a gtkada} \
    --no-build-var --no-lib-link -P src/gtkada.gpr

# Create the library link.
ln --symbolic --force libgtkada.so.%{version} stage%{_libdir}/libgtkada.so

# Additional flags to link the executable (gtkada-dialog) dynamically with the
# GNAT runtime and make it position-independent.
%global GPRbuild_flags_pie -cargs -fPIC -largs -pie -bargs -shared -gargs

# Build gtkada-dialog.
%{make_build} tools GPRBUILD_OPTIONS='%{GPRbuild_flags} %{GPRbuild_flags_pie} -largs -lm -gargs -aP stage%{_GNAT_project_dir}'

# Stage gtkada-dialog.
%{GPRinstall -d stage} --no-build-var --mode=usage \
    -aP stage%{_GNAT_project_dir} -P src/tools/tools.gpr


#############
## Install ##
#############

%install
%global demodir %{_pkgdocdir}/examples/testgtk
%global inst install --mode=u=rw,go=r,a-s --preserve-timestamps

# The library, gtkada-dialog and the documention have already been staged, so
# just copy them to the "buildroot" staging directory. Do not move (mv) because
# find-debuginfo will want to collect some files under stage.
cp --archive stage/* --target-directory=%{buildroot}

# Install the examples (testgtk plus related).
gprinstall --create-missing-dirs --no-manifest --no-build-var \
           --prefix=%{buildroot}%{demodir} \
           --sources-subdir=%{buildroot}%{demodir} \
           --project-subdir=%{buildroot}%{demodir} \
           --sources-only \
           -P testgtk/testgtk.gpr

gprinstall --create-missing-dirs --no-manifest --no-build-var \
           --prefix=%{buildroot}%{demodir}/task_project \
           --sources-subdir=%{buildroot}%{demodir}/task_project/src \
           --project-subdir=%{buildroot}%{demodir}/task_project/ \
           --sources-only \
           -P testgtk/task_project/task_project.gpr

# It's much easier to install our own multilib-compatible usage project file
# than to patch the one that GPRinstall generated.
# It needs the version string inserted though.
sed --expression='22 { s,@VERSION@,%{version}, ; t; q1 }' \
    %{SOURCE4} \
    >%{buildroot}%{_GNAT_project_dir}/gtkada.gpr

# Add a standalone build system for the demo programs so that users can build
# them and link them to the packaged libraries.
%{inst} --no-target-directory %{SOURCE2} %{buildroot}%{demodir}/Makefile
%{inst} %{SOURCE3} --target-directory=%{buildroot}%{demodir}

# Rename the GNAT Studio plugin.
mv %{buildroot}%{_datadir}/gps/plug-ins/gtkada.xml \
   %{buildroot}%{_datadir}/gps/plug-ins/gtkada3.xml

# Include these license and documentation files.
mkdir --parents %{buildroot}%{_licensedir}/%{name}
%{inst} COPYING* --target-directory=%{buildroot}%{_licensedir}/%{name}
%{inst} AUTHORS README.md features* known-problems* --target-directory=%{buildroot}%{_pkgdocdir}


###########
## Files ##
###########

%files
%{_libdir}/libgtkada.so.*
%license %{_licensedir}/%{name}
%dir %{_pkgdocdir}
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/README.md


%files devel
%dir %{_includedir}/gtkada
# Exclude some junk that doesn't belong under /usr/include:
%exclude %{_includedir}/gtkada/*.[ch]
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/gtkada/*.ad[sb]
%dir %{_libdir}/gtkada
%attr(444,-,-) %{_libdir}/gtkada/*.ali
%{_GNAT_project_dir}/*
%{_libdir}/lib*.so
# There's little reason to make a separate subpackage for gtkada-dialog, so
# it's included in the -devel package:
%{_bindir}/*


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
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package:
%exclude %{_pkgdocdir}/gtkada_ug/.buildinfo
%exclude %{_pkgdocdir}/gtkada_ug/objects.inv

%if %{with gps}
%{_datadir}/gps
%else
%exclude %{_datadir}/gps
%endif


###############
## Changelog ##
###############

%changelog
* Tue Jan 14 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2:25.0.0-2
- Rebuilt with GCC 15 prerelease.

* Sun Oct 27 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:25.0.0-1
- Updated to v25.0.0.
- Subpackage GtkAda3-devel now requires the GTK+-3.0 and GLib 2.0 development
  files.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:24.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 19 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:24.0.0-2
- Fixed a Constraint_Error.

* Wed Feb 07 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:24.0.0-1
- Updated to v24.0.0.
- Removed fix for a typo in the documentation; fixed upstream (commit 1def23a).

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:23.0.0-3
- Rebuilt with GCC 14 prerelease.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 14 2023 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:23.0.0-1
- Updated to v23.0.0, using the archive available on GitHub.
- The subpackage GtkAda3-gl and the library libgtkada_gl.so are gone because
  GTK.GLarea is now included in libgtkada.so.
- Removed patch GtkAda3-3.14.2-libs.patch; the unused direct dependencies are no
  longer there.
- Added a new build dependency: Sphinx theme from readthedocs.org
  (commit 7b446c4).
- The version string in 'gtkada.gpr' (SOURCE4) is now updated automatically.

* Sun Feb 12 2023 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:22.0.0-1
- Updated to v22.0.0, using the archive available on GitHub.
- Changed the epoch, to mark the new upstream version scheme.
- Removed year/version from the patch filenames; version control should suffice.
- Added a build step to make the GtkAda User's Guide (in HTML and PDF).
- Removed the GtkAda Reference Manual; build requires Gnatdoc which is not
  available yet on Fedora.
- License fields now contain SPDX license expressions.
- Use 'gprinstall' instead of 'make_install' to have better control of what goes
  where.
- The file 'testgtk.gpr' is now updated during prep to handle the artifacts
  properly.
- Fixed the package version and so-version.
- The build is now staged to allow gtkada-dialog to be a position-independent
  executable.
- Now using the python3 macro to reference the python3 interpreter (option to
  make generate).
- Updated the doc package license.
- Removed a reference to the GtkAda Reference Manual from the GNAT Studio
  plugin.
- Improved spec file readability.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2020-8
- Rebuilt with GCC 13.

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
