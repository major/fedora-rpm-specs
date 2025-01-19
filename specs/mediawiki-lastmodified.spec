# Linked to the version of mediawiki in each Fedora release.
# Rawhide has 1.34, so we package the latest commit in the REL_1_34 branch.
# For non rawhide releases, this will change accordingly
# Remember to ensure that the upgrade path is maintained
%global commit be28231ebcd539fc99775811e5dc6df9064cfa94

%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global reponame mediawiki-extensions-LastModified

Name:           mediawiki-lastmodified
Version:        0
Release:        0.16.20200627git%{commit}%{?dist}
Summary:        Show the last modified page time

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.mediawiki.org/wiki/Extension:LastModified
Source0:        https://github.com/wikimedia/%{reponame}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

Requires:       mediawiki >= 1.34

%description
The LastModified extension displays text on the page showing the last modified
page time.

%prep
%autosetup -n %{reponame}-%{commit}
# Remove unneeded dotfiles
rm ./{.gitignore,.gitreview,.jshintrc} -v

%build
# Nothing here

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/{i18n,modules}
install -cpm 644 ./LastModified.php $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./i18n/* $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/i18n/
install -cpm 644 ./modules/* $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/i18n/
install -cpm 644 ./*js $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./*json $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./*md $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/


%files
%{_datadir}/mediawiki/extensions/LastModified


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0-0.15.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 27 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.4.20200627gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Update for mediawiki 1.34 in rawhide

* Tue Feb 11 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.3.20200210gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Fix versioning in requires
- remove unneeded line in install section
- include all files

* Mon Feb 10 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.1.20200210gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Initial rpm build
