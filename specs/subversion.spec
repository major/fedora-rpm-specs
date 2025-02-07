# Disable to avoid all the test suites
%bcond tests 1

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

%bcond bdb %[0%{?fedora} < 33 && 0%{?rhel} < 9]
# Python 2 for F<32, Python 3 for F>=32 and RHEL>=9
%bcond python2 %[0%{?fedora} < 32 && 0%{?rhel} < 9]
%bcond python3 %{without python2}
%bcond pyswig 1
# Java, Ruby bindings and KWallet are not enabled on RHEL
%bcond kwallet %[0%{?fedora} != 0]
%bcond ruby %[0%{?fedora} != 0]
%ifarch %{java_arches}
%bcond java %[0%{?fedora} != 0]
%else
%bcond java 0
%endif

%if %{with python2} == %{with python3}
%error Pick exactly one Python version
%endif

# set JDK path to build javahl; default for JPackage
%define jdk_path /usr/lib/jvm/java

%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}

%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%if %{with python2}
%global svn_python_sitearch %{python2_sitearch}
%global svn_python %{__python2}
%global svn_python_br python2-devel
%else
%global svn_python_sitearch %{python3_sitearch}
%global svn_python %{__python3}
%global svn_python_br python3-devel
%endif

Summary: A Modern Concurrent Version Control System
Name: subversion
Version: 1.14.5
Release: 7%{?dist}
License: Apache-2.0
URL: https://subversion.apache.org/
Source0: https://downloads.apache.org/subversion/subversion-%{version}.tar.bz2
Source1: subversion.conf
Source3: filter-requires.sh
Source4: http://www.xsteve.at/prg/emacs/psvn.el
Source5: psvn-init.el
Source6: svnserve.service
Source7: svnserve.tmpfiles
Source8: svnserve.sysconf
Patch1: subversion-1.12.0-linking.patch
Patch2: subversion-1.14.0-testwarn.patch
Patch3: subversion-1.14.2-soversion.patch
Patch4: subversion-1.8.0-rubybind.patch
Patch5: subversion-1.8.5-swigplWall.patch
Patch6: subversion-1.14.1-testnomagic.patch
Patch7: subversion-1.14.2-modsyms.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2255746
Patch8: subversion-1.14.3-zlib-ng.patch
Patch9: subversion-1.14.5-progenv.patch
BuildRequires: make
BuildRequires: libxcrypt-devel
BuildRequires: autoconf, libtool, texinfo, which, gcc, gcc-c++
BuildRequires: swig >= 1.3.24, gettext
%if %{with bdb}
BuildRequires: libdb-devel >= 4.1.25
%endif
BuildRequires: %{svn_python_br}
BuildRequires: apr-devel >= 1.5.0, apr-util-devel >= 1.3.0
BuildRequires: libserf-devel >= 1.3.0, cyrus-sasl-devel
BuildRequires: sqlite-devel >= 3.4.0, file-devel, systemd-units
BuildRequires: utf8proc-devel, lz4-devel
# Any apr-util crypto backend needed
BuildRequires: apr-util-openssl
# For systemctl scriptlets
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Provides: svn = %{version}-%{release}
Requires: subversion-libs%{?_isa} = %{version}-%{release}

%define __perl_requires %{SOURCE3}

# Put Python bindings in site-packages
%define swigdirs swig_pydir=%{svn_python_sitearch}/libsvn swig_pydir_extra=%{svn_python_sitearch}/svn

%description
Subversion is a concurrent version control system which enables one
or more users to collaborate in developing and maintaining a
hierarchy of files and directories while keeping a history of all
changes.  Subversion only stores the differences between versions,
instead of every complete file.  Subversion is intended to be a
compelling replacement for CVS.

%package libs
Summary: Libraries for Subversion Version Control system
# APR 1.3.x interfaces are required
Conflicts: apr%{?_isa} < 1.5.0
# Enforced at run-time by ra_serf
Conflicts: libserf%{?_isa} < 1.3.0

%description libs
The subversion-libs package includes the essential shared libraries
used by the Subversion version control tools.

%if %{with python2} && %{with pyswig}
%package -n python2-subversion
%{?python_provide:%python_provide python2-subversion}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
BuildRequires: python2-devel
Summary: Python bindings for Subversion Version Control system

%description -n python2-subversion
The python2-subversion package includes the Python 2.x bindings to the
Subversion libraries.
%endif
%if %{with python3} && %{with pyswig}
%package -n python3-subversion
%{?python_provide:%python_provide python3-subversion}
Summary: Python bindings for Subversion Version Control system
BuildRequires: python3-devel py3c-devel
BuildRequires: (python3-setuptools if python3-devel >= 3.12)
Requires: subversion-libs%{?_isa} = %{version}-%{release}

%description -n python3-subversion
The python3-subversion package includes the Python 3.x bindings to the
Subversion libraries.
%endif

%package devel
Summary: Development package for the Subversion libraries
Requires: subversion-libs%{?_isa} = %{version}-%{release}
Requires: apr-devel%{?_isa}, apr-util-devel%{?_isa}

%description devel
The subversion-devel package includes the libraries and include files
for developers interacting with the subversion package.

%package gnome
Summary: GNOME Keyring support for Subversion
Requires: subversion-libs%{?_isa} = %{version}-%{release}
BuildRequires: dbus-devel, libsecret-devel

%description gnome
The subversion-gnome package adds support for storing Subversion
passwords in the GNOME Keyring.

%if %{with kwallet}
%package kde
Summary: KDE Wallet support for Subversion
Requires: subversion-libs%{?_isa} = %{version}-%{release}
BuildRequires: qt5-qtbase-devel >= 5.0.0, kf5-kwallet-devel, kf5-ki18n-devel
BuildRequires: kf5-kcoreaddons-devel

%description kde
The subversion-kde package adds support for storing Subversion
passwords in the KDE Wallet.
%endif

%package -n mod_dav_svn
Summary: Apache httpd module for Subversion server
Requires: httpd-mmn = %{_httpd_mmn}
Requires: subversion-libs%{?_isa} = %{version}-%{release}
BuildRequires: httpd-devel >= 2.0.45

%description -n mod_dav_svn
The mod_dav_svn package allows access to a Subversion repository
using HTTP, via the Apache httpd server.

%package perl
Summary: Perl bindings to the Subversion libraries
BuildRequires: perl-devel >= 2:5.8.0, perl-generators, perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More), perl(ExtUtils::Embed)
Requires: subversion-libs%{?_isa} = %{version}-%{release}

%description perl
This package includes the Perl bindings to the Subversion libraries.

%if %{with java}
%package javahl
Summary: JNI bindings to the Subversion libraries
Requires: subversion = %{version}-%{release}
BuildRequires: java-devel
# JAR repacking requires both zip and unzip in the buildroot
BuildRequires: zip, unzip
# For the tests
BuildRequires: junit
BuildArch: noarch

%description javahl
This package includes the JNI bindings to the Subversion libraries.
%endif

%if %{with ruby}
%package ruby
Summary: Ruby bindings to the Subversion libraries
BuildRequires: ruby-devel >= 1.9.1, ruby >= 1.9.1
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(csv)
Requires: subversion-libs%{?_isa} = %{version}-%{release}
Requires: rubygem(csv)
Conflicts: ruby-libs%{?_isa} < 1.8.2

%description ruby
This package includes the Ruby bindings to the Subversion libraries.
%endif

%package tools
Summary: Supplementary tools for Subversion
Requires: subversion-libs%{?_isa} = %{version}-%{release}

%description tools
This package includes supplementary tools for use with Subversion.

%prep
%autosetup -p1 -S gendiff

:
: === Building:
: === Python3=%{with python3} Python2=%{with python2} PySwig=%{with pyswig}
: === Java=%{with java} Ruby=%{with ruby}
: === BDB=%{with bdb} Tests=%{with tests} KWallet=%{with kwallet}
:

%build
# Regenerate the buildsystem, so that any patches applied to
# configure, swig bindings etc take effect.
mv build-outputs.mk build-outputs.mk.old
export PYTHON=%{svn_python}

### Force regeneration of swig bindings with the buildroot's SWIG.
# Generated files depend on the build/generator/swig/*.py which
# generates them, so when autogen-standalone.mk's autogen-swig target
# is run by autogen.sh it will regenerate them:
touch build/generator/swig/*.py

### Regenerate everything:
# This PATH order makes the fugly test for libtoolize work...
PATH=/usr/bin:$PATH ./autogen.sh --release

# fix shebang lines, #111498
perl -pi -e 's|/usr/bin/env perl -w|/usr/bin/perl -w|' tools/hook-scripts/*.pl.in
# fix python executable
perl -pi -e 's|/usr/bin/env python.*|%{svn_python}|' subversion/tests/cmdline/svneditor.py

# override weird -shrext from ruby
export svn_cv_ruby_link="%{__cc} -shared"
export svn_cv_ruby_sitedir_libsuffix=""
export svn_cv_ruby_sitedir_archsuffix=""
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
# Fix include path for ruby2.7
export svn_cv_ruby_includes="-I%{_includedir}"
%endif

#export EXTRA_CFLAGS="$RPM_OPT_FLAGS -DSVN_SQLITE_MIN_VERSION_NUMBER=3007012 \
#       -DSVN_SQLITE_MIN_VERSION=\\\"3.7.12\\\""
export APACHE_LDFLAGS="-Wl,-z,relro,-z,now"
export CC=gcc CXX=g++ JAVA_HOME=%{jdk_path}

export CFLAGS="%{build_cflags} -Wno-error=incompatible-pointer-types"
# neccessary for libtool compilation of bindings
export LT_CFLAGS="$CFLAGS"

%configure --with-apr=%{_prefix} --with-apr-util=%{_prefix} \
        --disable-debug \
        --with-swig --with-serf=%{_prefix} \
        --with-ruby-sitedir=%{ruby_vendorarchdir} \
        --with-ruby-test-verbose=verbose \
        --with-apxs=%{_httpd_apxs} --disable-mod-activation \
        --enable-plaintext-password-storage \
        --with-apache-libexecdir=%{_httpd_moddir} \
        --disable-static --with-sasl=%{_prefix} \
        --with-libmagic=%{_prefix} \
        --with-gnome-keyring \
%if %{with java}
        --enable-javahl \
        --with-junit=%{_prefix}/share/java/junit.jar \
%endif
%if %{with kwallet}
        --with-kwallet=%{_includedir}:%{_libdir} \
%endif
%if %{with bdb}
        --with-berkeley-db \
%else
        --without-berkeley-db \
%endif
        || (cat config.log; exit 1)
make %{?_smp_mflags} all tools
%if %{with pyswig}
make swig-py swig-py-lib %{swigdirs}
%endif
make swig-pl swig-pl-lib
%if %{with ruby}
make swig-rb swig-rb-lib
%endif
%if %{with java}
# javahl-javah does not parallel-make with javahl
#make javahl-java javahl-javah
make javahl
%endif

%install
make install DESTDIR=$RPM_BUILD_ROOT
%if %{with pyswig}
make install-swig-py %{swigdirs} DESTDIR=$RPM_BUILD_ROOT
%endif

make install-swig-pl-lib DESTDIR=$RPM_BUILD_ROOT
%if %{with ruby}
make install-swig-rb DESTDIR=$RPM_BUILD_ROOT
%endif

make pure_vendor_install -C subversion/bindings/swig/perl/native \
        PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with java}
make install-javahl-java install-javahl-lib javahl_javadir=%{_javadir} DESTDIR=$RPM_BUILD_ROOT
%endif

install -m 755 -d ${RPM_BUILD_ROOT}%{_sysconfdir}/subversion

mkdir -p ${RPM_BUILD_ROOT}{%{_httpd_modconfdir},%{_httpd_confdir}}

%if "%{_httpd_modconfdir}" == "%{_httpd_confdir}"
# httpd <= 2.2.x
install -p -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_httpd_confdir}
%else
sed -n /^LoadModule/p %{SOURCE1} > 10-subversion.conf
sed    /^LoadModule/d %{SOURCE1} > example.conf
touch -r %{SOURCE1} 10-subversion.conf example.conf
install -p -m 644 10-subversion.conf ${RPM_BUILD_ROOT}%{_httpd_modconfdir}
%endif

# Remove unpackaged files
rm -rf ${RPM_BUILD_ROOT}%{_includedir}/subversion-*/*.txt \
       ${RPM_BUILD_ROOT}%{svn_python_sitearch}/*/*.{a,la}

# The SVN build system is broken w.r.t. DSO support; it treats
# normal libraries as DSOs and puts them in $libdir, whereas they
# should go in some subdir somewhere, and be linked using -module,
# etc.  So, forcibly nuke the .so's for libsvn_auth_{gnome,kde},
# since nothing should ever link against them directly.
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libsvn_auth_*.so

# remove stuff produced with Perl modules
find $RPM_BUILD_ROOT -type f \
    -a \( -name .packlist -o \( -name '*.bs' -a -empty \) \) \
    -print0 | xargs -0 rm -f

# make Perl modules writable so they get stripped
find $RPM_BUILD_ROOT%{_libdir}/perl5 -type f -perm 555 -print0 |
        xargs -0 chmod 755

# unnecessary libraries for swig bindings
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libsvn_swig_*.{so,la,a}

# Remove unnecessary ruby libraries
rm -f ${RPM_BUILD_ROOT}%{ruby_vendorarchdir}/svn/ext/*.*a

# Trim what goes in docdir
rm -rvf tools/*/*.in tools/hook-scripts/mailer/tests

# Install psvn for emacs and xemacs
for f in emacs/site-lisp xemacs/site-packages/lisp; do
  install -m 755 -d ${RPM_BUILD_ROOT}%{_datadir}/$f
  install -m 644 $RPM_SOURCE_DIR/psvn.el ${RPM_BUILD_ROOT}%{_datadir}/$f
done

install -m 644 $RPM_SOURCE_DIR/psvn-init.el \
        ${RPM_BUILD_ROOT}%{_datadir}/emacs/site-lisp

# Rename authz_svn INSTALL doc for docdir
ln -f subversion/mod_authz_svn/INSTALL mod_authz_svn-INSTALL

# Trim exported dependencies to APR libraries only:
sed -i "/^dependency_libs/{
     s, -l[^ ']*, ,g;
     s, -L[^ ']*, ,g;
     s,%{_libdir}/lib[^a][^p][^r][^ ']*.la, ,g;
     }"  $RPM_BUILD_ROOT%{_libdir}/*.la

# Trim libdir in pkgconfig files to avoid multilib conflicts
sed -i '/^libdir=/d' $RPM_BUILD_ROOT%{_datadir}/pkgconfig/libsvn*.pc

# Install bash completion
install -Dpm 644 tools/client-side/bash_completion \
        $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/svn
for comp in svnadmin svndumpfilter svnlook svnsync svnversion; do
    ln -s svn \
        $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/${comp}
done

# Install svnserve bits
mkdir -p %{buildroot}%{_unitdir} \
      %{buildroot}/run/svnserve \
      %{buildroot}%{_prefix}/lib/tmpfiles.d \
      %{buildroot}%{_sysconfdir}/sysconfig

install -p -m 644 $RPM_SOURCE_DIR/svnserve.service \
        %{buildroot}%{_unitdir}/svnserve.service
install -p -m 644 $RPM_SOURCE_DIR/svnserve.tmpfiles \
        %{buildroot}%{_prefix}/lib/tmpfiles.d/svnserve.conf
install -p -m 644 $RPM_SOURCE_DIR/svnserve.sysconf \
        %{buildroot}%{_sysconfdir}/sysconfig/svnserve

# Install tools ex diff*, x509-parser
make install-tools DESTDIR=$RPM_BUILD_ROOT toolsdir=%{_bindir}
rm -f $RPM_BUILD_ROOT%{_bindir}/diff* $RPM_BUILD_ROOT%{_bindir}/x509-parser

# Don't add spurious dependency in libserf-devel
sed -i "/^Requires.private/s, serf-1, ," \
    $RPM_BUILD_ROOT%{_datadir}/pkgconfig/libsvn_ra_serf.pc

# Make svnauthz-validate a symlink
rm $RPM_BUILD_ROOT%{_bindir}/svnauthz-validate
ln -s svnauthz $RPM_BUILD_ROOT%{_bindir}/svnauthz-validate

for f in svn-populate-node-origins-index fsfs-access-map \
    svnauthz svnauthz-validate svnmucc svnraisetreeconflict svnbench \
    svn-mergeinfo-normalizer fsfs-stats svnmover svnconflict; do
    echo %{_bindir}/$f
    if test -f $RPM_BUILD_ROOT%{_mandir}/man?/${f}.*; then
       echo %{_mandir}/man?/${f}.*
    fi
done | tee tools.files | sed 's/^/%%exclude /' > exclude.tools.files

%find_lang %{name}

cat %{name}.lang exclude.tools.files >> %{name}.files

%if %{with tests}
%check
export LANG=C LC_ALL=C
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
export MALLOC_PERTURB_=171 MALLOC_CHECK_=3
export LIBC_FATAL_STDERR_=1
export PYTHON=%{svn_python}
if ! make check CLEANUP=yes PARALLEL=${RPM_BUILD_NCPUS}; then
   : Test suite failure.
   cat fails.log
   cat tests.log
   exit 1
fi
if ! make check-swig-pl; then
   : Swig test failure.
   exit 1
fi
%if %{with pyswig}
if ! make check-swig-py; then
   : Python swig test failure.
   exit 1
fi
%endif
%if %{with ruby}
if ! make check-swig-rb; then
   : Ruby swig test failure.
   exit 1
fi
%endif
%if %{with java}
make check-javahl
%endif
%endif

%post
%systemd_post svnserve.service

%preun
%systemd_preun svnserve.service

%postun
%systemd_postun_with_restart svnserve.service

%ldconfig_scriptlets libs

%ldconfig_scriptlets perl

%ldconfig_scriptlets ruby

%if %{with java}
%ldconfig_scriptlets javahl
%endif

%files -f %{name}.files
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%doc BUGS COMMITTERS INSTALL README CHANGES
%doc mod_authz_svn-INSTALL
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/emacs/site-lisp/*.el
%{_datadir}/xemacs/site-packages/lisp/*.el
%{_datadir}/bash-completion/
%config(noreplace) %{_sysconfdir}/sysconfig/svnserve
%dir %{_sysconfdir}/subversion
%exclude %{_mandir}/man*/*::*
%{_unitdir}/*.service
%attr(0700,root,root) %dir /run/svnserve
%{_prefix}/lib/tmpfiles.d/svnserve.conf

%files tools -f tools.files
%doc tools/hook-scripts tools/backup tools/examples tools/xslt
%if %{with bdb}
%doc tools/bdb
%endif

%files libs
%{!?_licensedir:%global license %%doc}
%license LICENSE NOTICE
%{_libdir}/libsvn*.so.*
%exclude %{_libdir}/libsvn_swig_perl*
%exclude %{_libdir}/libsvn_swig_ruby*
%if %{with java}
%{_libdir}/libsvnjavahl-*.so
%endif
%if %{with kwallet}
%exclude %{_libdir}/libsvn_auth_kwallet*
%endif
%exclude %{_libdir}/libsvn_auth_gnome*

%if %{with python2} && %{with pyswig}
%files -n python2-subversion
%{python2_sitearch}/svn
%{python2_sitearch}/libsvn
%endif

%if %{with python3} && %{with pyswig}
%files -n python3-subversion
%{python3_sitearch}/svn
%{python3_sitearch}/libsvn
%endif

%files gnome
%{_libdir}/libsvn_auth_gnome_keyring-*.so.*

%if %{with kwallet}
%files kde
%{_libdir}/libsvn_auth_kwallet-*.so.*
%endif

%files devel
%{_includedir}/subversion-1
%{_libdir}/libsvn*.*a
%{_libdir}/libsvn*.so
%{_datadir}/pkgconfig/*.pc
%exclude %{_libdir}/libsvn_swig_perl*
%exclude %{_libdir}/libsvnjavahl-*.so

%files -n mod_dav_svn
%config(noreplace) %{_httpd_modconfdir}/*.conf
%{_libdir}/httpd/modules/mod_*.so
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%doc example.conf
%endif

%files perl
%{perl_vendorarch}/auto/SVN
%{perl_vendorarch}/SVN
%{_libdir}/libsvn_swig_perl*
%{_mandir}/man*/*::*

%if %{with ruby}
%files ruby
%{_libdir}/libsvn_swig_ruby*
%{ruby_vendorarchdir}/svn
%endif

%if %{with java}
%files javahl
%{_javadir}/svn-javahl.jar
%endif

%changelog
* Mon Feb  3 2025 Joe Orton <jorton@redhat.com> - 1.14.5-7
- enable parallelisation in "make check"
- simplify build conditional definitions

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1.14.5-6
- Add explicit BR: libxcrypt-devel

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.14.5-4
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Wed Dec 18 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.14.5-3
- Explicitly add dependency for rubygem(csv) for ruby3.4

* Fri Dec 13 2024 Joe Orton <jorton@redhat.com> - 1.14.5-2
- fix ELN build failure

* Wed Dec 11 2024 Joe Orton <jorton@redhat.com> - 1.14.5-1
- update to 1.14.5 (#2331047)
- use %%autosetup
- enable tests by default again

* Fri Nov 01 2024 Tomas Korbar <tkorbar@redhat.com> - 1.14.4-1
- Rebase to version 1.14.4
- Resolves: rhbz#2317222

* Mon Oct 07 2024 Tomas Korbar <tkorbar@redhat.com> - 1.14.3-11
- Rebuild for utf8proc SONAME bump

* Tue Aug 06 2024 Tomas Korbar <tkorbar@redhat.com> - 1.14.3-10
- Fix debuginfo generation for bindings

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.14.3-8
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.14.3-7
- Rebuilt for Python 3.13

* Mon Mar 04 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.14.3-6
- Really rebuild for java-21-openjdk as system jdk

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.14.3-5
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Tomas Korbar <tkorbar@redhat.com> - 1.14.3-3
- Fix building with gcc 14
- incompatible-pointer-types warnings became errors, but they've
been present for a long time and posed no threat, thus revert
the behaviour
- Resolves: rhbz#2259155

* Fri Jan 12 2024 Tomas Korbar <tkorbar@redhat.com> - 1.14.3-2
- Fix testing of binary patch
- Resolves: rhbz#2255746

* Fri Jan 05 2024 Richard Lescak <rlescak@redhat.com> - 1.14.3-1
- rebase to version 1.14.3 (#2256062)

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.14.2-23
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Mon Nov 20 2023 Joe Orton <jorton@redhat.com> - 1.14.2-22
- fix mod_authz_svn, mod_dontdothat (#2250182)

* Wed Nov  8 2023 Joe Orton <jorton@redhat.com> - 1.14.2-21
- restore plaintext password storage by default (per upstream)
- restrict symbols exposed by DSOs built for httpd

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.14.2-19
- Perl 5.38 rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.14.2-18
- Rebuilt for Python 3.12

* Fri Jun 30 2023 Richard Lescak <rlescak@redhat.com> - 1.14.2-17
- temporary disable tests for eln to prevent FTBFS

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.14.2-16
- Rebuilt for Python 3.12

* Mon May 08 2023 Florian Weimer <fweimer@redhat.com> - 1.14.2-15
- Port to C99

* Thu Feb 16 2023 Richard Lescak <rlescak@redhat.com> - 1.14.2-14
- SPDX migration

* Fri Jan 27 2023 Richard Lescak <rlescak@redhat.com> - 1.14.2-13
- add requirement for python3-setuptools with new Python 3.12 (#2155420)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.14.2-11
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sun Oct 09 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.14.2-10
- Backport upstream fix for ruby3.2 support

* Wed Oct 05 2022 Richard Lescak <rlescak@redhat.com> - 1.14.2-8
- fix segfault in Python swig test (#2128024)

* Fri Jul 29 2022 Joe Orton <jorton@redhat.com> - 1.14.2-7
- improve library versioning so filenames are unique across releases

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Joe Orton <jorton@redhat.com> - 1.14.2-5
- disable libmagic during test runs

* Tue Jul  5 2022 Joe Orton <jorton@redhat.com> - 1.14.2-4
- update for new Java arches and bump to JDK 17 (#2103909)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.14.2-3
- Rebuilt for Python 3.11

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.14.2-2
- Perl 5.36 rebuild

* Wed May  4 2022 Joe Orton <jorton@redhat.com> - 1.14.2-1
- update to 1.14.2 (#2073852, CVE-2021-28544, CVE-2022-24070)

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.14.1-11
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.14.1-10
- F-36: rebuild against ruby31

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 1.14.1-9
- Disable automatic .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 16 2021 Richard Lescak <rlescak@redhat.com> - 1.14.1-7
- Replaced deprecated method readfp() in gen_base.py to build with Python 3.11 (#2019019)

* Thu Jul 29 2021 Joe Orton <jorton@redhat.com> - 1.14.1-6
- fix intermittent FTBFS in tests (#1956806)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.14.1-4
- Rebuilt for Python 3.10

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.14.1-3
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.14.1-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 10 2021 Joe Orton <jorton@redhat.com> - 1.14.1-1
- update to 1.14.1 (#1927265, #1768698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.14.0-11
- F-34: rebuild against ruby 3.0

* Fri Dec 11 2020 Joe Orton <jorton@redhat.com> - 1.14.0-10
- strip libdir from pkgconfig files
- add missing -libs dep from python3-subversion

* Thu Dec  3 2020 Joe Orton <jorton@redhat.com> - 1.14.0-9
- fix KWallet conditional (#1902598)

* Mon Nov 30 2020 Jan Grulich <jgrulich@redhat.com> - 1.14.0-8
- Disable KWallet for RHEL and ELN
  Resolves: bz#1902598

* Tue Sep 29 2020 Joe Orton <jorton@redhat.com> - 1.14.0-7
- bump required apr-devel
- BR gcc, gcc-c++

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.14.0-4
- Perl 5.32 rebuild

* Wed Jun  3 2020 Merlin Mathesius <mmathesi@redhat.com> - 1.14.0-3
- Minor conditional fixes for ELN

* Wed Jun  3 2020 Joe Orton <jorton@redhat.com> - 1.14.0-2
- use minor version as libtool library revision number

* Mon Jun  1 2020 Joe Orton <jorton@redhat.com> - 1.14.0-1
- update to 1.14.0 (#1840565, #1812195)

* Tue May 19 2020 Joe Orton <jorton@redhat.com> - 1.14.0~rc2-2
- switch subpackages to lock-step requires on -libs rather than subversion
- fixed the build-requires (Jitka Plesnikova)

* Thu Apr 30 2020 Joe Orton <jorton@redhat.com> - 1.14.0~rc2-1
- drop Berkeley DB support for Fedora > 32
- BR java-11-openjdk-devel

* Thu Apr 23 2020 Joe Orton <jorton@redhat.com> - 1.14.0~rc2-0
- update to 1.14.0-rc2

* Wed Feb 12 2020 Joe Orton <jorton@redhat.com> - 1.13.0-4
- fix FTBFS on 32-bit arches (#1800120)
- conditionally package bdb tools in -tools

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.12.2-4
- F-32: fix include path for ruby 2.7
- Rebuild for ruby 2.7

* Mon Jan  6 2020 Joe Orton <jorton@redhat.com> - 1.12.2-3
- update for KDE 5 (Phil O, #1768693)

* Fri Aug 30 2019 Joe Orton <jorton@redhat.com> - 1.12.2-2
- switch to Python 3 for F32+ (#1737928)

* Thu Jul 25 2019 Joe Orton <jorton@redhat.com> - 1.12.2-1
- update to 1.12.2

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.12.0-2
- Perl 5.30 rebuild

* Wed May  1 2019 Joe Orton <jorton@redhat.com> - 1.12.0-1
- update to 1.12.0 (#1702471)

* Wed Apr 17 2019 Joe Orton <jorton@redhat.com> - 1.11.1-5
- fix build with APR 1.7.0 (upstream r1857391)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.11.1-3
- F-30: rebuild against ruby26

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.11.1-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jan 11 2019 Joe Orton <jorton@redhat.com> - 1.11.1-1
- update to 1.11.1

* Wed Oct 31 2018 Joe Orton <jorton@redhat.com> - 1.11.0-1
- update to 1.11.0

* Thu Oct 11 2018 Joe Orton <jorton@redhat.com> - 1.10.3-1
- update to 1.10.3

* Fri Jul 20 2018 Joe Orton <jorton@redhat.com> - 1.10.2-1
- update to 1.10.2 (#1603197)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.10.0-9
- Perl 5.28 rebuild

* Thu Jun 28 2018 Joe Orton <jorton@redhat.com> - 1.10.0-8
- fix test suite invocation

* Thu Jun 28 2018 Joe Orton <jorton@redhat.com> - 1.10.0-7
- switch build conditional to disable only python bindings

* Thu May  3 2018 Joe Orton <jorton@redhat.com> - 1.10.0-6
- really disable Berkeley DB support if required by bcond
- add build conditional to disable swig binding subpackages

* Tue May  1 2018 Joe Orton <jorton@redhat.com> - 1.10.0-5
- remove build and -devel deps on libgnome-keyring-devel

* Tue May  1 2018 Joe Orton <jorton@redhat.com> - 1.10.0-4
- drop -devel dep on libserf-devel

* Tue Apr 24 2018 Joe Orton <jorton@redhat.com> - 1.10.0-3
- add bdb, tests as build conditional

* Tue Apr 17 2018 Joe Orton <jorton@redhat.com> - 1.10.0-2
- move new tools to -tools

* Mon Apr 16 2018 Joe Orton <jorton@redhat.com> - 1.10.0-1
- update to 1.10.0 (#1566493)

* Tue Mar 27 2018 Joe Orton <jorton@redhat.com> - 1.9.7-7
- add build conditionals for python2, python3 and kwallet

* Thu Feb  8 2018 Joe Orton <jorton@redhat.com> - 1.9.7-6
- force use of Python2 in test suite

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9.7-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.9.7-4
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.7-3
- F-28: rebuild for ruby25

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.9.7-2
- Python 2 binary package renamed to python2-subversion
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Fri Aug 11 2017 Joe Orton <jorton@redhat.com> - 1.9.7-1
- update to 1.9.7 (CVE-2017-9800, #1480402)
- add Documentation= to svnserve.service

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Joe Orton <jorton@redhat.com> - 1.9.6-2
- move javahl .so to -libs (#1469158)

* Thu Jul  6 2017 Joe Orton <jorton@redhat.com> - 1.9.6-1
- update to 1.9.6 (#1467890)
- update to latest upstream psvn.el
- move libsvnjavahl to -libs, build -javahl noarch
- fix javahl Requires

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.5-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.9.5-2
- F-26: rebuild for ruby24

* Mon Jan  2 2017 Joe Orton <jorton@redhat.com> - 1.9.5-1
- update to 1.9.5 (#1400040, CVE-2016-8734)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed May 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.4-3
- Enable tests
- Revert one of Ruby 2.2 fixes

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9.4-2
- Perl 5.24 rebuild

* Sun May  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.4-1
- Update to 1.9.4 (#1331222) CVE-2016-2167 CVE-2016-2168
- Move tools in docs to tools subpackage (rhbz 1171757 1199761)
- Disable make check to work around FTBFS

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Joe Orton <jorton@redhat.com> - 1.9.3-2
- rebuild for Ruby 2.3

* Tue Dec 15 2015 Joe Orton <jorton@redhat.com> - 1.9.3-1
- update to 1.9.3 (#1291683)
- use private /tmp in svnserve.service

* Thu Sep 24 2015 Joe Orton <jorton@redhat.com> - 1.9.2-1
- update to 1.9.2 (#1265447)

* Mon Sep 14 2015 Joe Orton <jorton@redhat.com> - 1.9.1-1
- update to 1.9.1 (#1259099)

* Mon Aug 24 2015 Joe Orton <jorton@redhat.com> - 1.9.0-1
- update to 1.9.0 (#1207835)
- package pkgconfig files

* Tue Jul 14 2015 Joe Orton <jorton@redhat.com> - 1.8.13-7
- move svnauthz to -tools; make svnauthz-validate a symlink
- move svnmucc man page to -tools
- restore dep on systemd (#1183873)

* Fri Jul 10 2015 Joe Orton <jorton@redhat.com> - 1.8.13-6
- rebuild with tests enabled

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.8.13-4
- Own bash-completion dirs not owned by anything in dep chain

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.13-3
- Perl 5.22 rebuild

* Tue Apr 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.13-2
- Disable tests to fix swig test issues

* Wed Apr 08 2015 <vondruch@redhat.com> - 1.8.13-1
- Fix Ruby's test suite.

* Tue Apr  7 2015 Joe Orton <jorton@redhat.com> - 1.8.13-1
- update to 1.8.13 (#1207835)
- attempt to patch around SWIG issues

* Tue Dec 16 2014 Joe Orton <jorton@redhat.com> - 1.8.11-1
- update to 1.8.11 (#1174521)
- require newer libserf (#1155670)

* Tue Sep 23 2014 Joe Orton <jorton@redhat.com> - 1.8.10-6
- prevents assert()ions in library code (#1058693)

* Tue Sep 23 2014 Joe Orton <jorton@redhat.com> - 1.8.10-5
- drop sysv conversion trigger (#1133786)

* Tue Sep 23 2014 Joe Orton <jorton@redhat.com> - 1.8.10-4
- move svn-bench, fsfs-* to -tools

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.10-3
- Perl 5.20 rebuild

* Thu Aug 21 2014 Kevin Fenzi <kevin@scrye.com> - 1.8.10-2
- Rebuild for rpm bug 1131960

* Mon Aug 18 2014 Joe Orton <jorton@redhat.com> - 1.8.10-1
- update to 1.8.10 (#1129100, #1128884, #1125800)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Joe Orton <jorton@redhat.com> - 1.8.9-1
- update to 1.8.9 (#1100779)

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Apr 22 2014 Joe Orton <jorton@redhat.com> - 1.8.8-2
- require minitest 4 to fix tests for Ruby bindings (#1089252)

* Fri Feb 28 2014 Joe Orton <jorton@redhat.com> - 1.8.8-1
- update to 1.8.8

* Thu Jan 23 2014 Joe Orton <jorton@redhat.com> - 1.8.5-4
- fix _httpd_mmn expansion in absence of httpd-devel

* Mon Jan  6 2014 Joe Orton <jorton@redhat.com> - 1.8.5-3
- fix permissions of /run/svnserve (#1048422)

* Tue Dec 10 2013 Joe Orton <jorton@redhat.com> - 1.8.5-2
- don't drop -Wall when building swig Perl bindings (#1037341)

* Tue Nov 26 2013 Joe Orton <jorton@redhat.com> - 1.8.5-1
- update to 1.8.5 (#1034130)
- add fix for wc-queries-test breakage (h/t Andreas Stieger, r1542774)

* Mon Nov 18 2013 Joe Orton <jorton@redhat.com> - 1.8.4-2
- add fix for ppc breakage (Andreas Stieger, #985582)

* Tue Oct 29 2013 Joe Orton <jorton@redhat.com> - 1.8.4-1
- update to 1.8.4

* Tue Sep  3 2013 Joe Orton <jorton@redhat.com> - 1.8.3-1
- update to 1.8.3
- move bash completions out of /etc (#922993)

* Tue Aug 06 2013 Adam Williamson <awilliam@redhat.com> - 1.8.1-2
- rebuild for perl 5.18 (again; 1.8.1-1 beat out 1.8.0-2)

* Thu Jul 25 2013 Joe Orton <jorton@redhat.com> - 1.8.1-1
- update to 1.8.1

* Fri Jul 19 2013 Joe Orton <jorton@redhat.com> - 1.8.0-3
- temporarily ignore test suite failures on ppc* (#985582)

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.8.0-2
- Perl 5.18 rebuild

* Tue Jun 18 2013 Joe Orton <jorton@redhat.com> - 1.8.0-1
- update to 1.8.0; switch to serf
- use full relro in mod_dav_svn build (#973694)

* Mon Jun  3 2013 Joe Orton <jorton@redhat.com> - 1.7.10-1
- update to 1.7.10 (#970014)
- fix aarch64 build issues (Dennis Gilmore, #926578)

* Thu May  9 2013 Joe Orton <jorton@redhat.com> - 1.7.9-3
- fix spurious failures in ruby test suite (upstream r1327373)

* Thu May  9 2013 Joe Orton <jorton@redhat.com> - 1.7.9-2
- try harder to avoid svnserve bind failures in ruby binding tests
- enable verbose output for ruby binding tests

* Tue Apr  9 2013 Joe Orton <jorton@redhat.com> - 1.7.9-1
- update to 1.7.9

* Wed Mar 27 2013 Vít Ondruch <vondruch@redhat.com> - 1.7.8-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Drop Ruby version checks from configuration script.
- Fix and enable Ruby test suite.

* Thu Mar 14 2013 Joe Orton <jorton@redhat.com> - 1.7.8-5
- drop specific dep on ruby(abi)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan  8 2013 Joe Orton <jorton@redhat.com> - 1.7.8-3
- update to latest psvn.el

* Tue Jan  8 2013 Lukáš Nykrýn <lnykryn@redhat.com> - 1.7.8-2
- Scriptlets replaced with new systemd macros (#850410)

* Fri Jan  4 2013 Joe Orton <jorton@redhat.com> - 1.7.8-1
- update to 1.7.8

* Thu Oct 11 2012 Joe Orton <jorton@redhat.com> - 1.7.7-1
- update to 1.7.7

* Fri Aug 17 2012 Joe Orton <jorton@redhat.com> - 1.7.6-1
- update to 1.7.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Joe Orton <jorton@redhat.com> - 1.7.5-5
- switch svnserve pidfile to use /run, use /usr/lib/tmpfiles.d (#840195)

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 1.7.5-4
- Perl 5.16 rebuild

* Mon Jun 18 2012 Dan Horák <dan[at]danny.cz - 1.7.5-3
- fix build with recent gcc 4.7 (svn rev 1345740)

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.7.5-2
- Perl 5.16 rebuild

* Tue May 22 2012 Joe Orton <jorton@redhat.com> - 1.7.5-1
- update to 1.7.5

* Tue Apr 24 2012 Joe Orton <jorton@redhat.com> - 1.7.4-6
- drop strict sqlite version requirement (#815396)

* Mon Apr 23 2012 Joe Orton <jorton@redhat.com> - 1.7.4-5
- switch to libdb-devel (#814090)

* Thu Apr 19 2012 Joe Orton <jorton@redhat.com> - 1.7.4-4
- adapt for conf.modules.d with httpd 2.4
- add possible workaround for kwallet crasher (#810861)

* Fri Mar 30 2012 Joe Orton <jorton@redhat.com> - 1.7.4-3
- re-enable test suite

* Fri Mar 30 2012 Joe Orton <jorton@redhat.com> - 1.7.4-2
- fix build with httpd 2.4

* Mon Mar 12 2012 Joe Orton <jorton@redhat.com> - 1.7.4-1
- update to 1.7.4
- fix build with httpd 2.4

* Thu Mar  1 2012 Joe Orton <jorton@redhat.com> - 1.7.3-7
- re-enable kwallet (#791031)

* Wed Feb 29 2012 Joe Orton <jorton@redhat.com> - 1.7.3-6
- update psvn

* Wed Feb 29 2012 Joe Orton <jorton@redhat.com> - 1.7.3-5
- add tools subpackage (#648015)

* Tue Feb 28 2012 Joe Orton <jorton@redhat.com> - 1.7.3-4
- trim contents of doc dic (#746433)

* Tue Feb 28 2012 Joe Orton <jorton@redhat.com> - 1.7.3-3
- re-enable test suite

* Tue Feb 28 2012 Joe Orton <jorton@redhat.com> - 1.7.3-2
- add upstream test suite fixes for APR hash change (r1293602, r1293811)
- use ruby vendorlib directory (#798203)
- convert svnserve to systemd (#754074)

* Mon Feb 13 2012 Joe Orton <jorton@redhat.com> - 1.7.3-1
- update to 1.7.3
- ship, enable mod_dontdothat

* Mon Feb 13 2012 Joe Orton <jorton@redhat.com> - 1.7.2-2
- require ruby 1.9.1 abi

* Thu Feb  9 2012 Joe Orton <jorton@redhat.com> - 1.7.2-1
- update to 1.7.2
- add Vincent Batts' Ruby 1.9 fixes from dev@

* Sun Feb  5 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.7.1-3
- fix gnome-keyring build deps 

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Joe Orton <jorton@redhat.com> - 1.7.1-1
- update to 1.7.1
- (temporarily) disable failing kwallet support

* Sun Nov 27 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.0-3
- Build with libmagic support.

* Sat Oct 15 2011 Ville Skyttä <ville.skytta@iki.fi> - 1.7.0-2
- Fix apr Conflicts syntax in -libs.
- Fix obsolete chown syntax in subversion.conf.
- Fix use of spaces vs tabs in specfile.

* Wed Oct 12 2011 Joe Orton <jorton@redhat.com> - 1.7.0-1
- update to 1.7.0
- drop svn2cl (no longer shipped in upstream tarball)
