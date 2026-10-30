Summary: %{nice_name} is a powerful open-source tool that parses and evaluates algebraic and mathematical expressions
%global nice_name ParserNG
Name: parserng
Version: 3.0.9.1
Release: 1%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/gbenroscience/ParserNG
# tarred cloned repo without hidden files and without idea iml
# usptream do not tag, but uses maven versionining
# so this is f619fad1fefa21116bab4a0abba2dd0ebe719e45
# which set pom to 0.1.9 and moved it to maven repos
# git clone https://github.com/gbenroscience/ParserNG &&  cd ParserNG  && git checkout f619fad1fefa21116bab4a0abba2dd0ebe719e45 && tar -cJf parserng-0.1.9.tar.xz *
Source0: v%{version}.tar.gz
Source1: parserng
Patch1: jdk21rounding.patch

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires: maven-local-openjdk25
BuildRequires: junit5
BuildRequires: ant-junit5
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-clean-plugin
BuildRequires: java-25-devel
Requires: java-25-headless
Provides: ParserNG
Provides: parser-ng

%description
Rich and Performant, Cross Platform Java Library(100% Java)...
Now allows the differentiation function to be differentiated with
respect to any variable(not just x).  Next to math.Main main cmdline entry point 
also parser.MathExpression and parser.cmd.ParserCmd  are here for cmdline service

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -c %{name}-%{version}
%patch -P1 -p0

# remove all tests deps
for x in `find | grep pom.xml` ; do
  if dirname $x | grep "/parser-ng$" ; then
    echo "will try the tests here"
  else
    pushd `dirname $x`
      %pom_remove_dep :junit-jupiter-api  || echo "not all are everywhere"
      %pom_remove_dep :junit-jupiter-engine || echo "not all are everywhere"
      %pom_remove_dep :junit-jupiter-params || echo "not all are everywhere"
      %pom_remove_dep :jmh-core || echo "not all are everywhere"
      %pom_remove_dep :jmh-generator-annprocess || echo "not all are everywhere"
      %pom_remove_dep :janino || echo "not all are everywhere"
    popd
  fi
done


pushd ParserNG-3.0.9.1
  %pom_remove_plugin :central-publishing-maven-plugin
  %pom_remove_plugin :maven-source-plugin
  %pom_remove_plugin :maven-gpg-plugin
  %pom_remove_plugin :maven-javadoc-plugin
  pushd parser-ng
    %pom_remove_plugin :maven-jar-plugin
  popd
  for x in parser-ng-parquet parser-ng-simd parser-ng-gpu-simd parser-ng-bench parser-ng-arrow; do
    pushd $x
      %pom_remove_plugin :maven-shade-plugin
    popd 
  done
  for x in parser-ng-sql parser-ng-arrow ; do
    pushd $x
      #os-maven-plugin
      %pom_xpath_remove  "pom:project/pom:build/pom:extensions"
    popd 
  done
  for x in parser-ng-simd parser-ng-gpu-simd; do
    pushd $x
      #jmh "for tests"
      %pom_xpath_remove  "pom:project/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:annotationProcessorPaths"
    popd 
  done
  #no apache java-arrow in fedora
  %pom_disable_module parser-ng-arrow
  %pom_disable_module parser-ng-parquet
  %pom_disable_module parser-ng-sql
  %pom_disable_module parser-ng-bench
popd


%build
cd ParserNG-%{version}
# run at least main tests and docs
pushd parser-ng
  xmvn --batch-mode --offline test
popd
# tests requires jmh:(
%mvn_build -f -j


%install
cd ParserNG-%{version}
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

%files -f ParserNG-%{version}/.mfiles
%license ParserNG-%{version}/LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
