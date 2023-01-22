# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# Configuration for rpmbuild, might be specified by options
# like e.g. 'rpmbuild --define "runselftest 0"'.

# =============================================================================
# IMPORTANT NOTE: This spec file is maintained on two places -- in native
# Fedora repo [1] and in pgjdbc upstream [2].  Please, keep that in sync
# (manual effort!) so both Fedora and Upstream can benefit from automatic
# packaging CI, this is now done in [3] Copr project.
# [1] https://src.fedoraproject.org/rpms/postgresql-jdbc
# [2] https://github.com/pgjdbc/pgjdbc/tree/master/packaging/rpm
# [3] https://copr.fedorainfracloud.org/coprs/g/pgjdbc/pgjdbc-travis/
# ============================================================================

%{!?runselftest:%global runselftest 1}

%global section		devel
%global source_path	pgjdbc/src/main/java/org/postgresql

Summary:	JDBC driver for PostgreSQL
Name:		postgresql-jdbc
Version:	42.5.1
Release:	2%{?dist}
License:	BSD
URL:		http://jdbc.postgresql.org/

Source0:	https://repo1.maven.org/maven2/org/postgresql/postgresql/%{version}/postgresql-%{version}-jdbc-src.tar.gz
Provides:	pgjdbc = %version-%release

BuildArch:	noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:	java-devel >= 1.8
BuildRequires:	maven-local
BuildRequires:	maven-enforcer-plugin
BuildRequires:	maven-plugin-bundle
BuildRequires:	classloader-leak-test-framework

BuildRequires:	mvn(com.ongres.scram:client)
BuildRequires:	mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires:	mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:	mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:	mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:	mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:	mvn(org.junit.vintage:junit-vintage-engine)

%if %runselftest
BuildRequires:	postgresql-contrib
BuildRequires:	postgresql-test-rpm-macros
%endif

# gettext is only needed if we try to update translations
#BuildRequires:	gettext

Obsoletes:	%{name}-parent-poms < 42.2.2-2

%description
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-jdbc package includes the .jar files needed for
Java programs to access a PostgreSQL database.


%package javadoc
Summary:	API docs for %{name}

%description javadoc
This package contains the API Documentation for %{name}.


%prep
%setup -c -q

mv postgresql-%{version}-jdbc-src/* .

# remove any binary libs
find -type f \( -name "*.jar" -or -name "*.class" \) | xargs rm -f

# Build parent POMs in the same Maven call.
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-shade-plugin']"

# compat symlink: requested by dtardon (libreoffice), reverts part of
# 0af97ce32de877 commit.
%mvn_file org.postgresql:postgresql %{name}/postgresql %{name} postgresql

# For compat reasons, make Maven artifact available under older coordinates.
%mvn_alias org.postgresql:postgresql postgresql:postgresql

# remove unmet dependency
%pom_remove_dep uk.org.webcompere:system-stubs-jupiter

# remove tests that depend on the system-stubs-jupiter
rm src/test/java/org/postgresql/test/jdbc2/DriverTest.java \
   src/test/java/org/postgresql/util/OSUtilTest.java \
   src/test/java/org/postgresql/jdbcurlresolver/PgServiceConfParserTest.java \
   src/test/java/org/postgresql/jdbcurlresolver/PgPassParserTest.java \
   src/test/java/org/postgresql/util/StubEnvironmentAndProperties.java


%build
# Ideally we would run "sh update-translations.sh" here, but that results
# in inserting the build timestamp into the generated messages_*.class
# files, which makes rpmdiff complain about multilib conflicts if the
# different platforms don't build in the same minute.  For now, rely on
# upstream to have updated the translations files before packaging.

# Include PostgreSQL testing methods and variables.
%if %runselftest
%postgresql_tests_init

PGTESTS_LOCALE=C.UTF-8

cat <<EOF > build.local.properties
server=localhost
port=$PGTESTS_PORT
database=test
username=test
password=test
privilegedUser=$PGTESTS_ADMIN
privilegedPassword=$PGTESTS_ADMINPASS
preparethreshold=5
loglevel=0
protocolVersion=0
EOF

# Start the local PG cluster.
%postgresql_tests_start
%else
# -f is equal to -Dmaven.test.skip=true
opts="-f"
%endif

%mvn_build $opts --xmvn-javadoc


%install
%mvn_install


%files -f .mfiles
%license LICENSE
%doc README.md


%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 42.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.5.1-1
- rebase to version 42.5.1 (bz#2147486)

* Mon Aug 29 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.5.0-1
- rebase to version 42.5.0 (bz#2119382)

* Thu Aug 04 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.4.1-1
- rebase to version 42.4.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 42.4.0-2
- Rebuilt for Drop i686 JDKs

* Tue Jun 14 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.4.0-1
- rebase to version 42.4.0

* Wed May 25 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.3.6-1
- rebase to version 42.3.6

* Thu May 05 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.3.5-1
- rebase to version 42.3.5

* Tue Apr 19 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.3.4-1
- rebase to version 42.3.4

* Thu Feb 17 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.3.3-1
- rebase to version 42.3.3

* Fri Feb 11 2022 Zuzana Miklankova <zmiklank@redhat.com> - 42.3.2-1
- rebase to version 42.3.2

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 42.3.1-3
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 42.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Zuzana Miklankova <zmiklank@redhat.com> - 42.3.1-1
- rebase to version 42.3.1

* Wed Oct 20 2021 Zuzana Miklankova <zmiklank@redhat.com> - 42.3.0-1
- rebase to version 42.3.0

* Mon Oct 04 2021 Zuzana Miklankova <zmiklank@redhat.com> - 42.2.24-1
- rebase to version 42.2.24

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 42.2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Ondrej Dubaj <odubaj@redhat.com> - 42.2.23-1
- rebase to version 42.2.23

* Wed May 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 42.2.19-2
- remove maven-javadoc-plugin dependency

* Sat Feb 20 2021 Ondrej Dubaj <odubaj@redhat.com> - 42.2.19-1
- rebase to version 42.2.19

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 42.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 20 2020 Ondrej Dubaj <odubaj@redhat.com> - 42.2.18-1
- rebase to version 42.2.18

* Wed Aug 26 2020 Ondrej Dubaj <odubaj@redhat.com> - 42.2.16-1
- rebased to version 42.2.16

* Fri Jul 24 2020 Ondrej Dubaj <odubaj@redhat.com> - 42.2.15-1
- rebased to version 42.2.15

* Fri Jul 24 2020 Ondrej Dubaj <odubaj@redhat.com> - 42.2.12-3
- fixed javadoc build problem + added missing dependencies
- remove SSPIClient for windows API
- fixed XXE vulnerability (CVE-2020-13692)

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 42.2.12-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed May 13 2020 Ondrej Dubaj <odubaj@redhat.com> - 42.2.12-1
- new upstream release + skip javadoc due to jdk-11

* Mon Mar 16 2020 Ondrej Dubaj <odubaj@redhat.com> - 42.2.11-1
- new upstream release

* Mon Mar 02 2020 Ondrej Dubaj <odubaj@redhat.com> - 42.3.0-1
- new upstream release (rhbz#1800440)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 42.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Ondrej Dubaj <odubaj@redhat.com> - 42.2.9-1
- new upstream release (rhbz#1782277)

* Fri Sep 20 2019 Pavel Raiskup <praiskup@redhat.com> - 42.2.8-1
- new upstream release (rhbz#1750766)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 42.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jakub Janco <jjanco@redhat.com> - 42.2.6-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 42.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Pavel Raiskup <praiskup@redhat.com> - 42.2.5-1
- new upstream release

* Fri Aug 03 2018 Pavel Raiskup <praiskup@redhat.com> - 42.2.4-1
- new upstream release (rhbz#1601193)

* Fri Jul 13 2018 Pavel Raiskup <praiskup@redhat.com> - 42.2.3-1
- new upstream release (rhbz#1600759)

* Wed May 30 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 42.2.2-4
- Remove and obsolete parent-poms subpackage

* Fri Apr 20 2018 Pavel Raiskup <praiskup@redhat.com> - 42.2.2-3
- provide postgresql.jar, as that's the upstream's artifactId

* Fri Apr 13 2018 Pavel Raiskup <praiskup@redhat.com> - 42.2.2-2
- BR postgresql-test-rpm-macros

* Fri Mar 16 2018 Pavel Raiskup <praiskup@redhat.com> - 42.2.2-1
- new upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 42.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Pavel Raiskup <praiskup@redhat.com> - 42.2.1-1
- new upstream release

* Fri Jan 19 2018 Pavel Raiskup <praiskup@redhat.com> - 42.2.0-1
- rebase to the latest upstream release
- nicer github source urls
- sync with upstream spec
- use new postgresql testing macros (rawhide only)

* Wed Aug 23 2017 Pavel Raiskup <praiskup@redhat.com> - 42.1.4-1
- rebase to latest upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1212-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1212-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Pavel Raiskup <praiskup@redhat.com> - 9.4.1212-2
- Disable unpredictable test to fix FTBFS (BZ#1406931),
  patch by Merlin Mathesius

* Thu Nov 03 2016 Pavel Raiskup <praiskup@redhat.com> - 9.4.1212-1
- new release, rhbz#1377317, per announcement:
  https://www.postgresql.org/message-id/CAB=Je-FjbvQ_MmAGmhZ-1sSMnodpjr9Uz6Q=faxqCxOvpRO-UQ@mail.gmail.com

* Tue Oct 04 2016 Pavel Raiskup <praiskup@redhat.com> - 9.4.1210-2
- depend on test macros from postgresql-setup

* Thu Sep 08 2016 Pavel Raiskup <praiskup@redhat.com> - 9.4.1210-1
- new release, rhbz#1374106, per announcement:
  https://www.postgresql.org/message-id/CAB=Je-FzuqwDXLTT62VfzvTUhR4QTfLjmw2D5QfgaykDkhW7nw@mail.gmail.com

* Mon Aug 29 2016 Pavel Raiskup <praiskup@redhat.com> - 9.4.1209-6
- fix License, pgjdbc is BSD only

* Thu Jul 21 2016 gil cattaneo <puntogil@libero.it> 9.4.1209-5
- fix postgresql-jdbc.jar symlink using javapackages macros
- adapt to current guideline
- install doc and license file in parent-poms sub package
- simplified runselftest check

* Wed Jul 20 2016 Pavel Raiskup <praiskup@redhat.com> - 9.4.1209-4
- restore one compat symlink

* Wed Jul 20 2016 Pavel Raiskup <praiskup@redhat.com> - 9.4.1209-3
- bump: for Mikolaj's fixes

* Wed Jul 20 2016 Pavel Raiskup <praiskup@redhat.com> - 9.4.1209-2
- update to latest release version, thanks to Pavel Kajaba, Michael Simacek and
  Vladimir Sitnikov for big help
- fix Provides, remove old compatibility hacks

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.1200-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.4.1200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Pavel Raiskup <praiskup@redhat.com> - 9.4.1200-1
- rebase to most recent version (#1188827)

* Mon Jul 14 2014 Pavel Raiskup <praiskup@redhat.com> - 9.3.1102-1
- Rebase to most recent version (#1118667)
- revert back upstream commit for travis build

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.3.1101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Pavel Raiskup <praiskup@redhat.com> - 9.3.1101-3
- run upstream testsuite when '%%runselftest' defined

* Wed Apr 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 9.3.1101-2
- Add explicit requires on java-headless

* Wed Apr 23 2014 Pavel Raiskup <praiskup@redhat.com> - 9.3.1101-1
- Rebase to most recent version (#1090366)

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 9.2.1002-5
- Use Requires: java-headless rebuild (#1067528)

* Tue Aug 06 2013 Pavel Raiskup <praiskup@redhat.com> - 9.2.1002-4
- add javadoc subpackage

* Tue Aug 06 2013 Pavel Raiskup <praiskup@redhat.com> - 9.2.1002-4
- don't use removed macro %%add_to_maven_depmap (#992816)
- lint: trim-lines, reuse %%{name} macro, fedora-review fixes
- merge cleanup changes by Stano Ochotnicky

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.2.1002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.2.1002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 14 2012 Tom Lane <tgl@redhat.com> 9.2.1002-1
- Update to build 9.2-1002 (just to correct mispackaging of source tarball)

* Tue Nov 13 2012 Tom Lane <tgl@redhat.com> 9.2.1001-1
- Update to build 9.2-1001 for compatibility with PostgreSQL 9.2

* Sun Jul 22 2012 Tom Lane <tgl@redhat.com> 9.1.902-1
- Update to build 9.1-902

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.1.901-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 23 2012 Tom Lane <tgl@redhat.com> 9.1.901-3
- Change BuildRequires: java-1.6.0-openjdk-devel to just java-devel.
  As of 9.1-901, upstream has support for JDBC4.1, so we don't have to
  restrict to JDK6 anymore, and Fedora is moving to JDK7
Resolves: #796580

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.1.901-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Tom Lane <tgl@redhat.com> 9.1.901-1
- Update to build 9.1-901 for compatibility with PostgreSQL 9.1

* Mon Aug 15 2011 Tom Lane <tgl@redhat.com> 9.0.801-4
- Add BuildRequires: java-1.6.0-openjdk-devel to ensure we have recent JDK
Related: #730588
- Remove long-obsolete minimum versions from BuildRequires

* Sun Jul 17 2011 Tom Lane <tgl@redhat.com> 9.0.801-3
- Switch to non-GCJ build, since GCJ is now deprecated in Fedora
Resolves: #722247
- Use %%{_mavendepmapfragdir} to fix FTBFS with maven 3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.0.801-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 Tom Lane <tgl@redhat.com> 9.0.801-1
- Update to build 9.0-801

* Mon May 31 2010 Tom Lane <tgl@redhat.com> 8.4.701-4
- Update gcj_support sections to meet Packaging/GCJGuidelines;
  fixes FTBFS in F-14 rawhide

* Tue Nov 24 2009 Tom Lane <tgl@redhat.com> 8.4.701-3
- Seems the .pom file *must* have a package version number in it, sigh
Resolves: #538487

* Mon Nov 23 2009 Tom Lane <tgl@redhat.com> 8.4.701-2
- Add a .pom file to ease use by maven-based packages (courtesy Deepak Bhole)
Resolves: #538487

* Tue Aug 18 2009 Tom Lane <tgl@redhat.com> 8.4.701-1
- Update to build 8.4-701

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:8.3.603-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Tom Lane <tgl@redhat.com> 8.3.603-3
- Avoid multilib conflict caused by overeager attempt to rebuild translations

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:8.3.603-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 8.3.603-1.1
- drop repotag

* Tue Feb 12 2008 Tom Lane <tgl@redhat.com> 8.3.603-1jpp
- Update to build 8.3-603

* Sun Aug 12 2007 Tom Lane <tgl@redhat.com> 8.2.506-1jpp
- Update to build 8.2-506

* Tue Apr 24 2007 Tom Lane <tgl@redhat.com> 8.2.505-1jpp
- Update to build 8.2-505
- Work around 1.4 vs 1.5 versioning inconsistency

* Fri Dec 15 2006 Tom Lane <tgl@redhat.com> 8.2.504-1jpp
- Update to build 8.2-504

* Wed Aug 16 2006 Tom Lane <tgl@redhat.com> 8.1.407-1jpp.4
- Fix Requires: for rebuild-gcj-db (bz #202544)

* Wed Aug 16 2006 Fernando Nasser <fnasser@redhat.com> 8.1.407-1jpp.3
- Merge with upstream

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> 8.1.407-1jpp.2
- Rebuilt

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0:8.1.407-1jpp.1
- rebuild

* Wed Jun 14 2006 Tom Lane <tgl@redhat.com> 8.1.407-1jpp
- Update to build 8.1-407

* Mon Mar 27 2006 Tom Lane <tgl@redhat.com> 8.1.405-2jpp
- Back-patch upstream fix to support unspecified-type strings.

* Thu Feb 16 2006 Tom Lane <tgl@redhat.com> 8.1.405-1jpp
- Split postgresql-jdbc into its own SRPM (at last).
- Build it from source.  Add support for gcj compilation.
