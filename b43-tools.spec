Name:		b43-tools
Version:	019
Release:	16%{?dist}
Summary:	Tools for the Broadcom 43xx series WLAN chip
# assembler — GPLv2
# debug — GPLv3
# disassembler — GPLv2
# ssb_sprom — GPLv2+
License:	GPLv2 and GPLv2+ and GPLv3
URL:		https://bues.ch/cgit/b43-tools.git
## git clone https://git.bues.ch/git/b43-tools.git
## cd b43-tools
## git archive --format=tar --prefix=%{name}-%{version}/ b43-fwcutter-%{version} | xz > ../%{name}-%{version}.tar.xz
Source0:	%{name}-%{version}.tar.xz
Patch1:		0001-b43-tools-fix-format-security-errors.patch
Patch2:		0002-Explicitly-use-python3.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	flex-static
BuildRequires:	gcc
BuildRequires:	python3-devel
BuildRequires: make


%description
Tools for the Broadcom 43xx series WLAN chip.


%prep
%autosetup -p1
install -p -m 0644 assembler/COPYING COPYING.assembler
install -p -m 0644 assembler/README README.assembler
install -p -m 0644 debug/COPYING COPYING.debug
install -p -m 0644 debug/README README.debug
install -p -m 0644 disassembler/COPYING COPYING.disassembler
install -p -m 0644 ssb_sprom/README README.ssb_sprom
install -p -m 0644 ssb_sprom/COPYING COPYING.ssb_sprom
# For py3_build/py3_install macros
install -p -m 0644 debug/install.py debug/setup.py

2to3 -w .


%build
CFLAGS="%{optflags}" %{make_build} -C assembler
CFLAGS="%{optflags}" %{make_build} -C disassembler
CFLAGS="%{optflags}" %{make_build} -C ssb_sprom
cd debug
%py3_build


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm %{buildroot}%{_bindir}
install -p -m 0755 assembler/b43-asm.bin %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-dasm %{buildroot}%{_bindir}
install -p -m 0755 disassembler/b43-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-fwconv %{buildroot}%{_bindir}
install -p -m 0755 disassembler/brcm80211-ivaldump %{buildroot}%{_bindir}
install -p -m 0755 ssb_sprom/ssb-sprom %{buildroot}%{_bindir}
cd debug
%py3_install


%files
%doc README.* COPYING.*
%{_bindir}/b43-asm
%{_bindir}/b43-asm.bin
%{_bindir}/b43-beautifier
%{_bindir}/b43-dasm
%{_bindir}/b43-fwdump
%{_bindir}/b43-ivaldump
%{_bindir}/brcm80211-fwconv
%{_bindir}/brcm80211-ivaldump
%{_bindir}/ssb-sprom
%{python3_sitelib}/*


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 019-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 019-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 019-14
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 019-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 019-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 019-11
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 019-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 019-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 019-8
- Rebuilt for Python 3.9

* Tue May 05 2020 Tom Stellard <tstellar@redhat.com> - 019-7
- Use make_build macro
- https://docs.fedoraproject.org/en-US/packaging-guidelines/#_parallel_make

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 019-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Pete Walter <pwalter@fedoraproject.org> - 019-5
- Switch to Python 3 (#1737905)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 019-3
- Fix FTBFS on Fedora 30+

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Peter Lemenkov <lemenkov@gmail.com> - 019-1
- Ver. 019
- Fix FTBFS

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 017-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 017-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Iryna Shcherbina <ishcherb@redhat.com> - 017-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Oct 06 2017 Troy Dawson <tdawson@redhat.com> - 017-11
- Fix format-security errors

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 017-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 017-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 017-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 017-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 017-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 017-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 017-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 017-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Peter Lemenkov <lemenkov@gmail.com> - 017-1
- Ver. 017

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.git20090125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git20090125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git20090125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git20090125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 14 2010 Ralf Corsépius <corsepiu@fedoraproject.org> - 0-0.6.git20090125
- Add BR: flex-static (Fix FTBFS: BZ 660756).

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0-0.5.git20090125
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git20090125
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Peter Lemenkov <lemenkov@gmail.com> 0-0.3.git20090125
- Corrected 'License' field
- Since now ssb_sprom honours optflags

* Sat Apr  4 2009 Peter Lemenkov <lemenkov@gmail.com> 0-0.2.git20090125
- Added missing BuildRequire

* Sat Mar 14 2009 Peter Lemenkov <lemenkov@gmail.com> 0-0.1.git20090125
- Initial package for Fedora

