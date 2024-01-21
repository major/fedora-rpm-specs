%global pkg logstash-conf

Name:           emacs-%{pkg}
Version:        0.4
Release:        6%{?dist}
Summary:        Emacs mode for editing Logstash configuration files

License:        GPLv3+
URL:            https://github.com/Wilfred/%{pkg}.el/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
BuildArch:      noarch

%description
A basic Emacs mode for editing Logstash configuration files.

Features:
  * Syntax highlighting
  * Indentation


%prep
%autosetup -n %{pkg}.el-%{version}


%build
%{_emacs_bytecompile} %{pkg}.el


%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_emacs_sitestartdir}/%{pkg}-init.el


%files
%doc README.md
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el


%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 06 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0.4-1
- Initial RPM release
