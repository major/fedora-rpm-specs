%global npm_name tape

Name:           nodejs-%{npm_name}
Version:        5.1.1
Release:        6%{?dist}
Summary:        Tap-producing test harness for Node.js and browsers

License:        MIT and ICS
URL:            https://github.com/substack/tape
Source0:        http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt

BuildArch:       noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:         nodejs
BuildRequires:  nodejs-devel

%description
%{summary}.


%prep
%setup -q -n package
cp %{SOURCE3} .
# Setup bundled runtime(prod) node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/tape
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/tape
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{nodejs_sitelib}/tape/bin
install -p -D -m0755 bin/tape %{buildroot}%{nodejs_sitelib}/tape/bin/tape
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/tape/bin/tape %{buildroot}%{_bindir}/tape

%check
# Setup bundled dev node_modules for testing
#   Note: this cannot be in %prep or the dev node_modules
#            can get pulled into the regular rpm
tar xfz %{SOURCE2}
pushd node_modules
ln -s ../node_modules_dev/* .
popd
pushd node_modules/.bin
ln -s ../../node_modules_dev/.bin/* .
popd
# Run tests
./node_modules/.bin/tap test/*.js


%files
%doc readme.markdown
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/tape
%{_bindir}/tape


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Troy Dawson <tdawson@redhat.com> - 5.1.1-1
- Update to 5.1.1
- Bundle runtime (prod) and testing (dev) dependencies

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 4.9.0-5
- Update npm(string.prototype.trim) dependency

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Jared K. Smith <jsmith@fedoraproject.org> - 4.9.0-1
- Update to upstream 4.9.0 release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct  2 2016 Tom Hughes <tom@compton.nu> - 4.6.2-1
- Update to 4.6.2 upstream release

* Fri Sep 30 2016 Tom Hughes <tom@compton.nu> - 4.6.1-2
- Patch npm(inherits) dependency

* Fri Sep 30 2016 Tom Hughes <tom@compton.nu> - 4.6.1-1
- Update to 4.6.1 upstream release

* Mon Jun 20 2016 Tom Hughes <tom@compton.nu> - 4.6.0-1
- Update to 4.6.0 upstream release

* Sun Apr 10 2016 Tom Hughes <tom@compton.nu> - 4.5.1-2
- Update npm(object-inspect) dependency

* Mon Mar  7 2016 Tom Hughes <tom@compton.nu> - 4.5.1-1
- Update to 4.5.1 upstream release

* Fri Mar  4 2016 Tom Hughes <tom@compton.nu> - 4.5.0-3
- Update npm(through) dependency

* Thu Mar  3 2016 Tom Hughes <tom@compton.nu> - 4.5.0-2
- Update npm(resolve) dependency

* Thu Mar  3 2016 Tom Hughes <tom@compton.nu> - 4.5.0-1
- Update to 4.5.0 upstream release
- Enable as many tests as possible.

* Sun Feb 14 2016 Tom Hughes <tom@compton.nu> - 4.4.0-3
- Update npm(function-bind) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Tom Hughes <tom@compton.nu> - 4.4.0-1
- Update to 4.4.0 upstream release

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 4.2.2-2
- Update npm(glob) dependency

* Wed Oct 21 2015 Tom Hughes <tom@compton.nu> - 4.2.2-1
- Update to 4.2.2 upstream release

* Sun Sep  6 2015 Tom Hughes <tom@compton.nu> - 4.2.0-1
- update to upstream release 4.2.0
- move LICENSE file to %%license

* Fri Sep  4 2015 Tom Hughes <tom@compton.nu> - 3.0.1-4
- Fix deep-equal dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.0.1-2
- fix dependency versions

* Sun Oct 26 2014 Tom Hughes <tom@compton.nu> - 3.0.1-1
- update to upstream release 3.0.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-1
- new upstream release 1.0.4
- conditionalize ExclusiveArch

* Wed May 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.2-1
- initial package
