%global giturl  https://github.com/victorhge/iedit

Name:           emacs-iedit
Version:        0.9.9.9.9
Release:        7%{?dist}
Summary:        Edit multiple regions simultaneously in Emacs

License:        GPL-3.0-or-later
URL:            https://www.emacswiki.org/emacs/Iedit
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/iedit-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  emacs-nw
BuildRequires:  make

Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description
This package includes Emacs minor modes (iedit-mode and
iedit-rectangle-mode) based on an API library (iedit-lib) and allows you
to alter one occurrence of some text in a buffer (possibly narrowed) or
region, and simultaneously have other occurrences changed in the same
way, with visual feedback as you type.

iedit-mode is a great alternative to built-in replace commands:

- A more intuitive way to alter all the occurrences at once
- Visual feedback
- Fewer keystrokes in most cases
- Optionally preserve case

%prep
%autosetup -n iedit-%{version}

%conf
# Fix permissions
chmod 0644 iedit-demo.gif

%build
%make_build

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/iedit
install -m 644 *.el{,c} %{buildroot}/%{_emacs_sitelispdir}/iedit

mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}/%{_emacs_sitelispdir}/iedit/iedit-autoloads.el \
  %{buildroot}%{_emacs_sitestartdir}

%files
%doc README.org iedit-demo.gif
%{_emacs_sitelispdir}/iedit/
%{_emacs_sitestartdir}/iedit-autoloads.el

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0.9.9.9.9-4
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 0.9.9.9.9-2
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Jerry James <loganjerry@gmail.com> - 0.9.9.9.9-1
- Version 0.9.9.9.9
- BR emacs-nox instead of emacs

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 21 2021 Jerry James <loganjerry@gmail.com> - 0.9.9.9-5.20211115git012de2e
- Update from git head, with numerous changes

* Tue Aug 17 2021 Jerry James <loganjerry@gmail.com> - 0.9.9.9-4.20210812git2f504c9
- Update from git head, with the following changes:
- Add iedit-update-key-bindings
- Add iedit-record-changes

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.9-3.20210611git3247f30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul  5 2021 Jerry James <loganjerry@gmail.com> - 0.9.9.9-2.20210611git3247f30
- Update from git head, with the following changes:
- Add prefix arguments to iedit-next-ocurrence and iedit-prev-occurrence
- Add option to save occurrence in the kill ring
- Bring back iedit-goto-first-occurrence

* Wed Mar 10 2021 Jerry James <loganjerry@gmail.com> - 0.9.9.9-1.20210202git0d6d238
- Initial RPM
