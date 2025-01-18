
Name:		php-oojs-oojs-ui
Version:	0.51.2
Release:	1%{?dist}
Summary:	Object-Oriented JavaScript – User Interface

License:	MIT
URL:		http://www.mediawiki.org/wiki/OOjs_UI
# Wikimedia changed server software and now doesn't support downloads
# https://phabricator.wikimedia.org/T111887
Source0:	https://github.com/wikimedia/oojs-ui/archive/refs/tags/v%{version}.tar.gz#/oojs-ui-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 7.4.3

Provides:	php-composer(oojs/oojs-ui) = %{version}

%description
OOjs UI (Object-Oriented JavaScript – User Interface) is a library that allows
developers to rapidly create front-end web applications that operate
consistently across a multitude of browsers.


%prep
%autosetup -n oojs-ui-%{version}


%build
phpab --output php/autoload.php php


%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/OOUI
cp -rp php/* %{buildroot}%{_datadir}/php/OOUI


%files
%license LICENSE-MIT
%doc AUTHORS.txt History.md README.md
%{_datadir}/php/OOUI


%changelog
* Thu Jan 16 2025 Michael Cronenworth <mike@cchtml.com> - 0.51.2-1
- Update to 0.51.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.48.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 03 2024 Michael Cronenworth <mike@cchtml.com> - 0.48.1-1
- version update

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.46.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.46.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Michael Cronenworth <mike@cchtml.com> - 0.46.3-1
- version update

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 26 2023 Michael Cronenworth <mike@cchtml.com> - 0.44.5-1
- version update

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.44.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Michael Cronenworth <mike@cchtml.com> - 0.44.3-1
- version update

* Tue Nov 01 2022 Michael Cronenworth <mike@cchtml.com> - 0.43.2-1
- version update

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Michael Cronenworth <mike@cchtml.com> - 0.42.0-1
- version update

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.41.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Michael Cronenworth <mike@cchtml.com> - 0.41.3-1
- version update

* Sun Apr 25 2021 Michael Cronenworth <mike@cchtml.com> - 0.39.3-3
- Remove old hack (RHBZ#1953335)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.39.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Michael Cronenworth <mike@cchtml.com> - 0.39.3-1
- version update

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 05 2020 Michael Cronenworth <mike@cchtml.com> - 0.34.1-1
- version update

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 0.31.3-1
- version update

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 01 2019 Michael Cronenworth <mike@cchtml.com> - 0.29.2-1
- version update

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Michael Cronenworth <mike@cchtml.com> - 0.21.2-1
- version update

* Fri Feb 24 2017 Michael Cronenworth <mike@cchtml.com> - 0.17.10-1
- version update
- tests were removed by upstream

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 26 2015 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.11.6-2
- Drop the non-ascii character in the summary field

* Thu Jun 25 2015 Michael Cronenworth <mike@cchtml.com> - 0.11.6-1
- Initial package

