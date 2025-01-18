%global pkg blacken

%global commit 880cf502198753643a3e2ccd4131ee6973be2e8a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20210406

Name:           emacs-%{pkg}
Version:        0
Release:        0.16.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Python Black for Emacs

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/pythonic-emacs/%{pkg}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        %{pkg}-init.el

BuildRequires:  emacs
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       python3-black
BuildArch:      noarch

%description
Blacken uses black to format a Python buffer. It can be called explicitly on a
certain buffer, but more conveniently, a minor-mode 'blacken-mode' is provided
that turns on automatically running black on a buffer before saving.

To automatically format all Python buffers before saving, add the function
blacken-mode to python-mode-hook:

  (add-hook 'python-mode-hook 'blacken-mode)


%prep
%autosetup -n %{pkg}-%{commit}


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
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20210406git880cf50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.15.20210406git880cf50
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20210406git880cf50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20210406git880cf50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20210406git880cf50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20210406git880cf50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20210406git880cf50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20210406git880cf50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20210406git880cf50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 05 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0-0.7.20210406git880cf50
- Update to latest snapshot

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200626git784da60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20200626git784da60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 01 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0-0.4.20200626git784da60
- Switch to new upstream
- Update to latest snapshot

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190521git1874018
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20190521git1874018
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 02 2019 Mohamed El Morabity <melmorabity@fedoraproject.org> - 0-0.1.20190521git1874018
- Initial RPM release
