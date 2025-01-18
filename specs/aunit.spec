# The test suite is normally run. It can be disabled with "--without=check".
%bcond_without check

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     aunit
%global upstream_version  25.0.0
%global upstream_gittag   v%{upstream_version}

Name:           aunit
Epoch:          2
Version:        %{upstream_version}
Release:        3%{?dist}
Summary:        A unit testing framework for Ada

License:        GPL-3.0-or-later WITH GCC-exception-3.1

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source:         %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# [Fedora-specific] Build a relocatable library.
Patch:          %{name}-disable-static.patch
# Correct paths from which GPRinstall is supposed to copy the documentation.
# See also: https://github.com/AdaCore/aunit/issues/50
Patch:          %{name}-fix-doc-build-path.patch
# Adjust pathnames in the manual, replacing the Adacore-specific pathnames with
# the FHS-compliant pathnames where this package installs the examples:
Patch:          %{name}-cb-examples-dir.patch

BuildRequires:  gcc-gnat gprbuild make sed findutils dos2unix
# A fedora-gnat-project-common that contains the new GPRinstall macro.
BuildRequires:  fedora-gnat-project-common >= 3.21
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  tex(titleref.sty)
%if %{with check}
# Used in `test/Makefile`.
BuildRequires:  grep
BuildRequires:  diffutils
%endif

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
This is the Ada unit test framework AUnit, derived from the JUnit/CPPUnit \
frameworks for Java/C++.

%description %{common_description_en}


#################
## Subpackages ##
#################

%package devel
Summary:        Development files for AUnit
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Recommends:     %{name}-doc

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use AUnit.


%package doc
Summary:        Documentation for AUnit
BuildArch:      noarch
License:        GFDL-1.3-no-invariants-or-later AND MIT AND BSD-2-Clause AND GPL-3.0-or-later WITH GCC-exception-3.1
# The documents have a GFDL 1.3 license with no invariants. Some Javascript and
# CSS files that Sphinx includes with the documentation are BSD 2-Clause and MIT
# licensed. The example code is licensed under GPLv3+ with the GCC runtime
# exception.

%description doc %{common_description_en}

This package contains the documentation in HTML and PDF, and some examples.


#############
## Prepare ##
#############

%prep
%autosetup -p1

# Version information in this file is used during the build.
echo '%{version}' > ./version_information

# Convert the line-endings in some GNAT project files.
find ./examples -name '*.gpr' -print0 \
    | xargs -0 dos2unix -ic0 \
    | xargs -0 dos2unix --keepdate

# One of the tests in the test suite fails because of a runtime accessibility
# check on line 101 of file `aunit-simple_test_cases.adb`. A workaround is to
# replace all runtime checks for anonymous access types with compile-time checks
# based on the "designated type model" (-gnatd_b). See also:
#
#   - https://github.com/AdaCore/aunit/issues/55
#   - https://blog.adacore.com/going-beyond-ada-2022

# Disable dynamic accessibility checks related to anonymous access types.
cat << EOF > gnat.adc
pragma Restrictions (No_Dynamic_Accessibility_Checks);
EOF


###########
## Build ##
###########

%build

# Use configuration file and enable the `designated type` model (-gnatd_b).
%global GPRbuild_adc_flags -cargs -gnatec=gnat.adc -gnatd_b -gargs

# Build the library.
gprbuild %{GPRbuild_flags} %{GPRbuild_adc_flags} \
         -XVERSION=%{version} -P lib/gnat/aunit.gpr

# Make the documentation.
make -C doc html-all pdf-all


#############
## Install ##
#############

%install

# Install the library.
%{GPRinstall} --no-build-var -XVERSION=%{version} -P lib/gnat/aunit.gpr

# Fix up the symlink.
ln --symbolic --force lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so

# Move the examples to the _pkgdocdir and remove the remaining empty directory.
mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples

rmdir %{buildroot}%{_datadir}/examples

# Clean PDF directory.
rm -r  %{buildroot}%{_pkgdocdir}/pdf/_static
find %{buildroot}%{_pkgdocdir}/pdf/ -type f -not -name 'aunit_cb.pdf' -delete

# Before making the project files architecture-independent, copy the buildroot
# into a separate directory for later testing. The testsuite fails if applied to
# the buildroot after making the project files architecture-independent because
# of the hardcoded paths in `directories.gpr`.
%if %{with check}
%global checkroot %{_builddir}/%{name}-%{version}/checkroot
mkdir %{checkroot}  # without --parents to not clobber any upstream directory
cp --recursive %{buildroot}/* %{checkroot}/
%endif

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=/package Linker is/,/end Linker/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}'");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}*.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Delete the package Linker, which contains linker parameters that a
#    shared library normally doesn't need, and can contain architecture-
#    specific pathnames.
# 4: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 5: Replace the value of Library_Dir with Directories.Libdir.
# 6: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.


###########
## Check ##
###########

%if %{with check}
%check

# Make the files of this packages visible to the test runner.
export PATH=%{checkroot}%{_bindir}:$PATH
export LD_LIBRARY_PATH=%{checkroot}%{_libdir}:$LD_LIBRARY_PATH
export GPR_PROJECT_PATH=%{checkroot}%{_GNAT_project_dir}:$GPR_PROJECT_PATH

# Run the test suite. If it fails, output its output so we can troubleshoot.
make -C test || { cat test/test.out.full >&2 ; false ; }

%endif


###########
## Files ##
###########

%files
%license COPYING3 COPYING.RUNTIME
%doc README*
%{_libdir}/lib%{name}.so.%{version}


%files devel
%{_GNAT_project_dir}/%{name}.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}.so
# Exclude the plugin for GNAT programming studio. The IDE is
# not available in Fedora, so there's no point including it.
%exclude %{_datadir}/gps


%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%dir %{_pkgdocdir}/pdf
%{_pkgdocdir}/pdf/aunit_cb.pdf
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/html/.buildinfo
%exclude %{_pkgdocdir}/html/objects.inv


###############
## Changelog ##
###############

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:25.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2:25.0.0-2
- Rebuilt with GCC 15 prerelease.

* Sun Oct 27 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:25.0.0-1
- Updated to v25.0.0.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:24.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun May 12 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:24.0.0-3
- Use the new GPRinstall macro.

* Wed Apr 03 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:24.0.0-2
- Adjusted pathnames in the manual.

* Sun Mar 24 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:24.0.0-1
- Updated to v24.0.0.
- Generated HTML-documentation now uses the 'Read the Docs' Sphinx theme.
- Added the 'findutils' package as build dependency.
- Added a check section and an option to disable it.
- Added the AUnit cookbook in PDF format after backporting an upstream patch.
- Now invoking GPRbuild and GPRinstall directly.

* Mon Jan 22 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:23.0.0-1
- Updated to v23.0.0.
- Removed backport patch aunit-remove-unnecessary-ancestor-withs.patch.
- Removed backport patch aunit-remove-unnecessary-pragma-unreferenced.patch.
- Switched to compile-time accessibility checks for anonymous access types.

* Mon Jan 22 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:22.0.0-1
- Updated to v22.0.0.
- Changed the epoch to mark the new upstream version scheme.
- Changed the epoch to 2 instead of 1 for consistency with the GNATcoll packages.
- Removed year/version from the patch filenames; version control should suffice.
- Added a build dependency for building the documentation with Sphinx.
- License fields now contain SPDX license expressions.
- Moved the examples to the _pkgdocdir.
- Re-enabled the _hardened_build flag; seems no need to disable it.
- Removed the build dependency on chrpath; the tool isn't used.
- Removed the invocation of ldconfig_scriptlets; the scriptlets are obsolete.
- Excluded the GNATstudio plugin instead of removing it post-build.
- Removed the unnecessary pre-install clean-up of the build root.
- Removed an unnecessary runtime dependency on fedora-gnat-project-common.
- Updated all summaries and descriptions.
- Moved the documentation and examples into a separate package.
- Added a fixup for the symlinks for the shared libraries.
- Made the generated project file architecture-independent.
- Added a build dependency on sed.
- Moved the license files to their correct location.
- Improved spec file readability.
- Convert the line-endings of some GPRbuild files during prep.

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-2
- Rebuild with new gnat

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2017-5
- rebuilt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 16 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-2
- Limit to grpbuild arches

* Fri Jul  7 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-1
- New release v2017

* Mon Feb 13 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 2015-5
- Remove unused link

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015  Pavel Zhukov <landgraf@fedoraproject.org> - 2015-2
- Build on arm

* Thu Jun 25 2015  Pavel Zhukov <landgraf@fedoraproject.org> - 2015-1
- New release (#2015)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 29 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-8
- Rebuild with new gnat

* Sat Oct 11 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-7
- Exclude arm

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2013-4
- Use GNAT_arches rather than an explicit list

* Wed May  7 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-3
- Rebuild with new libgnat

* Sun Feb 16 2014  Pavel Zhukov <landgraf@fedoraproject.org> - 2013-2
- New release (2014)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 2012-3
- Rebuild for new libgnat

* Tue Dec 18 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2012-1
- New release 2012
- Add gcc-gnat to BR

* Sun Mar 04 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2011-1
- Update to 2011

* Fri Jun 03 2011 Dan Horák <dan[at]danny.cz> - 2010-3
- updated the supported arch list

* Sat Apr 30 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2010-2
- Remove vendor optflags

* Mon Mar 28 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2010-1
%{GNAT_arches}- Initial build
