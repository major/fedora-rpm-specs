Name:           cksfv
Version:        1.3.15
Release:        13%{?dist}
Summary:        Utility to manipulate SFV files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.com/heikkiorsila/cksfv/
Source0:        https://zakalwe.fi/~shd/foss/%{name}/files/%{name}-%{version}.tar.bz2
Source1:        https://zakalwe.fi/~shd/foss/%{name}/files/%{name}-%{version}.tar.bz2.asc
Source2:        https://zakalwe.fi/~shd/keys/heikki-orsila-2017.pub
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires: make

%description
cksfv is a utility that can create and use SFV files. SFV (Simple File
Verification) files are used to verify file integrity using CRC32
checksums.


%prep
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

# fix rpmlint warnings
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv &&\
touch -r ChangeLog ChangeLog.conv &&\
mv -f ChangeLog.conv ChangeLog


%build
%set_build_flags
# custom configure does not take --libdir spec
./configure \
    --bindir=%{_bindir} \
    --mandir=%{_mandir} \
    --prefix=%{_prefix} \
    --package-prefix=%{buildroot}
%make_build


%install
%make_install


%check
%make_build check


%files
%license COPYING
%doc AUTHORS ChangeLog README.md TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.15-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Dominik Mierzejewski <rpm@greysector.net> - 1.3.15-1
- update to 1.3.15 (#1887064)
- update project URL and use HTTPS
- use modern macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Dominik Mierzejewski <rpm@greysector.net> - 1.3.14-17
- Add BR: gcc for https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot
- Verify source tarball GPG signature
- Clean-up and use modern macros to simplify build
- Preserve ChangeLog timestamp

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> - 1.3.14-7
- drop obsolete specfile parts
- remove redundant variable redirection
- fix license tag

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 30 2009 Christopher Stone <chris.stone@gmail.com> 1.3.14-1
- Upstream sync
- Remove no longer needed man page patch

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 11 2008 Christopher Stone <chris.stone@gmail.com> 1.3.13-1
- Upstream sync

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> 1.3.12-3
- Autorebuild for GCC 4.3

* Sat Oct 27 2007 Christohper Stone <chris.stone@gmail.com> 1.3.12-2
- Fix rpmlint issues

* Sat Sep 08 2007 Christopher Stone <chris.stone@gmail.com> 1.3.12-1
- Upstream sync

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.3.11-2
- Rebuild for selinux ppc32 issue.

* Fri Jul 13 2007 Christopher Stone <chris.stone@gmail.com> 1.3.11-1
- Upstream sync

* Tue Mar 27 2007 Christopher Stone <chris.stone@gmail.com> 1.3.10-1
- Upstream sync

* Mon Jan 29 2007 Christopher Stone <chris.stone@gmail.com> 1.3.9-3
- Build with %%{optflags} (bug #225096)
- Remove system macros from spec
- Use $RPM_BUILD_ROOT instead of %%{buildroot}

* Wed Aug 30 2006 Christopher Stone <chris.stone@gmail.com> 1.3.9-2
- FC6 rebuild

* Tue Jun 20 2006 Christopher Stone <chris.stone@gmail.com> 1.3.9-1
- Initial release
