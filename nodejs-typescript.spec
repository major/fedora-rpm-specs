%global npm_name typescript

Name:           nodejs-%{npm_name}
Version:        4.1.3
Release:        6%{?dist}
Summary:        A language for application scale JavaScript development
License:        ASL 2.0
URL:            https://www.typescriptlang.org
Source0:        http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-devel


%description
TypeScript is a language for application-scale JavaScript. TypeScript
adds optional types, classes, and modules to JavaScript. TypeScript
supports tools for large-scale JavaScript applications for any browser,
for any host, on any OS. TypeScript compiles to readable, standards-based
JavaScript.


%prep
%setup -qn package


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json bin/ lib/ %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Symlink tsc executable file to _bindir
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{npm_name}/bin/tsc %{buildroot}%{_bindir}


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'


%files
%{_bindir}/tsc
%{nodejs_sitelib}/%{npm_name}
%doc ThirdPartyNoticeText.txt README.md CopyrightNotice.txt
%license LICENSE.txt


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Carl George <carl@george.computer> - 4.1.3-1
- Latest upstream

* Mon Jan 11 2021 Carl George <carl@george.computer> - 4.0.2-2
- Rebuild from unretirement

* Tue Aug 25 2020 Carl George <carl@george.computer> - 4.0.2-1
- Latest upstream rhbz#1825686

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 23 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.8.3-1
- Update to upstream 2.8.3 release

* Fri Apr 06 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.8.1-1
- Update to upstream 2.8.1 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 Gerard Ryan <galileo@fedoraproject> - 1.4.1-1
- Initial package
