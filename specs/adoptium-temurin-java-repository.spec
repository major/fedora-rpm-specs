%global     reponame   %{name}.repo
%global     repodir    %{_sysconfdir}/yum.repos.d
%global     thirdparty %{_prefix}/lib/fedora-third-party/conf.d

%define obsoleteLine() %{expand:
Obsoletes: java-%{?1}-openjdk%{?2}%{?3} < 1:100000
Obsoletes: java-%{?1}-openjdk-portable%{?2}%{?3} < 1:1000
}

%define obsoleteLines() %{expand:
%{obsoleteLine -- %{?1} %{?2} %{nil}}
%{obsoleteLine -- %{?1} %{?2} -fastdebug}
%{obsoleteLine -- %{?1} %{?2} -slowdebug}
%{obsoleteLine -- %{?1} %{?2} -unstripped}
}

%define obsoleteJdk() %{expand:
%{obsoleteLines -- %{?1} %{nil}}
%{obsoleteLines -- %{?1} -headless}
%{obsoleteLines -- %{?1} -devel}
%{obsoleteLines -- %{?1} -demo}
%{obsoleteLines -- %{?1} -src}
%{obsoleteLines -- %{?1} -javadoc}
%{obsoleteLines -- %{?1} -javadoc-zip}
%{obsoleteLines -- %{?1} -jmods}
%{obsoleteLines -- %{?1} -static-libs}
%{obsoleteLines -- %{?1} -openjfx}
%{obsoleteLines -- %{?1} -openjfx-devel}
%{obsoleteLines -- %{?1} -docs}
%{obsoleteLines -- %{?1} -sources}
%{obsoleteLines -- %{?1} -misc}
}

# 0/1 may vary in time, and is always enabled to 1 per FESCO exception
%global     enabled_by_default 0

Name:       adoptium-temurin-java-repository
Version:    1
Release:    %autorelease
Summary:    Fedora package repository files for yum and dnf along with gpg public keys

License:    EPL-2.0
URL:        https://adoptium.net/installation/linux/#_centosrhelfedora_instructions
Source0:    LICENSE
Source1:    %{name}.conf
Source2:    %{reponame}
Source3:    README.md

BuildArch:  noarch
# fedora-third-party contains tools to work with 3rd party repos and owns fedora-third-party/conf.d/ directory
Requires:   fedora-third-party

#dont forget to update the lua list in pre and bash list in post
%{obsoleteJdk -- 1.8.0}
%{obsoleteJdk -- 11}
%{obsoleteJdk -- 17}
%{obsoleteJdk -- 21}
Obsoletes: openjfx8 < 1000
Obsoletes: openjfx8-devel < 1000

%description
This package adds configuration to add a remote repository
of https://adoptium.net/installation/linux/#_centosrhelfedora_instructions ,
if third-party repositories are enabled on a Fedora Linux system.
This repository contains all JDKS which are live and not available in fedora 
as per https://fedoraproject.org/wiki/Changes/ThirdPartyLegacyJdks .
It (4.1.2026) installs: temurin-11-jdktemurin-17-jdk temurin-21-jdk
temurin-25-jdk temurin-8-jdk, theirs -jre variants and we expect jre-headless in March 2026
Warning, jdk contains both jre and jdk, so if you install jdk and jre (of same version)
you will have two java alternatives masters, and one javac master.
Since f42 it will be obsoleting retired java-(1.8.0,11,17)-openjdk-*
Since f44 it will be obsoleting also java-(21)-openjdk-*
https://fedoraproject.org/wiki/Changes/Java21RemovedEarlierThenScheduled

%prep
cat %{SOURCE2} |  sed "s/^enabled=0/enabled=%{enabled_by_default}/" > %{reponame}

%build

%install
install -D -m0644 %{SOURCE0} %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -D -m0644 %{SOURCE1} -t %{buildroot}%{thirdparty}/
install -D -m0644 %{reponame} -t %{buildroot}%{repodir}/
install -D -m0644 %{SOURCE3} -t %{buildroot}%{_docdir}/%{name}/


%pre -p <lua>
-- in dnf5 lua goes to stdout, but not to logs
local posix = require ("posix")

local jdksKnown={"1.8.0", "11", "17", "21"}
local jdksFound={}

local javadir="/usr/lib/jvm"
local binJava="bin/java"
local binJavac="bin/javac"
local jreBinJava="jre/bin/java"

for key, value in pairs(jdksKnown) do
  jdksFound[value]=0;
  local java="java-"..value.."-openjdk"
  local jre="jre-"..value.."-openjdk"
  local statJavaJre1 = posix.stat(javadir.."/"..java.."/"..binJava, "type");
  local statJavaJre2 = posix.stat(javadir.."/"..java.."/"..jreBinJava, "type");
  local statJavaSdk = posix.stat(javadir.."/"..java.."/"..binJavac, "type");
  local statJreJre1 = posix.stat(javadir.."/"..jre.."/"..binJava, "type");
  local statJreJre2 = posix.stat(javadir.."/"..jre.."/"..jreBinJava, "type");
  local statJreSdk = posix.stat(javadir.."/"..jre.."/"..binJavac, "type");
  if ((statJavaJre1 ~= nil)) then
    jdksFound[value]=jdksFound[value]+1;
  end
  if ((statJavaJre2 ~= nil)) then
    jdksFound[value]=jdksFound[value]+1;
  end
  if ((statJreJre1 ~= nil)) then
    jdksFound[value]=jdksFound[value]+1;
  end
  if ((statJreJre2 ~= nil)) then
    jdksFound[value]=jdksFound[value]+1;
  end
  if ((statJavaSdk ~= nil)) then
      jdksFound[value]=jdksFound[value]+1000;
  end
  if ((statJavaSdk ~= nil)) then
      jdksFound[value]=jdksFound[value]+1000;
  end
end
local counter=0
for key, value in pairs(jdksFound) do
  temurinKey=key
  if key == "1.8.0" then
    temurinKey=8
  end
  if value > 0 then
    if (counter==0) then
      print("") --dnf5 is consuming first and alst line of output. this is it
    end
    print("You have java-"..key.."-openjdk installed. That is deprecated, and is replaced by temurin-"..temurinKey.."-jre")
  end
  if value > 999 then
    print("You have java-"..key.."-openjdk-devel installed. That is deprecated, and is replaced by temurin-"..temurinKey.."-jdk")
  end
  counter=counter+value
end
if counter>0 then
  print("https://fedoraproject.org/wiki/Changes/ThirdPartyLegacyJdks")
  print("https://fedoraproject.org/wiki/Changes/Java21RemovedEarlierThenScheduled")
  print("") --dnf5 is consuming first and alst line of output. this is it
end

%post
# in dnf5 bash goes to logs, but not to stdout
hits=0
for x in 1.8.0 11 17 21; do
  key="$x"
  if [ "$key" == "1.8.0" ] ; then
    key=8
  fi
  if [ -e /usr/lib/jvm/java-$x-openjdk/bin/java ] || [ -e /usr/lib/jvm/java-$x-openjdk/bin/jre/java ] || [ -e /usr/lib/jvm/jre-$x-openjdk/bin/java ] || [ -e /usr/lib/jvm/jre-$x-openjdk/jre/bin/java ] ; then
    echo "java-$x-openjdk installed. That is deprecated, and is replaced by temurin-$key-jdk"
    let hits=$hits+1
  fi
  if [ -e /usr/lib/jvm/java-$x-openjdk/bin/javac ] ; then
    echo "java-$x-openjdk-devel installed. That is deprecated, and is replaced by temurin-$key-jdk"
    let hits=$hits+1
  fi
done
if [ $hits -gt 0 ] ; then
  echo "https://fedoraproject.org/wiki/Changes/ThirdPartyLegacyJdks"
  echo "https://fedoraproject.org/wiki/Changes/Java21RemovedEarlierThenScheduled"
fi



%files
%license LICENSE
%{thirdparty}/*
%config(noreplace) %{repodir}/%{reponame}
%doc README.md

%changelog
%autochangelog
