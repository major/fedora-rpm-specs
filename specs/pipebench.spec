Name:		pipebench
Version:	0.40
Release:	34%{?dist}
Summary:	Measures the speed of STDIN/STDOUT communication

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.habets.pp.se/synscan/programs.php?prog=%{name}

Source0:	http://www.habets.pp.se/synscan/files/%{name}-%{version}.tar.gz

## From: http://www.gnu.org/licenses/gpl-2.0.txt
Source1:	%{name}-GPLv2.txt
Patch0: pipebench-c99.patch

BuildRequires: make
BuildRequires:  gcc
%description
Measures the speed of a pipe, by sitting in the middle passing the data along
to the next process. See the included README for example usage.


%prep
%autosetup -p1
## Update the included LICENSE file to match the current FSF GPLv2 text.
## (Fixes the FSF address and updates the "GNU Library GPL" references to "GNU
## Lesser GPL.") Submitted to upstream via email (2011-08-24).
install -D -m 0644 %{SOURCE1} LICENSE

## Fix the Makefile; taken from the Gentoo ebuild and modified slightly.
sed -i Makefile \
	-e 's:CFLAGS=-Wall:CFLAGS+= -Wall:' \
	-e 's:$(CFLAGS) -o:$(LDFLAGS) &:g' \
	-e 's:/usr/local/bin/:$(DESTDIR)%{_bindir}:' \
	-e 's:/usr/local/man/man1/:$(DESTDIR)%{_mandir}/man1:'


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
## Create the necessary filesystem skeleton.
mkdir -m 755 -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
make install DESTDIR=%{buildroot}


%files
%doc LICENSE README
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.*


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.40-33
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Florian Weimer <fweimer@redhat.com> - 0.40-27
- C99 compatibility fixes (#2159705)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.40-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 04 2012 Peter Gordon <peter@thecodergeek.com> - 0.40-6
- Rebuild for GCC 4.7

* Tue Sep 06 2011 Peter Gordon <peter@thecodergeek.com> - 0.40-5
- One last fix for %%name macro usage consistency in the URL (#731219).

* Sat Sep 03 2011 Peter Gordon <peter@thecodergeek.com> - 0.40-4
- More fixes in accordance with review request feedback (#731219):
  (1) Make %%name macro usage more consistent;
  (2) Remove unnecessary Group tag;
  (3) Remove unnecessary permissions on the man directory;
  (4) Fix Source0 URL.
  (5) Fix mixed use of tabs/spaces in Source1 line.

* Thu Aug 25 2011 Peter Gordon <peter@thecodergeek.com> - 0.40-3
- Remove GPLv2 patch; instead just upload it as an additional Source file.
  - fix-GPLv2.diff
  + GPLv2.txt

* Wed Aug 24 2011 Peter Gordon <peter@thecodergeek.com> - 0.40-2
- Fix description (capitalize "STDIN/STDOUT").
- Add patch to update included GPLv2 text to current FSF address
  and wording.
  + fix-GPLv2.diff

* Sat Aug 13 2011 Peter Gordon <peter@thecodergeek.com> - 0.40-1
- Initial Fedora package creation.
