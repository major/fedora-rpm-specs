%global pkg flycheck-pycheckers

Name:           emacs-%{pkg}
Version:        0.16
Release:        5%{?dist}
Summary:        Multiple syntax checker for Python in Emacs, using Flycheck

License:        GPL-3.0-or-later
URL:            https://github.com/msherry/%{pkg}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el
# Fix arguments in call to define-obsolete-variable-alias (since Emacs 28, see
# also https://github.com/msherry/flycheck-pycheckers/pull/60)
Patch0:         %{name}-0.15-emacs28.patch

BuildRequires:  emacs
BuildRequires:  emacs-flycheck
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-flycheck
BuildArch:      noarch

%description
This package provides a way to run multiple syntax checkers on Python code, in
parallel. The list of supported checkers includes:
* pylint
* flake8
* pep8
* pyflakes
* mypy
* bandit
This is an alternative way of running multiple Python syntax checkers in
Flycheck that doesn't depend on Flycheck's chaining mechanism.

Flycheck is opinionated about what checkers should be run, and chaining is
difficult to get right. This package assumes that the user knows what they want,
and can configure their checkers accordingly — if they want to run both flake8
and pylint, that's fine.

This also allows us to run multiple syntax checkers in parallel, rather than
sequentially.


%prep
%autosetup -n %{pkg}-%{version}

# Fix shebang
sed -e 's|^#!.*|#!%{__python3}|' bin/pycheckers.py >bin/pycheckers.py.new && \
touch -r bin/pycheckers.py bin/pycheckers.py.new && \
mv bin/pycheckers.py.new bin/pycheckers.py


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
cp -a bin/ $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
chmod 0755  $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/bin/pycheckers.py

install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc pycheckers-EXAMPLE README.md
%license LICENSE
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 24 2023 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.16-1
- Update to 0.16
- Switch license tag to SPDX

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.15-6
- Fix build with Emacs 28

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.15-1
- Initial RPM release
