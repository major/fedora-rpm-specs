# To reduce boilerplate.
%global make_flags bindir=%{_bindir} mandir="%{_mandir}" prefix="%{_prefix}" \\\
CC=%{__cc} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}" ENABLE_MAN=1


Name:           cc1541
Version:        4.1
Release:        6%{?dist}
Summary:        Tool for creating Commodore Floppy disk images in D64, G64, D71 or D81 format

License:        MIT
URL:            https://bitbucket.org/PTV_Claus/%{name}
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  make

%description
This is %{name} v%{version}, a tool for creating Commodore 1541
Floppy disk images in D64, G64, D71 or D81 format with custom
sector interleaving etc.   Also supports extended tracks 35-40
using either SPEED DOS or DOLPHIN DOS BAM-formatting.


%prep
%autosetup -p 1


%build
%make_build all test_cc1541 %{make_flags}


%install
%make_install %{make_flags}


%check
%make_build check %{make_flags}


%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Björn Esser <besser82@fedoraproject.org> - 4.1-1
- New upstream release

* Sat Feb 11 2023 Björn Esser <besser82@fedoraproject.org> - 4.0-5
- Update patches from upstream git

* Sun Jan 29 2023 Björn Esser <besser82@fedoraproject.org> - 4.0-4
- Patch Makefile to be thread-safe on all targets
- Clean trailing white-space in some files during %%prep

* Sat Jan 28 2023 Björn Esser <besser82@fedoraproject.org> - 4.0-3
- Apply two upstream patches fixing verbose file allocation table printout
- Tweak Makefile to build all targets in parallel
- Compile and link test binary during %%build stage

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 17 2022 Björn Esser <besser82@fedoraproject.org> - 4.0-1
- New upstream release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 09 2022 Björn Esser <besser82@fedoraproject.org> - 3.4-1
- New upstream release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Björn Esser <besser82@fedoraproject.org> - 3.3-1
- New upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 20 2021 Björn Esser <besser82@fedoraproject.org> - 3.2-4
- Add a patch to fix encoding of the README file

* Mon Jul 19 2021 Björn Esser <besser82@fedoraproject.org> - 3.2-3
- Add a patchset of upstream commits for several fixes

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 09 2020 Björn Esser <besser82@fedoraproject.org> - 3.2-1
- New upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 03 2019 Björn Esser <besser82@fedoraproject.org> - 3.1-1
- New upstream release

* Wed Aug 28 2019 Björn Esser <besser82@fedoraproject.org> - 3.0-2
- Add an upstream patch to fix a bug

* Sun Aug 25 2019 Björn Esser <besser82@fedoraproject.org> - 3.0-1
- New upstream release

* Sun Jul 28 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-3
- Add some upstream patches to improve rpm packaging

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-1
- Initial import (#1722942)

* Fri Jun 21 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-0.3
- Upstream PR has been merged

* Fri Jun 21 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-0.2
- Remove pre-built binaries from build-tree during %%prep.

* Fri Jun 21 2019 Björn Esser <besser82@fedoraproject.org> - 2.0-0.1
- Initial rpm release (#1722942)
