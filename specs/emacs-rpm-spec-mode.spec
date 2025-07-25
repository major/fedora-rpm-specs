%global commit  283d2aac4ede343586a1fb9e9d2a5917f34809a1
%global date    20241209
%global forgeurl https://github.com/Thaodan/rpm-spec-mode

Name:           emacs-rpm-spec-mode
Version:        0.16
Release:        24%{?dist}
Summary:        Major GNU Emacs mode for editing RPM spec files

%forgemeta

License:        GPL-2.0-or-later
URL:            https://github.com/Thaodan/rpm-spec-mode
VCS:            git:%{url}.git
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  emacs-nw
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description
Major GNU Emacs mode for editing RPM spec files.

%prep
%forgeautosetup -p1

%build
%_emacs_bytecompile rpm-spec-mode*.el
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/rpm-spec-mode-loaddefs.el\"))"

%install
mkdir -p %{buildroot}/%{_emacs_sitelispdir}
install -p -m 644 rpm-spec-mode.el{,c} %{buildroot}/%{_emacs_sitelispdir}

# Install rpm-spec-mode-loaddefs.el
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 644 rpm-spec-mode-loaddefs.el %{buildroot}%{_emacs_sitestartdir}

%files
%doc README.org
%license LICENSE
%{_emacs_sitestartdir}/rpm-spec-mode-loaddefs.el
%{_emacs_sitelispdir}/rpm-spec-mode.el
%{_emacs_sitelispdir}/rpm-spec-mode.elc

%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Mar 04 2025 Zbigniew Jedrzejewski-Szmek <zbyszek@in.waw.pl> - 0.16-23
- Update to latest upstream commit

* Tue Mar  4 2025 Jerry James <loganjerry@gmail.com> - 0.16-22.20240417gitd3c7d70
- Switch upstream repositories (rhbz#2303286, rhbz#1767852)
- Add patch to fix undefined list->string function (rhbz#2272197)
- Use the forge macros
- Generate and rename the init file
- Ship the README.md and LICENSE files

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.16-20
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 08 2022 Bhavin Gandhi <bhavin192@fedoraproject.org> - 0.16-14
- Fix compatibility with latest Emacs, fixes rhbz#2113202

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun  7 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.16-1
- Update to 0.16

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Michel Salim <salimma@fedoraproject.org> - 0.15-1
- Update to 0.15

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.12-5
- Fix and apply patch for rpm-goto-add-change-log-entry (#970924)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 19 2012 Karel Klíč <kklic@redhat.com> - 0.12-3
- Removed build dependency on emacs-el
- Require emacs without embedded rpm-spec-mode to avoid conflicts
  during updates

* Tue Sep 18 2012 Karel Klíč <kklic@redhat.com> - 0.12-2
- Moved rpm-spec-mode.el{,c} to a subdirectory

* Fri Sep 14 2012 Karel Klíč <kklic@redhat.com> - 0.12-1
- Initial package
