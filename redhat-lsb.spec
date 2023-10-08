# globals for redhat-lsb-20231006git8d00acdc.tar.gz
%global gitdate 20231006
%global gitversion 8d00acdc

%global snapshot %{gitdate}git%{gitversion}
%global gver .%{gitdate}git%{gitversion}

# Define this to link to which library version  eg. /lib64/ld-lsb-x86-64.so.3
%global lsbsover 3

%ifarch %{ix86}
%global ldso ld-linux.so.2
%global lsbldso ld-lsb.so
%endif

%ifarch alpha
%global ldso ld-linux-alpha.so.2
%global lsbldso ld-lsb-alpha.so
%endif

%ifarch ia64
%global ldso ld-linux-ia64.so.2
%global lsbldso ld-lsb-ia64.so
%endif

%ifarch ppc
%global ldso ld.so.1
%global lsbldso ld-lsb-ppc32.so
%endif

%ifarch ppc64
%global ldso ld64.so.1
%global lsbldso ld-lsb-ppc64.so
%endif

%ifarch ppc64le
%global ldso ld64.so.2
%global lsbldso ld-lsb-ppc64le.so
%endif

%ifarch s390
%global ldso ld.so.1
%global lsbldso ld-lsb-s390.so
%endif

%ifarch s390x
%global ldso ld64.so.1
%global lsbldso ld-lsb-s390x.so
%endif

%ifarch x86_64
%global ldso ld-linux-x86-64.so.2
%global lsbldso ld-lsb-x86-64.so
%endif

%ifarch %{arm}
%global ldso ld-linux.so.2
%global lsbldso ld-lsb-arm.so
%endif

%ifarch aarch64
%global ldso ld-linux-aarch64.so.1
%global lsbldso ld-lsb-aarch64.so
%endif

%global upstreamlsbrelver 2.0
%global lsbrelver 5.0

# for >= f28, __brp_ldconfig is added in __os_install_post, it removes the symlink %%{lsbldso}
# and thus leading to the FTBS.
%global __brp_ldconfig %{nil}

# The packages are architecture-specific, but do not contain any ELF
# binaries with debuginfo to extract.
%undefine _enable_debug_packages

Summary: Implementation of Linux Standard Base specification
Name: redhat-lsb
Version: 5.0
Release: 0.2%{gver}%{?dist}
URL: https://wiki.linuxfoundation.org/lsb/start
# https://github.com/LinuxStandardBase/lsb-samples/
Source0: redhat-lsb-%{snapshot}.tar.gz
License: GPLv2
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(Getopt::Long)

%ifarch %{ix86}
%global archname ia32
%endif
%ifarch ia64
%global archname ia64
%endif
%ifarch ppc
%global archname ppc32
%endif
%ifarch ppc64
%global archname ppc64
%endif
%ifarch ppc64le
%global archname ppc64le
%endif
%ifarch s390
%global archname s390
%endif
%ifarch s390x
%global archname s390x
%endif
%ifarch x86_64
%global archname amd64
%endif
%ifarch %{arm}
%global archname arm
%endif
%ifarch aarch64
%global archname aarch64
%endif
%ifarch alpha
%define archname alpha
%endif

Requires: redhat-lsb-core%{?_isa} = %{version}-%{release}
Requires: redhat-lsb-cxx%{?_isa} = %{version}-%{release}
Requires: redhat-lsb-desktop%{?_isa} = %{version}-%{release}
Requires: redhat-lsb-languages = %{version}-%{release}
Requires: redhat-lsb-printing = %{version}-%{release}
Obsoletes: redhat-lsb-trialuse <= 5

Provides: lsb = %{version}-%{release}
Provides: lsb-%{archname} = %{version}-%{release}
Provides: lsb-noarch = %{version}-%{release}

%description
The Linux Standard Base (LSB) is an attempt to develop a set of standards that
will increase compatibility among Linux distributions. It is designed to be 
binary-compatible and produce a stable application binary interface (ABI) for
independent software vendors.
The lsb package provides utilities, libraries etc. needed for LSB Compliant 
Applications. It also contains requirements that will ensure that all 
components required by the LSB are installed on the system.

%package core
Summary: LSB Core module support
# gLSB Library
Requires: glibc%{?_isa}
Requires: glibc-common
Requires: libgcc%{?_isa}
#LSB requires libcrypt.so.1
Requires: libxcrypt-compat%{?_isa}
#LSB requires libncurses.so.5 for some reason
Requires: ncurses-compat-libs%{?_isa}
Requires: pam%{?_isa}
Requires: zlib%{?_isa}

# gLSB Command and Utilities
Requires: /usr/bin/[
Requires: /usr/bin/ar
Requires: /usr/bin/at
Requires: /usr/bin/awk
Requires: /usr/bin/basename
Requires: /usr/bin/batch
Requires: /usr/bin/bc
Requires: /usr/bin/cat
Requires: /usr/bin/chfn
Requires: /usr/bin/chgrp
Requires: /usr/bin/chmod
Requires: /usr/bin/chown
Requires: /usr/bin/chsh
Requires: /usr/bin/cksum
Requires: /usr/bin/cmp
Requires: /usr/bin/col
Requires: /usr/bin/comm
Requires: /usr/bin/cp
Requires: /usr/bin/cpio
Requires: /usr/bin/crontab
Requires: /usr/bin/csplit
Requires: /usr/bin/cut
Requires: /usr/bin/date
Requires: /usr/bin/dd
Requires: /usr/bin/df
Requires: /usr/bin/diff
Requires: /usr/bin/dirname
Requires: /usr/bin/dmesg
Requires: /usr/bin/du
Requires: /usr/bin/echo
Requires: /usr/bin/ed
Requires: /usr/bin/egrep
Requires: /usr/bin/env
Requires: /usr/bin/expand
Requires: /usr/bin/expr
Requires: /usr/bin/false
Requires: /usr/bin/fgrep
Requires: /usr/bin/file
Requires: /usr/bin/find
Requires: /usr/bin/fold
Requires: /usr/sbin/fuser
Requires: /usr/bin/gencat
Requires: /usr/bin/getconf
Requires: /usr/bin/gettext
Requires: /usr/bin/grep
Requires: /usr/sbin/groupadd
Requires: /usr/sbin/groupdel
Requires: /usr/sbin/groupmod
Requires: /usr/bin/groups
Requires: /usr/bin/gunzip
Requires: /usr/bin/gzip
Requires: /usr/bin/head
Requires: /usr/bin/hostname
Requires: /usr/bin/iconv
Requires: /usr/bin/id
Requires: /usr/bin/install
Requires: /usr/bin/ipcrm
Requires: /usr/bin/ipcs
Requires: /usr/bin/join
Requires: /usr/bin/kill
Requires: /usr/bin/killall
Requires: /usr/bin/ln
Requires: /usr/bin/locale
Requires: /usr/bin/localedef
Requires: /usr/bin/logger
Requires: /usr/bin/logname
Requires: /usr/bin/lp
Requires: /usr/bin/lpr
Requires: /usr/bin/ls
Requires: /usr/bin/m4
Requires: /bin/mailx
Requires: /usr/bin/make
Requires: /usr/bin/man
Requires: /usr/bin/md5sum
Requires: /usr/bin/mkdir
Requires: /usr/bin/mkfifo
Requires: /usr/bin/mknod
Requires: /usr/bin/mktemp
Requires: /usr/bin/more
Requires: /usr/bin/mount
Requires: /usr/bin/msgfmt
Requires: /usr/bin/mv
Requires: /usr/bin/newgrp
Requires: /usr/bin/nice
Requires: /usr/bin/nl
Requires: /usr/bin/nohup
Requires: /usr/bin/od
Requires: /usr/bin/passwd
Requires: /usr/bin/paste
Requires: /usr/bin/patch
Requires: /usr/bin/pathchk
#better POSIX conformance of /usr/bin/pax
Requires: spax
Requires: /usr/bin/pidof
Requires: /usr/bin/pr
Requires: /usr/bin/printf
Requires: /usr/bin/ps
Requires: /usr/bin/pwd
Requires: /usr/bin/renice
Requires: /usr/bin/rm
Requires: /usr/bin/rmdir
Requires: /usr/bin/sed
Requires: /usr/sbin/sendmail
Requires: /usr/bin/seq
Requires: /usr/bin/sh
Requires: /usr/sbin/shutdown
Requires: /usr/bin/sleep
Requires: /usr/bin/sort
Requires: /usr/bin/split
Requires: /usr/bin/strings
Requires: /usr/bin/strip
Requires: /usr/bin/stty
Requires: /usr/bin/su
Requires: /usr/bin/sync
Requires: /usr/bin/tail
Requires: /usr/bin/tar
Requires: /usr/bin/tee
Requires: /usr/bin/test
Requires: /usr/bin/time
Requires: /usr/bin/touch
Requires: /usr/bin/tr
Requires: /usr/bin/true
Requires: /usr/bin/tsort
Requires: /usr/bin/tty
Requires: /usr/bin/umount
Requires: /usr/bin/uname
Requires: /usr/bin/unexpand
Requires: /usr/bin/uniq
Requires: /usr/sbin/useradd
Requires: /usr/sbin/userdel
Requires: /usr/sbin/usermod
Requires: /usr/bin/wc
Requires: /usr/bin/xargs
Requires: /usr/bin/zcat

Provides: lsb-core-%{archname} = %{version}-%{release}
Provides: lsb-core-noarch = %{version}-%{release}
#Obsoletes: redhat-lsb < %%{version}-%%{release}

%description core
The Linux Standard Base (LSB) Core module support provides the fundamental
system interfaces, libraries, and runtime environment upon which all conforming
applications and libraries depend.

%package cxx
Summary: LSB CXX module support
Requires: libstdc++%{?_isa}
Requires: redhat-lsb-core%{?_isa} = %{version}-%{release}

Provides: lsb-cxx-%{archname} = %{version}-%{release}
Provides: lsb-cxx-noarch = %{version}-%{release}

%description cxx
The Linux Standard Base (LSB) CXX module supports the core interfaces by
providing system interfaces, libraries, and a runtime environment for
applications built using the C++ programming language. These interfaces
provide low-level support for the core constructs of the language, and
implement the standard base C++ libraries.

%package desktop
Summary: LSB Desktop module support
Requires: xdg-utils
# LSB_Graphics library
Requires: libICE%{?_isa}
Requires: libSM%{?_isa}
Requires: libX11%{?_isa}
Requires: libXext%{?_isa}
Requires: libXi%{?_isa}
Requires: libXt%{?_isa}
Requires: libXtst%{?_isa}
Requires: mesa-libGL%{?_isa}
Requires: mesa-libGLU%{?_isa}
# gLSB Graphics and gLSB Graphics Ext Command and Utilities
Requires: /usr/bin/fc-cache
Requires: /usr/bin/fc-list
Requires: /usr/bin/fc-match
# gLSB Graphics Ext library
Requires: cairo%{?_isa}
Requires: freetype%{?_isa}
Requires: libjpeg-turbo%{?_isa}

%ifarch %{ix86} ppc s390 arm
Requires: libpng12.so.0
%endif
%ifarch x86_64 ppc64 s390x aarch64 ppc64le
Requires: libpng12.so.0()(64bit)
%endif
Requires: libpng%{?_isa}
Requires: libXft%{?_isa}
Requires: libXrender%{?_isa}
# toolkit-gtk
Requires: atk%{?_isa}
Requires: gdk-pixbuf2%{?_isa}
Requires: glib2%{?_isa}
Requires: gtk2%{?_isa}
Requires: pango%{?_isa}
%if 0%{?fedora} || 0%{?epel}
# toolkit-qt is not in rhel
Requires: qt%{?_isa}
Requires: qt-x11%{?_isa}
%endif
# xml
Requires: libxml2%{?_isa}
Requires: redhat-lsb-core%{?_isa} = %{version}-%{release}

Provides: lsb-desktop-%{archname} = %{version}-%{release}
Provides: lsb-desktop-noarch = %{version}-%{release}
Provides: lsb-graphics-%{archname} = %{version}-%{release}
Provides: lsb-graphics-noarch = %{version}-%{release}
Obsoletes: redhat-lsb-graphics < %{version}-%{release}

%description desktop
The Linux Standard Base (LSB) Desktop Specifications define components that are
required to be present on an LSB conforming system.

%package languages
Summary: LSB Languages module support
# Perl and Perl non-builtin modules
Requires: /usr/bin/perl
Requires: perl(CGI)
Requires: perl(Class::ISA)
Requires: perl(CPAN)
# Locale::Constants has been Locale::Codes::Costants, so we need
# create a /usr/share/perl5/vendor_perl/Constants.pm manually.
# Requires: perl(Locale::Constants)
# perl(Locale::Constants) requires perl(Locale::Codes)
# DB module is a builtin module, but perl package doesn't contain this provide.
# Requires: perl(DB)
# we also need perl(Pod::Plainer), we need to rpm this package ourself
Requires: perl(Locale::Codes)
Requires: perl(File::Spec)
Requires: perl(Scalar::Util)
Requires: perl(Test::Harness)
Requires: perl(Test::Simple)
Requires: perl(ExtUtils::MakeMaker)
Requires: perl(Pod::Plainer)
Requires: perl(XML::LibXML)
Requires: perl(Pod::LaTeX)
Requires: perl(Pod::Checker)
Requires: perl(B::Lint)
Requires: perl(Text::Soundex)
Requires: perl(Env)
Requires: perl(Time::HiRes)
Requires: perl(Locale::Maketext)
Requires: perl(Fatal)
Requires: perl(File::CheckTree)
Requires: perl(Sys::Syslog)
Requires: perl(Getopt::Long)

# python3
Requires: /usr/bin/python3
# java
Requires: redhat-lsb-core%{?_isa} = %{version}-%{release}

Provides: lsb-languages-%{archname} = %{version}-%{release}
Provides: lsb-languages-noarch = %{version}-%{release}

%description languages
The Linux Standard Base (LSB) Languages module supports components for runtime
languages which are found on an LSB conforming system.

%package printing
Summary: LSB Printing module support
# gLSB Printing Libraries
Requires: cups-libs
# gLSB Printing Command and Utilities
Requires: /usr/bin/foomatic-rip
Requires: /usr/bin/gs
Requires: redhat-lsb-core%{?_isa} = %{version}-%{release}

Provides: lsb-printing-%{archname} = %{version}-%{release}
Provides: lsb-printing-noarch = %{version}-%{release}
Obsoletes: redhat-lsb-printing < %{version}-%{release}

%description printing
The Linux Standard Base (LSB) Printing specifications define components that
are required to be present on an LSB conforming system.

%package supplemental
Summary: LSB supplemental dependencies required by LSB certification tests
Requires: net-tools
Requires: xorg-x11-fonts-ISO8859-1-75dpi
Requires: xorg-x11-fonts-ISO8859-1-100dpi
Requires: abattis-cantarell-fonts
Requires: sil-abyssinica-fonts
Requires: xorg-x11-server-Xvfb

%description supplemental
This subpackage brings in supplemental dependencies for components required for
passing LSB (Linux Standard Base) certification testsuite, but not directly required
to be on LSB conforming system.

%prep
%setup -q -n redhat-lsb-%{snapshot}

%build
cd lsb_release/src
%make_build

%install
pushd redhat-lsb
%make_install

# manually add Locale::Constants. This module is just an alias of Locale::Codes::Constants
mkdir -p %{buildroot}%{perl_vendorlib}/Locale
cp -p Constants.pm %{buildroot}%{perl_vendorlib}/Locale
cp -p Constants.pod %{buildroot}%{perl_vendorlib}/Locale
popd

pushd lsb_release/src
make mandir=%{buildroot}%{_mandir} prefix=%{buildroot}%{_prefix} install
popd

#prepare installation of doc
cp -p lsb_release/src/COPYING .
cp -p lsb_release/src/README README.lsb_release

# modules
mkdir -p %{buildroot}%{_sysconfdir}/lsb-release.d/
modules="core cxx desktop languages printing"

core="core security"
cxx="cpp"
desktop="desktop-misc graphics graphics-ext multimedia toolkit-gtk toolkit-qt toolkit-qt3"
desktop="${desktop} xml"
languages="perl python"
printing="printing"
trialuse="security multimedia"

for mod in ${modules};do
  touch $RPM_BUILD_ROOT%{_sysconfdir}/lsb-release.d/${mod}-%{lsbrelver}-%{archname}
  touch $RPM_BUILD_ROOT%{_sysconfdir}/lsb-release.d/${mod}-%{lsbrelver}-noarch
done

mkdir -p %{buildroot}%{_libdir}
for LSBVER in %{lsbsover}; do
  ln -snf %{ldso} %{buildroot}%{_libdir}/%{lsbldso}.$LSBVER
done

# LSB uses /usr/lib rather than /usr/lib64 even for 64bit OS
# According to the lsb-core documentation provided by
# http://refspecs.linux-foundation.org/LSB_3.2.0/LSB-Core-generic/LSB-Core-generic.pdf
# it's OK to put non binary in /usr/lib.
ln -snf ../../../sbin/chkconfig %{buildroot}/usr/lib/lsb/install_initd
ln -snf ../../../sbin/chkconfig %{buildroot}/usr/lib/lsb/remove_initd
#ln -snf mail %{buildroot}/bin/mailx

#mkdir -p %{buildroot}/usr/X11R6/lib/X11/xserver
#ln -snf /usr/%{_lib}/xserver/SecurityPolicy %{buildroot}/usr/X11R6/lib/X11/xserver/SecurityPolicy
#ln -snf /usr/share/X11/fonts %{buildroot}/usr/X11R6/lib/X11/fonts
#ln -snf /usr/share/X11/rgb.txt  %{buildroot}/usr/X11R6/lib/X11/rgb.txt


%files

%files core
%doc README.md README.lsb_release
%license COPYING
%{_sysconfdir}/redhat-lsb
%dir %{_sysconfdir}/lsb-release.d
%{_mandir}/*/*
%{_bindir}/*
/usr/lib/lsb
%{_libdir}/*so*
%{_sysconfdir}/lsb-release.d/core*

%files cxx
%{_sysconfdir}/lsb-release.d/cxx*

%files desktop
%{_sysconfdir}/lsb-release.d/desktop*

%files languages
%{_sysconfdir}/lsb-release.d/languages*
%{perl_vendorlib}/Locale/Constants.pm
%{perl_vendorlib}/Locale/Constants.pod

%files printing
%{_sysconfdir}/lsb-release.d/printing*

%files supplemental
#no files, just dependencies


%changelog
* Fri Oct 06 2023 Sérgio Basto <sergio@serjux.com> - 5.0-0.2.20231006gita9c49411
- Update README.md with actual status

* Fri Oct 06 2023 Sérgio Basto <sergio@serjux.com> - 5.0-0.1.20231006git92f8ab57
- redhat-lsb 5.0 with new source location

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-62
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 10 2023 Sérgio Basto <sergio@serjux.com> - 4.1-61
- Remove "Trial Use" specs, because LSB 5.0 Trial Use is completely outdated

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jul 02 2022 Sérgio Basto <sergio@serjux.com> - 4.1-58
- Require libxcrypt-compat in core, as libcrypt.so.1 is mandatory (rhbz#2055953)

* Mon Jun 27 2022 Sérgio Basto <sergio@serjux.com> - 4.1-57
- ncurses-compat-libs was dropped in F37, to workaround and fix FTI (fails to
  install), since F37 we use ncurses-libs

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Florian Weimer <fweimer@redhat.com> - 4.1-54
- Remove unnecessary redhat_lsb_trigger.* programs (#1964367)

* Tue May 25 2021 Florian Weimer <fweimer@redhat.com> - 4.1-53
- Do not call non-existing lsn program on glibc updates (#1625584)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Tom Stellard <tstellar@redhat.com> - 4.1-50
- Use macros when invoking for invoking make and gcc

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Than Ngo <than@redhat.com> - 4.1-47
- fixed FTBS in f30

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Parag Nemade <pnemade AT redhat DOT com> - 4.1-44
- Add BuildRequires: gcc as per packaging guidelines

* Tue Feb 13 2018 Than Ngo <than@redhat.com> - 4.1-43
- fixed FTBS

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1-41
- greps are now in /usr/bin

* Mon Nov 13 2017 Sébastien Santoro <dereckson@espace-win.org> - 4.1-40
- Resolves:rh#1512650: /bin/mailx is still in /bin

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1-39
- /bin/ed is in /usr/bin/ed now
- /usr/bin/*grep are in /bin still

* Thu Nov 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1-38
- change /bin requirements to /usr/bin

* Mon Nov 06 2017 Ondrej Vasik <ovasik@redhat.com> - 4.1-37
- drop the postscriptlet specific for itanium completely(#1508613)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 10 2016 Ondrej Vasik <ovasik@redhat.com> - 4.1-33
- require ncurses-compat-libs - as LSB strictly requires libncurses.so.5
  (#1392972)

* Tue Feb 23 2016 Parag Nemade <pnemade AT redhat DOT com> - 4.1-32
- Resolves:rh#1307989: FTBFS in rawhide by adding perl-Getopt-Long in BuildRequires
- Drop Group: tag
- Added %%license tag
- Changed %%define -> %%global

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 27 2014 Parag <pnemade AT redhat DOT com> - 4.1-29
- Resolves:rh#1133536 - redhat-lsb does not requires /usr/sbin/sendmail

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Ondrej Vasik <ovasik@redhat.com> - 4.1-26
- add support for ppc64le (#1094371)

* Wed Apr 23 2014 Peter Robinson <pbrobinson@fedoraproject.org> 4.1-25
- Update aarch64 patch

* Mon Nov 25 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-24
- remove nsswitch handling - broken and unnecessary
  (#986728, #915147)

* Tue Oct 29 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-23
- fuser moved from /sbin to /usr/sbin/ (#1023283)

* Thu Oct 17 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-22
- pidof moved from /sbin to /usr/bin/ as part of the
  transfer to procps-ng package

* Wed Oct 16 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-21
- fix the broken dependency caused by hostname move after
  recent post UsrMove cleanup

* Tue Aug 13 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-20
- fix the patch for aarch64 support to be not patch of
  patch but real patch (sorry, simply, fix aarch64 build)

* Thu Aug 08 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-19
- Require sil-abyssinica-fonts in supplemental(#994341)
- Fully specify requirements on subpackages(#971386)

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 4.1-18
- Perl 5.18 rebuild

* Fri Jul 26 2013 Dennis Gilmore <dennis@ausil.us> - 4.1-17
- dont use -static when compiling redhat_lsb_trigger on arm

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.1-16
- Perl 5.18 rebuild

* Tue Jun 11 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-15
- fix build on aarch64 (#973343)
- fix the defines for arm and aarch64 (may need adjustment)

* Thu May 23 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-14
- require spax instead of pax (more POSIX compatible) (#965658)
- require another set of perl modules in -languages (#959129)
- polish a bit the nsswitch.conf hack - include mdns4_minimal (#915147)

* Tue Mar 12 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-13
- require /usr/bin/cpio (binary moved as part of UsrMove)

* Fri Mar 01 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-12
- require perl(Pod::Checker), perl(B::Lint) and
  perl(Text::Soundex) in languages (#916898)

* Fri Feb 08 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-11
- require perl(Pod::LaTeX) in languages (#908705)
- require xorg-x11-server-Xvfb in supplemental (#896058)

* Thu Jan 10 2013 Ondrej Vasik <ovasik@redhat.com> - 4.1-10
- require abattis-cantarell-fonts in supplemental (#892998)

* Fri Dec 14 2012 Ondrej Vasik <ovasik@redhat.com> - 4.1-9
- ship README and COPYING file in -core subpackage
  (#887195)

* Wed Dec 12 2012 Ondrej Vasik <ovasik@redhat.com> - 4.1-8
- require libpng12.so.0 in other architectures (#881596)

* Wed Dec 05 2012 Ondrej Vasik <ovasik@redhat.com> - 4.1-7
- add new subpackage -supplemental for LSB testuite-only dependencies
- require net-tools in -supplemental (#882122)
- require xorg-x11-fonts-ISO8859-1-{75,100}dpi in -supplemental
  (#883385)
- require perl(XML::LibXML) (#880954)
- keep usermodified /etc/nsswitch.conf as /etc/nsswitch.conf.rpmsave,
  warn about modification (#867124)

* Mon Nov 05 2012 Parag <pnemade AT redhat DOT com> - 4.1-6
- Resolves:rh#873066 - missing dependency /bin/su moved to /usr/bin/su

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 xning <xning AT redhat DOT com> - 4.1-4
- Resolves:rh:#825261: redhat-lsb scripts blow away my /etc/nsswitch.conf

* Wed May 23 2012 Parag <pnemade AT redhat DOT com> - 4.1-3
- Resolves:rh#824305: Dependency glibc-common%%{?_isa} should be changed to glibc-common only

* Mon May 14 2012 xning <xning AT redhat DOT com> - 4.1-2
- Resolves:rh:#806190: gethostbyaddr sets h_errno to 3, not HOST_NOT_FOUND
- Resolves:rh:#799284: perl(Pod::Plainer) is required by LSB 4.1
- Resolves:rh:#821308: redhat-lsb 4.1 test libpn12.so.0 failed on fedora 17

* Mon Mar 19 2012 xning <xning AT redhat DOT com> - 4.1-1
- Update to 4.1 release
- Added -core, -cxx, -desktop, -languages, -printing modules as subpackages
- Added submod-security, -submod-multimedia subpackages
- Implements http://refspecs.linux-foundation.org/LSB_4.1.0/ 
- Resolves:rh#800249: new package update review by Parag.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Parag <pnemade AT redhat DOT com> - 4.0-10
- Resolves:rh#758383:- redhat-lsb does not pull in required perl-Pod-Perldoc

* Wed Nov 30 2011 Parag <pnemade AT redhat DOT com> - 4.0-9
- Resolves:rh#738256:- redhat-lsb fails to build on ARM

* Thu Oct 13 2011 Parag <pnemade AT redhat DOT com> - 4.0-8
- Resolves:rh#745100: Add requires: perl-Digest-MD5

* Wed Oct 12 2011 Parag <pnemade AT redhat DOT com> - 4.0-7
- Resolves:rh#654689,rh#736822
- Added dependencies for perl-Locale-Codes and perl-Class-ISA

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 09 2010 Parag <pnemade AT redhat.com> - 4.0-5
- Fix directory ownership issue for %%{_sysconfdir}/lsb-release.d
- Fix duplicate files issue as reported in bodhi testing for 4.0-4

* Fri Jun 25 2010 Parag <pnemade AT redhat.com> - 4.0-4
- Revert license back to GPLv2

* Thu Jun 24 2010 Parag <pnemade AT redhat.com> - 4.0-3
- Resolves:rh#585858:-redhat-lsb-graphics broken

* Fri Jan 15 2010 Lawrence Lim <llim@redhat.com> - 4.0-2
- update spec file to split package into core, desktop and printing (Curtis Doty, #472633)

* Fri Jan 8 2010 Lawrence Lim <llim@redhat.com> - 4.0-1
- update to LSB4.0

* Tue Oct 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2-7
- apply fix from bz514760 (thanks to Jakub Jelinek)

* Wed Oct 21 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 3.2-6
- apply fix from bz485367 (thanks to Jon Thomas)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 24 2009 Jens Petersen <petersen@redhat.com>
- improve url to LSB WG

* Thu Apr 23 2009 Jens Petersen <petersen@redhat.com> - 3.2-4
- use dist tag (Debarshi, #496553)
- update to ix86 (caillon)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Hao Liu <hliu@redhat.com> 3.2-2
- Modify "Requires: /usr/bin/mailx" to "Requires: mailx" (Bug #460249)

* Wed Aug 20 2008 Hao Liu <hliu@redhat.com> 3.2-1
- Port forward to LSB 3.2
- Remove symlink for mailx if user is upgrading from the redhat-lsb of older version 
- Since F10 put mailx under /usr/bin, change the corresponding requires

* Tue Aug 5 2008 Hao Liu <hliu@redhat.com> - 3.1-22
- Remove 2 requires which provided by redhat-lsb
- Add comments explaining why hard-coded path is kept
- Resolve some hard-coded path problems
- Add comments explaining why importing '-static' option while compiling redhat_lsb_trigger
- Replace %%{_libdir}/lsb with /usr/lib/lsb
- Replace /%%{_lib}/* with /%%{_lib}/*so*
- Replace /lib/lsb with /lib/lsb*

* Thu Jul 31 2008 Lawrence Lim <llim@redhat.com> - 3.1-21
- remove symlink for mailx (Bug #457241)

* Wed Apr 16 2008 Mats Wichmann <mats@freestandards.org> 3.2-1
- port forward to LSB 3.2

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.1-20
- Autorebuild for GCC 4.3

* Wed Oct 3 2007 Lawrence Lim <llim@redhat.com> - 3.1-19
- fix build issue on ppc - (.opd+0x10): multiple definition of `__libc_start_main'

* Fri Sep 21 2007 Lawrence Lim <llim@redhat.com> - 3.1-18
- fix build issue in minimal build root (Bug #265241)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 3.1-17
- Rebuild for selinux ppc32 issue.

* Mon Aug 20 2007 Lawrence Lim <llim@redhat.com> - 3.1-16
- update spec file in accordance to feedback provided through merge review - merge-review.patch - #226363

* Wed Jul 18 2007 Lawrence Lim <llim@redhat.com> - 3.1-15.f8
- Resolved: #239842 - /lib/lsb/init-functions shall use aliases but not functions
- forward port the patch from 3.1-12.3.EL which fix #217566, #233530, #240916

* Wed Jul 4 2007 Lawrence Lim <llim@redhat.com> - 3.1-14.fc7
- fixed Bug 232918 for new glibc version

* Tue Jun 26 2007 Lawrence Lim <llim@redhat.com> - 3.1-12.3.EL
- Resolves: #217566 - rewrite /lib/lsb/init-functions file needs to define the commands as true shell functions rather than aliases.
- Resolves: #233530 - LSB pidofproc misspelled as pidofprof.
- Resolves: #240916 - "log_warning_message" replaced with "log_warning_msg" per the LSB 3.1 spec

* Wed Dec 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-12.2.EL
- Resolves: bug 217566
- revise patch

* Wed Nov 29 2006 Lawrence Lim <llim@redhat.com> - 3.1-12
- replaced aliases with functions in /lib/lsb/init-functions; Bug 217566

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 3.1-11
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.3
- Fix upgrade issue; Bug 202548 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.1-10.2.1
- rebuild

* Thu Jul 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.2
- for some strange reason, ld-lsb-x86-64.so need to be ld-lsb-x86-64.so.3 (LSB3.0) rather than ld-lsb-x86-64.so.3.1 (LSB3.1)

* Thu Jul 6 2006 Lawrence Lim <llim@redhat.com> - 3.1-10.1
- generate spec file on RHEL5-Alpha system
- fix vsw4 test suite setup by creating symlink for X11 SecurityPolicy and XFontPath

* Thu Jun 22 2006 Lawrence Lim <llim@redhat.com> - 3.0-10
- Rewrite most part of the mkredhat-lsb to obtain information directly via specdb 
  rather than sniffing through sgml
- remove redundent script and bump up tarball version

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.0-9.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0-9.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 13 2006 Leon Ho <llch@redhat.com> 3.0-9
- Migrated back to rawhide

* Wed Aug  3 2005 Leon Ho <llch@redhat.com> 3.0-8.EL
- Added libstdc++.so.6/libGL.so.1 requirement (RH#154605)

* Wed Aug  3 2005 Leon Ho <llch@redhat.com> 3.0-7.EL
- Fixed multilib problem on lsb_release not to read /etc/lsb-release and solely
  depends on /etc/lsb-release.d/ (Advised by LSB committee)
- Removed /etc/lsb-release (Advised by LSB committee)

* Mon Aug  1 2005 Leon Ho <llch@redhat.com> 3.0-6.EL
- Made the /etc/lsb-release useful (RH#154605)
- Added redhat_lsb_trigger to fix RH#160585 (Jakub Jelinek)
- Fixed AMD64 base libraries requirement parsing (RH#154605)

* Tue Jul 26 2005 Leon Ho <llch@redhat.com> 3.0-5.EL
- Fixed redhat-lsb's mkredhat-lsb on fetching lib and 
  cmd requirements

* Mon Jul 18 2005 Leon Ho <llch@redhat.com> 3.0-4.EL
- Rebuilt

* Tue Jul 05 2005 Leon Ho <llch@redhat.com> 3.0-3.EL
- Disabled support for LSB 1.3 and 2.0

* Mon Jun 20 2005 Leon Ho <llch@redhat.com> 3.0-2.EL
- Upgraded to lsb-release 2.0

* Thu Jun 09 2005 Leon Ho <llch@redhat.com> 3.0-1.EL
- Moved to LSB 3.0

* Wed Apr 13 2005 Leon Ho <llch@redhat.com> 1.3-10
- Fixed ix86 package with ia32 emul support 

* Tue Feb 01 2005 Leon Ho <llch@redhat.com> 1.3-9
- Sync what we have changed on the branches
  Wed Nov 24 2004 Harald Hoyer <harald@redhat.com>
  - added post section to recreate the softlink in emul mode (bug 140739)
  Mon Nov 15 2004 Phil Knirsch <pknirsch@redhat.com>
  Tiny correction of bug in new triggers

* Mon Jan 24 2005 Leon Ho <llch@redhat.com> 1.3-8
- Add support provide on lsb-core-* for each arch

* Fri Jan 21 2005 Leon Ho <llch@redhat.com> 1.3-7
- Add to support multiple LSB test suite version
- Add %%endif in trigger postun

* Thu Nov 11 2004 Phil Knirsch <pknirsch@redhat.com> 1.3-6
- Fixed invalid sln call for trigger in postun on ia64 (#137647)

* Mon Aug 09 2004 Phil Knirsch <pknirsch@redhat.com> 1.3-4
- Bump release and rebuilt for RHEL4.

* Thu Jul 24 2003 Matt Wilson <msw@redhat.com> 1.3-3
- fix lsb ld.so name for ia64 (#100613)

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.3-2
- use /usr/lib/lsb for install_initd, remove_initd

* Fri May 23 2003 Matt Wilson <msw@redhat.com> 1.3-2
- add ia64 x86_64 ppc ppc64 s390 s390x

* Tue Feb 18 2003 Matt Wilson <msw@redhat.com> 1.3-1
- 1.3

* Wed Sep  4 2002 Matt Wilson <msw@redhat.com>
- 1.2.0

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Mar 27 2002 Matt Wilson <msw@redhat.com>
- addeed trigger on glibc to re-establish the ld-lsb.so.1 symlink in the
  forced downgrade case.

* Tue Mar 12 2002 Bill Nottingham <notting@redhat.com>
- add initscripts support

* Thu Jan 24 2002 Matt Wilson <msw@redhat.com>
- Initial build.
