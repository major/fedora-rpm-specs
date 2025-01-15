# This package has a bootstrap build mode that can be used to create a source
# code package for bootstrapping GPRbuild. See the 'gprbuild' spec file for more
# information.
%bcond_with bootstrap

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     xmlada
%global upstream_version  25.0.0
%global upstream_gittag   v%{upstream_version}

Name:           xmlada
Epoch:          2
Version:        %{upstream_version}
Release:        3%{?dist}
Summary:        XML library for Ada

License:        GPL-3.0-or-later WITH GCC-exception-3.1 AND Unicode-DFS-2016
# XML/Ada itself is licensed under GPL v3 or later with a runtime exception. The
# Unicode license is mentioned as Unicode data files were used as an input for
# generating some of XML/Ada's source code.

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# XML/Ada's aggregate project file. This project file is normally generated and
# installed by GPRinstall, but as we'll install each XML/Ada component
# separately, we need to maintain and install it manually.
Source1:        xmlada.gpr

BuildRequires:  make
%if %{without bootstrap}
BuildRequires:  gcc-gnat gprbuild sed
# A fedora-gnat-project-common that contains the macro GPRinstall is needed.
BuildRequires:  fedora-gnat-project-common >= 3.21
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%else
BuildRequires:  findutils
%endif

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
XML/Ada includes support for parsing XML files, including DTDs, full support for \
SAX, and an almost complete support for the core part of the DOM. It includes \
support for validating XML files with XML schemas.

%description %{common_description_en}


#################
## Subpackages ##
#################

%if %{without bootstrap}

%package devel
Summary:        Development files for the XML/Ada library
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Recommends:     %{name}-doc

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use the XML/Ada library.


%package static
Summary:        Static libraries of XML/Ada
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description static %{common_description_en}

This package contains the XML/Ada libraries for static linking. It is needed
for linking GPRbuild statically so that GPRbuild will remain functional when
libraries are upgraded.

Other Fedora packages shall require xmlada-devel rather than xmlada-static if
possible.


%package doc
Summary:        Documentation for the XML/Ada library
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause
# License for the documentation is AdaCore-doc. The Javascript and CSS files
# that Sphinx includes with the documentation are BSD 2-Clause and MIT-licensed.

%description doc %{common_description_en}

This package contains the documentation in HTML and PDF, and some examples.


%else

# When bootstrapping gprbuild, only a package that contains source code is
# produced, so a debug package is not needed.
%global debug_package %{nil}

%package sources
Summary:        Sources of the XML/Ada library (for bootstrapping GPRbuild)
BuildArch:      noarch

%description sources %{common_description_en}

This package contains source code for bootstrapping GPRbuild on architectures
on which GPRbuild is not yet available.

%endif


#############
## Prepare ##
#############

%prep
%autosetup -p1

# Set version number.
sed --in-place --expression 's/18.0w/%{version}/' configure configure.in


###########
## Build ##
###########

%build
%if %{without bootstrap}
%configure --enable-build=distrib --enable-shared

# Build the libraries.
%{make_build} shared static-pic GPROPTS='%{GPRbuild_flags}'

# Make the documentation.
make -C docs html latexpdf

%else
%{configure} --enable-build=distrib

%endif


#############
## Install ##
#############

%install
%if %{without bootstrap}

# Verify that the ALI files of both builds (relocatable and static-pic) match.
# The verfication is necessary as GPRinstall will overwrite the ALI files during
# the installation of the static-pic build (which is installed after the
# relocatable build).
for component_dir in dom schema unicode sax input_sources ; do
    diff --exclude "*.a" --exclude "*.so*" --exclude ".cvsignore" \
         %{_builddir}/%{name}-%{version}/${component_dir}/lib/relocatable \
         %{_builddir}/%{name}-%{version}/${component_dir}/lib/static-pic
done

# Install each component.
function run_gprinstall {
    local libtype=$1
    local component=$2
    local directory=$3  # directory name in the source tree
    %{GPRinstall -s xmlada/${component}} \
               --build-var=LIBRARY_TYPE --build-var=XMLADA_BUILD \
               --build-name=${libtype} -XLIBRARY_TYPE=${libtype} \
               -P ${directory}/%{name}_${component}.gpr
}

for libtype in relocatable static-pic ; do
    for component in dom schema unicode sax ; do
        run_gprinstall ${libtype} ${component} ${component}
    done

    # The "input" component needs special treatment as its dirname in the source
    # tree ("input_sources") is not reflected in its GNAT project file
    # ("xmlada_input.gpr").
    run_gprinstall ${libtype} input input_sources
done

# Install the aggregate project file ("xmlada.gpr").
install --mode=u=rw,go=r,a-s --preserve-timestamps \
        %{SOURCE1} --target-directory=%{buildroot}%{_GNAT_project_dir}

# Fix up the symbolic links for the shared libraries.
for component in dom input_sources schema unicode sax ; do
    ln --symbolic --force lib%{name}_${component}.so.%{version} \
       %{buildroot}%{_libdir}/lib%{name}_${component}.so
done

# Move examples to the _pkgdocdir and remove the remaining empty directory.
mv --no-target-directory %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples

rmdir %{buildroot}%{_datadir}/examples

# Make the generated project files architecture-independent.
for component in dom input schema unicode sax ; do
    sed --regexp-extended --in-place \
        '--expression=1i with "directories";' \
        '--expression=/^--  This project has been generated/d' \
        '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}/${component}'");|i' \
        '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
        '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
        %{buildroot}%{_GNAT_project_dir}/%{name}_${component}.gpr
    # The Sed commands are:
    # 1: Insert a with clause before the first line to import the directories
    #    project.
    # 2: Delete a comment that mentions the architecture.
    # 3: Replace the value of Source_Dirs with a pathname based on
    #    Directories.Includedir.
    # 4: Replace the value of Library_Dir with Directories.Libdir.
    # 5: Replace the value of Library_ALI_Dir with a pathname based on
    #    Directories.Libdir.
done

%else

# Copy the source files.
mkdir --parents %{buildroot}%{_includedir}/%{name}/sources
cp -r . %{buildroot}%{_includedir}/%{name}/sources
find %{buildroot}%{_includedir}/%{name}/sources -type f ! -name "*ad[sb]" ! -name "*gpr" -delete
find %{buildroot}%{_includedir}/%{name}/sources -type d -empty -delete

%endif


###########
## Files ##
###########

%if %{without bootstrap}

%files
%license COPYING3 COPYING.RUNTIME
%doc README* TODO AUTHORS
%{_libdir}/lib%{name}*.so.%{version}

%files devel
%{_GNAT_project_dir}/%{name}*.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}*.so

%files static
%{_libdir}/lib%{name}*.a

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/*.html
%{_pkgdocdir}/searchindex.js
%{_pkgdocdir}/_sources
%{_pkgdocdir}/_static
%{_pkgdocdir}/XMLAda.pdf
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/.buildinfo
%exclude %{_pkgdocdir}/objects.inv

%else

%files sources
%{_includedir}/%{name}

%endif


###############
## Changelog ##
###############

%changelog
* Mon Jan 13 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2:25.0.0-3
- Rebuilt with GCC 15 prerelease.

* Wed Dec 04 2024 Pavel Zhukov <landgraf@fedoraproject.org> - 2:25.0.0-2
- Disable bootstrap

* Sun Oct 27 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:25.0.0-1
- Updated to v25.0.0.

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:24.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jan 28 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:24.0.0-1
- Updated to v24.0.0.
- Generated HTML-documentation now uses the 'Read the Docs' Sphinx theme.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:23.0.0-4
- Rebuilt with GCC 14 prerelease.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:23.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 13 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2:23.0.0-2
- Set a minimum version of fedora-gnat-project-common.
- Simplified the install section a bit.

* Tue Feb 14 2023 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:23.0.0-1
- Updated to v23.0.0, using the archive available on GitHub.
- Removed backport patch for improved Unicode support.
- Removed fix for file permissions; has been fixed upstream (commit: 9e1bd23).
- Removed patch gprbuild-gprinstall-relocate-artifacts.patch; move files after
  GPRinstall has run.
- Moved the documentation back to where is was until version 2:22.0.0.

* Sun Feb 12 2023 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:22.0.0-1
- Updated to v22.0.0, using the archive available on GitHub.
- Changed the epoch to mark the new upstream version scheme.
- Changed the epoch to 2 instead of 1 for consistency with the GNATcoll
  packages.
- Updated the license, a runtime exception has now been added.
- Added new build dependencies to build the documentation with Sphinx and LaTeX.
- Examples are now located in _pkgdocdir/examples.
- License field now contains an SPDX license expression.
- Added the Unicode license to cover all code that has been generated using
  Unicode data.
- Removed some post-install steps that are no longer required.
- Static libraries are now build position independent (PIC).
- Fix permission errors in the prep step; these are source packaging errors.
- Updated some summaries and descriptions.
- Improved spec file readability.
- Marked the source package as architecture independent.
- Removed empty directory '_libdir/static'; it seems to have no purpose.
- Moved all libraries from '_libdir/xmlada' to '_libdir'.
- Fix up the symbolic links for the shared libraries.
- Moved documentation and examples into a separate package.
- Made the generated project files architecture-independent.
- Added a build dependency on sed, removed the explicit version dependency on
  GPRbuild.
- Bootstrap mode can now be enabled via a configuration option.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2020-9
- Rebuilt with GCC 13.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Björn Persson <Bjorn@Rombobjörn.se> - 2020-6
- Rebuilt with GCC 12 prerelease.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Pavel Zhukov <pavel@zhukoff.net> - 2020-3
- Rebuild. Ali files invalidated by gcc update

* Tue Dec  8 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-2
- Disable gprbuild's bootstraping

* Tue Dec  8 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-1
- New version v2020

* Mon Dec 07 2020 Jeff Law <releng@fedoraproject.org> - 2019-4
- Gcc 11 bootstrap

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 3 2020 Björn Persson <Bjorn@Rombobjörn.se> - 2019-1
- Upgraded to the 2019 release.

* Mon Feb  3 2020 Pavel Zhukov <pzhukov@redhat.com> - 2018-11
- rebuild with new gprbuild

* Mon Feb  3 2020 Pavel Zhukov <pzhukov@redhat.com> - 2018-10
- Gcc 10 bootstrap

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  9 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-7
- Rebuld with new gnat-rpm-macros
- Build with gprbuild 2018

* Tue Feb  5 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-4
- Rebuild with new gprbuild

* Tue Feb  5 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-2
- Produce source only package in bootstrap mode

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr  3 2018 Pavel Zhukov <pzhukov@redhat.com> - 2017-6
- Build source packages on non gprbuild enabled arches for bootstraping

* Tue Feb  6 2018 Pavel Zhukov <pzhukov@redhat.com> - 2017-5
- Rebuild with new gnat

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-2
- rebuild with new gprbuild

* Fri Jul  7 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-1
- New version (2017)

* Wed Apr 20 2017 Pavel Zhukov <<landgraf@fedoraproject.org>> - 2016-5
- Rebuild to fix non x86 arches ali versions

* Fri Feb 17 2017 Björn Persson <Bjorn@Rombobjörn.se> - 2016-4
- Reverted the temporary workaround.

* Sun Feb 12 2017 Björn Persson <Bjorn@Rombobjörn.se> - 2016-3
- Made a temporary workaround to rebuild with GCC 7 prerelease.

* Sat Feb  4 2017 Pavel Zhukov <pavel@zhukoff.net> - 2016-1
- Rebuild with new gnat

* Mon Aug 08 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2016-1
- Upgraded to the 2016 release.
- Removed the irrelevant and FHS-violating manifest file.
- The license has changed to GPLv3+.

* Sun May 01 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2015-12
- Tagged the license file as such.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2015-10
- Rebuilt with GCC 6 prerelease.

* Sat Dec 19 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2015-8
- Added a -static subpackage for linking GPRbuild statically.

* Wed Jun 24 2015 Pavel Zhukov <<landgraf@fedoraproject.org>> - 2015-7
- Remove temporary links

* Wed Jun 24 2015 Pavel Zhukov <<landgraf@fedoraproject.org>> - 2015-6
- Move sources to separate directories
- Add temporary symlinks to allow gprbuiild bootstraping
- Fix temporary (upgrade) links pattern
- Provide previous version to upgrade gprbuild

* Tue Jun 23 2015 Pavel Zhukov <<landgraf@fedoraproject.org>> - 2015-2
- Install xmlada.gpr

* Wed Jun 17 2015 Pavel Zhukov <<landgraf@fedoraproject.org>> - 2015-1
- New release (#2015)

* Wed Apr 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2013-11
- rebuild (gcc / gnat 5)

* Sun Mar 15 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-10
- Create unversioned symlinks

* Sat Feb 14 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-9
- Rebuild with new gcc 4.9

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2013-6
- Use GNAT_arches rather than an explicit list

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2013-5
- aarch64 now has Ada

* Sun Apr 20 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2013-4
- Rebuild for new gcc

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 Pavel ZHukov <landgraf@fedoraproject.org> - 2013-2
- New release
- AdaCore has moved to years in version.
- Fix gpr error

* Sat Mar 09 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 4.3-5
- Aws failed to bind with xmlada

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 4.3-4
- Rebuild for new libgnat

* Fri Jan 25 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 4.3-3
- Rebuild with GCC 4.8

* Tue Dec 18 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 4.3-2
- Fix gpr patch

* Mon Dec 17 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 4.3-1
- New release
