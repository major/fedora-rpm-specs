%define debug_package %{nil}


%global year 2020
%global month 07


Name:		nqp
Version:	0.0.%{year}.%{month}
Release:	5%{?dist}
Summary:	Not Quite Perl (6)

License:	Artistic 2.0 and ISC and WTFPL
URL:		https://github.com/Raku/nqp
Source0:	https://github.com/Raku/nqp/releases/download/%{year}.%{month}/nqp-%{year}.%{month}.tar.gz
# https://github.com/perl6 -> https://github.com/Raku
#https://rakudo.org/dl/nqp/nqp-2020.02.tar.gz

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	libuv-devel
BuildRequires:	libatomic_ops-devel
BuildRequires:	libffi-devel
BuildRequires:	libtommath-devel
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(ExtUtils::Command)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)

BuildRequires:	moarvm, moarvm-devel >= 0.%{year}.%{month}

Requires:	moarvm >= 0.%{year}.%{month}


%description
This is "Not Quite Perl" -- a lightweight Perl 6-like environment for virtual
machines. The key feature of NQP is that it's designed to be a very small
environment (as compared with, say, perl6 or Rakudo) and is focused on being
a high-level way to create compilers and libraries for virtual machines (such
as JVM and MoarVM). Unlike a full-fledged implementation of Perl 6, NQP
strives to have as small a run-time footprint as it can, while still providing
a Perl 6 object model and regular expression engine for the virtual machine.


#--

%package doc
Summary:	Documentation for Not Quite Perl (6)

BuildArch:	noarch


%description doc
Documentation and also examples about NQP.

#--


%prep
%setup -q -n %{name}-%{year}.%{month}


%build

rm -r 3rdparty/jna	# make sure not to bundle 'jna'
# src/vm/jvm/runners/nqp-j.bat	this file is only for windows


# prevent rpmlint errors in the doc subpackage
find examples -maxdepth 1 -name "*.nqp" \
     -exec %{__sed} -i -e '1 s&#!.*\(nqp\)&#!/usr/bin/\1&' {} \;
# convert Windows newlines to Linx format (CR-LF -> LF)
%{__perl} -pi -e 's/\r\n$/\n/g' examples/rubyish/t/recursion.t \
      examples/rubyish/examples-rubyish/fractal-tree.rbi \
      examples/rubyish/t/bitwise.t docs/ops.markdown \
      examples/rubyish/t/inheritance.t examples/rubyish/t/line-spanning.t \
      examples/rubyish/examples-rubyish/closure.rbi
# correct file mode bits to prevent rpmlint warning
%{__chmod} 644 docs/ops.markdown

%{__perl} Configure.pl --backends=moar --prefix=%{_usr}

CFLAGS="$RPM_OPT_FLAGS -fPIC" %{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT


%check
%{?!_without_tests: make test}


%files
%doc CREDITS README.pod
%license LICENSE
%{_bindir}/nqp
%{_bindir}/nqp-m
%{_datadir}/nqp


%files doc
%doc docs examples


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.07-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2020.07-1
- update to 2020.07

* Wed Aug 12 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2020.02-4
- add BuildRequies perl(FindBin) and perl(lib)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.02-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 24 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2020.02-1
- update to 2020.02

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2019.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2019.07.1-1
- update to 2019.11
- the configuration option --libdir can no longer be used (_libdir/nqp -> _datadir/nqp)
- BuildRequires gcc, libuv-devel, libatomic_ops-devel, libffi-devel needed

* Fri Oct 04 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2019.07.1-1
- update to 2019.07.1
- build on epel8
- add the perl dependencies Data::Dumper and IPC::Cmd
- refer to the source from github

* Tue Mar 19 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2019.03-1
- update to 2019.03

* Mon Oct 29 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2018.10-1
- update to 2018.10

* Mon Apr 30 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2018.04.1-1
- follow the change of the source URL from upstream
- all tests passes

* Wed Apr 25 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2018.04-1
- nqp builds again on all primary architectures
- add BuildRequires for perl-Digest-SHA
- update to 2018.04

* Mon Aug 28 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2017.08-2
- add symlink to template.html in datadir

* Tue Aug 22 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2017.08-1
- exclude architectures s390x ppc64
- update to 2017.08

* Sun Jun 18 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2017.06-1
- update to 2017.06

* Mon May 08 2017  Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2017.04-4
- rebuild with changed moarvm build

* Fri Apr 28 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2017.04-1
- update to 2017.04 

* Wed Feb 01 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2017.01-2
- remove jvm subpackage
- build architecture dependent
- add libdir configuration option
- add license macro
- disable debug package

* Wed Feb 01 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2017.01-1
- update to 2017.01

* Tue Jan 17 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2016.11-2
- better support updates with version dependent require for moarvm

* Sat Dec 10 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2016.11-1
- also build for epel7
- update to 2016.11

* Sun Jul 24 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2016.07-2
- bundle jna again, because building rakudo on top off it would not work

* Tue Jul 19 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2016.07-1
- remove commands to not bundle 'jna' rather use the new configuration
  option --with-jna
- update to 2016.07

* Fri Feb 26 2016 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2016.02-1
- update to 2016.02

* Mon Dec 07 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2015.11-3
- do not bundle 'jna'

* Tue Dec 01 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2015.11-1
- jvm subpackage builds on all architectures
- update 2015.11

* Mon Sep 28 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2015.09.1-1
- update to 2015.09.1

* Sun May 24 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2015.05-1
- update to 2015.05

* Thu Apr 30 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2015.04-3
- add subpackage doc
- define __jar_repack nil

* Wed Apr 29 2015 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2015.04-2
- build architecture independent

* Fri Aug 15 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2014.04-1
- update to 20014.04

* Fri Apr 04 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2014.03-4
- add subpackage jvm

* Fri Apr 04 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2014.03-3
- add a comment while not all libtommath source files are deleted

* Thu Apr 03 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2014.03-2
- add deleting of libtommath source files in prep section

* Thu Apr 03 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2014.03-1
- update to 20014.03
- run tests only on x86_64 architecture
- add flag has-libtommath to Configure.pl and a patch for it

* Wed Feb 19 2014 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2014.01-1
- update to 20014.01
- rebuild for new ICU
- the executable is renamed from nqp to nqp-p

* Fri Oct 04 2013 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2013.09-1
- update to 20013.09
- add docs and examples directories to dokumentation files

* Thu Jan 31 2013 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2013.01-1
- update to 2013.01
- add additional header files
- change the source to the new URL

* Wed Nov 07 2012 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2012.10-1
- update to 2012.10

* Wed Nov  7 2012 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.2012.08.1-2
- compile with distro CFLAGs and -fPIC

* Mon Sep 03 2012 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2012.08.1-1
- update to 2012.08.1

* Tue Aug 14 2012 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2012.07-5
- added check section
- removed clean section
- added ISC to License tag

* Mon Aug 13 2012 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2012.07-4
- changed License tag  
- removed defattr

* Mon Aug 13 2012 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2012.07-3
- replaced "define" with "global"
- removed BuildRoot tag

* Wed Aug 08 2012 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2012.07-2
- fixed description error from rpmlint

* Tue Aug 07 2012 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.0.2012.07-1
- did not build with _smp_mflags
- initial .spec file created
