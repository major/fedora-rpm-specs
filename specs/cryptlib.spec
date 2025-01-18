%global includetests 1
# 0=no, 1=yes
%global cryptlibdir %{_libdir}/%{name}
%global withpython2 0

Name:       cryptlib
Version:    3.4.8  
Release:    4%{?dist}
Summary:    Security library and toolkit for encryption and authentication services    

License:    Sleepycat and OpenSSL and BSD-3-Clause   
URL:        https://www.cs.auckland.ac.nz/~pgut001/cryptlib      
Source0:    https://senderek.ie/fedora/cl348_fedora.zip      
Source1:    https://senderek.ie/fedora/cl348_fedora.zip.sig
# for security reasons a public signing key should always be stored in distgit
# and never be used with a URL to make impersonation attacks harder
# (verified: https://senderek.ie/keys/codesigningkey)
Source2:    gpgkey-3274CB29956498038A9C874BFBF6E2C28E9C98DD.asc
Source3:    https://senderek.ie/fedora/README-manual
Source4:    https://senderek.ie/fedora/cryptlib-tests.tar.gz
Source5:    https://senderek.ie/fedora/cryptlib-perlfiles.tar.gz
Source6:    https://senderek.ie/fedora/cryptlib-tools.tar.gz
Source7:    https://senderek.ie/fedora/claes
Source8:    https://senderek.ie/fedora/claes.sig

# soname is now libcl.so.3.4
Patch0:     m64patch

ExclusiveArch: x86_64 aarch64 ppc64le riscv64

BuildRequires: gcc 
BuildRequires: libbsd-devel   
BuildRequires: gnupg2
BuildRequires: coreutils
BuildRequires: python3-devel
BuildRequires: python-setuptools
BuildRequires: java-devel
BuildRequires: perl-interpreter
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-Data-Dumper
BuildRequires: perl-ExtUtils-MakeMaker
BuildRequires: make


%if %{withpython2}
    BuildRequires: python2-devel >= 2.7
%endif


%description
Cryptlib is a powerful security toolkit that allows even inexperienced crypto
programmers to easily add encryption and authentication services to their
software. The high-level interface provides anyone with the ability to add
strong security capabilities to an application in as little as half an hour,
without needing to know any of the low-level details that make the encryption
or authentication work.  Because of this, cryptlib dramatically reduces the
cost involved in adding security to new or existing applications.

At the highest level, cryptlib provides implementations of complete security
services such as S/MIME and PGP/OpenPGP secure enveloping, SSL/TLS and
SSH secure sessions, CA services such as CMP, SCEP, RTCS, and OCSP, and other
security operations such as secure time-stamping. Since cryptlib uses
industry-standard X.509, S/MIME, PGP/OpenPGP, and SSH/SSL/TLS data formats,
the resulting encrypted or signed data can be easily transported to other
systems and processed there, and cryptlib itself runs on virtually any
operating system - cryptlib doesn't tie you to a single system.
This allows email, files and EDI transactions to be authenticated with
digital signatures and encrypted in an industry-standard format.


%package devel
Summary:  Cryptlib application development files 
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and code for application development in C (and C++)


%package test
Summary:  Cryptlib test program
Requires: %{name}%{?_isa} = %{version}-%{release}

%description test
Cryptlib test programs for C, Java, Perl and Python3


%package java
Summary:  Cryptlib bindings for Java
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: java-headless

%description java
Cryptlib module for application development in Java


%package javadoc
Summary:  Cryptlib Java documentation
Buildarch : noarch

%description javadoc
Cryptlib Javadoc information

%if %{withpython2}
    %package python2
    Summary:  Cryptlib bindings for python2
    Group:    System Environment/Libraries
    Requires: %{name}%{?_isa} = %{version}-%{release}
    Requires: python2 >= 2.7
    %description python2
    Cryptlib module for application development in Python 2
%endif

%package python3
Summary:  Cryptlib bindings for python3
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: python3 >= 3.5  

%description python3
Cryptlib module for application development in Python3

%package perl
Summary:  Cryptlib bindings for perl
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: man

%description perl
Cryptlib module for application development in Perl

%package tools
Summary:  Collection of stand-alone programs that use Cryptlib
Requires: python3 >= 3.5
Requires: man
Requires: %{name}%-python3

%description tools
Collection of stand-alone programs that use Cryptlib


%prep
# source code signature check with GnuPG
KEYRING=$(echo %{SOURCE2})
KEYRING=${KEYRING%%.asc}.gpg
mkdir -p .gnupg
gpg2 --homedir .gnupg --no-default-keyring --quiet --yes --output $KEYRING --dearmor  %{SOURCE2}
gpg2 --homedir .gnupg --no-default-keyring --keyring $KEYRING --verify %{SOURCE1} %{SOURCE0}
gpg2 --homedir .gnupg --no-default-keyring --keyring $KEYRING --verify %{SOURCE8} %{SOURCE7}

rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
/usr/bin/unzip -a %{SOURCE0}

%patch 0 -p1

# enable ADDFLAGS
sed -i '97s/-I./-I. \$(ADDFLAGS)/' makefile
# enable JAVA in config
sed -i 's/\/\* #define USE_JAVA \*\// #define USE_JAVA /' misc/config.h


# remove pre-build jar file
rm %{_builddir}/%{name}-%{version}/bindings/cryptlib.jar
# adapt perl files in bindings
cd %{_builddir}/%{name}-%{version}/bindings
/usr/bin/tar xpzf %{SOURCE5}

%build
cd %{name}-%{version}
chmod +x tools/mkhdr.sh

tools/mkhdr.sh

# rename cryptlib symbols that may collide with openssl symbols
chmod +x tools/rename.sh
tools/rename.sh
# build java bindings
cp /etc/alternatives/java_sdk/include/jni.h .
cp /etc/alternatives/java_sdk/include/linux/jni_md.h .

make clean
make shared  ADDFLAGS="%{optflags}"
ln -s libcl.so.3.4.8 libcl.so
ln -s libcl.so libcl.so.3.4
make stestlib  ADDFLAGS="%{optflags}"

# build python modules
cd bindings
%if %{withpython2}
     python2 setup.py build
%endif
python3 setup.py build

# build javadoc
mkdir javadoc
cd javadoc
jar -xf ../cryptlib.jar
javadoc cryptlib


%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp %{_builddir}/%{name}-%{version}/libcl.so.3.4.8 %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
ln -s libcl.so.3.4.8 libcl.so.3.4
ln -s libcl.so.3.4 libcl.so

# install header files
mkdir -p %{buildroot}/%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/crypt.h %{buildroot}%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/cryptkrn.h %{buildroot}%{_includedir}/%{name}
cp %{_builddir}/%{name}-%{version}/cryptlib.h %{buildroot}%{_includedir}/%{name}

# add Java bindings
mkdir -p %{buildroot}/%{cryptlibdir}/java
mkdir -p %{buildroot}/usr/lib/java
cp %{_builddir}/%{name}-%{version}/bindings/cryptlib.jar %{buildroot}/usr/lib/java

# install docs
cp %{_builddir}/%{name}-%{version}/COPYING %{buildroot}%{_datadir}/licenses/%{name}
cp %{_builddir}/%{name}-%{version}/README %{buildroot}%{_docdir}/%{name}/README
echo "No tests performed." > %{_builddir}/%{name}-%{version}/stestlib.log
cp %{_builddir}/%{name}-%{version}/stestlib.log %{buildroot}%{_docdir}/%{name}/stestlib.log
cp %{SOURCE3} %{buildroot}%{_docdir}/%{name}

# install javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
rm -rf %{_builddir}/%{name}-%{version}/bindings/javadoc/META-INF
cp -r %{_builddir}/%{name}-%{version}/bindings/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%if %{withpython2}
     # install python2 module
     mkdir -p %{buildroot}%{python2_sitelib}
     cp %{_builddir}/%{name}-%{version}/bindings/build/lib.linux-*%{python2_version}/cryptlib_py.so %{buildroot}%{python2_sitelib}
%endif

# install python3 module
mkdir -p %{buildroot}%{python3_sitelib}
# cp %{_builddir}/%{name}-%{version}/bindings/build/lib.linux-*%{python3_version}/cryptlib_py%{python3_ext_suffix} %{buildroot}%{python3_sitelib}/cryptlib_py.so
cp %{_builddir}/%{name}-%{version}/bindings/build/lib.linux-*/cryptlib_py%{python3_ext_suffix} %{buildroot}%{python3_sitelib}/cryptlib_py.so

# install Perl module
mkdir -p %{buildroot}/usr/local/lib64
mkdir -p %{buildroot}%{_libdir}/perl5
mkdir -p %{buildroot}%{_mandir}/man3
cd %{_builddir}/%{name}-%{version}/bindings
mkdir -p %{_builddir}/include
cp ../cryptlib.h %{_builddir}/include
cp ../tools/GenPerl.pl .
export PERL_CRYPT_LIB_HEADER=%{_builddir}/include/cryptlib.h
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
sed -i '/LDLOADLIBS = /s/thread/thread -L.. -lcl/' Makefile
make
make pure_install DESTDIR=%{buildroot}
# clean the install
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name 'PerlCryptLib.so' -exec chmod 0755 {} \;

# install test programs
cp %{_builddir}/%{name}-%{version}/stestlib %{buildroot}%{cryptlibdir}
cp -r %{_builddir}/%{name}-%{version}/test %{buildroot}%{cryptlibdir}/test
# remove all c code from the test directory
rm -rf $(find %{buildroot}%{cryptlibdir}/test -name "*.c")

# extract test files
cd %{buildroot}%{cryptlibdir}
tar xpzf %{SOURCE4} 

# install cryptlib tools 
mkdir -p %{buildroot}%{cryptlibdir}/tools
cd %{buildroot}%{cryptlibdir}/tools
tar xpzf %{SOURCE6} 
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_bindir}
cp %{SOURCE7} %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/clsha1 %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/clsha2 %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/clkeys %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/clsmime %{buildroot}%{_bindir}
cp /%{buildroot}%{cryptlibdir}/tools/man/clsha1.1 %{buildroot}%{_mandir}/man1
cp /%{buildroot}%{cryptlibdir}/tools/man/clsha2.1 %{buildroot}%{_mandir}/man1
cp /%{buildroot}%{cryptlibdir}/tools/man/claes.1  %{buildroot}%{_mandir}/man1
cp /%{buildroot}%{cryptlibdir}/tools/man/clkeys.1 %{buildroot}%{_mandir}/man1
cp /%{buildroot}%{cryptlibdir}/tools/man/clsmime.1 %{buildroot}%{_mandir}/man1

%check
# checks are performed after install
# in KOJI tests must be disabled as there is no networking
%if %{includetests}
     cd %{_builddir}/%{name}-%{version}
     export LD_LIBRARY_PATH=.
     echo "Running tests on the cryptlib library. This will take a few minutes."
     cp %{buildroot}%{cryptlibdir}/c/cryptlib-test.c .
     sed -i '41s/<cryptlib\/cryptlib.h>/\".\/cryptlib.h\"/' cryptlib-test.c
     gcc  -o cryptlib-test cryptlib-test.c -L. libcl.so.3.4.8
     ./cryptlib-test
%endif


%ldconfig_scriptlets


%files
%{_libdir}/libcl.so.3.4.8
%{_libdir}/libcl.so.3.4
%{_libdir}/libcl.so

%license   %{_datadir}/licenses/%{name}/COPYING
%doc       %{_docdir}/%{name}/README
%doc       %{_docdir}/%{name}/stestlib.log
%doc       %{_docdir}/%{name}/README-manual


%files devel
%{_libdir}/libcl.so
%{_includedir}/%{name}/crypt.h
%{_includedir}/%{name}/cryptkrn.h
%{_includedir}/%{name}/cryptlib.h

%files java
/usr/lib/java/cryptlib.jar

%files javadoc
%{_javadocdir}/%{name}

%if %{withpython2}
     %files python2
     %{python2_sitelib}/cryptlib_py.so
%endif

%files python3
%{python3_sitelib}/cryptlib_py.so

%files perl
%{_libdir}/perl5
%{_mandir}/man3/PerlCryptLib.3pm.gz

%files test
%{cryptlibdir}

%files tools
%{_bindir}/clsha1
%{_bindir}/clsha2
%{_bindir}/claes
%{_bindir}/clkeys
%{_bindir}/clsmime
%{_mandir}/man1/clsha2.1.gz
%{_mandir}/man1/clsha1.1.gz
%{_mandir}/man1/claes.1.gz
%{_mandir}/man1/clkeys.1.gz
%{_mandir}/man1/clsmime.1.gz



%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Ralf Senderek <innovation@senderek.ie>  3.4.8-3
- add BSD-3-Clause to License tag 

* Thu Dec 19 2024 Ralf Senderek <innovation@senderek.ie>  3.4.8-2
- add test programs for claes, clkeys and clsmime and riscv64 support

* Wed Dec 4 2024 Ralf Senderek <innovation@senderek.ie>  3.4.8-1
- update to version 3.4.8

* Fri Nov 29 2024 Ralf Senderek <innovation@senderek.ie>  3.4.7-9
- update MIN_TIME_VALUE in misc/consts.h

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.7-7
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.4.7-6
- Rebuilt for Python 3.13

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.4.7-5
- Rebuilt for java-21-openjdk as system jdk

* Sun Feb 25 2024 Ralf Senderek <innovation@senderek.ie> - 3.4.7-4
- Add clsmime to cryptlib-tools

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Ralf Senderek <innovation@senderek.ie> - 3.4.7-1
- Update to version 3.4.7

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.6-18
- Perl 5.38 rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.4.6-17
- Rebuilt for Python 3.12

* Wed Apr 05 2023 Ralf Senderek <innovation@senderek.ie> - 3.4.6-16
- Remove obsolete gcc flags

* Wed Apr 05 2023 Ralf Senderek <innovation@senderek.ie> - 3.4.6-15
- Resolve Bug RHBZ#2182688

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Ralf Senderek <innovation@senderek.ie> - 3.4.6-13
- Resolve Bug #2155050 python 3.12 setup.py

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 3.4.6-11
- Rebuilt for Python 3.11

* Wed Jun 15 2022 Ralf Senderek <innovation@senderek.ie> - 3.4.6-10
- Add claes ver 1.0 to cryptlib-tools

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.4.6-9
- Rebuilt for Python 3.11

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.6-8
- Perl 5.36 rebuild
* Sat Mar 05 2022 Ralf Senderek <innovation@senderek.ie> - 3.4.6-7
- Add subpackage cryptlib-tools

* Fri Mar 04 2022 Ralf Senderek <innovation@senderek.ie> - 3.4.6-6
- Define -march=x86-64

* Sat Feb 26 2022 Ralf Senderek <innovation@senderek.ie> - 3.4.6-5
- Correct date in test/cert.c

* Thu Feb 17 2022 Ralf Senderek <innovation@senderek.ie> - 3.4.6-4
- Drop i686

* Fri Feb 11 2022 Ralf Senderek <innovation@senderek.ie> - 3.4.5-22
- Update patches for version 3.4.5
	
* Fri Feb 11 2022 Ralf Senderek <innovation@senderek.ie> - 3.4.5-21
- Rebuilt for java-17-openjdk as system jdk

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.4.6-3
- Rebuilt for java-17-openjdk as system jdk

* Tue Feb 01 2022 Ralf Senderek <innovation@senderek.ie>  - 3.4.6-2
- 3.4.6 with flagspatch

* Sun Jan 30 2022 Ralf Senderek <innovation@senderek.ie>  - 3.4.6-1
- update SCM to version 3.4.6, new test-files

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 24 2021 Ralf Senderek <innovation@senderek.ie> - 3.4.5-18
- Fix pthread issue (RHBZ #1974247) 

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.4.5-17
- Rebuilt for Python 3.10

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.5-16
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Ralf Senderek <innovation@senderek.ie> - 3.4.5-14
- Fix Python Upstream Architecture Names for powerpc architecture 

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.4.5-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.5-11
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-10
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Ralf Senderek <innovation@senderek.ie> - 3.4.5-8
- gcc-10: remove deprecated flag -mcpu (RHBZ #1793394)

* Sat Nov 23 2019 Ralf Senderek <innovation@senderek.ie> - 3.4.5-7
- Enable gcc versions > 9

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.4.5-6
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.5-4
- Perl 5.30 rebuild

* Fri May 24 2019 Ralf Senderek <innovation@senderek.ie> - 3.4.5-3
- Update Perl installation paths

* Mon Mar 18 2019 Ralf Senderek <innovation@senderek.ie> - 3.4.5-2
- Removing obsolete conflict with beignet

* Sun Mar 10 2019 Ralf Senderek <innovation@senderek.ie> - 3.4.5-1
- Update to version 3.4.5 and porting to python3 only

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Ralf Senderek <innovation@senderek.ie> - 3.4.4-11
- Remove python2 module (RHBZ #1634602)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Petr Pisar <ppisar@redhat.com> - 3.4.4-9
- Perl 5.28 rebuild

* Wed Jul 04 2018 Ralf Senderek <innovation@senderek.ie> - 3.4.4-8
- Force use of python2 in mkhdr.sh

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 3.4.4-7
- Perl 5.28 rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.4-6
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.4.4-5
- Rebuilt for Python 3.7

* Sun May 27 2018 Ralf Senderek <innovation@senderek.ie> - 3.4.4-4
- Fix Java jar path

* Fri Apr 20 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 3.4.4-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Ralf Senderek <innovation@senderek.ie> - 3.4.4-1
- Update to version 3.4.4

* Wed Aug 09 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3.1-7
- update configuration code for powerpc64

* Wed Aug 02 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3.1-6
- include ppc64/ppc64le and introducing the new python3 module

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 05 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3.1-3
- include aarch64 and exclude ppc64 

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.3.1-2
- Perl 5.26 rebuild

* Sat Feb 11 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3.1-1
- update to version 3.4.3.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Senderek Web Security <innovation@senderek.ie> - 3.4.3-9
- compile with gcc-7.0 and -march=native

* Tue Jul 26 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-8
- change license tag (RHBZ #1352406)
- rename symbols that collide with openssl (RHBZ #1352404)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 16 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-6
- Remove perl-generators for epel7
- Remove python3 script from test subpackage (fixes RHBZ #1347294)

* Tue Jun 14 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-5
- Fix source locations
- Clean up perl file installation
- Fix python3 module code in spec file

* Thu Jun 9 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-4
- Removed the doc subpackage

* Mon Jun 6 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-3
- Fixed Java subpackage dependency
- Made devel arch specific

* Fri Jun 3 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-2
- Added javadoc subpackage and made docs noarch
- Added a perl subpackage
- Modified native stestlib program with two tests disabled
  (testSessionSSH and testSessionSSHClientCert)

* Wed Jun 1 2016 Senderek Web Security <innovation@senderek.ie> - 3.4.3-1
- Added python2/python3 subpackage
- Source code signature check with GnuPG enabled

* Sun May 29 2016 Senderek Web Security <innovation@senderek.ie> - 3.4-2
- Added doc and java subpackage

* Fri May 27 2016 Senderek Web Security <innovation@senderek.ie> - 3.4-1
- Initial version of the rpm package build
