%global npm_name supervisor

%{?nodejs_find_provides_and_requires}

Summary:       A supervisor program for running nodejs programs
Name:          nodejs-%{npm_name}
Version:       0.12.0
Release:       12%{?dist}
License:       MIT
URL:           https://github.com/isaacs/node-supervisor
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-devel
BuildRequires: txt2man
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
A little supervisor script for nodejs. It runs your program,
and watches for code changes, so you can have hot-code 
reloading like behavior, without worrying about memory leaks 
and making sure you clean up all the inter-module references, 
and without a whole new require system. 

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr lib package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

# Setup Binaries
mkdir %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js %{buildroot}%{_bindir}/node-supervisor
ln -s %{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js %{buildroot}%{_bindir}/supervisor

# Create man pages
mkdir -p %{buildroot}%{_mandir}/man1
%{buildroot}%{nodejs_sitelib}/%{npm_name}/lib/cli-wrapper.js -h > helpfile
txt2man -P node-supervisor -t node-supervisor -r %{version} helpfile > %{buildroot}%{_mandir}/man1/node-supervisor.1
txt2man -P supervisor -t supervisor -r %{version} helpfile > %{buildroot}%{_mandir}/man1/supervisor.1
rm -f helpfile

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}
%{_bindir}/node-supervisor
%{_bindir}/supervisor
%{_mandir}/man1/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Tom Hughes <tom@compton.nu> - 0.12.0-1
- Update to 0.12.0
- Use %%{nodejs_arches}

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 09 2016 Troy Dawson <tdawson@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Fri Apr 29 2016 Troy Dawson <tdawson@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Troy Dawson <tdawson@redhat.com> - 0.9.0-1
- Update to 0.9.0

* Mon Sep 21 2015 Troy Dawson <tdawson@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Mon Jul 27 2015 Troy Dawson <tdawson@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 21 2014 Troy Dawson <tdawson@redhat.com> - 0.6.0-1
- Update to version 0.6.0

* Wed Feb 19 2014 Troy Dawson <tdawson@redhat.com> - 0.5.7-1
- Update to version 0.5.7

* Thu Feb 06 2014 Troy Dawson <tdawson@redhat.com> - 0.5.6-1
- Update to version 0.5.6
- add nodejs exclusive arch
- add macro to invoke dependency generator on EL6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Troy Dawson <tdawson@redhat.com> - 0.5.2-2
- Fixed Summary and Description spelling errors
- Added BSD License file, from upstream
- Create man pages

* Fri Mar 01 2013 Troy Dawson <tdawson@redhat.com> - 0.5.2-1
- Update to 0.5.2
- Update spec to Fedora nodejs standards

* Wed Sep 05 2012 Troy Dawson <tdawson@redhat.com> - 0.4.1-2
- Rewored spec file using tchor template

* Wed Sep 05 2012 Troy Dawson <tdawson@redhat.com> - 0.4.1-1
- Initial build

