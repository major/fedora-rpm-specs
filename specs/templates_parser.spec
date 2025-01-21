# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     templates-parser
%global upstream_version  25.0.0
%global upstream_gittag   v%{upstream_version}

Name:           templates_parser
Version:        %{upstream_version}
Release:        3%{?dist}
Summary:        An Ada library for parsing templates

License:        GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception
# The license is GPLv3+ with either GCC or GNAT runtime exception.
#
# OPEN ISSUE: What are the licenses of the manpages? Can't find a "Debian
# contributors license" (or alike).

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# Manpages from Debian package
Source1:        templates2ada.1
Source2:        templatespp.1

BuildRequires:  gcc-gnat gprbuild make sed
# A fedora-gnat-project-common that contains the new GPRinstall macro.
BuildRequires:  fedora-gnat-project-common >= 3.21
BuildRequires:  xmlada-devel

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
Templates Parser is the templates engine of the Ada Web Server. It is \
designed to parse files and replace some specific tags in these files \
with some specified values.

%description %{common_description_en}


#################
## Subpackages ##
#################

%package devel
Summary:        Development files for Templates Parser
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       xmlada-devel
Recommends:     %{name}-doc
Recommends:     %{name}-tools

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use Templates Parser.


%package doc
Summary:        Documentation for Templates Parser
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause
# License for the documentation is AdaCore-doc. The Javascript and CSS files
# that Sphinx includes with the documentation are BSD 2-Clause and MIT-licensed.

%description doc %{common_description_en}

This package contains the documentation in HTML and PDF.


%package tools
Summary:        Tools based on Templates Parser
License:        GPL-3.0-or-later

%description tools %{common_description_en}

This package contains the tools templates2ada and templatespp. Templates2ada is
a tool that will generate a set of Ada packages from a template file.
Templatespp is a pre-processor based on Templates Parser. It is generally used
from scripts to process files and generate other files.


#############
## Prepare ##
#############

%prep
%autosetup -n %{upstream_name}-%{upstream_version} -p1

# XML/Ada is installed.
cp config/tp_xmlada_installed.gpr tp_xmlada.gpr

# The makefile must be edited to correct the version number because docs/conf.py
# reads Makefile directly to get VERSION.
sed --regexp-extended --in-place \
    '--expression=s|^( *VERSION[ 	]*[:?]?=[ 	]*).*$|\1%{version}|' \
    Makefile


###########
## Build ##
###########

%build

# Options (project variables) for Templates Parser.
%global tp_options -XVERSION=%{version} \\\
                   -XPRJ_BUILD=Release \\\
                   -XPRJ_TARGET=Linux \\\
                   -XTP_TASKING=Standard_Tasking \\\
                   -XTP_XMLADA=Installed \\\
                   -XLIBRARY_TYPE=relocatable \\\
                   -XXMLADA_BUILD=relocatable

# Build the library and tools.
gprbuild %{GPRbuild_flags} %{tp_options} -P templates_parser.gpr
gprbuild %{GPRbuild_flags} %{tp_options} -P tools/tools.gpr -cargs -fPIE

# Make the documentation. Additional makefile variables are required
# by the GPRbuild project of the examples that need to be built before
# the documentation can be compiled. Compiler switch "-fPIE" is
# required as hardened builds are enabled for this package.
make -C docs html latexpdf \
     GPRBUILD="gprbuild -cargs -fPIE -gargs" \
     PRJ_TARGET=Linux PRJ_BUILD=Release \
     TARGET=$(gcc -dumpmachine) VERSION=%{version}


#############
## Install ##
#############

%install

# Install the library and tools.
%{GPRinstall} %{tp_options} --no-build-var -P templates_parser.gpr
%{GPRinstall} %{tp_options} --mode=usage -P tools/tools.gpr

# Fix up the symlink.
ln --symbolic --force lib%{name}-%{version}.so %{buildroot}%{_libdir}/lib%{name}.so

# Install the man pages.
mkdir --parents %{buildroot}%{_mandir}/man1
cp --preserve=timestamps %{SOURCE1} %{buildroot}%{_mandir}/man1/
cp --preserve=timestamps %{SOURCE2} %{buildroot}%{_mandir}/man1/

# Copy the examples.
mkdir --parents %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps tools/templates.tads %{buildroot}%{_pkgdocdir}/examples
cp --preserve=timestamps tools/all_urls.thtml %{buildroot}%{_pkgdocdir}/examples

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/%{name}");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/%{name}";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}.gpr
# The Sed commands are:
# 1: Insert a with clause before the first line to import the directories
#    project.
# 2: Delete a comment that mentions the architecture.
# 3: Replace the value of Source_Dirs with a pathname based on
#    Directories.Includedir.
# 4: Replace the value of Library_Dir with Directories.Libdir.
# 5: Replace the value of Library_ALI_Dir with a pathname based on
#    Directories.Libdir.


###########
## Files ##
###########

%files
%license COPYING3 COPYING.RUNTIME
%{_libdir}/lib%{name}-%{version}.so

%files devel
%{_GNAT_project_dir}/%{name}.gpr
%{_includedir}/%{name}
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}.so

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%{_pkgdocdir}/pdf
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/html/.buildinfo
%exclude %{_pkgdocdir}/html/objects.inv

%files tools
%{_bindir}/templates2ada
%{_bindir}/templatespp
%attr(644,-,-) %{_mandir}/man1/*.1*


###############
## Changelog ##
###############

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Björn Persson <Bjorn@Rombobjörn.se> - 25.0.0-2
- Rebuilt with GCC 15 prerelease.

* Sun Oct 27 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 25.0.0-1
- Updated to v25.0.0.

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 24.0.0-1
- Updated to v24.0.0.
- Generated HTML-documentation now uses the 'Read the Docs' Sphinx theme.

* Thu Jul 11 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 23.0.0-1
- Updated to v23.0.0.
- Enabled support for XML-templates.
- Re-enabled hardened build.
- The examples are now in the package documentation directory.

* Thu Jul 11 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 22.0.0-1
- Updated to v22.0.0.
- Added build dependencies for building the documentation with Sphinx and LaTeX.
- Updated the license to GPLv3+ with GCC or GNAT runtime exception.
- License fields now contain SPDX license expressions.
- Removed rpath removal step; it's no longer needed.
- Updated all summaries and descriptions.
- Moved the documentation into a separate package.
- Fix up the symbolic links for the shared libraries.
- Made the generated project files architecture-independent.
- Attributes of the man pages are now set after installation.
- Improved spec file readability.

* Sun Feb 11 2024 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-38
- Rebuilt with XMLada 24.

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-36
- Rebuilt with GCC 14 prerelease.

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-34
- Rebuilt with XMLada 23.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-32
- Rebuilt with GCC 13.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.8.0-30
- Rebuild for new gnat

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-27
- rebuilt with gcc-11.0.1-0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  8 2020 Pavel Zhukov <pzhukov@redhat.com> - 11.8.0-25
- rebuild with new gnat

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org - 11.8.0-18
- rebuilt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Pavel Zhukov <pzhukov@redhat.com> - 11.8.0-15
- Build on GPRbuild_arches only

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 11.8.0-14
- Rebuild with new gnat

* Mon Feb 13 2017 Pavel Zhukov <landgraf@fedoraproject.org> - 11.8.0-13
- Disable doc build as a workaround

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-11
- Rebuilt to let it be built on new architectures.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 11.8.0-10
- Rebuilt with GCC 6 prerelease.

* Thu Jun 25 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 11.8.0-9
- Rebuild with new xmlada
- Build on arm

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May  4 2015 Peter Robinson <pbrobinson@fedoraproject.org> 11.8.0-6
- Don't build ADA hardened

* Sun Feb 15 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 11.8.0-5
- Rebuild with gnat-5.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 julian@vgai.de - 11.8.0-3
- add temporary fix for gprbuild using wrong target

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 07 2014 Julian Leyh <julian@vgai.de> - 11.8.0-1
- Update to 11.8.0 and rebuild for gcc

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Tomáš Mráz <tmraz@redhat.com> - 11.6.0-6
- Rebuild (#918586)

* Sat Jan 26 2013 Kevin Fenzi <kevin@scrye.com> - 11.6.0-5
- Rebuild for new gnat

* Mon Aug 06 2012 Julian Leyh <julian@vgai.de> - 11.6.0-3
- add manpages for the tools

* Fri Jun 29 2012 Julian Leyh <julian@vgai.de> - 11.6.0-2
- build documentation
- use other URL
- smaller source tarball with --exclude-vcs
- correct soname
- adjust path to gpr files
- add tools subpackage
- add ldconfig call

* Wed Jun 27 2012 Julian Leyh <julian@vgai.de> - 11.6.0-1
- Initial Package
