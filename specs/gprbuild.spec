# Bootstrapping GPRbuild
# ======================
#
# GPRbuild needs GPRbuild to be built. When GPRbuild is not available (for
# example, because it is being introduced on a new architecture, or because a
# bug prevents GPRbuild from building a newer version of itself), then one can
# follow a bootstrapping procedure that will eventually produce a `gprbuild`
# package with which a normal (full) build can be performed.
#
# The procedure consists of the following steps:
#
#    1. Make sure the package `gprconfig-kb` is available. If the bootstrapping
#       procedure is used to introduce `gprbuild` on a new architecture, then
#       make sure that the knowledge base contains the necessary information
#       to find and identify the GNAT compiler on that architecture.
#
#    2. Build the `xmlada` package in bootstrap mode to produce a package named
#       `xmlada-sources~bootstrap` which will contain the necessary XML/Ada
#       source files needed by the bootstrap build in step 3.
#
#    3. Build this package in bootstrap mode to produce the`gprbuild~bootstrap`
#       package that can be used to run a normal build of the XML/Ada and
#       GPRbuild packages. This may require temporary changes to ExclusiveArch
#       below, for example to add an architecture that isn't yet listed in
#       GPRbuild_arches.
#
# Historical Note
#
# Before upstream included the `bootstrap.sh` script, one had to bootstrap
# GPRbuild by including a pre-built GPRbuild binary as a "Source" and use that
# binary to build GPRbuild again from sources. This method requires a special
# exception according to the packaging guidelines. While no longer required, the
# so-called bootstrap exception for GPRbuild is still available here:
#
#    https://pagure.io/packaging-committee/issue/605
#
# Enabling Bootstrap Mode
#
# Either pass `--with=bootstrap` to mock(1) or change `bcond_with` to
# `bcond_without`, then commit, build, revert to `bcond_with` and commit again.
#
%bcond_with bootstrap

# The test suite is normally run. It can be disabled with "--without=check".
%bcond_without check

# Stripping out debugging information isn't important when bootstrapping.
%if %{with bootstrap}
%global debug_package %{nil}
%endif

# Don't build libgpr when bootstrapping.
%if %{with bootstrap}
%define with_libgpr 0
%else
%define with_libgpr 1
%endif

# Upstream source information.
%global upstream_owner         AdaCore
%global upstream_name          gprbuild
%global upstream_version       25.0.0
%global upstream_release_date  20241007
%global upstream_gittag        v%{upstream_version}

Name:           gprbuild
Epoch:          2
Version:        %{upstream_version}
Release:        3%{?dist}
Summary:        A multi-language extensible build tool

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND Unicode-DFS-2016
# GPRbuild itself is licensed under GPL v3 or later with a runtime
# exception, but is statically linked to both the GNAT runtime library
# and the XML/Ada library to prevent the package from breaking when
# GCC or XML/Ada is updated.
#
# - The GNAT runtime library is licensed under the the same license
#   and exception: GPL v3 or later with a runtime exception.
#
# - XML/Ada is also licensed under the same GPL v3 or later and
#   runtime exception, but also mentions the Unicode license as
#   Unicode data files are used as an input for generating some of
#   XML/Ada's source code.

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz
# For testing.
Source1:        gprbuild-sanity.tar.gz

# [unbundling] The GPRconfig KB is already available when bootstrapping.
Patch:          %{name}-dont-reinstall-the-gprconfig-kb.patch
# Set the library so version; rejected upstream as "finicky":
# https://github.com/AdaCore/gprbuild/issues/108
Patch:          %{name}-set-library-so-version.patch

# Resolve naming conflict with libraries for Google gRPC.
#    GPRbuild and Google's gRPC both want the filename "libgpr.so". This patch
#    renames the library to "libgnatprj.so" to resolve the conflict. The name is
#    chosen for consistency with Debian.
#    As of this writing the conflict is unresolved in both upstreams:
#    https://github.com/grpc/grpc/issues/27850
#    https://github.com/AdaCore/gprbuild/issues/120
Patch:          %{name}-resolve-libgpr-conflict.patch

# [Fedora-specific] Follow soft links when resolving the compiler driver.
#    This usrmove patch works for this package. Upstream a different solution
#    would be needed to handle other possible setups.
Patch:          %{name}-usrmove.patch

# [Fedora-specific] Hard code the default KB dir to `/usr/share/gprconfig`.
#    In the upstream code, the default location of the knowledge base is
#    defined to be relative to the installation folder. This is a problem
#    when testing GPRbuild and utilities in a staging directory. For Fedora,
#    installation paths are fixed so the location of the KB can be hard coded.
Patch:          %{name}-hard-code-default-kb-dir.patch

BuildRequires:  gcc-gnat make sed dos2unix findutils
BuildRequires:  libgnat-static
# A fedora-gnat-project-common that contains the macro GPRinstall is needed.
BuildRequires:  fedora-gnat-project-common >= 3.21

%if %{with bootstrap}
BuildRequires:  gprconfig-kb >= 24.0.0
BuildRequires:  xmlada-sources
%else
BuildRequires:  gprbuild
# xmlada-devel must be explicitly specified for first build after bootstrap.
BuildRequires:  xmlada-devel
# An XMLada build that accepts LIBRARY_TYPE=static-pic is needed.
BuildRequires:  xmlada-static >= 2:23
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  texinfo
BuildRequires:  latexmk
BuildRequires:  tex(titleref.sty)
%endif

%if %{with check}
# To verify if G++ and GFortran are detected by gprconfig.
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
# Language packs used for testing.
# -- list derived from: https://gcc.gnu.org/git/?p=gcc.git;a=tree;f=gcc/po;hb=HEAD
BuildRequires:  glibc-langpack-be
BuildRequires:  glibc-langpack-da
BuildRequires:  glibc-langpack-de
BuildRequires:  glibc-langpack-el
BuildRequires:  glibc-langpack-es
BuildRequires:  glibc-langpack-fi
BuildRequires:  glibc-langpack-fr
BuildRequires:  glibc-langpack-hr
BuildRequires:  glibc-langpack-id
BuildRequires:  glibc-langpack-ja
BuildRequires:  glibc-langpack-nl
BuildRequires:  glibc-langpack-ru
BuildRequires:  glibc-langpack-sr
BuildRequires:  glibc-langpack-sv
BuildRequires:  glibc-langpack-tr
BuildRequires:  glibc-langpack-uk
BuildRequires:  glibc-langpack-vi
BuildRequires:  glibc-langpack-zh
# Moreutils parallel and chronic parallelize the compiler detection test:
BuildRequires:  moreutils-parallel moreutils
BuildRequires:  tar
%endif

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

Requires:       gprconfig-kb >= 24.0.0
Requires:       fedora-gnat-project-common
Recommends:     %{name}-doc

%global common_description_en \
GPRbuild is an advanced software tool designed to help automate the \
construction of multi-language systems. It removes complexity from \
multi-language development by allowing developers to quickly and easily \
compile and link software written in a combination of languages including \
Ada, Assembler, C, C++, and Fortran. Easily extendable by users to cover \
new toolchains and languages it is primarily aimed at projects of all \
sizes organized into subsystems and libraries and is particularly \
well-suited for compiled languages.

%description %{common_description_en}


#################
## Subpackages ##
#################

%if %{without bootstrap}

%package doc
Summary:        Documentation for GPRbuild
BuildArch:      noarch
License:        GFDL-1.3-no-invariants-or-later AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-3.0-or-later WITH GNAT-exception
# The license of the documentation itself is GFDL 1.3. Some Javascript and CSS
# files that Sphinx includes with the documentation are BSD 2-Clause and
# MIT-licensed. Some examples are licensed under GPL 3.0 or later with GCC
# runtime exception. Some other examples are licensed under GPL 3.0 or later
# with GNAT exception.

%description doc %{common_description_en}

This package contains the documentation in HTML, plain text, PDF, and Info
format, and some examples.

%if %{with_libgpr}

%package -n libgpr
Summary:        The GNAT project manager library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       libgnatprj

%description -n libgpr
An Ada library for handling GNAT project files.

This is not the libgpr that is part of gRPC from Google.

%package -n libgpr-devel
Summary:        Development files for the GNAT project manager library
License:        GPL-3.0-or-later WITH GCC-exception-3.1
Requires:       libgpr%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
# gpr.gpr imports XMLada project files, so require xmlada-devel.
Requires:       xmlada-devel
Provides:       libgnatprj-devel

%description -n libgpr-devel
An Ada library for handling GNAT project files.

This package contains source code and linking information for developing
applications that use the GNAT project manager library.

This is not the libgpr that is part of gRPC from Google.
%endif
%endif


#############
## Prepare ##
#############

%prep
%autosetup -p1

# Convert the line-endings of some files.
find ./examples -type f -a \( -name '*.gpr' -o -name '*.ada' \) -print0 \
    | xargs -0 dos2unix -ic0 \
    | xargs -0 dos2unix --keepdate

# Update some release specific information in the source code. The substitutions
# are scoped to specific lines to increase the chance of detecting code changes
# at this point. Sed should exit with exit code 0 if the substitution succeeded
# (using `t`, jump to end of script) or exit with a non-zero exit code if the
# substitution failed (using `q1`, quit with exit code 1).
sed --in-place \
    --expression='33 { s,18.0w,%{upstream_version},         ; t; q1 }' \
    --expression='36 { s,19940713,%{upstream_release_date}, ; t; q1 }' \
    --expression='38 { s,"2016",Date (1 .. 4),              ; t; q1 }' \
    --expression='43 { s,Gnatpro,GPL,                       ; t; q1 }' \
    gpr/src/gpr-version.ads


###########
## Build ##
###########

%build
%if %{with bootstrap}

# Emit some useful output.
gcc -v
gcc -dumpmachine
gcc -dumpversion
gnatls -v --version

# Additional flags to make executables position-independent.
%global Gnatmake_flags_pie -cargs -fPIC -largs -pie -lgnarl_pic -lgnat_pic

export GNATMAKEFLAGS='%{Gnatmake_flags} %{Gnatmake_flags_pie}'

# This will build the bootstrapped binaries.
./bootstrap.sh \
    --with-xmlada=%{_includedir}/xmlada/sources/ \
    --prefix=%{buildroot}%{_prefix}/ \
    build

%else

# Additional flags to make executables position-independent. Note that the tools
# are still statically linked to prevent them from breaking when updating to a
# new GCC release.
%global GPRbuild_flags_pie -cargs -fPIC -largs -pie -lgnarl_pic -lgnat_pic -gargs

gprbuild -v -p %{GPRbuild_flags} %{GPRbuild_flags_pie} \
         -XBUILD=production -XLIBRARY_TYPE=static-pic -XVERSION=%{version} \
         -P gprbuild.gpr

%if %{with_libgpr}
gprbuild -v -p %{GPRbuild_flags} \
         -XBUILD=production -XLIBRARY_TYPE=relocatable -XVERSION=%{version} \
         -P gpr/gpr.gpr
%endif

# Make the documentation.
make -C doc html txt pdf info

%endif


#############
## Install ##
#############

%install
%if %{with bootstrap}

# This will install the bootstrapped binaries.
bash -x ./bootstrap.sh \
     --with-xmlada=%{_includedir}/xmlada/sources/ \
     --prefix=%{buildroot}%{_prefix}/ \
     install

%else

# Install the external tools.
%{GPRinstall} \
           --install-name=gprbuild --mode=usage \
           -XBUILD=production -XINSTALL_MODE=nointernal -XVERSION=%{version} \
           -P gprbuild.gpr

# Install the internal tools.
gprinstall --create-missing-dirs --no-manifest \
           --prefix=%{buildroot}%{_prefix} \
           --install-name=gprbuild --mode=usage \
           -XBUILD=production -XINSTALL_MODE=internal -XVERSION=%{version} \
           -P gprbuild.gpr

%if %{with_libgpr}

# Install the library.
%{GPRinstall -s libgpr -a libgpr} --no-build-var \
           -XBUILD=production -XLIBRARY_TYPE=relocatable -XVERSION=%{version} \
           -P gpr/gpr.gpr

# Fix up the symbolic links for the shared libraries.
ln --symbolic --force libgnatprj.so.%{version} %{buildroot}%{_libdir}/libgnatprj.so

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/libgpr");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/libgpr";|i' \
    %{buildroot}%{_GNAT_project_dir}/gpr.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.

%endif

# Install the Info version of the manual where Info files belong.
mv --no-target-directory %{buildroot}%{_pkgdocdir}/info %{buildroot}%{_infodir}

# Move the examples to the _pkgdocdir and remove the remaining empty directory.
mv --no-target-directory %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples
rmdir %{buildroot}%{_datadir}/examples

%endif


###########
## Check ##
###########

%if %{with check}
%check

# Make the files installed in the buildroot visible to the testsuite.
export PATH=%{buildroot}%{_bindir}:%{buildroot}%{_libexecdir}:$PATH
export GPR_PROJECT_PATH=%{buildroot}%{_GNAT_project_dir}:$GPR_PROJECT_PATH

# TEST 1: Validate knowledge base.

gprconfig --batch -o /dev/null --validate

# TEST 2: Verify detection of compilers and linkers under different locales.

# Tests 1 and 2 mostly test the knowledge base. These tests are done here
# instead of in gprconfig-kb.spec to avoid a dependency loop that would make
# bootstrapping GPRbuild even more complicated.

# In each locale, ask GPRconfig to find GCC compilers for Ada, Assembly, C, C++
# and Fortran, and LD for linking object files ("Bin_Img"). Prevent mixing of
# error messages from parallel processes by collecting each one's error stream
# with chronic.
parallel -i \
         chronic env 'LANG={}' \
                     gprconfig --batch -o /dev/null \
                               --config=Ada,,default,%{_bindir},GNAT \
                               --config=Asm,,,%{_bindir},GCC-ASM \
                               --config=Asm2,,,%{_bindir},GCC-ASM \
                               --config=Asm_Cpp,,,%{_bindir},GCC-ASM \
                               --config=C,,,%{_bindir},GCC \
                               --config=C++,,,%{_bindir},G++ \
                               --config=Fortran,,,%{_bindir},GFORTRAN \
                               --config=Bin_Img,,,%{_bindir},LD \
         -- $(locale -a)

# TEST 3: Perform a test build.

# Unpack the test project.
tar --verbose --extract --gzip --file %{SOURCE1}

# Try to build the test project; use the pre-installed GPRconfig KB.
gprbuild -v -P gprbuild-tests/tests_shared.gpr

# TEST 4: Build and run the examples.

make -C examples run

%endif


###########
## Files ##
###########

%files
%license COPYING3 COPYING.RUNTIME
%doc README*
%{_bindir}/gpr*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/gpr*
%attr(444,-,-) %{_GNAT_project_dir}/_default.gpr
# Exclude the installation script; it serves no purpose in this context.
%exclude %{_prefix}/doinstall

%if %{without bootstrap}

%files doc
%{_infodir}/*
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%{_pkgdocdir}/pdf
%{_pkgdocdir}/txt
%{_pkgdocdir}/examples
# Remove Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/html/.buildinfo
%exclude %{_pkgdocdir}/html/objects.inv

%if %{with_libgpr}

%files -n libgpr
%{_libdir}/libgnatprj.so.%{version}

%files -n libgpr-devel
%{_GNAT_project_dir}/gpr.gpr
%dir %{_includedir}/libgpr
# Exclude a file that doesn't belong under /usr/include:
%exclude %{_includedir}/libgpr/gpr_imports.c
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/libgpr/*.ad[sb]
%dir %{_libdir}/libgpr
%attr(444,-,-) %{_libdir}/libgpr/*.ali
%{_libdir}/libgnatprj.so

%endif
%endif


###############
## Changelog ##
###############

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:25.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jan 13 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2:25.0.0-2
- Rebuilt with GCC 15 prerelease.

* Sun Oct 27 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:25.0.0-1
- Updated to v25.0.0.
- The user's guide is now available in PDF format.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:24.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jan 28 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:24.0.0-1
- Updated to v24.0.0.
- The default KB dir is now hard coded to /usr/share/gprconfig.
- New test that validates the knowledge base.
- New test detecting compilers and linkers under different locales.
- New test that builds and runs the examples.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:23.0.0-4
- Rebuilt with GCC 14 prerelease.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 14 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2:23.0.0-2
- The packages now require their dependencies correctly.

* Tue Feb 14 2023 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:23.0.0-1
- Updated to v23.0.0, using the archive available on GitHub.
- Removed patch gprbuild-drop-exe-prefix.patch; has been fixed upstream (commit
  7395727).
- New version specific build dependency on gprconfig-kb (content of commit
  8a9f79e is required).

* Sun Feb 12 2023 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:22.0.0-1
- Updated to v22.0.0, using the archive available on GitHub.
- Changed the epoch to mark the new upstream version scheme.
- Changed the epoch to 2 instead of 1 for consistency with the GNATcoll
  packages.
- GPRconfig knowledge files are know packaged separately (gprconfig-kb).
- Removed patch fedora_arches.xml; now part of gprconfig-kb.
- Removed patch gprbuild-2016-gcc7.patch; now part of gprconfig-kb.
- Removed patch gprbuild-2017-bootstrap.patch; has been fixed upstream (commit:
  81c0d3d).
- Removed patch gprbuild-2017-fedora_compilers.patch; now part of gprconfig-kb.
- Removed patch gprbuild-2017-libsubdir.patch; Makefile is no longer used to
  build package.
- Removed patch gprbuild-2020-case_util_conflicts.patch; has been fixed upstream
  (commit: d803338).
- Removed patch gprbuild-symlinked_dirs.patch; has been fixed upstream (commit:
  685aa45).
- Removed patch gprbuild-2016-gcc5.patch; GCC 4 and earlier are no longer
  supported.
- Changed build kind from 'debug' to 'production'.
- Tools are now position-independent executables (PIE).
- Added a new build dependency to build the documentation with Sphinx.
- Moved documentation and examples into the _pkgdocdir.
- Updated the license of the doc package.
- Added a runtime exception for all other packages, following upstream.
- Added the Unicode license as gprbuild is statically linked to xmlada.
- License fields now contain SPDX license expressions.
- Fixed the symbolic links for the shared libraries.
- Fixed the so-version of libgnatprj.so.
- Subpackage libgpr now provides libgnatprj.
- Subpackage libgpr-devel now provides libgnatprj-devel.
- Some release specific information in the source code is now updated during
  prep.
- Moved the license files to the correct location.
- Removed the explicit reset of _python_bytecompile_extra; flag seems to have no
  purpose here.
- Added fedora-gnat-project-common as a dependency to libgpr-devel.
- Marked the doc package as architecture-independent.
- Removed runtime dependency from the doc package.
- Added the doc package as a recommendation to the main package.
- Moved the check section after the install section.
- Refactored the bootstrap install sequence.
- Removed GNAT version requirement; all versions supported by Fedora are more
  recent.
- Made the generated usage project file architecture-independent.
- Updated some summaries and descriptions.
- Improved spec file readability.
- Added a fix for incorrect line-endings for some example files during prep.
- Updated the comment on bootstrap mode.
- Updated the bootstrapping exception issue link.
- Bootstrap mode can now be enabled via a configuration option.
- Dropped the 'bootstrap_arch' macro; tweak RPM spec manually if needed.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
