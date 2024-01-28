%global gem_name selenium-webdriver

Summary: Selenium is a browser automation tool for automated testing of webapps and more
Name: rubygem-%{gem_name}
Version: 4.1.0
Release: 8%{?dist}
License: ASL 2.0
URL: https://selenium.dev
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# The tests are not shipped with the gem; you can get them like so:
# git clone https://github.com/SeleniumHQ/selenium --no-checkout
# git -C selenium archive -v -o selenium-webdriver-4.1.0-spec.txz selenium-4.1.0 rb/spec

Source1: %{gem_name}-%{version}-spec.txz
# https://github.com/SeleniumHQ/selenium/commit/590cfbb9c894a692283d25e138627a0828799c5a
# Extracted minimum part from the above change to make test pass with ruby32
# A bit modified to apply v4.1.0
Patch0:  rubygem-selenium-webdriver-gets-tests-passing-with-ruby32.patch

BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(childprocess)
BuildRequires: rubygem(rubyzip)
BuildRequires: rubygem(rack)
BuildRequires: ruby
BuildArch: noarch

%description
Selenium implements the W3C WebDriver protocol to automate popular browsers.
It aims to mimic the behaviour of a real user as it interacts with the
application's HTML. It's primarily intended for web application testing,
but any web-based task can automated.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -n %{gem_name}-%{version} -b1
(
cd %{_builddir}
%patch0 -p1
)

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_libdir}/selenium/webdriver/firefox/native/linux/x86/x_ignore_nofocus.so
rm -f %{buildroot}%{gem_libdir}/selenium/webdriver/firefox/native/linux/amd64/x_ignore_nofocus.so
rm -f %{buildroot}%{gem_libdir}/selenium/webdriver/ie/native/x64/IEDriver.dll
rm -f %{buildroot}%{gem_libdir}/selenium/webdriver/ie/native/win32/IEDriver.dll

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/rb/spec .

# Fake java runtime (needed for spec/unit/selenium/server_spec.rb testsuite)
rm -rf TMPBINDIR
mkdir TMPBINDIR
cd TMPBINDIR
ln -sf /bin/true java
cd ..
export PATH=$(pwd)/TMPBINDIR:$PATH

# Require firefox extension jar
# (included in thirdparty directory, available on github, not included in gem)
sed -i spec/unit/selenium/webdriver/firefox/profile_spec.rb \
    -e '\@can install extension@s|^\(.*\)$|\1 ; skip|' \
    -e '\@can install web extension@s|^\(.*\)$|\1 ; skip|' \
    %{nil}

# Unable to run integration tests (requires FF or chrome)
# Skipping execution spec/integration
rspec -Ilib:%{_builddir}/rb/lib spec/unit
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/NOTICE
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec


%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan  2 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.0-5
- Apply the upstream patch for ruy3.2 instead of previous patch

* Sat Dec 31 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.0-4
- Apply upstream PR under review for ruby3.2 test failure wrt new IO#path method
  and selenium rspec internal mocking File.exist? issue

* Sat Dec 31 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.0-3
- Clean up spec file for test suite
  - BR: firefox is actually not needed, just skip test suite
    requiring real extension jar file
  - Fake java runtime
  - Explicity execute spec/unit testsuite only

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 13 2022 Pavel Valena <pvalena@redhat.com> - 4.1.0-1
- Update to selenium-webdriver 4.1.0.
  Resolves: rhbz#2013663

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.142.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.142.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.142.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 14:13:22 GMT 2020 Pavel Valena <pvalena@redhat.com> - 3.142.7-3
- Relax Childprocess dependency.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.142.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Pavel Valena <pvalena@redhat.com> - 3.142.7-1
- Update to selenium-webdriver 3.142.7.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Vít Ondruch <vondruch@redhat.com> - 2.45.0-12
- Relax rubyzip dependency.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 07 2019 Vít Ondruch <vondruch@redhat.com> - 2.45.0-10
- Relax childprocess dependency.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.45.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.45.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Mo Morsi <mmorsi@redhat.com> - 2.45.0-2
- Fix dependencies

* Thu Apr 09 2015 Mo Morsi <mmorsi@redhat.com> - 2.45.0-1
- Update to 2.45.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.3.2-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 2.3.2-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 03 2011 Chris Lalancette <clalance@redhat.com> - 2.3.2-1
- Initial package
