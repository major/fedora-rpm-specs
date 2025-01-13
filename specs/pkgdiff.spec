Name:           pkgdiff
Version:        1.8
Release:        1%{?dist}
Summary:        A tool for analyzing changes in Linux software packages

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://lvc.github.io/pkgdiff/
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  help2man

Requires:       perl-interpreter >= 5.8
Requires:       diffutils
Requires:       wdiff
Requires:       binutils
Requires:       gawk
Requires:       rpm
Requires:       abi-compliance-checker >= 1.99.1
Requires:       abi-dumper >= 0.97


%description
Package Changes Analyzer (pkgdiff) is a tool for analyzing changes
in Linux software packages (RPM, DEB, TAR.GZ, etc). The tool is
intended for Linux maintainers who are interested in ensuring
compatibility of old and new versions of packages.


%prep
%setup -q
chmod 0644 LICENSE README.md
chmod 0755 %{name}.pl


%build
# Nothing to build.


%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_mandir}/man1
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

# Generate man page
cp %{name}.pl %{name}
%if 0%{?rhel} && 0%{?rhel} <= 6
help2man -N -o %{name}.1 ./%{name}
%else
help2man -N --no-discard-stderr -o %{name}.1 ./%{name}
%endif
sed -i 's/\(.\)/\n\1/' %{name}.1
sed -i 's/PACKAGE/PKGDIFF/g' %{name}.1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1


%files
%license LICENSE
%doc README.md doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*


%changelog
* Sat Jan 11 2025 Richard Shaw <hobbes1069@gmail.com> - 1.8-1
- Update to 1.8.

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.2-20
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 1.7.2-3
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar 21 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7.2-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Richard Shaw <hobbes1069@gmail.com> - 1.7.1-1
- Update to latest upstream release.

* Sun Oct 18 2015 Richard Shaw <hobbes1069@gmail.com> - 1.7.0-1
- Update to latest upstream release.

* Tue Sep  8 2015 Richard Shaw <hobbes1069@gmail.com> - 1.6.4-1
- Update to latest upstream release.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov  5 2014 Richard Shaw <hobbes1069@gmail.com> - 1.6.3-1
- Update to latest upstream release.

* Mon Aug  4 2014 Richard Shaw <hobbes1069@gmail.com> - 1.6.2-1
- Update to latest upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Richard Shaw <hobbes1069@gmail.com> - 1.6.1-1
- Fixes homepage link.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.6-2
- Perl 5.18 rebuild

* Mon Jun 10 2013 Richard Shaw <hobbes1069@gmail.com> - 1.6-1
- Update to latest upstream release.

* Sat Mar 06 2013 Richard Shaw <hobbes1069@gmail.com> - 1.5-1
- Update to latest upstream release.

* Tue Dec 18 2012 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-1
- Update to latest upstream release.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 17 2012 Richard Shaw <hobbes1069@gmail.com> - 1.2-1
- Update to latest release.
- rfcdiff is now considered forked.

* Tue Feb 14 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0-3
- Unbundle rfcdiff.
- Add rfcdiff as requirement to spec file.

* Mon Jan 30 2012 Richard Shaw <hobbes1069@gmail.com> - 1.0-1
- Initial release.
