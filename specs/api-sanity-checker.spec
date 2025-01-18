%global commit ed74fbc05c007696b31db207d44af1372067ccf9

Name:           api-sanity-checker
Version:        1.98.7
Release:        22%{?dist}
Summary:        An automatic generator of basic unit tests for a shared C/C++ library

License:        GPL-2.0-only
URL:            http://forge.ispras.ru/projects/api-sanity-autotest
# https://github.com/lvc/api-sanity-checker/archive/%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  abi-compliance-checker >= 1.98.7
BuildRequires:  coreutils
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  sed
Requires:       abi-compliance-checker >= 1.98.7
Requires:       binutils

%{?perl_default_filter}

%description
API Sanity Checker (ASC) is an automatic generator of basic unit tests for
shared C/C++ libraries. It is able to generate reasonable (in most, but
unfortunately not all, cases) input data for parameters and compose simple
("sanity" or "shallow"-quality) test cases for every function in the API through
the analysis of declarations in header files. The quality of generated tests
allows to check absence of critical errors in simple use cases. The tool is able
to build and execute generated tests and detect crashes (segfaults), aborts, all
kinds of emitted signals, non-zero program return code and program hanging. It
may be considered as a tool for out-of-the-box low-cost sanity checking
(fuzzing) of the library API or as a test development framework for initial
generation of templates for advanced tests. Also it supports universal format of
tests, random test generation mode, specialized data types and other useful
features.


%prep
%autosetup
chmod -x LICENSE


%build
# Nothing to build.


%install
mkdir -p %{buildroot}%{_bindir}
perl ./Makefile.pl -install --destdir=%{buildroot} --prefix=%{_prefix}

# Create a man page.
mkdir -p %{buildroot}%{_mandir}/man1
help2man -h --info -o %{buildroot}%{_mandir}/man1/api-sanity-checker.1 \
         -N %{buildroot}%{_bindir}/api-sanity-checker
sed -i 's|API(1)|API-SANITY-CHECKER(1)|g' %{buildroot}%{_mandir}/man1/api-sanity-checker.1
sed -i '3,5d' %{buildroot}%{_mandir}/man1/api-sanity-checker.1


%files
%license LICENSE
%doc README doc/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr 10 2023 Richard Shaw <hobbes1069@gmail.com> - 1.98.7-17
- Migrate to SPDX license format.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.98.7-10
- Specify all dependencies

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.98.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep  8 2015 Richard Shaw <hobbes1069@gmail.com> - 1.98.7-1
- Update to latest upstream release.
- Update spec to use license macro on supported branches.
- Remove upstreamed patch.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 27 2015 Richard Shaw <hobbes1069@gmail.com> - 1.98.6-3
- Fix non-standard permissions on binary (BZ#1131946).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.98.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar  4 2014 Richard Shaw <hobbes1069@gmail.com> - 1.98.6-1
- Update to latest upstrem release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.98-3
- Perl 5.18 rebuild

* Tue Dec 18 2012 Richard Shaw <hobbes1069@gmail.com> - 1.98-1
- Update to latest upstream release.

* Wed Dec 05 2012 Richard Shaw <hobbes1069@gmail.com> - 1.12.10-1
- Update to latest upstream release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Richard Shaw <hobbes1069@gmail.com> - 1.12.9-3
- Fix man page generation and license in spec file.

* Tue Mar 13 2012 Richard Shaw <hobbes1069@gmail.com> - 1.12.9-2
- Minor spec fixes and crate man page.

* Tue Jan 10 2012 Richard Shaw <hobbes1069@gmail.com> - 1.12.9-1
- Initial release.
