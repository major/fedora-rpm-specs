Epoch:          1
Name:           kawa
Version:        3.1.1
Release:        22%{?dist}
Summary:        Scheme programming language
License:        MIT
URL:            https://www.gnu.org/software/kawa/
Source0:        https://ftp.gnu.org/gnu/kawa/kawa-%{version}.tar.gz
# Exclude i686 due to dropping i686 JDKS: https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
ExcludeArch:    i686
BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  groff
BuildRequires:  java-21-openjdk-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  jakarta-servlet
BuildRequires:  texinfo
BuildRequires:  util-linux-ng
BuildRequires:  make
Requires:       jakarta-servlet
Requires:       java-21-openjdk-headless

#Test doesn't pass against Jboss servlet 3.0 till Kawa support Tomcat servlet 4.0
#See https://gitlab.com/kashell/Kawa/issues/41
Patch0:         kawa-3.1.1-disable-servelet-tests.patch
Patch1:         kawa-3.1.1-remove-unfound-javadoc.patch
# Port https://gitlab.com/kashell/Kawa/-/commit/53b9750e1a4707902ecb0743284d667cba944031
# Removed ChangLog modification
Patch2:         kawa-3.1.1-CharSequence-isEmpty-was-added-in-JDK15-so-override.patch
# Port https://gitlab.com/kashell/Kawa/-/commit/42f88a1dcba7264587fc177a2721a012d035ef66
# Removed ChangLog modification
Patch3:         kawa-3.1.1-IString.java-isEmpty-New-method-added-for-Java-15.patch
# Port https://gitlab.com/kashell/Kawa/-/commit/2b9674927ba82847cc830eb05466086d3fdcebd2
# Removed ChangLog modification
Patch4:         kawa-3.1.1-standard-make.java-Explicitly-import-kawa.lang.Recor.patch
# Port https://gitlab.com/kashell/Kawa/-/commit/dd940c01f4ee9dd3263bca844f035bc4a31c76c4
# Removed ChangLog modification
Patch5:         kawa-3.1.1-gnu-.java-kawa-.java-Fix-Java17-depreciation-warning.patch

%description
Kawa is an implementation of the Scheme programming language.  It is
implemented in Java, and compiles Scheme into Java byte-codes.  It
also includes an XQuery implementation, accessible via the qexo
script.

%prep
%autosetup -p1

%build
%configure --enable-kawa-frontend \
           --with-servlet=$(build-classpath jboss-servlet-3.0-api) \
           --with-libtool
export CLASSPATH=$(build-classpath jboss-servlet-3.0-api antlr)
make

# Override the Makefile for generating kawa.1, since it should be
# unformatted man page source.
cp -p doc/kawa.man doc/kawa.1
cp -p doc/qexo.man doc/qexo.1

%install
%make_install
rm -frv %{buildroot}%{_infodir}/dir
mkdir -p %{buildroot}%{_javadir}
mv %{buildroot}%{_datadir}/kawa/lib/kawa.jar %{buildroot}%{_javadir}/kawa.jar
ln -s %{_javadir}/kawa.jar %{buildroot}%{_datadir}/kawa/lib/kawa.jar
cp -p bin/cgi-servlet %{buildroot}%{_bindir}/cgi-servlet
rm -rf %{buildroot}%{_datadir}/kawa/bin

%check
# Current test scripts don't compatible with JAVA11
#make check

%files
%doc AUTHORS ChangeLog NEWS TODO
%license COPYING
%{_bindir}/cgi-servlet
%{_bindir}/kawa
%{_bindir}/qexo
%{_datadir}/java/kawa*.jar
%{_mandir}/man1/*
%{_infodir}/kawa*
#Just links
%{_datadir}/kawa/lib/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 20 2024 Markku Korkeala <markku.korkeala@iki.fi> - 1:3.1.1-21
- Port patches from version control to fix builds on JDK 21
- Closes rhbz#2323985

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1:3.1.1-19
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 17 2022 Markku Korkeala <markku.korkeala@iki.fi> - 1:3.1.1-13
- ExcludeArch i686, #2104066
  https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:3.1.1-12
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Markku Korkeala <markku.korkeala@iki.fi> - 1:3.1.1-10
- Use jdk11.

* Sat Aug 14 2021 Markku Korkeala <markku.korkeala@iki.fi> - 1:3.1.1-9
- Change requires from jboss-servlet to jakarta-servlet, fix #1987612
- Fix rpmlint errors

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 17 2021 Mosaab Alzoubi <moceap[at]hotmail[dot]com> - 1:3.1.1-7
- First success built for Java11

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:3.1.1-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Mosaab Alzoubi <moceap[at]hotmail[dot]com> - 1:3.1.1-2
- Fix notes in #1795884

* Mon Jan 27 2020 Mosaab Alzoubi <moceap[at]hotmail[dot]com> - 1:3.1.1-1
- Pass FTBFS state
- More clear summary
- Update to 3.1.1
- Release Java version
- Use JBoss servlet instead of Tomcat serverlet
- Build against JBossServlet 3.0
- Remove info from Requires
- Use license macro

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:2.0-5
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Mosaab Alzoubi <moceap@hotmail.com> - 1:2.0-2
- Repair unable to launch by reverting fixing #1022128

* Sat Feb 21 2015 Mosaab Alzoubi <moceap@hotmail.com> - 1:2.0-1
- Update to 2.0
- Remove version of Jar file #1022128
- Manual cgi-servlet install

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 26 2014 Christopher Meng <rpm@cicku.me> - 1:1.14-2
- Minor cleanup, explicitly requires java.

* Thu Jun 19 2014 Christopher Meng <rpm@cicku.me> - 1:1.14-1
- Update to 1.14

* Mon Sep 23 2013 Christopher Meng <rpm@cicku.me> - 1:1.13-1
- Update to 1.13

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 23 2011 Alexander Kurtakov <akurtako@redhat.com> 1:1.11-2
- BR java 1.6.0.

* Wed Mar 23 2011 Alexander Kurtakov <akurtako@redhat.com> 1:1.11-1
- Update to new upstream version.
- Drop gcj bits.
- Adapt to current guidelines.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 12 2009 Alex Lancaster <alexlan[AT]fedoraproject org> - 1:1.9.1-7
- Requires in -javadoc subpackage needs epoch

* Mon Nov 10 2008 Anthony Green <green@redhat.com> - 1:1.9.1-6
- The -javadoc package should Require the main package. (#451861)

* Thu Feb 28 2008 Anthony Green <green@redhat.com> - 1:1.9.1-5
- BuildRequire util-linux-ng.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:1.9.1-4
- Autorebuild for GCC 4.3

* Mon Oct 15 2007 Anthony Green <green@redhat.com> - 1:1.9.1-3
- Don't build with icedtea, as it's not portable.
- Build .class files with gcj to work around ecj bug.

* Mon Oct 15 2007 Anthony Green <green@redhat.com> - 1:1.9.1-2
- Oops.  Change %%License to MIT.

* Mon Oct 15 2007 Anthony Green <green@redhat.com> - 1:1.9.1-1
- BuildRequire java-1.7.0-icedtea-devel, since that's what we'll build
  with now.
- Upgrade to 1.9.1.
- Change %%License to BSD.

* Mon Jan 22 2007 Anthony Green <green@redhat.com> - 1:1.9.0-2
- BuildRequire libtool.

* Mon Jan 22 2007 Anthony Green <green@redhat.com> - 1:1.9.0-1
- Upgrade to 1.9.0.

* Thu Oct 05 2006 Anthony Green <green@redhat.com> - 1:1.8-11
- Add antlr to classpath for gjdoc.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.8-10
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Anthony Green <green@redhat.com> - 1:1.8-9
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com> - 1:1.8-8.2
- Rebuild.

* Wed Aug 30 2006 Anthony Green <green@redhat.com> - 1:1.8-8.1
- Rebuild with new aot-compile-rpm

* Mon Jul 31 2006 Anthony Green <green@redhat.com> - 1:1.8-8
- Add ncurses-devel BuildRequires.

* Tue Jul 25 2006 Anthony Green <green@redhat.com> - 1:1.8-7
- Rebuild with new compiler.

* Wed Jul 19 2006 Anthony Green <green@redhat.com> - 1:1.8-6
- Rebuild with new compiler.

* Thu Feb  9 2006 Anthony Green <green@redhat.com> - 1:1.8-5
- Add groff build requirement for man page processing.

* Thu Feb  9 2006 Anthony Green <green@redhat.com> - 1:1.8-4
- Rebuild with new 4.1 compiler (post ABI change).

* Mon Nov 14 2005 Anthony Green <green@redhat.com> - 1:1.8-3
- Rebuild with GCC 4.1.

* Sat Oct  8 2005 Anthony Green <green@redhat.com> - 1:1.8-1
- Upgrade to 1.8.
- Add qexo man page.
- Use an epoch because previous releases had bad names that confuse RPM.  My bad.

* Wed Sep 28 2005 Anthony Green <green@redhat.com> - 1.8rc2-1
- Upgrade to 1.8 rc2.

* Sun Sep 11 2005 Anthony Green <green@redhat.com> - 1.8beta-5
- Remove Requires for realine.  This is handled automagically.
- Remove ldconfig.

* Sun Sep 11 2005 Anthony Green <green@redhat.com> - 1.8beta-4
- Install unformatted man page source.
- Remove BuildRequires groff.
- Force kawa binary to use /usr/bin/java.
- Add javadoc package.
- Happy birthday, spec file!

* Sat Sep 10 2005 Anthony Green <green@redhat.com> - 1.8beta-3
- Add BuildRequires for groff and readline-devel.
- Add Requires for readline.
- Configure with --enable-kawa-frontend.

* Sat Sep 10 2005 Anthony Green <green@redhat.com> - 1.8beta-2
- Add BuildRequires for ant, texinfo and servletapi5.
- Add Requires for servletapi5.
- Add servletapi5.jar to classpath.

* Wed Sep  7 2005 Anthony Green <green@redhat.com> - 1.8beta-1
- Updgrade to 1.8beta

* Wed Sep  7 2005 Anthony Green <green@redhat.com> - 1.7-2
- Build for Fedora Extras.

* Sat Sep 11 2004 Anthony Green <green@spindazzle.org> - 1.7-1
- Initial build.
