Name:           abi-tracker
Version:        1.11
Release:        24%{?dist}
Summary:        Tool to visualize ABI changes timeline of a C/C++ library

License:        GPL-2.0-or-later OR  LGPL-2.1-or-later
URL:            https://github.com/lvc/abi-tracker
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl%{?fedora:-interpreter}
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
# Needed to run abi-tracker to generate man page.
BuildRequires:  help2man
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)


Requires:       abi-dumper >= 0.99.16
Requires:       vtable-dumper >= 1.1
Requires:       abi-compliance-checker >= 1.99.21
Requires:       pkgdiff >= 1.6.4
Requires:       rfcdiff >= 1.41
Requires:       elfutils


%description
A tool to visualize ABI changes timeline of a C/C++ software library.
  
The tool requires the input profile of the library in JSON format. It can be
created manually or automatically generated by the ABI Monitor:
https://github.com/lvc/abi-monitor


%prep
%setup -q


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}
%{_fixperms} %{buildroot}/*

# Create man page
mkdir -p %{buildroot}%{_mandir}/man1
help2man -s 1 -N --version-string %{version} \
    %{buildroot}%{_bindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1


%files
%license LICENSE
%doc HOWTO README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 07 2023 Richard Shaw <hobbes1069@gmail.com> - 1.11-18
- Update to SPDX license format.

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-15
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-12
- Perl 5.34 rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-9
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-6
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.11-3
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 30 2017 Richard Shaw <hobbes1069@gmail.com> - 1.11-1
- Update to latest upstream release.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Richard Shaw <hobbes1069@gmail.com> - 1.10-1
- Update to latest upstream release.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9-3
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Richard Shaw <hobbes1069@gmail.com> - 1.9-1
- Update to latest upstream release.

* Wed Jul  6 2016 Richard Shaw <hobbes1069@gmail.com> - 1.8-1
- Update to latest upstream release.

* Wed Jun  1 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7-1
- Update to latest upstream release.

* Thu May 19 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6-2
- Perl 5.24 re-rebuild of bootstrapped packages

* Sun May 15 2016 Richard Shaw <hobbes1069@gmail.com> - 1.6-1
- Update to latest upstream release.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.5-2
- Perl 5.24 rebuild

* Sun Mar 13 2016 Richard Shaw <hobbes1069@gmail.com> - 1.5-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Richard Shaw <hobbes1069@gmail.com> - 1.4-2
- Add manpage via help2man.
- Query upstream to clarify licensing.
  https://github.com/lvc/abi-tracker/issues/1

* Sun Dec  6 2015 Richard Shaw <hobbes1069@gmail.com> - 1.4-1
- Initial packaging.
- 
