Name:		mediawiki-backtick-code
Version:	0.0.4
Release:	9%{?dist}
Summary:	MediaWiki extension to wrap text between backticks in code tags

License:	GPLv2+
URL:		https://www.mediawiki.org/wiki/Extension:BacktickCode
Source0:	https://pagure.io/%{name}-extension/raw/master/f/%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	php(language) >= 5.3.0
BuildRequires:	mediawiki >= 1.29.0


%description
The BacktickCode extension wraps <code> tags around wikitext which is placed
 `between backtick characters`. This provides a handy wiki-editing shortcut 
for wikis that expect a lot of inlined <code> snippets in its pages, and 
functions similarly to the standard MediaWiki ''' -> <b> bold formatting
shortcut. Backtick characters within <pre> blocks will not be altered by 
this extension. Backticks outside of <pre> blocks can also be output to the
 page by escaping them as \`. 

%prep
%setup -q -n %{name}-%{version}


%build


%install
install -d %{buildroot}%{_datadir}/mediawiki/extensions/BacktickCode/
install -cpm 644 BacktickCode.php %{buildroot}%{_datadir}/mediawiki/extensions/BacktickCode/
install -cpm 644 extension.json %{buildroot}%{_datadir}/mediawiki/extensions/BacktickCode/

%files
%license LICENSE
%doc README.md 
%dir %{_datadir}/mediawiki/extensions/BacktickCode
%{_datadir}/mediawiki/extensions/BacktickCode/BacktickCode.php
%{_datadir}/mediawiki/extensions/BacktickCode/extension.json

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 10 2018 Zach Villers <zachvatwork@gmail.com> 0.0.4-1
- removed defattr macro and update install subsection
- bumped version to '0.0.4-1.fc28' 

* Mon Jul 09 2018 Zach Villers <zachvatwork@gmail.com>
- Cleaned up files subsection
- Cleaned up build subsection
- Added README

* Wed Jul 04 2018 Zach Villers <zachvatwork@gmail.com> 0.0.3-1
- Updated based on package review feedback
- removed uneccesary buildroot
- make sure package owns its directory
- bumped to ver 0.0.3

* Fri Jun 29 2018 Zach Villers <zachvatwork@gmail.com> 0.0.2-1
- hooked to pagure
- fixed grumblings from rpmlint of srpm

* Thu Jun 28 2018 Zach Villers <zachvatwork@gmail.com> 0.0.1-1
- update name of package and install location
- bumped ver

* Thu Jun 21 2018 Zach Villers <zachvatwork@gmail.com> 0.0.1-1
- updates to confirm with mediawiki extension packages

* Wed Jun 20 2018 Zach Villers <zachvatwork@gmail.com> 0.0.1-1
- initial build try

