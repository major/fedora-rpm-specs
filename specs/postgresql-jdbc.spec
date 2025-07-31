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

%global section devel
%global source_path pgjdbc/src/main/java/org/postgresql

Summary:        JDBC driver for PostgreSQL
Name:           postgresql-jdbc
Version:        42.7.7
Release:        %autorelease
License:        BSD-2-Clause
URL:            https://jdbc.postgresql.org/
Source0:        https://repo1.maven.org/maven2/org/postgresql/postgresql/%{version}/postgresql-%{version}-jdbc-src.tar.gz
Source1:        postgresql_jdbc_tests_init.sh
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Provides:       pgjdbc = %{version}-%{release}

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.ongres.scram:scram-client)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(se.jiderhamn:classloader-leak-test-framework)

%if %runselftest
BuildRequires:  postgresql17-contrib
BuildRequires:  postgresql17-test-rpm-macros
%endif

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 42.7.4-9

# gettext is only needed if we try to update translations
# BuildRequires:  gettext

%description
PostgreSQL is an advanced Object-Relational database management system. The
postgresql-jdbc package includes the .jar files needed for Java programs to
access a PostgreSQL database.

%package tests
Summary:        Tests for %{name}

%description tests
This package contains tests for %{name}.

%prep
%autosetup -p1 -n postgresql-%{version}-jdbc-src

# remove any binary libs
find -type f \( -name "*.jar" -or -name "*.class" \) -delete

# Build parent POMs in the same Maven call.
%pom_remove_plugin :maven-shade-plugin

# compat symlink: requested by dtardon (libreoffice), reverts part of
# 0af97ce32de877 commit.
%mvn_file org.postgresql:postgresql %{name}/postgresql %{name} postgresql

# For compat reasons, make Maven artifact available under older coordinates.
%mvn_alias org.postgresql:postgresql postgresql:postgresql

# remove unmet dependency
%pom_remove_dep uk.org.webcompere:system-stubs-jupiter
# remove tests that depend on the system-stubs-jupiter
grep -l -r '^import uk\.org\.webcompere\.systemstubs' src/test | xargs rm -v

# Install -tests Jar as well
%pom_xpath_inject 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-jar-plugin"]' '
<executions>
  <execution>
    <goals>
      <goal>test-jar</goal>
    </goals>
  </execution>
</executions>'
%mvn_package org.postgresql:postgresql::tests: tests

%build
# Ideally we would run "sh update-translations.sh" here, but that results
# in inserting the build timestamp into the generated messages_*.class
# files, which makes rpmdiff complain about multilib conflicts if the
# different platforms don't build in the same minute.  For now, rely on
# upstream to have updated the translations files before packaging.

# Include PostgreSQL testing methods and variables.
%if %runselftest
. %{SOURCE1}
setup_build_local_properties > build.local.properties

# Start the local PG cluster.
%postgresql_tests_start
%else
# NOTE this parameter skips running tests but still compiles them
opts="-DskipTests=true"
%endif

%mvn_build -j -- $opts

xmvn -Dmdep.outputFile=tests-classpath dependency:build-classpath --offline

%install
%mvn_install
install -m 644 -D tests-classpath %{buildroot}%{_datadir}/%{name}-tests/classpath
install -m 644 -D -t %{buildroot}%{_datadir}/%{name}-tests build.properties ssltest.properties
cp -r -t %{buildroot}%{_datadir}/%{name}-tests certdir
install -m 755 -D -t %{buildroot}%{_libexecdir}/%{name}-tests %{SOURCE1}

%files -f .mfiles
%license LICENSE
%doc README.md

%files tests -f .mfiles-tests
%license LICENSE
%{_datadir}/%{name}-tests
%{_libexecdir}/%{name}-tests

%changelog
%autochangelog
