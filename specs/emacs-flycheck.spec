%global pkg flycheck

Name:           emacs-%{pkg}
Version:        34.1
Release:        3%{?dist}
Summary:        On the fly syntax checking for GNU Emacs

License:        GPL-3.0-or-later
URL:            https://www.flycheck.org/
Source0:        https://github.com/%{pkg}/%{pkg}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-dash
BuildRequires:  emacs-pkg-info
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash
Requires:       emacs-pkg-info
BuildArch:      noarch

%description
Flycheck is a modern on-the-fly syntax checking extension for GNU Emacs,
intended as replacement for the older Flymake extension which is part of GNU
Emacs.


%prep
%autosetup -n %{pkg}-%{version}


%build
for i in *.el; do
    %{_emacs_bytecompile} $i
done


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc CHANGES.old CHANGES.rst MAINTAINERS README.md
%license COPYING
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 34.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 01 2024 Mohamed El Morabity <melmorabity@fedoraproject.org> - 34.1-1
- Update to 34.1
- Migrate to SPDX license

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Mar 30 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 32-1
- Update to 32

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 31-1
- Initial RPM release
