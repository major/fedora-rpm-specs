Name:           colossus
%global         rev        5331
%global         revdate    20130917
Version:        0.14.0
%global         branch    %{nil}
Release:        30%{?dist}
Summary:        Allows people to play Titan against each other or AIs

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://colossus.sourceforge.net/

# The svn repo includes some prebuilt jar files that need to be removed
# The colossus-gen-tarball.sh can be used to fetch either the latest
# revision or a specified revision from the repo, strip the jar files
# and some artwork and then build a tar.gz archive.
# colossus-rev.xsl is used to extract the current revision of HEAD
# when grabbing the latest revision, using svn info.
# The repo is at:
# https://colossus.svn.sourceforge.net/svnroot/colossus/trunk/Colossus
Source0:        colossus-%{branch}-%{revdate}-%{rev}.tar.gz
Source1:        colossus-gen-tarball.sh
Source2:        colossus-rev.xsl

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch


# Note the intention is to eventually require only java 1.5 for both building
# and installing. But bug 510243 in gjdoc currently blocks this.
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  jdom
BuildRequires:  desktop-file-utils
BuildRequires:  zip
Requires:       java
Requires:       jpackage-utils
Requires:       jdom
Requires(post):  coreutils
Requires(postun):  coreutils

%description
Colossus allows people to play Titan
(http://www.boardgamegeek.com/boardgame/103) and several Titan variants, hot
seat or via a network. Several different AIs are provided that can play instead
of humans.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{branch}-%{revdate}-%{rev}

%build

# Create file for local build properties
cp /dev/null local_build.properties

# Tell colossus' build process where to look for needed jar files
echo "libs.dir=%{_javadir}" >> local_build.properties

# Override 1.5 requirement to work with Java 11
echo "source.level=1.8" >> local_build.properties
echo "target.level=1.8" >> local_build.properties

# Tell colossus some build info that the game will display
mkdir -p build/ant/classes/META-INF
cat <<EOF > build/ant/classes/META-INF/build.properties
release.version=%{version}
svn.revision.max-with-flags=%{rev}
build.timestamp=%{revdate}
username=rpmbuild
EOF

ant jar

# The supplied build.xml adds a classpath to the manifest that needs to
# be removed.

# First remove the existing manifest file
zip -d Colossus.jar META-INF/MANIFEST.MF

# Then put one back without a class path
cat <<EOF > fixup.xml
<?xml version="1.0"?>
<!-- Replace manifest with one without a classpath -->
<project name="Colossus" default="fixup" basedir=".">
  <target name="fixup"
  description="Remove classpath from manifest">
    <jar jarfile="Colossus.jar" update="true">
      <manifest>
        <attribute name="Main-Class"
        value="net.sf.colossus.appmain.Start" /> 
      </manifest>
    </jar>
  </target>
</project>
EOF

ant -f fixup.xml

ant -lib %{_javadir}/jdom.jar javadoc

# Allow for simple command to run colossus
echo -e "#!/bin/sh\njava -cp %{_javadir}/jdom.jar:%{_javadir}/colossus.jar net.sf.colossus.appmain.Start" > %{name}

# Make a .desktop file
cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=Colossus
GenericName=Strategy Game
Comment=Multiplayer turned based fantasy game with AIs available
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 Colossus.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -D -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 644 core/src/main/resource/icons/ColossusIcon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rpv build/ant/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}
chmod -R og=u-w $RPM_BUILD_ROOT%{_javadocdir}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/colossus/feature-requests/225/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">colossus.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fantasy board game with strategic and tactical battle elements</summary>
  <description>
    <p>
      Colossus is a clone of Avalon Hill's "Titan" Board game.
    </p>
    <p>
      It is a fantasy board game where you lead an army of mythological creatures
      against other players.
    </p>
  </description>
  <url type="homepage">http://colossus.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://colossus.sourceforge.net/pics/screenshots/Colossi.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
%{_javadir}/*
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.14.0-29
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.14.0-27
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.14.0-21
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.14.0-20
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.14.0-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sun May 03 2020 Bruno Wolff III <bruno@wolff.to> - 0.14.0-14
- New Fedora release that is hoped will work with java 11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.0-8
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.14.0-3
- Add an AppData file for the software center

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 29 2013 Bruno Wolff III <bruno@wolff.to> - 0.14.0-1
- Upstream release 0.14.0
- Release notes: http://colossus.sourceforge.net/docs/RecentChangesDetails.html

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Bruno Wolff III <bruno@wolff.to> - 0.13.2-4
- Fix hang on applying carry over damage

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 24 2012 Bruno Wolff III <bruno@wolff.to> - 0.13.2-1
- Upstream update to 0.13.2
- Release notes at http://colossus.sourceforge.net/docs/RecentChangesDetails.html
- Some minor fixes and client/server cleanup
- Adjust for extra directory level in source tree

* Sun Feb 05 2012 Bruno Wolff III <bruno@wolff.to> - 0.13.0-1
- Upstream update to 0.13.0
- Release notes at http://colossus.sourceforge.net/docs/RecentChangesDetails.html

* Sat Feb 04 2012 Bruno Wolff III <bruno@wolff.to> - 0.13.0-0.1.rc1
- Upstream RC 1 for 0.13.0
- Release notes at http://colossus.sourceforge.net/public-testing/docs/RecentChangesDetails.html

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-0.2.svn5033
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Bruno Wolff III <bruno@wolff.to> - 0.12.2-0.1.svn5033
- Update to 0.12.2 test release.
- Fix problem running colossus under java 1.7.
- Release notes at http://colossus.sourceforge.net/public-testing/docs/RecentChangesDetails.html

* Sat Mar 05 2011 Bruno Wolff III <bruno@wolff.to> - 0.12.1-1
- Upstream 0.12.1 release with a few minor bug fixes.
- Release notes at http://colossus.sourceforge.net/docs/RecentChangesDetails.html

* Mon Feb 15 2011 Bruno Wolff III <bruno@wolff.to> - 0.12.0-1
- Some minor changes to the dino varient
- Some fixes for playing via the server
- Release notes at http://colossus.sourceforge.net/docs/RecentChangesDetails.html


* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild


* Sun Jan 16 2011 Bruno Wolff III <bruno@wolff.to> - 0.12.0-0.1.beta1
- Rebase to 0.12.0-beta1
- New DinoTitan varient
- http://colossus.sourceforge.net/docs/RecentChangesDetails.html
- Drop gcj building as that is discouraged these days.

* Sat Aug 21 2010 Bruno Wolff III <bruno@wolff.to> - 0.11.0-1
- Rebase to 0.11.0
- Play colored angels and captured legion markers
- Reminders for splitting, moving and recruiting available
- http://colossus.sourceforge.net/docs/RecentChangesDetails.html

* Tue Apr 06 2010 Bruno Wolff III <bruno@wolff.to> - 0.10.3-1
- Rebase to 0.10.3
- UI improvements to prevent accidentally conceding
- Various fixes for playing using the central server
- http://colossus.sourceforge.net/docs/RecentChangesDetails.html

* Sat Feb 06 2010 Bruno Wolff III <bruno@wolff.to> - 0.10.2-1
- Rebase to 0.10.2
- Some useability changes
- A number of fixes and enhancements when using the public game server
- http://colossus.sourceforge.net/docs/RecentChangesDetails.html

* Sat Jan 02 2010 Bruno Wolff III <bruno@wolff.to> - 0.10.1-1
- Rebase to 0.10.1
- Tell the names of logged in users, not only the number
- PGS: Access to userMaps now synchronized to prevent the hang/crash we had once recently
- PGS/WebClient: Most of the text fields now automatically select all text when they gain focus
- Corrected the text "redisplaying last 50 messages" (from 10 10 50)
- Improved text in MasterBoard BottomBar during engagements phase
- Added options for: when my (masterboard) turn starts, beep and/or bring my masterboard to front
- PGS: when lastOnline was changed (user does login or logoff), write back users file to disk
- When webclient user logs out, cancel proposed instant games he created. Also clear running games table and gameHash.

* Sat Dec 26 2009 Bruno Wolff III <bruno@wolff.to> - 0.10.0-1
- Rebase to 0.10.0
- Fixed undo that reblocks a split
- Fix AI crash
- Enable public game server alpha feature
- See http://colossus.sourceforge.net/docs/RecentChangesDetails.html
- Include post release typo fix as a patch

* Fri Oct 16 2009 Bruno Wolff III <bruno@wolff.to> - 0.9.3-1
- Rebase to 0.9.3
- Adjust script for grabbing source to be able to grab from branches
- Fixed 2877055: Some GUI preferences don't load on startup
- Fixed: 2864777 Illegal rangestrike over walls
- Do not choose Experimental AI as "A Random AI" because it occasionally crashes
- Fixed: 2859914 Balrog placement ignores score (aka: Balrog every 300 again, not 50)
- Fixed: 2864790 Aborting load game with remote player - No GetPlayers dialog
- Fixed: 2838276 "my Strike Skill" is wrong for nonnatives to bramble (actually, just improved the dialog to make it's meaning clearer)
- Fixed: 2855208 Balrog exception in V0.9.2 (ConcurrentModificationException)
- See: http://colossus.sourceforge.net/docs/RecentChangesDetails.html

* Sun Sep 06 2009 Bruno Wolff III <bruno@wolff.to> - 0.9.2-1.20090906svn4519
- Rebase to 0.9.2
- See: http://colossus.sourceforge.net/docs/RecentChangesDetails.html
- Fixed: 2835558 WARNING: Could not find creature with name none
- Fixed: 2820231 Illegal rangestrike
- Fixed: 2848651 and 2828028: Legion flyouts
- Fixed: 2837746 Balrog variant: Caretaker counts not reset between games
- Fixed: 2839241 Faulty anchor tags (Crossreference links in docs worked for Inetnet Explorer but not for Netscape)
- Make loading and saving of Balrog games work
- Make Auto Done act properly when there is no Recruit action or undo possible
- Add in save game also a property that tells with which release / revision of Colossus that save game was created.
- Eliminated some race situations in game startup (thread interaction/notifications)

* Wed Aug 19 2009 Bruno Wolff III <bruno@wolff.to> - 0.9.1-2.20090817svn4489
- Fix for desert LOS bug

* Mon Aug 17 2009 Bruno Wolff III <bruno@wolff.to> - 0.9.1-1.20090817svn4489
- Rebase to new public release 0.9.1
- 2 additional bug fixes
- See http://colossus.sourceforge.net/public-build/docs/RecentChangesDetails.html

* Sun Aug 16 2009 Bruno Wolff III <bruno@wolff.to> - 0.9.0-2.20090810svn4482
- Patch 4485 Fix creature info popup
- Patch 4486 Fix Help problem when a logging property is not set

* Mon Aug 10 2009 Bruno Wolff III <bruno@wolff.to> - 0.9.0-1.20090810svn4482
- New public build.
- Upstream is now using real version numbers.

* Sun Jul 26 2009 Bruno Wolff III <bruno@wolff.to> - 0-0.5.20090726svn4462
- Just when I thought it would be safe to rebase, a new public test build was released
- Details at http://colossus.sourceforge.net/public-testing/docs/RecentChangesDetails.html
- Rebase to 4462

* Sat Jul 25 2009 Bruno Wolff III <bruno@wolff.to> - 0-0.4.20090725svn4454
- Fix for off by one roll, movement roll in master board header
- Rebase to 4454

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20090710svn4432
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild


* Sun Jul 12 2009 Bruno Wolff III <bruno@wolff.to> - 0-0.2.20090710svn4432
- A couple of final spec file tweaks based on comments from my sponsor

* Fri Jul 10 2009 Bruno Wolff III <bruno@wolff.to> - 0-0.1.20090710svn4432
- Prerelease snapshot with a public build expected in a week or two
