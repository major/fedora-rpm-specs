Name:           snapraid
Summary:        Disk array backup for many large rarely-changed files
Version:        12.3
Release:        3%{?dist}
# snapraid itself is GPL-3.0-or-later but uses other source codes, breakdown:
# Apache-2.0 AND GPL-3.0-or-later: cmdline/metro.c
# BSD-2-Clause: tommyds/*
# GPL-2.0-or-later: raid/*
# GPL-3.0-or-later AND LicenseRef-Fedora-Public-Domain: cmdline/murmur3.c
# LGPL-2.0-or-later: cmdline/fnmatch.[ch]
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND BSD-2-Clause

URL:            https://www.snapraid.it/
Source0:        https://github.com/amadvance/snapraid/releases/download/v%{version}/snapraid-%{version}.tar.gz

BuildRequires:  gcc make libblkid-devel

%description
SnapRAID is a backup program for disk arrays. It stores parity
information of your data and it's able to recover from up to six disk
failures. SnapRAID is mainly targeted for a home media center, with a
lot of big files that rarely change.

%prep
%setup -q
mv raid/COPYING raid/COPYING-raid

%build
%configure
%make_build

%check
make check

%install
%make_install

%files
%license COPYING tommyds/LICENSE raid/COPYING-raid
%doc AUTHORS HISTORY README
%{_bindir}/snapraid
%{_mandir}/man1/snapraid.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Jens Kuehnel <bugzilla-redhat@jens.kuehnel.org> - 12.3-1
- Update to 12.3

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Aug 05 2023 Jens Kuehnel <bugzilla-redhat@jens.kuehnel.org> - 12.2-1
- Update to 12.2

* Sun Apr 19 2020 Filipe Rosset <rosset.filipe@gmail.com> - 11.3-1
- Update to 11.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Eric Smith <brouhaha@fedoraproject.org> - 11.2-1
- Updated to latest upstream.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 01 2016 Eric Smith <brouhaha@fedoraproject.org> - 10.0-1
- Updated to latest upstream.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 24 2015 Eric Smith <brouhaha@fedoraproject.org> - 8.1-1
- Updated to latest upstream.

* Sat Feb 14 2015 Eric Smith <brouhaha@fedoraproject.org> - 7.1-1
- Updated to latest upstream.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 14 2014 Eric Smith <brouhaha@fedoraproject.org> - 6.3-1
- Updated to latest upstream.

* Thu Jun 12 2014 Eric Smith <brouhaha@fedoraproject.org> - 6.2-1
- Updated to latest upstream.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Eric Smith <brouhaha@fedoraproject.org> - 6.1-3
- Revert to using bundled tommyds library, per request of the author
  of both, and bundling exception granted by FPC ticket #423.

* Fri Apr 18 2014 Eric Smith <brouhaha@fedoraproject.org> - 6.1-2
- Use separately packaged tommyds library.

* Fri Apr 18 2014 Eric Smith <brouhaha@fedoraproject.org> - 6.1-1
- Updated to latest upstream.

* Sun Jan 19 2014 Eric Smith <brouhaha@fedoraproject.org> - 5.2-1
- Initial build.
