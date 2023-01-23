Name:		taggle
Version:	1.0
Release:	26%{?dist}
Summary:	An online french word game

License:	GPLv3+
URL:		http://www.inouire.net/baggle/
Source0:	http://www.inouire.net/fedora/baggle_%{version}_src.tar.gz
Source1:	%{name}.sh
Source2:	%{name}.desktop
Source3:	%{name}.png
Source4:	%{name}-server.sh

BuildArch:	noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:	java-devel >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:	desktop-file-utils

Requires:	java-headless >= 1:1.6.0
Requires:	jpackage-utils

%description
Taggle is an online french word game that lets you play
against your friends. Letters are displayed at random
in a grid and players attempt to find words in sequence
of adjacent letters

%package server
Summary:	Server for %{name}
Requires:	java-headless >= 1:1.6.0
Requires:	jpackage-utils

%description server
The server for the taggle game

%prep
%setup -q -n baggle_%{version}_src

%build
# for legal reason, entirely rename the software
find . -name \*.java | xargs sed -i s/B@ggle/T@ggle/g
find . -name \*.java | xargs sed -i s/b@ggle/t@ggle/g

# Build client
cd baggle_client_%{version}_src
mkdir -p classes/META-INF
javac -encoding utf-8 -d classes boggleclient/Main.java
cp -R icons classes
# fix the class-path-in-manifest rpmlint issue
sed -i '/class-path/I d' MANIFEST.MF
cp MANIFEST.MF classes/META-INF
cd classes
jar cmvf META-INF/MANIFEST.MF %{name}.jar boggleclient/ GUI/ icons/ Thread/
cd ..
mv classes/%{name}.jar ..

# Build server
cd ../baggle_server_%{version}_src
mkdir -p classes/META-INF
javac -encoding utf-8 -d classes boggleserver/Main.java
sed -i '/class-path/I d' MANIFEST.MF
cp MANIFEST.MF classes/META-INF
cp Dico/dico.txt classes/Dico
cd classes
jar cvmf META-INF/MANIFEST.MF %{name}_server.jar boggleserver/ boggle/ Dico/
cd ..
mv classes/%{name}_server.jar ..


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_bindir}
install -D -p %{name}.jar %{buildroot}%{_javadir}
install -D -p -m 0755 %{S:1} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{S:3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications	%{S:2}

install -D -p %{name}_server.jar %{buildroot}%{_javadir}/%{name}-server.jar
install -D -p -m 0755 %{S:4} %{buildroot}%{_bindir}/%{name}-server

%files
%doc baggle_client_%{version}_src/COPYING
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files server
%doc baggle_server_%{version}_src/COPYING
%{_javadir}/%{name}-server.jar
%{_bindir}/%{name}-server

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0-24
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0-23
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0-18
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0-7
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 26 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 1.0-1
- Update sources to 1.0

* Wed Mar 11 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.11-1
- Update sources to 0.11

* Mon Feb 22 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.10-1
- Update sources to 0.10

* Wed Feb 3 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.9-1
- Update sources to 0.9

* Sun Jan 31 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-9
- Rename (again) because of conflict.

* Sun Jan 31 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-8
- Remove a useless Obsoletes/Provides

* Sun Jan 31 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-7
- Fix some issues reported on rhbz

* Tue Jan 26 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-6
- Rename the package for legal reason (rhbz 555187)

* Thu Jan 21 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-5
- Fix the .sh files to pass arguments to the program

* Tue Jan 19 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-4
- Fix buildrequires: a JDK >= 6 is needed to build and run the software.

* Wed Jan 13 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-3
- Combine server spec file

* Wed Jan 13 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-2
- Change logo

* Tue Jan 12 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.8-1
- Update sources to 0.8

* Tue Jan 12 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.7-4
- little cleanup

* Tue Jan 12 2010 Le Coz Florent <louizatakk@fedoraproject.org> - 0.7-3
- Fix encoding

* Thu Dec 24 2009 Le Coz Florent <louizatakk@fedoraproject.org> - 0.7-2
- Add the .desktop file and the icon

* Thu Dec 24 2009 Le Coz Florent <louizatakk@fedoraproject.org> - 0.7-1
- First version from scratch
