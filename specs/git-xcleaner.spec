Name:           git-xcleaner
Version:        2.0
Release:        4%{?dist}

Summary:        Interactive git branch removal TUI

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/lzap/git-xcleaner
Source:         https://github.com/lzap/git-xcleaner/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  sed
BuildRequires:  rubygem-ronn
Requires:       /usr/bin/resize
Requires:       newt

%description
git-xcleaner helps with deleting unused topic branches using TUI (text user
interface). It also offers mechanisms for pre-selecting branches that can be
safely removed.

%prep
%setup -q -n %{name}-%{version}

%build
# Man page and ANSII-only text version of the man page for the embedded help
ronn man/%{name}.md
ronn -m man/%{name}.md | sed -r 's/\x1b\[[0-9;]*m?//g' > man/%{name}.1.txt

%install
rm -rf $RPM_BUILD_ROOT

install -Dp %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 644 man/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%doc LICENSE README.md man/%{name}.1.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 30 2024 Lukas Zapletal <lzap+git@redhat.com> 2.0-1
- New upstream release 2.0 with new tarball URL on github.com
- Drop Remote option - was not working correctly (lzap+git@redhat.com)
- Reformat with tabs (lzap+git@redhat.com)
- Implement pruned cleaning properly (lzap+git@redhat.com)
- Remove unnecessary resize call (lzap+git@redhat.com)
- Added email (lzap+git@redhat.com)
- Added install section (lzap+git@redhat.com)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 15 2016 Lukas Zapletal <lzap+git@redhat.com> 1.5-1
- Updated man page (lzap+git@redhat.com)
- Fixed bugs (lzap+git@redhat.com)

* Wed Mar 09 2016 Lukas Zapletal <lzap+git@redhat.com> 1.4-1
- Improved confirmation message (lzap+git@redhat.com)
- Menu width is also fixed now (lzap+git@redhat.com)
- Added undelete instructions (lzap+git@redhat.com)
- Updated dependencies in README (lzap+git@redhat.com)
- Main menu is now smaller (lzap+git@redhat.com)
- Merged mode works with any base branch (lzap+git@redhat.com)
- Most of the lists are sorted by branch name now (lzap+git@redhat.com)
- Fix branch variables in message search mode (dcleal@redhat.com)
- Check for resize/xterm dependency (dcleal@redhat.com)
- Add missing require on resize/xterm (dcleal@redhat.com)

* Mon Aug 11 2014 Lukas Zapletal <lzap+git@redhat.com> 1.3-1
- Added dependency check during start (lzap+git@redhat.com)
- Cleaned source URL in SPEC (lzap+git@redhat.com)

* Thu Jul 24 2014 Lukas Zapletal <lzap+git@redhat.com> 1.2-1
- Reworded the welcome screen and URL change (lzap+git@redhat.com)

* Wed Jul 23 2014 Lukas Zapletal <lzap+git@redhat.com> 1.1-1
- new package built with tito

* Wed Jul 23 2014 Lukas Zapletal <lzap+rpm@redhat.com> 1.0-1
- Initial version

