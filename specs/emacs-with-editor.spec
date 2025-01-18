%global pkg with-editor
%global pkgname With-Editor

Name:           emacs-%{pkg}
Version:        3.0.2
Release:        12%{?dist}
Summary:        Use Emacsclient as the editor of child processes
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/magit/with-editor
Source0:        %{url}/archive/v%{version}/%{pkg}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs make texinfo texinfo-tex
BuildRequires:  emacs-dash >= 2.13
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-dash >= 2.13

%description
%{pkgname} makes it possible to reliably use the Emacsclient as the editor
of child processes.

%prep
%autosetup -n %{pkg}-%{version}

%build
%make_build

%install
# With-Editor doesn't provide an install target.
install -D -p -m 644 %{pkg}.info %{buildroot}/%{_infodir}/%{pkg}.info
install -D -p -m 644 -t %{buildroot}/%{_emacs_sitelispdir}/%{pkg} \
  %{pkg}-autoloads.el %{pkg}.el %{pkg}.elc

%files
%license LICENSE
%doc README.md
%{_emacs_sitelispdir}/%{pkg}
%{_infodir}/%{pkg}.info.*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.2-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 3.0.2-1
- Initial packaging
