# Disabling LTO for now. LTO triggers an internal compiler error when
# SSL (GnuTLS) is enabled (error message : "lto1: internal compiler
# error: resolution sub id 0x7eb8fd216cff1b34 not in object file").
%global _lto_cflags %nil

# To harden the AWS executables, we need to perform a staged build during which
# we first build the library and then the executables. Unfortunately, this is
# harder than it seems due to the complicated Makefile. Hence, for now, we skip
# hardening for this package.
%undefine _hardened_build

# Support for GnuTLS is normally enabled.
# It can be disabled with "--without=gnutls".
%bcond_without gnutls

# Support for LDAP normally enabled.
# It can be disabled with "--without=ldap".
%bcond_without ldap

# The GNATstudio plug-in is normally excluded because GNATstudio isn't packaged.
# It can be included with "--with=gps".
%bcond_with gps

# Upstream source information.
%global upstream_owner    AdaCore
%global upstream_name     aws
%global upstream_version  25.1.0
%global upstream_gittag   v%{upstream_version}

Name:           aws
Epoch:          2
Version:        %{upstream_version}
Release:        1%{?dist}
Summary:        The Ada Web Server

License:        (GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception) AND GPL-2.0-or-later WITH GNAT-exception
# The license is GPLv3+ with either GCC or GNAT runtime exception,
# except for:
# - include/memory_streams.ads    : GPLv2+ with GNAT runtime exception
# - include/memory_streams.adb    : GPLv2+ with GNAT runtime exception
# - config/ssl/gnutls/wrappers.c  : GPLv2+ with GNAT runtime exception
# - config/ssl/openssl/wrappers.c : GPLv2+ with GNAT runtime exception
#
# OPEN ISSUE: What are the licenses of the manpages?

URL:            https://github.com/%{upstream_owner}/%{upstream_name}
Source0:        %{url}/archive/%{upstream_gittag}/%{upstream_name}-%{upstream_version}.tar.gz

# Man pages.
Source1:        aws-manpages.tar.gz

# [Fedora-specific] Use external template parser.
Patch:          %{name}-use-external-template-parser.patch
# [Fedora-specific] Use external zlib library.
Patch:          %{name}-use-external-zlib-library.patch
# [Fedora-specific] Use external xmlada library.
Patch:          %{name}-use-external-xmlada-library.patch
# [Fedora-specific] Set soname of the AWS library.
Patch:          %{name}-set-soname-of-aws-library.patch
# [Fedora-specific] Set soname of the AWS SSL library.
Patch:          %{name}-set-soname-of-aws-ssl-library.patch
# [Fedora-specific] Link components dynamically.
Patch:          %{name}-link-components-dynamically.patch
# [Fedora-specific] Don't strip debugger symbol information for release builds.
Patch:          %{name}-no-symbol-stripping.patch
# [Fedora-specific] No build and install names.
Patch:          %{name}-no-build-and-install-names.patch
# [Fedora-specific] Don't install Javascript sources with an unclear license.
Patch:          %{name}-no-third-party-javascript-source-code.patch
# [Fedora-specific] Recommend the mailcap package for an up-to-date mime.types.
Patch:          %{name}-recommend-mailcap-for-mime-types.patch
# Handle comments in mime.types:
# https://github.com/AdaCore/aws/issues/379
Patch:          %{name}-mime-types-comments.patch
# [Fedora-specific] Use 'gnatcoll_core.gpr' instead of 'gnatcoll.gpr'.
Patch:          %{name}-refine-dependencies-to-gnatcoll.patch
# Let GnuTLS rely on P11-kit's knowledge of what the system trust store is.
# Don't use the Debian-oriented pathname of a file that would at best just add
# the same set of certificates again:
# https://github.com/AdaCore/aws/issues/386
Patch:          aws-trust-the-system-trust-store.patch

BuildRequires:  gcc-gnat gprbuild make sed findutils tar
# A fedora-gnat-project-common that contains the new GPRinstall macro.
BuildRequires:  fedora-gnat-project-common >= 3.21
BuildRequires:  templates_parser-devel
BuildRequires:  xmlada-devel
# A gnatcoll-core that contains gnatcoll_core.gpr is needed.
BuildRequires:  gnatcoll-core-devel >= 25.0.0
# A zlib-ada that contains the 'End_Of_Stream' function is needed.
BuildRequires:  zlib-ada-devel >= 1.4-0.37.20210811gitca39312
%if %{with ldap}
BuildRequires:  openldap-devel
%endif
%if %{with gnutls}
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
%endif

# python3-rpm-macros is used in adjusting the shebang in awsascb.
BuildRequires:  python3-rpm-macros

BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk

# Build only on architectures where GPRbuild is available.
ExclusiveArch:  %{GPRbuild_arches}

%global common_description_en \
AWS is a complete framework to develop Web based applications. The main part \
of the framework is the embedded Web server. This small yet powerful Web \
server can be embedded into your application so your application will be able \
to talk with a standard Web browser.

%description %{common_description_en}


#################
## Subpackages ##
#################

%package tools
Summary:        Tools for the Ada Web Server
License:        GPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception)
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gnutls-devel
Requires:       libgcrypt-devel
# FIXME: What are these devel package dependencies doing in aws-tools?

%description tools %{common_description_en}

This package contains contains supporting tools for the Ada Web Server.


%package doc
Summary:        Documentation for the Ada Web Server
BuildArch:      noarch
License:        AdaCore-doc AND MIT AND BSD-2-Clause AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain AND GPL-1.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1 OR GPL-3.0-or-later WITH GNAT-exception)
# License for the documentation is AdaCore-doc. The Javascript and CSS files
# that Sphinx includes with the documentation are BSD 2-Clause and
# MIT-licensed.
# Ada package specifications quoted in the manual may be covered by GPL 3 or
# later with GCC and/or GNAT exceptions.
# The example code is licensed under GPLv3+. Various icons in
# 'examples/shared/web_elements/icons' are either in the public domain or
# licensed under GPL (no version mentioned). Template
# 'examples/runme/aws_status.thtml' has license GPLv3+ with either GCC or GNAT
# runtime exception.

%description doc %{common_description_en}

This package contains the documentation in HTML and PDF, and some examples.


%package devel
Summary:        Development files for the Ada Web Server
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       fedora-gnat-project-common
Requires:       templates_parser-devel
Requires:       xmlada-devel
Requires:       gnatcoll-core-devel
Requires:       zlib-ada-devel
%if %{with gnutls}
Requires:       gnutls-devel
Requires:       libgcrypt-devel
%endif
%if %{with ldap}
Requires:       openldap-devel
%endif
Recommends:     %{name}-tools
Recommends:     %{name}-doc
# Recommend the mailcap package for an up-to-date list of MIME types instead of
# packaging the older list bundled with AWS. The list is available at
# '/etc/mime.types' after installing mailcap.
Recommends:     mailcap

%description devel %{common_description_en}

This package contains source code and linking information for developing
applications that use the Ada Web Server.


#############
## Prepare ##
#############

%prep
%autosetup -p1

# Update some release specific information in the source code. The substitution
# is scoped to a specific line to increase the chance of detecting code changes
# at this point. Sed should exit with exit code 0 if the substitution succeeded
# (using `t`, jump to end of script) or exit with a non-zero exit code if the
# substitution failed (using `q1`, quit with exit code 1).
sed --in-place \
    --expression='34 { s,20\.0,%{upstream_version}, ; t; q1 }' \
    src/core/aws.ads

# Unpack the man pages.
tar -xvf %SOURCE1

# Ignore the templates_parser Git submodule.
rm -rf templates_parser
# Delete the bundled zlib library.
rm -rf include/zlib*

# No silent makefiles.
# Issue: https://github.com/AdaCore/aws/issues/378
find -type f -name "Makefile" \
    | xargs sed --regexp-extended --in-place \
                --expression '/^\.SILENT:/d'

# Convert readme.txt to UTF-8.
mv readme.txt readme.txt.old
iconv --from=ISO-8859-1 --to=UTF-8 readme.txt.old > readme.txt
rm readme.txt.old

# Exclude all third-party Javascript source code with unclear license, the demos
# that depend on it and the readme file that promotes usage of the Javascript
# source code.
rm -rf ./web_elements/javascripts
rm -rf ./web_elements/notebook
rm     ./web_elements/readme.txt

rm -rf ./demos/web_block_ajax
rm -rf ./demos/web_block_ajax_templates
rm -rf ./demos/web_elements
rm -rf ./demos/websockets
rm -rf ./demos/ws_candy

# Exclude demo "soap_hello" as it requires ada2wsdl - a tool not included in the
# ada-tools package as it depends on libadalang - a library not available in
# Fedora.
rm -rf ./demos/soap_hello

# Fix demo "wps". The WWW-root will be ../shared/web_elements instead of
# ../../web_elements after installation. The demo also needs a certificate from
# the testsuite.
cp --preserve=timestamp regtests/0111_sslcfg/cert.pem ./demos/wps

sed --regexp-extended --in-place \
    --expression '/^www_root/ { s,\.\./\.\./web_elements,../shared/web_elements, ; t; q1 }' \
    --expression '/^certificate/ { s,\.\./\.\./regtests/0111_sslcfg/cert.pem,cert.pem, ; t; q1 }' \
    ./demos/wps/wps.ini

# Fix demo "ws". The WWW-root will be ../shared/web_elements instead of
# ../../web_elements after installation.
sed --regexp-extended --in-place \
    --expression '/^www_root/ { s,\.\./\.\./web_elements,../shared/web_elements, ; t; q1 }' \
    ./demos/ws/ws.ini

# Improve instructions for building the demos. The wsdl2aws-tool must know where
# to find the templates.
sed --regexp-extended --in-place \
    --expression '7 { s,\$ make$,$ AWS_TEMPLATE_FILES=${PWD}/shared/wsdl2aws-templates make, ; t; q1 }' \
    ./demos/README


###########
## Build ##
###########

%build

%if %{with ldap}
LDAP=true
%else
LDAP=false
%endif

# SSL dynamic binding option (SSL_DYNAMIC) is disabled as it requires
# libadalang; a library not (yet) available in Fedora (see also:
# config/ssl/dynamo.gpr).

%if %{with gnutls}
SOCKET=gnutls
SSL_DYNAMIC=false
%else
SOCKET=std
SSL_DYNAMIC=false
%endif

make setup GPRBUILD='gprbuild %{GPRbuild_flags} -XVERSION=%{version}' \
     PYTHON='%python3' ENABLE_SHARED=true DEBUG=false \
     XMLADA=true LAL=false ZLIB=true \
     LDAP=$LDAP SOCKET=$SOCKET SSL_DYNAMIC=$SSL_DYNAMIC

# Limit build to 1 CPU (-j1). Linking fails when building with parallel make
# (-j4) and at the same time using Zlib-Ada version 1.4^20210830gitca39312. No
# idea what might be the cause. Errors are somewhat incomprehensible: Lots of
# undefined references in the files generated by the binder.

%{make_build} -j1 GPRBUILD='gprbuild %{GPRbuild_flags} -XVERSION=%{version}' \
     LIBRARY_TYPE=relocatable

# Make the documentation.
make -C docs html latexpdf


#############
## Install ##
#############

%install

# Note: Cannot use the make_install macro: the INSTALL variable, which is part
# of the macro definition, is rejected by Makefile.checks.
make install \
     GPRINSTALL='%{GPRinstall} -XVERSION=%{version}' \
     prefix=%{buildroot}%{_prefix}

# Add the missing libaws_ssl.so that the tools are linked to.
cp --preserve=timestamps \
   %{_builddir}/%{name}-%{version}/*/release/relocatable/lib/ssl/lib%{name}_ssl.so* \
   %{buildroot}%{_libdir}/
# To do: Figure out libaws_ssl. If programs need it, why doesn't the makefile
# install it? If programs don't need it, why are the tools linked to it? Why is
# neither of libaws and libaws_ssl linked to the other? libaws is linked to
# libgnutls, and libaws_ssl is not. Does it actually do anything useful? Can we
# get rid of it?

# Fix up the symbolic links to the shared libraries.
ln --symbolic --force lib%{name}.so.%{version} %{buildroot}%{_libdir}/lib%{name}.so
ln --symbolic --force lib%{name}_ssl.so.%{version} %{buildroot}%{_libdir}/lib%{name}_ssl.so

# Copy all demos and move the shared demo artifacts.
mkdir --parents %{buildroot}%{_pkgdocdir}/examples

cp --preserve=timestamps --recursive \
   demos/* %{buildroot}%{_pkgdocdir}/examples

mv --no-target-directory \
   %{buildroot}%{_datadir}/examples/%{name} \
   %{buildroot}%{_pkgdocdir}/examples/shared

rmdir %{buildroot}%{_datadir}/examples

# Remove all demo artifacts that are not shared.
# - The content of examples/shared/images is part of demo "runme".
# - The content of examples/shared/templates is part of demo "web_mail".
rm -rf %{buildroot}%{_pkgdocdir}/examples/shared/images
rm -rf %{buildroot}%{_pkgdocdir}/examples/shared/templates

# Remove an outdated version of mime.types. Developers should use the version
# provided by package mailcap as recommended for aws-devel and suggested in the
# documention (see patch aws-recommend-mailcap-for-mime-types.patch).
rm -rf %{buildroot}%{_pkgdocdir}/examples/shared/web_elements/mime.types

# Copy the man pages.
mkdir --parents %{buildroot}%{_mandir}/man1
cp --preserve=timestamps *.1 %{buildroot}%{_mandir}/man1/

# Adjust the shebang in awsascb to run Python the Fedora way.
%{py3_shebang_fix} %{buildroot}/%{_bindir}/awsascb

# Make the generated usage project file architecture-independent.
sed --regexp-extended --in-place \
    '--expression=1i with "directories";' \
    '--expression=/^--  This project has been generated/d' \
    '--expression=/package Linker is/,/end Linker/d' \
    '--expression=s|^( *for +Source_Dirs +use +).*;$|\1(Directories.Includedir \& "/'%{name}'");|i' \
    '--expression=s|^( *for +Library_Dir +use +).*;$|\1Directories.Libdir;|i' \
    '--expression=s|^( *for +Library_ALI_Dir +use +).*;$|\1Directories.Libdir \& "/'%{name}'";|i' \
    %{buildroot}%{_GNAT_project_dir}/%{name}.gpr
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
## Files ##
###########

%files
%doc readme* AUTHORS
%license COPYING3 COPYING.RUNTIME
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}_ssl.so.%{version}


%files devel
%{_GNAT_project_dir}/*.gpr
%dir %{_includedir}/%{name}
# Exclude some junk that doesn't belong under /usr/include:
%exclude %{_includedir}/%{name}/Makefile
%exclude %{_includedir}/%{name}/readme.txt
%exclude %{_includedir}/%{name}/*.gpr
%exclude %{_includedir}/%{name}/wrappers.c
%exclude %{_includedir}/%{name}/urandom.c
%exclude %{_includedir}/%{name}/aws-os_lib.h
# Include only Ada files so it will be an error if more junk appears:
%{_includedir}/%{name}/*.ad[sb]
%dir %{_libdir}/%{name}
%attr(444,-,-) %{_libdir}/%{name}/*.ali
%{_libdir}/lib%{name}*.so
# Optional GNATstudio plugin.
%if %{with gps}
%{_datadir}/gps
%else
%exclude %{_datadir}/gps
%endif


%files tools
# Make awsascb executable.
%attr(755,-,-) %{_bindir}/awsascb
%{_bindir}/aws_password
%{_bindir}/awsres
%{_bindir}/webxref
%{_bindir}/wsdl2aws
%attr(644,-,-) %{_mandir}/man1/awsres.1*
%attr(644,-,-) %{_mandir}/man1/wsdl2aws.1*
# Tool ada2wsdl is not included as it requires libadalang.
%exclude %{_mandir}/man1/ada2wsdl.1*


%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/html
%{_pkgdocdir}/pdf
%{_pkgdocdir}/examples
# Exclude Sphinx-generated files that aren't needed in the package.
%exclude %{_pkgdocdir}/html/.buildinfo
%exclude %{_pkgdocdir}/html/objects.inv


###############
## Changelog ##
###############

%changelog
* Mon Feb 03 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2:25.1.0-1
- Updated to bugfix release 25.1.0.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:25.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 27 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:25.0.0-1
- Updated to v25.0.0.
- This fixes CVE-2024-37015.

* Thu Sep 26 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:24.0.0-3
- Fixed to use /dev/urandom instead of a non-cryptographic PRNG.
  Resolves: CVE-2024-41708 (RHBZ#2314766)

* Wed Aug 14 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2:24.0.0-2
- Fixed a bug where AWS read comments in MIME types files as content type
  definitions.

* Sun Jul 28 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:24.0.0-1
- Updated to v24.0.0.
- Generated HTML-documentation now uses the 'Read the Docs' Sphinx theme.
- Changed build from 'debug' to 'release'.
- Removed all third-party Javascript source code with an unclear license.
- Added back all demos that do not depend on the third-party Javascript source
  code or the ada2wsdl tool. They are now in the aws-doc package.
- Moved all shared demo artifacts into /usr/share/doc/aws/examples/shared.
- Removed an older version of mime.types, recommending package mailcap for
  aws-devel instead. Added a note to section 3.4, "Configuration options",
  of the documentation to point out the availability of /etc/mime.types.

* Sun Jul 28 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:23.0.0-1
- Updated to v23.0.0.

* Sun Jul 28 2024 Dennis van Raaij <dvraaij@fedoraproject.org> - 2:22.0.0-1
- Updated to v22.0.0.
- Changed the epoch to mark the new upstream version scheme.
- Changed the epoch to 2 instead of 1 for consistency with the GNATcoll
  packages.
- Removed year/version from the patch filenames; version control should suffice.
- Added Sphinx and LaTeX as build dependencies for the documentation.
- License fields now contain SPDX license expressions.
- Updated the license of the doc package.
- Removed the build dependency on chrpath; the tool isn't used.
- Fix up the symbolic links for the shared libraries.
- Made the generated project files architecture-independent.
- Made the GNATstudio plugin depend on a bcond_with.
- Support for GnuTLS now depends on a bcond_without.
- Support for LDAP now depends on a bcond_without.
- Updated all summaries and descriptions.
- Improved spec file readability.
- Removed all runtime dependencies from the doc package.
- Added the tools package as a recommendation to the devel package.
- Added the doc package as a recommendation to the devel package.
- Added missing build dependency 'tar'.
- Use the new GPRinstall macro.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2020-16
- Rebuilt with XMLada 24.

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Björn Persson <Bjorn@Rombobjörn.se> - 2020-13
- Rebuilt with GCC 14 prerelease.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2020-11
- Rebuilt with XMLada 23.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Björn Persson <Bjorn@Rombobjörn.se> - 2020-9
- Rebuilt with GCC 13.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2020-7
- Rebuild for new gnat

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 Björn Persson <Bjorn@Rombobjörn.se> - 2020-4
- rebuilt with gcc-11.0.1-0.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 2020 Pavel Zhukov <pzhukov@redhat.com> - 2020-2
- Update to new version 2020

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb  9 2020 Pavel Zhukov <pzhukov@redhat.com> - 2019-2
- New release (2019) build with gcc10 (#1800306)

* Sun Feb 09 2020 Björn Persson <Bjorn@Rombobjörn.se> - 2018-6
- Adapted to compiler and API changes in GCC 10.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Pavel Zhukov <pzhukov@redhat.com> - 2018-4
- Revert changes which were lost on rebase

* Tue Feb 12 2019 Pavel Zhukov <landgraf@fedoraproject.org> -2018-2
- New release 2018

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Björn Persson <Bjorn@Rombobjörn.se> - 2017-11
- Migrated to Python 3.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017-9
- Escape macros in changelog

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-8
- Add ssl library to the list of installed files

* Tue Feb 06 2018 Pavel Zhukov <landgraf@fedoraproject.org> - 2017-7
- rebuilt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 15 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-4
- aws needs gprbuild. Limit to gprbuild_arches

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-3
- Add python version

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-2
- Fix so version

* Mon Jul 10 2017 Pavel Zhukov <pzhukov@redhat.com> - 2017-1
- New release v2017

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 20 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2016-2
- Removed an ln command as GPRinstall apparently creates that link now.

* Tue Aug 09 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2016-1
- Upgraded to the 2016 release.
- Tagged the license file as such.

* Tue Feb 02 2016 Björn Persson <Bjorn@Rombobjörn.se> - 2015-5
- Rebuilt with GCC 6 prerelease.

* Fri Nov 27 2015  Pavel Zhukov <landgraf@fedoraproject.org> - 2015-4
- Added openldap requirement (#1285661)

* Thu Sep 24 2015 Björn Persson <Bjorn@Rombobjörn.se> - 2015-3
- Added the missing libaws_ssl.so.
- Disabled PDF generation as it doesn't currently work.

* Fri Jun 26 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2015-2
- Remove references to gnutls rsa_params as deprecated

* Thu Jun 25 2015 Pavel Zhukov <landgraf@fedoraproject.org> - 2015-1
- New release (#2015)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2.git20150523
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Björn Persson <Bjorn@xn--rombobjrn-67a.se> - 3.1.0-13
- Patched to build with GCC 5.

* Sat Oct 11 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-12
- Fixed typos

* Thu Oct 02 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-11
- Exclude %%{arm}

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 17 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.1.0-9
- Fix typo: R: libgcrypt-devel, not libgrypt-devel.
- Add missing %%changelog entry.

* Tue Jun 24 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-8
- Add missed requirements.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-5
- Rebuild with new GCC

* Wed Dec 18 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-4
- Add demos
- Fix libdir in subpackages

* Tue Dec 17 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 3.1.0-1
- New release 3.1.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-16
- Disable gnutls support (rhbz#918554)

* Sun Mar 10 2013  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-15
- Rebuild with new xmlada

* Wed Mar  6 2013 Tomáš Mráz <tmraz@redhat.com> 2.11.0-14
- Rebuild with new gnutls

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 2.11.0-13
- Rebuild for new libgnat

* Tue Dec 18 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-12
- New xmlada

* Fri Nov  2 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-11
- Add gcc-gnat and zlib-ada-devel dependencies

* Sun Oct 28 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-10
- Remove "-lz" flag
- Remove dependencies -doc from base package
- Fix tools license
- Add man pages

* Sat Oct 13 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-8
- Remove zlib-ada sources
- Fix license tag
- Multiple fixes https://bugzilla.redhat.com/show_bug.cgi?id=810676#c28
- Fix gpr

* Mon Aug 20 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-6
- Fix templates_parser import
- Add gnutls patch
- Fix license
- Add LDAP support

* Fri Aug 17 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-4
- Change group
- Remove template_parsers.gpr
- Add doc subpackages

* Thu Aug 16 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-2
- Fix ipv6 issue
- Add tools package

* Thu Aug 16 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.11.0-1
- Update to AWS-2012

* Sun May 20 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-7
- Change cp with cp -a
- Remove chrpath dependency

* Fri Apr 13 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-6
- Fix copyright in aws.gpr file

* Mon Apr 09 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-5
- Fix -devel requires
- Fix -devel license
- Fix version in ChangeLog

* Sun Apr 08 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-4
- Fix smp optflag

* Sun Mar 25 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-3
- Fix gpr file with "xmlada"; added

* Sat Mar 24 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.10.0-2
- Initial build
- add "directories"
