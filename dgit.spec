Name:           dgit
Version:        10.4
Release:        1%{?dist}
Summary:        Integration between git and Debian-style archives
License:        GPLv3+
URL:            https://browse.dgit.debian.org/dgit.git/
Source0:        https://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.gz
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  make
Requires:       devscripts
Requires:       curl
Requires:       git
Requires:       dpkg-dev
Requires:       tar
Requires:       coreutils
BuildArch:      noarch

%description
dgit (with the associated infrastructure) makes it possible to
treat the Debian archive as a git repository:

"dgit push" constructs uploads from git commits

"dgit clone" and "dgit fetch" construct git commits from uploads.


%prep
%autosetup -n work

%build


%check
# dput is not packaged,
# possibly need Internet connectivity anyway
#EMAIL=jello.biafra@dead.kennedys \
#       tests/using-intree make -f tests/Makefile


%install
# We don't do an install-infra, not sure if the Debian specific
# infrastructure tools would make sense to be packaged in Fedora.
make install DESTDIR="%{buildroot}" \
        prefix="%{_prefix}" \
        bindir="%{_bindir}" \
        mandir="%{_mandir}" \
        perldir="%{perl_vendorlib}" \
        infraexamplesdir="%{_pkgdocdir}/examples"


%files
%{_bindir}/dgit
%{_bindir}/dgit-badcommit-fixup
%{_bindir}/git-playtree-setup
%{_datadir}/%{name}
%{_mandir}/man1/dgit*.1*
%{_mandir}/man7/dgit*.7*
%{perl_vendorlib}/Debian
%doc debian/changelog README.*
%license debian/copyright

%changelog
* Tue Jan 03 2023 Filipe Rosset <rosset.filipe@gmail.com> - 10.4-1
- Update to 10.4 fixes rhbz#2152459

* Tue Nov 15 2022 Filipe Rosset <rosset.filipe@gmail.com> - 10.1-1
- Update to 10.1 fixes rhbz#2142228

* Fri Sep 09 2022 Filipe Rosset <rosset.filipe@gmail.com> - 10.0-1
- Update to 10.0 fixes rhbz#2124070

* Wed Aug 24 2022 Filipe Rosset <rosset.filipe@gmail.com> - 9.16-1
- Update to 9.16 fixes rhbz#2091330

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 21 2022 Filipe Rosset <rosset.filipe@gmail.com> - 9.15-1
- Update to 9.15 fixes rhbz#2036480

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Filipe Rosset <rosset.filipe@gmail.com> - 9.14-1
- Update to 9.14 fixes rhbz#2002117

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 13 2021 Filipe Rosset <rosset.filipe@gmail.com> - 9.13-1
- Update to 9.13 fixes rhbz#1928148

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 9.12-1
- Update to 9.12 fixes rhbz#1849759

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Filipe Rosset <rosset.filipe@gmail.com> - 9.10-1
- Update to 9.10 fixes rhbz#1797498

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Filipe Rosset <rosset.filipe@gmail.com> - 9.9-1
- Update to 9.9 fixes rhbz#1749966

* Sun Aug 18 2019 Filipe Rosset <rosset.filipe@gmail.com> - 9.7-1
- Update to 9.7 fixes rhbz#1742662

* Mon Aug 05 2019 Filipe Rosset <rosset.filipe@gmail.com> - 9.6-1
- Update to 9.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Filipe Rosset <rosset.filipe@gmail.com> - 9.2-1
- new upstream version 9.2, fixes rhbz #1727619

* Tue Jul 09 2019 Filipe Rosset <rosset.filipe@gmail.com> - 9.1-1
- new upstream version 9.1, fixes rhbz #1727619

* Tue Jul 02 2019 Filipe Rosset <rosset.filipe@gmail.com> - 9.0-1
- new upstream version 9.0, fixes rhbz #1726367

* Mon May 27 2019 Filipe Rosset <rosset.filipe@gmail.com> - 8.5-1
- new upstream version 8.5, fixes rhbz #1714052

* Thu Apr 04 2019 Filipe Rosset <rosset.filipe@gmail.com> - 8.4-1
- new upstream version 8.4, fixes rhbz #1684723

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Filipe Rosset <rosset.filipe@gmail.com> - 8.1-1
- new upstream version 8.1, fixes rhbz #1635456

* Sat Sep 29 2018 Filipe Rosset <rosset.filipe@gmail.com> - 6.12-1
- Rebuilt for new upstream version 6.12, fixes rhbz #1634209

* Sat Sep 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 6.11-1
- Rebuilt for new upstream version 6.11, fixes rhbz #1592156

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.4-1
- Rebuilt for new upstream version 4.4, fixes rhbz #1571005

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.3-1
- Rebuilt for new upstream version 4.3, fixes rhbz #1538598

* Wed Jan 17 2018 Filipe Rosset <rosset.filipe@gmail.com> - 4.2-1
- Rebuilt for new upstream version 4.2, fixes rhbz #1532087

* Tue Aug 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 4.1-1
- Rebuilt for new upstream release 4.1

* Sun Aug 06 2017 Filipe Rosset <rosset.filipe@gmail.com> - 4.0-1
- Rebuilt for new upstream version 4.0, fixes rhbz #1358042

* Sun Aug 06 2017 Filipe Rosset <rosset.filipe@gmail.com> - 3.12-1
- Rebuilt for new upstream release 3.12

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Filipe Rosset <rosset.filipe@gmail.com> - 2.12-1
- Rebuilt for new upstream release 2.12, fixes rhbz #1358042

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0-1
- Initial packaging
