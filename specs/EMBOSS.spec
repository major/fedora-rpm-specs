# TODO:
# fix jemboss and enable it
# This would involve packaging jalview (specifically, the Applet)
# The jalview code has a LOT of bundled pre-built jars.

# NOTE: If EMBOSS updates, please ensure that Patch9 is properly redone to match.
# Notably, emboss/acd/epscan.acd should stay in sync with pscan.acd.

#jemboss is disabled by default due to the fact it bundles a few .jar files which are not built from source.
%bcond_with jemboss

#use --with sunjava if sun's jre is used
%bcond_with sunjava

%if %{with sunjava}
%global _java /usr/java/default
%endif

%global emhome %{_datadir}/EMBOSS

Name:           EMBOSS
Version:        6.6.0
Release:        32%{?dist}
Summary:        The European Molecular Biology Open Software Suite

# Files under jemboss/, ajax/ensembl/ are LGPLv2+
#
# There are some other files which are included in the source tarball 
# but not used, specifically:
# Files under ajax/pcre/ are BSD
# Files under ajax/zlib/ are zlib/libpng
# Because they are not used (they're deleted in %%prep), 
# we do not include them in the license tag.
# There are some included ontologies, thanks to Debian for tracking down all
# the licenses:
# emboss/data/OBO/gene_ontology*.obo : CC-BY-3.0
# emboss/data/OBO/evidence_code.obo : GPLv3+
# emboss/data/OBO/pathway.obo : CC-BY-3.0
# emboss/data/OBO/ro.obo : CC-BY-3.0
# emboss/data/OBO/so.obo : Public Domain
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND CC-BY-3.0 AND GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain
URL:            http://emboss.sf.net/
Source0:        ftp://emboss.open-bio.org/pub/EMBOSS/%{name}-%{version}.tar.gz
# Source1:        ftp://emboss.open-bio.org/pub/EMBOSS/fixes/README.fixes
%if %{with jemboss}
Source2:        jemboss.desktop
%endif
# Use system-wide pcre. Sent upstream. Updated patch created on 2011-11-23.
Patch1:         EMBOSS-6.6.0-system-pcre.patch
# Use system-wide plplot
# Patch3:        EMBOSS-6.3.1-system-plplot.patch
# Use system-wide expat. Updated patch created on 2011-11-23.
Patch4:         EMBOSS-6.6.0-system-expat.patch
# Use system-wide zlib. Updated patch created on 2011-11-23.
Patch5:         EMBOSS-6.6.0-system-zlib.patch

# Fedora-specific. Not sent upstream.
Patch7:         %{name}-fedora.patch
# Fix conflict with pscan (Fedora package, unrelated to EMBOSS)
# https://bugzilla.redhat.com/show_bug.cgi?id=797804
# Emailed upstream on the issue on 2012-02-27
Patch9:		EMBOSS-6.6.0-fix-conflict-with-pscan.patch
# No, we don't need to run a non-existent binary to check across the network
# for updates. *sigh*
Patch10:	EMBOSS-6.6.0-no-update.patch

# PCRE2
Patch11:	EMBOSS-6.6.0-pcre2-v2.patch

# s390 is not so differe... ok, well, it is, but not like this
Patch12:	EMBOSS-s390-too.patch

# Set the proper type for nkeys in ajindex.c
Patch13:	EMBOSS-6.6.0-ajax-nkeys-right-type.patch

BuildRequires:  gd-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  zlib-devel
# BuildRequires:  plplot-devel
BuildRequires:  expat-devel
BuildRequires:  libharu-devel
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel openssl-devel
BuildRequires:  libtool, autoconf
%if %{with jemboss}
BuildRequires:  ant
BuildRequires:  desktop-file-utils
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils
BuildRequires:  axis classpathx-mail jaf jakarta-commons-discovery jakarta-commons-logging
BuildRequires:  log4j regexp servlet xerces-j2 wsdl4j
%endif
BuildRequires: make

%if %{with sunjava}
Requires:       jdk = 2000:1.6.0_17-fcs
%endif

# We need this to force updates across minor releases where sonames do not change
Requires:       %{name}-libs = %{version}-%{release}

%description
EMBOSS is a new, free Open Source software analysis package specially
developed for the needs of the molecular biology (e.g. EMBnet) user community.
The software automatically copes with data in a variety of formats and even
allows transparent retrieval of sequence data from the web. Also, as extensive
libraries are provided with the package, it is a platform to allow other
scientists to develop and release software in true open source spirit.
EMBOSS also integrates a range of currently available packages and tools for
sequence analysis into a seamless whole.

Reference for EMBOSS: Rice,P. Longden,I. and Bleasby,A.
"EMBOSS: The European Molecular Biology Open Software Suite"
Trends in Genetics June 2000, vol 16, No 6. pp.276-277


%package devel
Summary:        Development tools for programs which will use the %{name} library
Requires:       %{name}-libs = %{version}-%{release}
Requires:       libeplplot-devel = %{version}-%{release}

%description devel
The %{name}-devel package includes the header files and static libraries
necessary for developing programs which will use the %{name} library.


%package libs
Summary:        Shared libraries for %{name}

%description libs
The %{name}-libs package includes the dynamic libraries
necessary for %{name}.

%if %{with jemboss}
%package -n jemboss
Summary:        Java interface to %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       java >= 1:1.6.0
Requires:       jpackage-utils
Requires:       axis jaf javamail jakarta-commons-discovery jakarta-commons-logging
Requires:       log4j regexp servlet xerces-j2 wsdl4j

%description -n jemboss
Jemboss is a Java interface to EMBOSS, developed at
the HGMP-RC and in close collaboration with the EMBOSS
development team. It is distributed as part of the EMBOSS
software.

Documentation on Jemboss can be found at:
http://www.hgmp.mrc.ac.uk/Software/EMBOSS/Jemboss/
%endif

%package -n libeplplot
Summary:        A modified version of plplot used by EMBOSS

%description -n libeplplot
A modified version of plplot used by EMBOSS.

%package -n libeplplot-devel
Summary:        Development files for eplplot
Requires:       libeplplot = %{version}-%{release}

%description -n libeplplot-devel
The libeplplot-devel package includes the header files and libraries
necessary for developing programs which will use the eplplot library.


%prep
%setup -q
%patch -P1 -p1 -b .system-pcre
%patch -P4 -p1 -b .system-expat
%patch -P5 -p1 -b .system-zlib
%patch -P7 -p0 -b .fedora
%patch -P9 -p1 -b .fixconflict
%patch -P10 -p1 -b .noupdate
%patch -P11 -p1 -b .pcre2
%patch -P12 -p1 -b .s390-too
%patch -P13 -p1 -b .nkeys-right-type

# Remove bundled expat, pcre and zlib files to make sure that system versions are used
rm -rf ajax/{expat,pcre,zlib}/*

#install the patch readme
# install -pm 644 %{SOURCE1} README.fixes

#these files were executable for some reason
chmod 644 emboss/prettyplot.c emboss/polydot.c emboss/supermatcher.c

%if %{with jemboss}
#use newer log4j version
sed -i "s@log4j-1.2.8@log4j-1.2.14@" \
    jemboss/lib/axis/Makefile.am \
    jemboss/lib/axis/Makefile.in \
    jemboss/utils/makeFileManagerJNLP.sh \
    jemboss/utils/makeJNLP.sh

#use system java libraries
rm jemboss/lib/{activation,jakarta-regexp-1.2,jemboss,mail,xerces}.jar
build-jar-repository -s -p jemboss/lib activation regexp javamail xerces-j2
mv jemboss/lib/regexp.jar jemboss/lib/jakarta-regexp-1.2.jar
mv jemboss/lib/javamail.jar jemboss/lib/mail.jar
mv jemboss/lib/xerces-j2.jar jemboss/lib/xerces.jar
rm jemboss/lib/axis/*.jar
build-jar-repository -s -p jemboss/lib/axis axis/axis-ant axis/axis axis/jaxrpc axis/saaj commons-discovery commons-logging log4j-1.2.14 servlet wsdl4j
for i in axis axis-ant jaxrpc saaj;
do
mv jemboss/lib/axis/axis_$i.jar jemboss/lib/axis/$i.jar;
done
%endif


%build
%if %{with sunjava}
export PATH=$PATH:%{_java}/bin/
%endif

autoreconf -i

%configure \
  --disable-static \
  --with-x \
  --with-auth \
  --with-thread \
  --includedir=%{_includedir}/EMBOSS \
  --enable-systemlibs \
%ifarch ppc64 sparc64 x86_64
  --enable-64 \
%endif
%if %{with jemboss}
  --with-java=/usr/lib/jvm/java/include \
  --with-javaos=/usr/lib/jvm/java/include/linux
%endif
%if %{with sunjava}
  --with-java=%{_java}/include
  --with-javaos=%{_java}/include/linux
%endif


%{__make} %{?_smp_mflags}


%install
%if %{with sunjava}
export PATH=$PATH:%{_java}/bin/
%endif

rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat << __EOF__ >> $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/emboss.sh
export PLPLOT_LIB=%{emhome}
export EMBOSS_ACDROOT=%{emhome}/acd
export EMBOSS_DOCROOT=%{emhome}/doc
export EMBOSS_DATABASE_DIR=%{emhome}/data
export EMBOSS_DATA=%{emhome}/data
__EOF__

cat << __EOF__ >> $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/emboss.csh
setenv PLPLOT_LIB %{emhome}
setenv EMBOSS_ACDROOT %{emhome}/acd
setenv EMBOSS_DOCROOT %{emhome}/doc
setenv EMBOSS_DATABASE_DIR %{emhome}/data
setenv EMBOSS_DATA %{emhome}/data
__EOF__

rm $RPM_BUILD_ROOT%{_libdir}/*.la

#this file has zero length, so kill it
rm $RPM_BUILD_ROOT%{_datadir}/EMBOSS/test/data/dna.aln

#fix executable permissions
pushd $RPM_BUILD_ROOT%{_datadir}/EMBOSS/jemboss/utils
chmod +x install-jemboss-server.sh keys.sh makeFileManagerJNLP.sh makeJar.csh \
     makeJNLP.sh
popd
# pushd $RPM_BUILD_ROOT%{_datadir}/EMBOSS/jemboss/api
# chmod +x getClasses.pl makeDocs.csh
# popd

# rename conflicting binaries because of generic names
mv $RPM_BUILD_ROOT%{_bindir}/chaos $RPM_BUILD_ROOT%{_bindir}/em_chaos
mv $RPM_BUILD_ROOT%{_bindir}/remap $RPM_BUILD_ROOT%{_bindir}/em_remap
mv $RPM_BUILD_ROOT%{_bindir}/wordcount $RPM_BUILD_ROOT%{_bindir}/em_wordcount

%if %{with jemboss}
#install the desktop file
desktop-file-install                                    \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
%{SOURCE2}
%else
# Nuke the binaries so they don't make debuginfo
rm -rf ${RPM_BUILD_ROOT}%{_bindir}/runJemboss.csh
rm -rf ${RPM_BUILD_ROOT}%{_bindir}/jembossctl
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/EMBOSS/jemboss
%endif


%ldconfig_scriptlets libs

%ldconfig_scriptlets -n libeplplot


%files
%doc AUTHORS ChangeLog FAQ INSTALL NEWS README THANKS
%{_bindir}/*
%{_datadir}/EMBOSS
%if %{with jemboss}
%exclude %{_bindir}/runJemboss.csh
%exclude %{_bindir}/jembossctl
%exclude %{_datadir}/EMBOSS/jemboss
%endif
%config %{_sysconfdir}/profile.d/*

%files devel
%{_libdir}/*.so
%{_includedir}/EMBOSS
%exclude %{_includedir}/EMBOSS/eplplot/

%files libs
%license COPYING LICENSE
%{_libdir}/*.so.*
%exclude %{_libdir}/libeplplot*

%if 0%{?with_jemboss} || 0%{?with_sunjava}
%files -n jemboss
%doc jemboss/README jemboss/resources jemboss/api
%{_bindir}/runJemboss.csh
%{_bindir}/jembossctl
%{_datadir}/applications/jemboss.desktop
%{_datadir}/EMBOSS/jemboss
%endif

%files -n libeplplot
%{_libdir}/libeplplot*.so.*

%files -n libeplplot-devel
%{_includedir}/EMBOSS/eplplot/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 10 2024 Tom Callaway <spot@fedoraproject.org> - 6.6.0-30
- patch up s390 support

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Tom Callaway <spot@fedoraproject.org> - 6.6.0-26
- fix pcre2 patch (no more segfaults, hopefully)
- update license tag

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Orion Poplawski <orion@nwra.com> - 6.6.0-23
- Rebuild for libharu 2.4.3

* Tue Sep 20 2022 Tom Callaway <spot@fedoraproject.org> - 6.6.0-22
- use pcre2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 6.6.0-18
- rebuild for libpq ABI fix rhbz#1908268

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Tom Callaway <spot@fedoraproject.org> - 6.6.0-11
- rename "wordcount" to "em_wordcount" to resolve conflict with texlive

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 28 2017 Tom Callaway <spot@fedoraproject.org> - 6.6.0-9
- fix mariadb issues (bz1493684)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Tom Callaway <spot@fedoraproject.org> - 6.6.0-7
- rebuild against new mariadb

* Thu Jun 15 2017 Tom Callaway <spot@fedoraproject.org> - 6.6.0-6
- rebuild against new libharu (2.3.0)

* Tue May 16 2017 Tom Callaway <spot@fedoraproject.org> - 6.6.0-5
- rename "remap" to "em_remap" (bz1450190)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 6.6.0-2
- spec file cleanup

* Fri Oct 30 2015 Tom Callaway <spot@fedoraproject.org> - 6.6.0-1
- update to 6.6.0

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep  3 2013 Tom Callaway <spot@fedoraproject.org> - 6.4.0-11
- add ontology license tags, thanks to Debian

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Remi Collet <rcollet@redhat.com> - 6.4.0-9
- rebuild for new GD 2.1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Tom Callaway <spot@fedoraproject.org> - 6.4.0-7
- rebuild for new libharu

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Tom Callaway <spot@fedoraproject.org> - 6.4.0-5
- resolve conflict with pscan

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 6.4.0-4
- Rebuild against PCRE 8.30

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jan 07 2012 Julian Sikorski <belegdol@fedoraproject.org> - 6.4.0-2
- Rebuilt for gcc-4.7
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Wed Nov 23 2011 Julian Sikorski <belegdol@fedoraproject.org> - 6.4.0-1
- Updated to 6.4.0
- Dropped included new-fix-doc-finding and fix-amd64-check patches
- Updated system libs patches
- tabs → spaces to satisfy rpmlint

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 6.3.1-11
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Mar 22 2011 Julian Sikorski <belegdol@fedoraproject.org> - 6.3.1-10
- Rebuilt for mysql-5.5.10

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 6.3.1-8
- split libeplplot into its own package

* Tue Nov  9 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 6.3.1-7
- use bundled plplot (EMBOSS depends on fork)
- add BR for postgresql-devel and mysql-devel
- use autotools to generate updated configure/Makefiles
- fix amd64 check to be finer grained, eliminate koji false positive

* Thu Nov  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 6.3.1-6
- more intricate fix doc finding patch for 6.3.1

* Thu Nov  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 6.3.1-5
- add forced requires to ensure proper (and matched) updates
- cleaner fix doc finding patch

* Wed Oct 27 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 6.3.1-4
- fix doc finding (bz 647140)

* Mon Oct 11 2010 Orion Poplawski <orion@cora.nwra.com> - 6.3.1-3
- Rebuild for plplot 5.9.7

* Tue Aug 10 2010 Julian Sikorski <belegdol@fedoraproject.org> - 6.3.1-2
- Updated the upstream patch to 1-4

* Mon Aug 02 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 6.3.1-1
- update to 6.3.1

* Wed Jul 07 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 6.2.0-4
- include license information in EMBOSS-libs package, instead of EMBOSS
  since EMBOSS-libs always gets pulled in when EMBOSS is installed

* Wed Apr 07 2010 Julian Sikorski <belegdol@fedoraproject.org> - 6.2.0-3
- Added upstream 1-18 patch

* Wed Apr  7 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 6.2.0-2
- fix pcre patch, use system pcre
- add patch to use system zlib
- add patch to use system plplot
- add patch to use system expat

* Wed Feb 24 2010 Julian Sikorski <belegdol@fedoraproject.org> - 6.2.0-1
- Updated to 6.2.0
- jemboss can be built using --with jemboss
- Disabled the pcre patch
- Made the licensing information more detailed
- --with sunjava allows building against Sun's JVM

* Sun Dec 13 2009 Julian Sikorski <belegdol@fedoraproject.org> - 6.1.0-6
- Added the upstream 1-3 patch
- Fixed bogus Patch3 description
- Jemboss is still disabled, but some improvements have been made
  - Backported patch enabling jemboss rebuild from CVS
  - Added ant and jpackage-utils to BuildRequires
  - Made java-devel dependency versioned
  - Switched to build-jar-repository to fill the dependencies
  - Replaced versioned log4j calls with latest version
  - Renamed EMBOSS-java to jemboss
  - Added a desktop entry for jemboss from Debian

* Sat Oct 17 2009 Julian Sikorski <belegdol@fedoraproject.org> - 6.1.0-5
- Added comments explaining the purpose of each patch

* Mon Oct 05 2009 Julian Sikorski <belegdol@fedoraproject.org> - 6.1.0-4
- Renamed conflicting binaries
- Disabled jemboss

* Tue Sep 29 2009 Julian Sikorski <belegdol@fedoraproject.org> - 6.1.0-3
- Re-enabled system pcre usage
- Initial attempt at using system-wide .jar files

* Tue Sep 22 2009 Julian Sikorski <belegdol@fedoraproject.org> - 6.1.0-2
- Added the upstream 1-2 patch

* Wed Jul 29 2009 Julian Sikorski <belegdol@fedoraproject.org> - 6.1.0-1
- Updated to 6.1.0
- Dropped pcre-devel from BuildRequires for the time being
- Ditto --with-java and --with-javaos
- Patched jemboss/Makefile.am not to include DESTDIR in runJemboss.sh
- Install the header files in EMBOSS subdir
- Added the missing executable bits

* Fri Jun 12 2009 Julian Sikorski <belegdol@fedoraproject.org> - 6.0.1-3
- Updated the upstream patch to 1-12
- Added the patch readme to %%doc

* Thu Apr 16 2009 Julian Sikorski <belegdol@fedoraproject.org> - 6.0.1-2
- Own %%{_datadir}/EMBOSS
- Don't use %%{name} macro in %%files
- Updated the upstream patch to 1-7
- Use dist instead of dist_tag
- Adjusted whitespaces
- Added pcre-devel to BuildRequires
- Fixed spurious executable permissions
- Removed the empty dna.aln file
- Patched jemboss.properties to include the paths this package uses
- Made the -java package require the main one

* Mon Sep 29 2008 Dominik Mierzejewski <rpm@greysector.net> 6.0.1-1
- updated to 6.0.1
- applied upstream patch 1-1
- patched to use system pcre

* Tue Jan 08 2008 Dominik Mierzejewski <rpm@greysector.net> 5.0.0-1
- Cleaned up BioRPMs' spec
- Updated to 5.0.0

* Thu Mar 17 2005 Bent Terp <Bent.Terp@biosci.ki.se>
- Upped to 2.10.0

* Fri Jul 16 2004 Bent Terp <Bent.Terp@biosci.ki.se>
- Had forgotten the emboss_database_dir env var

* Wed Feb 18 2004 Bent Terp <Bent.Terp@biosci.ki.se>
- Tried to make the building more dynamic. Added Requires and BuildRequires

* Thu Dec 04 2003 Luc Ducazu <luc@biolinux.org>
- Build for EMBOSS 2.8.0
- subpackage jemboss

* Wed Jun 11 2003 Luc Ducazu <luc@biolinux.org>
- Build for EMBOSS 2.7.1

* Tue Jan 28 2003 Luc Ducazu <luc@biolinux.org>
- Build for EMBOSS 2.6.0
- Programs moved to /usr/local/bin
- Adopted many ideas from Guillaume Rousse <g.rousse@linux-mandrake.com>

* Wed Nov 27 2002 Luc Ducazu <luc@biolinux.org>
- Initial build for EMBOSS 2.5.1
