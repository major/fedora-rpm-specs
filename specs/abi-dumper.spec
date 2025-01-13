Name:           abi-dumper
Version:        1.4
Release:        1%{?dist}
Summary:        Tool to dump ABI of an ELF object containing DWARF debug info

License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            http://github.com/lvc/abi-dumper/
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  sed
BuildRequires:  txt2man

Requires:       elfutils
Requires:       vtable-dumper >= 1.1

%{?perl_default_filter}

%description
A tool to dump ABI of an ELF object containing DWARF debug info.

The tool is intended to be used with ABI Compliance Checker tool for tracking
ABI changes of a C/C++ library or kernel module.

%prep
%autosetup -p1


%build
# Nothing to build.


%install
mkdir -p %{buildroot}%{_prefix}
%{__perl} Makefile.pl -install --prefix=%{buildroot}%{_prefix}

chmod 0755 %{buildroot}%{_bindir}/%{name}

# Create manpage
mkdir -p %{buildroot}%{_mandir}/man1
%{__perl} abi-dumper.pl --help | sed "s|:$||g" | \
  txt2man -t ABI-DUMPER -s 1 -v "User Commands" -r "ABI Dumper %{version}" > \
  %{buildroot}%{_mandir}/man1/%{name}.1


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Sat Jan 11 2025 Richard Shaw <hobbes1069@gmail.com> - 1.4-1
- Update to 1.4.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 07 2023 Richard Shaw <hobbes1069@gmail.com> - 1.2-9
- Update license to SPDX format.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-6
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.2-3
- Perl 5.34 rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 22 2020 Richard Shaw <hobbes1069@gmail.com> - 1.2-1
- Update to 1.2.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-12
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1-9
- Appy patch to fix debuginfo ouput for Fedora 30+, fixes RHBZ#1726719.

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-8.1
- Perl 5.30 rebuild

* Tue Mar 12 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1-7.1
- Actually apply the patch.

* Mon Mar 11 2019 Richard Shaw <hobbes1069@gmail.com> - 1.1-7
- Fix un-escaped left brace, fixex BZ#1685441.

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.1-4
- Perl 5.28 rebuild

* Thu May 10 2018 Richard Shaw <hobbes1069@gmail.com> - 1.1-3
- Add elfutils as a package requirement, fixes 1576565.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Richard Shaw <hobbes1069@gmail.com> - 1.1-1
- Update to latest upstream release.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Richard Shaw <hobbes1069@gmail.com> - 1.0-1
- Update to latest upstream release.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.19-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 10 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.19-1
- Update to latest upstream release.

* Thu Oct  6 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.18-1
- Update to latest upstream release.

* Fri Aug 26 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.17-1
- Update to latest upstream release.

* Wed Jul  6 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.16-1
- Update to latest upstream release.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.15-2
- Perl 5.24 rebuild

* Sun Mar 13 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.15-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.99.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Richard Shaw <hobbes1069@gmail.com> - 0.99.14-1
- Update to latest upstream release.

* Sat Dec 12 2015 Richard Shaw <hobbes1069@gmail.com> - 0.99.13-1
- Update to latest upstream release.

* Sun Nov  1 2015 Richard Shaw <hobbes1069@gmail.com> - 0.99.12-1
- Update to latest upstream release.

* Sun Oct 18 2015 Richard Shaw <hobbes1069@gmail.com> - 0.99.11-1
- Update to latest upstream release.

* Thu Sep 17 2015 Richard Shaw <hobbes1069@gmail.com> - 0.99.10-1
- Update to latest upstream release.

* Thu Aug 27 2015 Petr Šabata <contyk@redhat.com> - 0.99.8-6
- Prevent FTBFS by correcting the build time dependency list

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.8-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.99.8-3
- Perl 5.20 rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar  4 2014 Richard Shaw <hobbes1069@gmail.com> - 0.99.8-1
- Update to latest upstream release.

* Sun Oct 27 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99.7-1
- Update to latest upstream release.

* Wed Sep 18 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99.6-1
- Update to latest upstream release.

* Thu Aug  8 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99.5-1
- Update to latest upstream release.

* Wed Jul 31 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99.1-1
- Update to latest upstream release with reduced memory usage.

* Fri Jul 19 2013 Richard Shaw <hobbes1069@gmail.com> - 0.99-1
- Update to latest upstream release.

* Wed Jul  3 2013 Richard Shaw <hobbes1069@gmail.com> - 0.98-1
- Initial packaging.
