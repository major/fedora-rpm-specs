%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-generic-pool
Version:    2.2.2
Release:    7%{?dist}
Summary:    Generic resource pooling for Node.js
# License text is included in README.md.
License:    MIT
URL:        https://github.com/coopernurse/node-pool
Source0:    http://registry.npmjs.org/generic-pool/-/generic-pool-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs

%if 0%{?enable_tests}
BuildRequires:  npm(expresso)
%endif

%description
%{summary}


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/generic-pool
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/generic-pool

%nodejs_symlink_deps


%check
%{__nodejs} -e 'require("./")'

%if 0%{?enable_tests}
%{nodejs_sitelib}/expresso/bin/expresso -I lib test/*.js
%endif


%files
%doc README.md
%{nodejs_sitelib}/generic-pool


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 Piotr Popieluch <piotr1212@gmail.com> - 2.2.2-1
- Unretire and update to 2.2.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.3-2
- restrict to compatible arches

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.3-1
- initial package
