Name:		freedink-data
Version:	1.08.20190120
Release:	16%{?dist}
Summary:	Adventure and role-playing game (assets)

License:	Zlib AND CC-BY-SA-3.0 AND GPL-2.0-or-later
URL:		https://www.gnu.org/software/freedink/
Source0:	https://ftp.gnu.org/gnu/freedink/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires: make

%description
Dink Smallwood is an adventure/role-playing game, similar to Zelda,
made by RTsoft. Besides twisted humor, it includes the actual game
editor, allowing players to create hundreds of new adventures called
Dink Modules or D-Mods for short.

This package contains architecture-independent data for the original
game, along with free sound and music replacements.


%prep
%setup -q
# Strip DOS EOL from documentation
# https://fedoraproject.org/wiki/PackageMaintainers/Common_Rpmlint_Issues#wrong-file-end-of-line-encoding
sed -i 's/\r//' README.txt README-REPLACEMENTS.txt


%build


%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
# D-Mod .mo files are pre-generated in upstream tarball, and engine uses an alternate $dmod/l10n/ path
#%%find_lang dink


%files
%doc README.txt README-REPLACEMENTS.txt licenses/
%{_datadir}/dink/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.08.20190120-11
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20190120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Sylvain Beucler <beuc@beuc.net> - 1.08.20190120-1
- New upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20170409-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20170409-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20170409-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Sylvain Beucler <beuc@beuc.net> - 1.08.20170409-1
- New upstream release

* Sat Apr 01 2017 Sylvain Beucler <beuc@beuc.net> - 1.08.20170401-1
- New upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20140901-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.08.20140901-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20140901-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 01 2014 Sylvain Beucler <beuc@beuc.net> - 1.08.20140901-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20121209-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20121209-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20121209-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Sylvain Beucler <beuc@beuc.net> - 1.08.20121209-1
- New upstream release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20111016-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20111016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Sylvain Beucler <beuc@beuc.net> - 1.08.20111016-1
- New upstream release

* Sat Jul 23 2011 Sylvain Beucler <beuc@beuc.net> - 1.08.20110723-1
- New upstream release
- Update homepage URL

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20100103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan  3 2010 Sylvain Beucler <beuc@beuc.net> - 1.08.20100103-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20090706-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090706-1
- New upstream release (remove savegame)

* Sun Jul 05 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090705-1
- New upstream release
- Removed patch to preserve timestamps (applied upstream)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20080920-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-3
- Actually apply patch0 (preserve timestamps)

* Tue Sep 23 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-2
- Specify all licenses used by the package
- Added licenses texts in docs
- Replaced /usr by a RPM macro
- Add patch from upstream to preserve timestamps no install
- Converted DOS newlines

* Sat Sep 20 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-1
- Initial package
