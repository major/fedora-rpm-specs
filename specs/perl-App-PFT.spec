%global module App-PFT

Name:           perl-%{module}
Version:        1.4.1
Release:        17%{?dist}
Summary:        Hacker friendly static blog generator

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/dacav/%{module}
Source0:        https://github.com/dacav/%{module}/archive/v%{version}.tar.gz#/%{module}-%{version}.tar.gz

# This software packet is composed by a toolkit of executable scripts, which
# are chain loaded by a main script named 'pft`. The position of the scripts is
# determined by using perl(FindBin). If the package is installed via CPAN it
# makes sense to seek for the scripts in the same directory as the library. For
# the Fedora package the appropriate position is /usr/libexec/%%{module}.
# The following patch makes it compliant with this requirement without breaking
# the desirable behavior in the CPAN distribution.
Patch0:         %{name}.libexec.patch

BuildArch:      noarch
Provides:       pft = %{version}-%{release}

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

# Generated BuildRequires via the following command:
# tangerine -c Makefile.PL bin lib t | perl -nE '/^\s/ and next; s/^/BuildRequires:  perl(/; s/$/)/; print'

BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Escape)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(PFT)
BuildRequires:  perl(PFT::Conf)
BuildRequires:  perl(PFT::Date)
BuildRequires:  perl(PFT::Header)
BuildRequires:  perl(PFT::Text)
BuildRequires:  perl(PFT::Tree)
BuildRequires:  perl(PFT::Util)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Template::Alloy)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
PFT stands for *Plain F. Text*, where the meaning of *F.* is up to
personal interpretation. Like *Fancy* or *Fantastic*.

It is yet another static website generator. This means your content is
compiled once and the result can be served by a simple HTTP server,
without need of server-side dynamic content generation.


%prep
%autosetup -n %{module}-%{version} -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}


%install
%{__make} pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} %{buildroot}/*
%{__install} -d %{buildroot}%{_libexecdir}/%{name}
%{__install} -d %{buildroot}%{_datadir}/bash-completion/completions
%{__install} -t %{buildroot}%{_datadir}/bash-completion/completions bash_completion.d/pft

%{__mv} "%{buildroot}%{_bindir}/pft-clean"   "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-edit"    "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-gen-rss" "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-grab"    "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-init"    "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-ls"      "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-make"    "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-pub"     "%{buildroot}%{_libexecdir}/%{name}"
%{__mv} "%{buildroot}%{_bindir}/pft-show"    "%{buildroot}%{_libexecdir}/%{name}"

%check
LC_ALL=C.UTF-8 make test


%files
%{!?_licensedir:%global license %%doc}
%doc %{_mandir}/man1/*.1*
%doc README.md
%{perl_vendorlib}/*
%{_bindir}/pft
%{_libexecdir}/%{name}/pft-clean
%{_libexecdir}/%{name}/pft-edit
%{_libexecdir}/%{name}/pft-gen-rss
%{_libexecdir}/%{name}/pft-grab
%{_libexecdir}/%{name}/pft-init
%{_libexecdir}/%{name}/pft-ls
%{_libexecdir}/%{name}/pft-make
%{_libexecdir}/%{name}/pft-pub
%{_libexecdir}/%{name}/pft-show
%{_datadir}/bash-completion/completions/pft
%license COPYING


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.1-16
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.1-9
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.1-6
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.4.1-3
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Giovanni Simoni <dacav@teknik.io> - 1.4.1-1
- Release 1.4.1

* Wed Jul 24 2019 Giovanni Simoni <dacav@teknik.io> - 1.4.0-1
- Release 1.4.0

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.2-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.2-5
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.2-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 11 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.2-1
- Release 1.2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.2.0-2
- Perl 5.26 rebuild

* Mon May 08 2017 dacav <dacav@openmailbox.org> - 1.2.0-1
- Release 1.2.0

* Wed Mar 01 2017 dacav <dacav@openmailbox.org> - 1.1.2-1
- Release 1.1.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 dacav <dacav@openmailbox.org> - 1.1.0-3
- Added "pft" as Provides

* Thu Dec 29 2016 dacav <dacav@openmailbox.org> - 1.1.0-2
- Fixed source name

* Tue Dec 27 2016 dacav@openmailbox.org - 1.1.0-1
- Release 1.1.0

* Thu Sep 29 2016 dacav@openmailbox.org - 1.0.6-2
- Fixed patch description
- Removed explicit dependency

* Sat Sep 03 2016 <dacav@openmailbox.org> - 1.0.6-1
- Release 1.0.6

* Wed Aug 24 2016 <dacav@openmailbox.org> - 1.0.5-4
- Generated BuildRequires with tangerine.
- Fixed changelog

* Tue Aug 23 2016 <dacav@openmailbox.org> - 1.0.5-3
- Fixes as by Bug 1368790 in bugzilla.redhat.com

* Sun Aug 14 2016 <dacav@openmailbox.org> - 1.0.5-2
- Fixed changelog

* Sun Aug 14 2016 <dacav@openmailbox.org> - 1.0.5-1
- Release v1.0.5

* Sat Jul 23 2016 <dacav@openmailbox.org>
- Patches from github according to version tag

* Tue Jun 21 2016 <dacav@openmailbox.org> 1.0.2-1
- Moved transitive call binaries in /usr/libexec

* Mon Jun 20 2016 <dacav@openmailbox.org> 1.0.2-1
- First packaging
