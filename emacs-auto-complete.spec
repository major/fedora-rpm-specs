%global pkg auto-complete

Name:           emacs-%{pkg}
Version:        1.5.1
Release:        7%{?dist}
Summary:        Emacs auto-complete package

License:        GPLv3+
URL:            https://github.com/%{pkg}/%{pkg}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
BuildRequires:  emacs-popup
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-popup
BuildArch:      noarch

%description
Auto-Complete is an intelligent auto-completion extension for Emacs. It extends
the standard Emacs completion interface and provides an environment that allows
users to concentrate more on their own work.


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


%check
emacs --batch -q --no-site-file --no-splash \
    -L $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/ \
    -l tests/run-test.el \
    -f ert-run-tests-batch-and-exit


%files
%doc README.md
%license COPYING.GPLv3
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 07 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.1-4
- Update autostart file
- Add tests

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 20 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.5.1-1
- Initial RPM release
