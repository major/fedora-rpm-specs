Name:           examiner
Version:        0.5
Release:        37%{?dist}
Summary:        Utility to disassemble and comment foreign executable binaries 

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.academicunderground.org/examiner
Source0:        http://www.academicunderground.org/examiner/%{name}-%{version}.tar.gz
Patch0:         examiner-0.5-examiner_hashes_pl.patch
BuildArch:      noarch

BuildRequires:  /usr/bin/pod2man
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# Required perl modules.
BuildRequires:  perl(strict)
BuildRequires:  perl(Env)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(File::Basename)
BuildRequires: make


%description
The Examiner is an application that utilizes the objdump command to disassemble
and comment foreign executable binaries. This app was designed to analyze static
compiled binaries but works ok with others. The intention is for forensic
research but could also be used in general reverse engineering.
This program can only handle basic dissassembly. If the binary has been modified
to resist debugging then the Examinier probably will not be able to analyze the
code. Also the Examiner will not analyze live running code.

%prep
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .hashes

%build
# empty build
chmod 644 utils/*

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1/

sed -i -e 's@cp @cp -p @' Makefile  # Save timestamp

make install BIN=%{buildroot}%{_bindir}/ \
    MAN=%{buildroot}%{_mandir}/man1/ \
    SHARE=%{buildroot}%{_datadir}/%{name} INSTALL="install -p"

# Bogusly installed patch-suffixed file
rm %{buildroot}%{_datadir}/%{name}/os/linux/examiner_hashes.pl.hashes

%files
%doc docs/BUGS docs/CHANGELOG docs/README docs/TODO docs/TUTORIAL
%license docs/COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5-36
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 08 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.5-18
- Add BR: /usr/bin/pod2man (F24FTBFS).
- Add %%license.
- Build-require perl-modules.
- Remove bogusly installed file.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Fabian Affolter <mail@fabian-affolter.ch>- 0.5-15
- Add docs

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 17 2013 Fabian Affolter <mail@fabian-affolter.ch>- 0.5-13
- Spec file updated
- FTBFS (#913994) fixed

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.5-11
- Perl 5.18 rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 23 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 0.5-6
- Applied  examiner-0.5-examiner_hashes_pl.patch #515452

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 31 2009 Rakesh Pandit <rakesh@fedorapeople.org> 0.5-3
- Fixed unowned directory

* Sat Nov 08 2008 Rakesh Pandit <rakesh@fedorapeople.org> 0.5-2
- Cleaned up sed mess.

* Tue Nov 04 2008 Rakesh Pandit <rakesh@fedorapeople.org> 0.5-1
- Initial package
