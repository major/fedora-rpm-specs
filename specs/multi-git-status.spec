%global forgeurl https://github.com/fboender/multi-git-status
Version:         2.3

%forgemeta

Name:            multi-git-status
Release:         2%{?dist}
Summary:         Show uncommitted, untracked and unpushed changes for multiple Git repos
URL:             %{forgeurl}
Source:          https://github.com/fboender/multi-git-status/archive/%{name}-%{version}.tar.gz
License:         MIT
BuildArch:       noarch

Requires:        coreutils
Requires:        findutils
Requires:        gawk
Requires:        git
Requires:        sed

%description
Show uncommitted, untracked and unpushed changes for multiple Git repos.

multi-git-status shows:
* Uncommitted changes if there are unstaged or uncommitted changes on the
  checked out branch.
* Untracked files if there are untracked files which are not ignored.
* Needs push (BRANCH) if the branch is tracking a (remote) branch which is
  behind.
* Needs upstream (BRANCH) if a branch does not have a local or remote
  upstream branch configured. Changes in the branch may otherwise
  never be pushed or merged.
* Needs pull (BRANCH) if the branch is tracking a (remote) branch which is
  ahead. This requires that the local git repo already knows about the remote
  changes (i.e. you've done a fetch), or that you specify the -f option.
  Multi-git-status does NOT contact the remote by default.
* X stashes if there are stashes.

%prep
%forgesetup

%build

%install
install -p -D -m755 mgitstatus %{buildroot}%{_bindir}/mgitstatus
install -p -D -m755 mgitstatus.1 %{buildroot}%{_mandir}/man1/mgitstatus.1

%files
%{_bindir}/mgitstatus
%license LICENSE.txt
%doc README.md
%doc screenshot.png
%doc %{_mandir}/man1/mgitstatus.1*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 01 2024 Vojtech Trefny <vtrefny@redhat.com> - 2.3-1
- New version 2.3

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Vojtech Trefny <vtrefny@redhat.com> - 2.2-1
- New version 2.2

* Mon Mar 14 2022 Vojtech Trefny <vtrefny@redhat.com> - 2.1-1
- New version 2.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Brian (bex) Exelbierd <bex@pobox.com> - 2.0-1
* New Version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Brian (bex) Exelbierd <bex@pobox.com> - 1.0-1
* New Version

* Sat Jul 27 2019 Brian (bex) Exelbierd <bex@pobox.com> - 1.0-1.20190728git2e6049d
- Initial package
