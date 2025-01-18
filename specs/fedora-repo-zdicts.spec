Name:           fedora-repo-zdicts
Version:        2403.1
Release:        3%{?dist}
Summary:        Zstd dictionaries for Fedora repository metadata
License:        BSD-2-Clause
URL:            https://pagure.io/fedora-repo-zdicts
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  /bin/bash
BuildRequires:  make
 
%description
zchunk is a compressed file format that splits the file into independent
chunks.  This package contains zstd libraries tailored for Fedora's repository
metadata to improve their compression.


%prep
%autosetup


%build
# This package contains pregenerated zstd dictionaries so we don't have to
# carry 60+MB of metadata per Fedora release in the SRPM (and so we're not
# filling up our git repository)


%install
%make_install


%check


%files
%license LICENSE
%doc README.md
%{_datadir}/fedora-repo-zdicts


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2403.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2403.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Mar 17 2024 Jonathan Dieter <jdieter@gmail.com> - 2403.1-1
- Update with F40 dictionaries and drop F37 dictionaries

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2309.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2309.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 06 2023 Jonathan Dieter <jdieter@gmail.com> - 2309.1-1
- Update with F39 dictionaries and drop F36 dictionaries

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2303.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Mar 20 2023 Jonathan Dieter <jdieter@gmail.com> - 2303.1-1
- Update with F38 dictionaries and drop F34 and F35 dictionaries

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2208.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 23 2022 Jonathan Dieter <jdieter@gmail.com> - 2208.1-1
- Update with F37 dictionaries and drop F32 and F33 dictionaries

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2203.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 02 2022 Jonathan Dieter <jdieter@gmail.com> - 2203.1-1
- Update with F36 dictionaries

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2108.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 22 2021 Jonathan Dieter <jdieter@gmail.com> - 2108.1-1
- Update with F35 dictionaries

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2103.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 10 2021 Jonathan Dieter <jdieter@gmail.com> - 2103.1-2
- Update with F34 dictionaries
- Fix changelog entry

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2010.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Jonathan Dieter <jdieter@gmail.com> - 2010.1-1
- Update with F33 dictionaries

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2004.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Jonathan Dieter <jdieter@gmail.com> - 2004.2-1
- Update with F32 dictionaries

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1910.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Jonathan Dieter <jdieter@gmail.com> - 1920.1-1
- Update with F31 dictionaries

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1812.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1812.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Jonathan Dieter <jdieter@gmail.com> - 1812.1-1
- Switch versioning to match yearmonth.release
- Fix paths to use koji tags

* Thu Dec 06 2018 Jonathan Dieter <jdieter@gmail.com> - 30.4-1
- Preserve timestamps

* Wed Dec 05 2018 Jonathan Dieter <jdieter@gmail.com> - 30.3-1
- Initial build of Fedora 30 repodata
