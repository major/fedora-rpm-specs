# -*- rpm-spec -*-

################ Build Options ###################
%define dbtests 1
%{?_with_dbtests:    %{expand: %%global dbtests 1}}
%{?_without_dbtests: %{expand: %%global dbtests 0}}
%define debug_package %{nil}
################ End Build Options ################

Name: EekBoek
Summary: Bookkeeping software for small and medium-size businesses
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 2.051
Release: 12%{?dist}
Source: https://www.eekboek.nl/dl/%{name}-%{version}.tar.gz
URL: https://www.eekboek.nl

# The package name is CamelCased. However, for convenience some
# of its data is located in files and directories that are all
# lowercase. See the %%install section.
%global lcname eekboek

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# note intended for general use.
AutoReqProv: 0

Requires: perl-interpreter
Requires: perl-generators
Requires: perl(:VERSION) >= 5.10.1
Requires: perl(Archive::Zip)
Requires: perl(HTML::Parser)
Requires: perl(Term::ReadLine)
Requires: perl(Term::ReadLine::Gnu)
Requires: perl(DBI) >= 1.40
Requires: perl(DBD::SQLite) >= 1.12
Requires: perl(App::Packager) >= 1.430

BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.5503
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(Archive::Zip)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(Term::ReadLine)
BuildRequires: perl(Term::ReadLine::Gnu)
BuildRequires: perl(DBI) >= 1.40
BuildRequires: perl(DBD::SQLite) >= 1.12
BuildRequires: perl(App::Packager) >= 1.430
BuildRequires: perl(Test::More)
BuildRequires: desktop-file-utils
BuildRequires: zip
BuildRequires: make

Obsoletes: %{name}-core < 2.00.01
Obsoletes: %{name}-contrib < 2.00.01
Conflicts: %{name}-core < 2.00.01

# For symmetry.
%global __zip   /usr/bin/zip
%global __rmdir /bin/rmdir
%global __find  /usr/bin/find

%description
EekBoek is a bookkeeping package for small and medium-size businesses.
Unlike other accounting software, EekBoek has both a command-line
interface (CLI) and a graphical user-interface (GUI, currently under
development and not included in this package). Furthermore, it has a
complete Perl API to create your own custom applications. EekBoek is
designed for the Dutch/European market and currently available in
Dutch only. An English translation is in the works (help appreciated).

EekBoek can make use of several database systems for its storage.
Support for the SQLite database is included.

For GUI support, install %{name}-gui.

For production use, you are invited to install the %{name}-db-postgresql
database package.

%package gui

Summary: %{name} graphical user interface
AutoReqProv: 0

Requires: %{name} = %{version}-%{release}
Requires: perl(Wx) >= 0.99

%description gui
This package contains the wxWidgets (GUI) extension for %{name}.

%package db-postgresql

# This package only contains the necessary module(s) for EekBoek
# to use the PostgreSQL database.
# Installing this package will pull in the main package and
# the Perl PostgreSQL modules, if necessary.
# No %%doc required.

Summary: PostgreSQL database driver for %{name}
AutoReqProv: 0
Requires: %{name} = %{version}-%{release}
Requires: perl(DBD::Pg) >= 1.41

%description db-postgresql
EekBoek can make use of several database systems for its storage.
This package contains the PostgreSQL database driver for %{name}.

%prep
%setup -q

chmod 0664 MANIFEST

%build
%{__perl} Makefile.PL
make

# Move some files into better places.
%{__mkdir} examples
%{__mv} emacs/eekboek-mode.el examples

%install
%{__rm} -rf %{buildroot}

# Short names for our libraries.
%global ebconf  %{_sysconfdir}/%{lcname}
%global ebshare %{_datadir}/%{name}-%{version}

%{__mkdir_p} %{buildroot}%{ebconf}
%{__mkdir_p} %{buildroot}%{ebshare}/lib
%{__mkdir_p} %{buildroot}%{_bindir}

# Install the default, system-wide config file.
%{__install} -p -m 0644 blib/lib/EB/examples/%{lcname}.conf %{buildroot}%{ebconf}/%{lcname}.conf

# Create lib dirs and copy files.
%{__find} blib/lib -type f -name .exists -delete
%{__find} blib/lib -depth -type d -name auto -exec rm -fr {} \;
%{__find} blib/lib -type d -printf "%{__mkdir} %{buildroot}%{ebshare}/lib/%%P\n" | sh -x
%{__find} blib/lib ! -type d -printf "%{__install} -p -m 0644 %p %{buildroot}%{ebshare}/lib/%%P\n" | sh -x

for script in ebshell ebwxshell
do

  # Create the main scripts.
  echo "#!%{__perl}" > %{buildroot}%{_bindir}/${script}
  %{__sed} -s "s;# use lib qw(EekBoekLibrary;use lib qw(%{ebshare}/lib;" \
    < script/${script} >> %{buildroot}%{_bindir}/${script}
  %{__chmod} 0755 %{buildroot}%{_bindir}/${script}

  # And its manual page.
  %{__mkdir_p} %{buildroot}%{_mandir}/man1
  pod2man blib/script/${script} > %{buildroot}%{_mandir}/man1/${script}.1

done

# Desktop file, icons, ...
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__install} -p -m 0664 lib/EB/res/Wx/icons/ebicon.png %{buildroot}%{_datadir}/pixmaps/
for script in ebwxshell
do
  desktop-file-install --delete-original \
    --dir=%{buildroot}%{_datadir}/applications ${script}.desktop
  desktop-file-validate %{buildroot}/%{_datadir}/applications/${script}.desktop
done

# End of install section.

%check
%if %{dbtests}
make test
%else
env EB_SKIPDBTESTS=1 make test
%endif

%files
%doc CHANGES README examples/
%dir %{_sysconfdir}/%{lcname}
%config(noreplace) %{_sysconfdir}/%{lcname}/%{lcname}.conf
%{ebshare}/
%exclude %{ebshare}/lib/EB/DB/Postgres.pm
%exclude %{ebshare}/lib/EB/Wx
%{_bindir}/ebshell
%{_mandir}/man1/ebshell*

%files gui
%doc README.gui
%{ebshare}/lib/EB/Wx
%{_bindir}/ebwxshell
%{_mandir}/man1/ebwxshell*
%{_datadir}/applications/ebwxshell.desktop
%{_datadir}/pixmaps/ebicon.png

%files db-postgresql
%doc README.postgres
%{ebshare}/lib/EB/DB/Postgres.pm

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 2.051-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.051-3
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.051-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 Johan Vromans <jvromans@squirrel.nl> - 2.051-1
- Upgrade to upstream 2.051.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.04-3
- Perl 5.34 rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Johan Vromans <jvromans@squirrel.nl> - 2.04-1
- Upgrade to upstream 2.04.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-12
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-9
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Scott Talbert <swt@techie.net> - 2.03-7
- Remove dependency on wxWidgets.  wxWidgets is pulled in by perl(Wx).

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.03-5
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Johan Vromans <jvromans@squirrel.nl> - 2.03-3
- Updates to spec file according to guidelines.

* Tue Sep 26 2017 Johan Vromans <jvromans@squirrel.nl> - 2.03-2
- Updates to spec file according to guidelines.
- Fix FSF address.

* Sat Sep 23 2017 Johan Vromans <jvromans@squirrel.nl> - 2.03-1
- Upgrade to upstream 2.03.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.05.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Johan Vromans <jvromans@squirrel.nl> - 2.02.05.6-4
- Upgrade to upstream 2.02.05.6.

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 2.02.05-3
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 09 2016 Johan Vromans <jvromans@squirrel.nl> - 2.02.05-1
- Upgrade to upstream 2.02.05 (emergency bugfix).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.02.02-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.02-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 16 2014 Richard Hughes <richard@hughsie.com> - 2.02.02-5
- Do not create the invalid path /usr/share/locale/en/LC_MESSAGES/LC_MESSAGES

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.02-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.02-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Aug 02 2013 Petr Pisar <ppisar@redhat.com> - 2.02.02-2
- Perl 5.18 rebuild

* Tue Jun 11 2013 Johan Vromans <jvromans@squirrel.nl> - 2.02.02-1
- Upgrade to upstream 2.02.02.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.00-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 21 2012 Johan Vromans <jvromans@squirrel.nl> - 2.02.00-1
- Upgrade to upstream 2.02.00.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Johan Vromans <jvromans@squirrel.nl> - 2.00.04-1
- Upgrade to upstream 2.00.04.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Mar 22 2011 Johan Vromans <jvromans@squirrel.nl> - 2.00.03-1
- Upgrade to upstream 2.00.03.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 06 2010 Johan Vromans <jvromans@squirrel.nl> - 2.00.02-1
- Upgrade to upstream 2.00.02.

* Mon Mar 29 2010 Johan Vromans <jvromans@squirrel.nl> - 2.00.01-3
- More Obsoletes.

* Mon Mar 29 2010 Johan Vromans <jvromans@squirrel.nl> - 2.00.01-2
- Fix duplicate %%description.
- Fix BuildRequires and Obsoletes.

* Sun Mar 28 2010 Johan Vromans <jvromans@squirrel.nl> - 2.00.01-1
- Upgrade to upstream 2.00.01.

* Sat Mar 27 2010 Johan Vromans <jvromans@squirrel.nl> - 2.00.00-2
- Repackage according to user concensus.

* Tue Mar 23 2010 Johan Vromans <jvromans@squirrel.nl> - 2.00.00-1
- Upgrade to upstream 2.00.00.

* Mon Feb 08 2010 Johan Vromans <jvromans@squirrel.nl> - 1.05.20-1
- Upgrade to upstream 1.05.20.

* Sat Jan 16 2010 Johan Vromans <jvromans@squirrel.nl> - 1.05.16-1
- Upgrade to upstream 1.05.16.

* Fri Jan 15 2010 Johan Vromans <jvromans@squirrel.nl> - 1.05.15-2
- Add missing file to db-postgres package.

* Fri Jan 15 2010 Johan Vromans <jvromans@squirrel.nl> - 1.05.15-1
- Upgrade to upstream 1.05.15.

* Fri Jan 15 2010 Johan Vromans <jvromans@squirrel.nl> - 1.05.14-1
- Upgrade to upstream 1.05.14.
- Re-structure the package into several subpackages.

* Wed Jan 06 2010 Johan Vromans <jvromans@squirrel.nl> - 1.04.06-1
- Upgrade to upstream 1.04.06.

* Mon Dec 28 2009 Johan Vromans <jvromans@squirrel.nl> - 1.04.05-2
- Fix for table detection with newer SQLite.

* Mon Dec 28 2009 Johan Vromans <jvromans@squirrel.nl> - 1.04.05-1
- Upgrade to upstream 1.04.05.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Johan Vromans <jvromans@squirrel.nl> - 1.04.04-1
- Upgrade to upstream 1.04.04.
- Obsolete script patch.
- Obsolete conversion to UTF-8 of README.

* Wed Apr 22 2009 Johan Vromans <jvromans@squirrel.nl> - 1.04.03-3
- Remove Epoch: since it it not needed.
- Make subpackage depend on EVR.

* Mon Apr 20 2009 Johan Vromans <jvromans@squirrel.nl> - 1:1.04.03-2
- Use Epoch: to tighten dependency between basepackage and subpackage.
- Use %%global instead of %%define.
- Provide README.postgres as source, not as a patch.
- Keep timestamps when copying and installing.
- Simplify filelist building.
- Remove INSTALL from %%doc.

* Fri Apr 17 2009 Johan Vromans <jvromans@squirrel.nl> - 1.04.03-1
- Upgrade to upstream 1.04.03.
- Include SQLite with the base package.
- Enable database tests since we now require a db driver.

* Fri Jan 30 2009 Johan Vromans <jvromans@squirrel.nl> - 1.04.02-1
- Adapt to Fedora guidelines

* Mon Jan 26 2009 Johan Vromans <jvromans@squirrel.nl> - 1.04.02
- Remove QUICKSTART.

* Sat Jul 19 2008 Johan Vromans <jvromans@squirrel.nl> - 1.03.90
- Remove debian stuff
- Don't use unstable.

* Fri Apr 11 2008 Johan Vromans <jvromans@squirrel.nl> - 1.03.12
- Simplify by setting variables from the .in template

* Sun Apr 01 2007 Johan Vromans <jvromans@squirrel.nl> - 1.03.03
- Exclude some Wx files.

* Sun Nov 05 2006 Johan Vromans <jvromans@squirrel.nl> - 1.03.00
- Move DB drivers to separate package, and adjust req/prov.

* Mon Oct 16 2006 Johan Vromans <jvromans@squirrel.nl> - 1.01.02
- Prepare (but don't use) suffixes to separate production and unstable versions.

* Wed Aug 02 2006 Johan Vromans <jvromans@squirrel.nl> 0.92
- New URL. Add Vendor.

* Fri Jun 09 2006 Johan Vromans <jvromans@squirrel.nl> 0.60
- Remove man3.

* Thu Jun 08 2006 Johan Vromans <jvromans@squirrel.nl> 0.60
- Fix example.

* Mon Jun 05 2006 Johan Vromans <jvromans@squirrel.nl> 0.59
- Better script handling.

* Mon Apr 17 2006 Johan Vromans <jvromans@squirrel.nl> 0.56
- Initial provisions for GUI.

* Wed Apr 12 2006 Johan Vromans <jvromans@squirrel.nl> 0.56
- %%config(noreplace) for eekboek.conf.

* Tue Mar 28 2006 Johan Vromans <jvromans@squirrel.nl> 0.52
- Perl Independent Install

* Mon Mar 27 2006 Johan Vromans <jvromans@squirrel.nl> 0.52
- Add "--with dbtests" parameter for rpmbuild.
- Resultant rpm may be signed.

* Sun Mar 19 2006 Johan Vromans <jvromans@squirrel.nl> 0.50
- Switch to Build.PL instead of Makefile.PL.

* Mon Jan 30 2006 Johan Vromans <jvromans@squirrel.nl> 0.37
- Add build dep perl(Config::IniFiles).

* Fri Dec 23 2005 Wytze van der Raay <wytze@nlnet.nl> 0.23
- Fixes for x86_64 building problems.

* Mon Dec 12 2005 Johan Vromans <jvromans@squirrel.nl> 0.22
- Change some wordings.
- Add man1.

* Sun Dec 11 2005 Johan Vromans <jvromans@squirrel.nl> 0.21
- Add INSTALL QUICKSTART

* Thu Dec 08 2005 Johan Vromans <jvromans@squirrel.nl> 0.20
- Include doc/html.

* Tue Nov 22 2005 Johan Vromans <jvromans@squirrel.nl> 0.19
- More.

* Sun Nov 20 2005 Jos Vos <jos@xos.nl> 0.17-XOS.0beta1
- Initial version.
