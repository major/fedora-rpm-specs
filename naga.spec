# Upstream was originally located at http://code.google.com/p/naga/.  The
# primary author later created a github repo and added some documentation, but
# never tagged any releases.  We take his latest github commit.

Name:           naga
Version:        3.0

%global commit  6f1e95ddfdb1aa7719c98168f0a5efc5be191426
%global date    20200930
%global forgeurl https://github.com/lerno/naga

%forgemeta

URL:            %{forgeurl}
Release:        25%{?dist}
Summary:        Simplified Java NIO asynchronous sockets

License:        MIT
Source0:        %{forgesource}
# Fix javadoc errors and warnings
Patch0:         %{name}-javadoc.patch
# Build for Java 1.8 and tell javac that the sources are UTF-8 encoded
Patch1:         %{name}-java18.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  javapackages-tools

Requires:       java-headless
Requires:       javapackages-filesystem

%description
Naga aims to be a very small NIO library that provides a handful of
java classes to wrap the usual Socket and ServerSocket with
asynchronous NIO counterparts (similar to NIO2 planned for Java 1.7).

All of this is driven from a single thread, making it useful for both
client (e.g. allowing I/O to be done in the AWT-thread without any
need for threads) and server programming (1 thread for all connections
instead of 2 threads/connection).

Internally Naga is a straightforward NIO implementation without any
threads or event-queues thrown in, it is "just the NIO-stuff", to let
you build things on top of it.

Naga contains the code needed to get NIO up and running without having
to code partially read buffers and setting various selection key
flags.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       javapackages-filesystem

%description javadoc
This package contains the API documentation for %{name}.

%prep
%forgeautosetup -p1

%build
ant build javadoc

%install
mkdir -p %{buildroot}%{_javadir}
install -D -p -m 644 _DIST/naga-3_0.jar %{buildroot}%{_javadir}/naga.jar
ln -s %{_javadir}/naga.jar %{buildroot}%{_javadir}/naga-3_0.jar

# Javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp _BUILD/docs/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc Echoserver.md Eventmachine.md Gotchas.md PacketReader.md README.md
%license COPYING
%{_javadir}/naga.jar
%{_javadir}/naga-3_0.jar

%files javadoc
%license COPYING
%{_javadocdir}/%{name}

%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.0-20
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.0-19
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Jerry James <loganjerry@gmail.com> - 3.0-15.20200930git6f1e95d
- Bring back to Fedora
- Switch to github repo

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-14.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-13.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-12.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-11.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-10.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-8.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-7.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-6.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-5.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.0-4.82svn
- Use Requires: java-headless rebuild (#1067528)

* Tue Oct 22 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0-3.82svn
- Real .jar file is shipped unversioned (BZ #1022145).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2.82svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.0-1.82svn
- First release.
