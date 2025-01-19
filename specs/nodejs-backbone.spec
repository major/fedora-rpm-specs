%global modname backbone

%if ! ( 0%{?fedora} || 0%{?rhel} >= 7 )
%{?nodejs_find_provides_and_requires}
%global nodejs_arches %{ix86} x86_64 %{arm}
%endif

# tests are disabled for now (need QUnit, runs in PhantomJS?)
%bcond_with tests

Name:           nodejs-%{modname}
Version:        1.3.3
Release:        20%{?dist}
Summary:        Models, Views, Collections, and Events for JavaScript applications (Nodejs module)
License:        MIT
URL:            http://backbonejs.org/
Source0:        http://registry.npmjs.org/%{modname}/-/%{modname}-%{version}.tgz
# git archive --format=tar --prefix=test/ 1.3.3:test/ | bzip2 >tests-1.3.3.tar.bz2
Source1:        tests-%{version}.tar.bz2
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel
BuildRequires:  uglify-js
Requires:       js-%{modname} = %{version}-%{release}
%if %{with tests}
BuildRequires:  nodejs
BuildRequires:  nodejs-qunit
%endif

%description
Backbone supplies structure to JavaScript-heavy applications by providing 
models key-value binding and custom events, collections with a rich API of 
enumerable functions, views with declarative event handling, and connects it 
all to your existing application over a RESTful JSON interface.

This package provides Backbone as a Nodejs module, for use in server-side 
applications or with browserify.

%package -n js-%{modname}
Summary:        Models, Views, Collections and Events for JavaScript applications
Requires:       web-assets-filesystem

%description -n js-%{modname}
Backbone supplies structure to JavaScript-heavy applications by providing 
models key-value binding and custom events, collections with a rich API of 
enumerable functions, views with declarative event handling, and connects it 
all to your existing application over a RESTful JSON interface.

%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package
rm backbone-min.{js,map}

%build
uglifyjs backbone.js -m --source-map -o backbone-min.js

%if %{with tests}
%check
%nodejs_symlink_deps --check
# ?
%endif

%install
mkdir -p %{buildroot}%{_jsdir}/%{modname}
cp -p backbone.js backbone-min.js backbone-min.js.map %{buildroot}%{_jsdir}/%{modname}/
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modname}
cp -p backbone.js package.json %{buildroot}%{nodejs_sitelib}/%{modname}/
%nodejs_symlink_deps

%files
%{nodejs_sitelib}/%{modname}

%files -n js-%{modname}
%doc README.md
%license LICENSE
%{_jsdir}/%{modname}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Dan Callaghan <dcallagh@redhat.com> - 1.3.3-1
- upstream release 1.3.3: http://backbonejs.org/#changelog

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 27 2015 Dan Callaghan <dcallagh@redhat.com> - 1.2.3-1
- upstream bug fix release 1.2.3: http://backbonejs.org/#changelog

* Tue Sep 01 2015 Dan Callaghan <dcallagh@redhat.com> - 1.2.2-1
- upstream release 1.2.2: http://backbonejs.org/#changelog

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 12 2014 Dan Callaghan <dcallagh@redhat.com> - 1.1.2-2
- updated package summaries and descriptions

* Sun Oct 12 2014 Dan Callaghan <dcallagh@redhat.com> - 1.1.2-1
- initial version
