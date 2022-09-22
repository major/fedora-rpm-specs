%global BR_PERL6_VENDOR %{buildroot}%{perl6_vendor_dir}


Name:		rakudo-zef
Version:	0.8.2
Release:	7%{?dist}
Summary:	Perl6 Module Management

License:	Artistic 2.0
URL:		https://github.com/ugexe/zef
Source0:	%url/archive/v%{version}.tar.gz

# Build
BuildRequires:	coreutils sed
# includes pod2man 
BuildRequires:	perl-podlators
# includes prove
BuildRequires:	perl-Test-Harness
BuildRequires:	rakudo >= %rakudo_rpm_version

# needed for testing with the 'zef install' command
Requires:	perl-Test-Harness
Requires:	rakudo >= %rakudo_rpm_version


%description
Zef is a Perl6 module manager that query, download, update and install modules
from of a file path (starting with . or /), URNs, URLs, paths, or identities
from the Perl6 modules directory: https://modules.perl6.org/
It automates and simplifies the installation. Depending on your privileges zef
installs the modules at the system directories or at the home directory in
'.perl6' or if you specify a destination then to that destination directory.


%prep
%setup -q -n zef-%{version}


%install
#RAKUDO_RERESOLVE_DEPENDENCIES=0 ... ??
%perl6_mod_inst --to=%{BR_PERL6_VENDOR} --for=vendor

%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} %{perl6_vendor_dir}/bin/zef %{buildroot}%{_bindir}/zef

%{__sed} -i -e '1 s/env perl6/perl6/' %{BR_PERL6_VENDOR}/bin/zef
%{__sed} -i -e '1 s/env perl6-m/rakudo/' %{BR_PERL6_VENDOR}/bin/zef-m

# Generating man-page
%{__mkdir_p} %{buildroot}%{_mandir}/man1
pod2man --section=1 --name=zef README.pod > %{buildroot}%{_mandir}/man1/zef.1

# perl6 on JVM or JavaScript is currently not included at Fedora
%{__rm} -f %{buildroot}%{perl6_vendor_dir}/bin/zef-j*


%check
prove -e '%{__perl6} -Ilib'


%files
%doc README.pod
%license LICENSE
%{_bindir}/zef
%{perl6_vendor_dir}/*/*

%{_mandir}/man1/zef.1*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.8.2-1
- update to 0.8.2
- QA_SKIP_BUILD_ROOT no longer used

* Wed Mar 20 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.7.1-1
- update to 0.7.1
- add 'export QA_SKIP_BUILD_ROOT=1'
- exclude zef-j* (zef-j and zef-js)

* Tue Oct 30 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.5.3-1
- update to 0.5.3

* Fri Apr 27 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2.9-2
- to exclude the architectures s390x ppc64 is not neccesary any more

* Fri Apr 27 2018 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.2.9-1
- update to 0.2.9

* Wed Oct 11 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.1.30-1
- use prove command in check session
- add perl-Test-Harness for BuildRequires and Requires
- update to 0.1.30

* Fri Sep 15 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.1.29-1
- get the sources from Github
- need to exclude the architectures: s390x ppc64
- update to 0.1.29

* Fri Jun 30 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.1.15-1
- get the sources from the Perl6 directory of CPAN

* Mon Jun 19 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.20170619git.48efafc-2
- added check-section
- switched to install with the 'tools/install-dist.pl' script from the rakudo sources
- install to vendor_dir

* Mon Jun 19 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.20170619git.48efafc-1
- remove QA_SKIP_BUILD_ROOT variable
- split installation in two steps
- add information of the creating of the tar archive
- rename the package to rakudo-zef
- update to 0.20170619git.48efafc

* Mon Jun 12 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.20170520git.1490608-4
- use the new perl6 rpm build macros provided from the rakudo package

* Fri Jun 02 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.20170520git.1490608-3
- add macros for rakudo
- use macros where possible
- the manpage is not explicitly gzipped any more
- add BR: coreutils sed and perl-podlators

* Sat May 20 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 0.20170520git.1490608-1 
- create initail spec file
