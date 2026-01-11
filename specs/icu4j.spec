%global giturl  https://github.com/unicode-org/icu

Name:           icu4j
Version:        78.2
Release:        %autorelease
Epoch:          1
Summary:        International Components for Unicode for Java
License:        Unicode-3.0
URL:            https://icu.unicode.org/
VCS:            git:%{giturl}.git

Source:         %{giturl}/archive/release-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(pl.pragmatists:JUnitParams)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# This can be removed when F47 reaches EOL
Obsoletes:      %{name}-localespi < 78
Provides:       %{name}-localespi = 1:%{version}-%{release}

%description
The International Components for Unicode (ICU) library provides robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and provides support for
supplementary characters (needed for GB 18030 repertoire support).

Java provides a very strong foundation for global programs, and IBM and the
ICU team played a key role in providing globalization technology into Sun's
Java. But because of its long release schedule, Java cannot always keep
up-to-date with evolving standards. The ICU team continues to extend Java's
Unicode and internationalization support, focusing on improving performance,
keeping current with the Unicode standard, and providing richer APIs, while
remaining as compatible as possible with the original Java text and
internationalization API design.

%package        charset
Summary:        Charset converter library of %{name}
Requires:       %{name} = 1:%{version}-%{release}

%description    charset
Charset converter library of %{name}.

%package        parent
Summary:        Parent POM for %{name}

%description    parent
Parent POM for %{name}.

%package        javadoc
# Unicode-3.0: the content
# MIT: jquery
License:        Unicode-3.0 AND MIT
Summary:        API documentation for %{name}
Provides:       bundled(js-jquery)

%description    javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -n icu-release-%{version}

%conf
cd icu4j
# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_plugin -r :maven-clean-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-install-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-project-info-reports-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin

# Modules we do not want to ship
%pom_disable_module demos
%pom_disable_module perf-tests
%pom_disable_module samples
%pom_disable_module tools/build
%pom_disable_module tools/misc
%pom_disable_module tools/pmd
cd -

%build
cd icu4j
%mvn_build -s
cd -

%install
cd icu4j
%mvn_install
cd -

# We do not want the dev and test component jars
rm %{buildroot}%{_javadir}/icu4j/{common_tests,framework}.jar
rm %{buildroot}%{_datadir}/maven-metadata/icu4j-{common_tests,framework}.xml
rm %{buildroot}%{_mavenpomdir}/icu4j/{common_tests,framework}.pom
sed -i '/%dir/d' icu4j/.mfiles-{c,f,l,r,t}* icu4j/.mfiles-icu4j-charset

%files -f icu4j/.mfiles-icu4j -f icu4j/.mfiles-collate -f icu4j/.mfiles-core -f icu4j/.mfiles-currdata -f icu4j/.mfiles-langdata -f icu4j/.mfiles-regiondata -f icu4j/.mfiles-tools_taglets -f icu4j/.mfiles-translit
%license LICENSE
%doc icu4j/readme.html icu4j/APIChangeReport.html

%files charset -f icu4j/.mfiles-icu4j-charset

%files parent -f icu4j/.mfiles-icu4j-root

%files javadoc -f icu4j/.mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
