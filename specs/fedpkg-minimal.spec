Name:           fedpkg-minimal
Version:        1.2.0
Release:        13%{?dist}
Summary:        Script to allow fedpkg fetch to work

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pagure.io/%{name}
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
Patch1:         0001-curl-max-time-in-seconds-not-minutes.patch


BuildArch:      noarch

Requires:       curl

Conflicts:      fedpkg


%description
Script for use in Koji to allow sources to be fetched

%prep
%autosetup -p1

%build

%install
install -d %{buildroot}%{_bindir}
install -pm 755 bin/fedpkg %{buildroot}%{_bindir}/fedpkg
install -pm 755 bin/fedpkg-stg %{buildroot}%{_bindir}/fedpkg-stg
install -pm 755 bin/fedpkg-base %{buildroot}%{_bindir}/fedpkg-base

%check
./tests/run-tests.sh

%files
%doc README.md AUTHORS.md
%license LICENSE
%{_bindir}/fedpkg
%{_bindir}/fedpkg-stg
%{_bindir}/fedpkg-base

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Ondřej Nosek <onosek@redhat.com> - 1.2.0-4
- Patch: curl --max-time in seconds, not minutes

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Kevin Fenzi <kevin@scrye.com> - 1.2.0-2
- Patch max-time to 900 seconds from 15. https://pagure.io/fedpkg-minimal/issue/13

* Mon Mar 29 2021 Ondřej Nosek <onosek@redhat.com> - 1.2.0-1
- 1.2.0 Release (onosek)
- Accept files without trailing new-line - rhbz#1943593 (onosek)
- Handle empty lines in sources file (onosek)
- Retry stalled downloads after 15 minutes, with the maximum of 5 retries (contyk)
- Make a fedpkg-base to distinguish between prod and stg (puiterwijk)
- Add a basic set of tests (lsedlar)
- Update $baseurl to src.fpo (lsedlar)
- Make curl follow redirects (lsedlar)
- remove the () in two steps (dennis)
- Read BSD formatted sources (lsedlar)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.0-7
- use upstreamed more robust patches for switch to https and src

* Mon Dec 12 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.0-6
- switch the lookcaside cache url to src.fp.o and use https://

* Sun Dec 11 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.0-5
- update patch to support new sources format to work on rhel6

* Thu Dec 08 2016 Dennis Gilmore <dennis@ausil.us> - 1.1.0-4
- add patch to support new sources format

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Pavol Babincak <pbabinca@redhat.com> - 1.1.0-1
- Verify sources
- Add Till and Jesse to Authors and Till to Copyright header
- Remove redundant whitespace at the end of file
- Simplify parsing sources file
- Abort on errors
- Added copyright and authors
- Use curl instead of wget

* Wed Mar 04 2015 Pavol Babincak <pbabinca@redhat.com> - 1.0.0-3
- Use %%setup instead of %%autosetup in %%prep
- Define BuildRoot
- Move license back under %%doc macro

* Fri Feb 06 2015 Pavol Babincak <pbabinca@redhat.com> - 1.0.0-2
- use %%license tag instead of %%doc for the LICENSE file (rhbz#1189611)
- preserve timestamp of original installed files (rhbz#1189611)
- drop installation README.md and LICENSE from %%install section to install it
  only once from %%doc and %%license macro (rhbz#1189611)

* Wed Feb 04 2015 Pavol Babincak <pbabinca@redhat.com> - 1.0.0-1
- Initial release made from
  http://koji.fedoraproject.org/koji/packageinfo?packageID=17475
