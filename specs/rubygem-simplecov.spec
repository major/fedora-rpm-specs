%global gem_name simplecov
%global rubyabi 1.9.1

Summary:       Code coverage analysis tool for Ruby 1.9
Name:          rubygem-%{gem_name}
Version:       0.13.0
Release:       18%{?dist}
License:       MIT
URL:           http://github.com/colszowka/simplecov
Source0:       http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} >= 19 || 0%{?rhel} > 6
Requires:      ruby(release)
%else
Requires:      ruby(abi) >= %{rubyabi}
%endif
Requires:      ruby 
Requires:      rubygems
Requires:      rubygem(docile) => 1.1.0
Requires:      rubygem(multi_json) => 1.0
Requires:      rubygem(simplecov-html) => 0.8.0
BuildRequires: ruby 
BuildRequires: rubygems-devel 
# For tests
BuildRequires: rubygem(aruba)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(capybara)
BuildRequires: rubygem(cucumber)
BuildRequires: rubygem(docile)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(simplecov-html)
BuildRequires: rubygem(test-unit)
BuildArch:     noarch
Provides:      rubygem(%{gem_name}) = %{version}

%description
Code coverage for Ruby 1.9 with a powerful configuration library and automatic
merging of coverage across test suites


%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

#cleanup
rm -f %{buildroot}%{gem_instdir}/.gitignore
rm -f %{buildroot}%{gem_instdir}/.rspec
rm -f %{buildroot}%{gem_instdir}/.rubocop.yml
rm -f %{buildroot}%{gem_instdir}/.travis.yml
rm -rf %{buildroot}%{gem_instdir}/.yardopts
rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -f %{buildroot}%{gem_instdir}/Gemfile
rm -f %{buildroot}%{gem_instdir}/simplecov.gemspec
chmod 0755 %{buildroot}%{gem_instdir}/Rakefile
mv %{buildroot}%{gem_instdir}/doc %{buildroot}/%{gem_docdir}/

%check
pushd %{buildroot}%{gem_instdir}
rm -rf spec/faked_project/
rspec -Ilib spec
rm -rf %{buildroot}%{gem_instdir}/tmp
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/cucumber.yml
%{gem_instdir}/features
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/README.md
%{gem_instdir}/CONTRIBUTING.md

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Vít Ondruch <vondruch@redhat.com> - 0.13.0-1
- Update to SimpleCov 0.13.0 (Ruby 2.4 compatibility).

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0 (to match json 2)

* Tue Nov 29 2016 Petr Šabata <contyk@redhat.com> - 0.11.2-2
- Remove the unneded build dependancy on shoulda

* Tue Feb 23 2016 Troy Dawson <tdawson@redhat.com> - 0.11.2-1
- Updated to version 0.11.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jul 21 2015 Troy Dawson <tdawson@redhat.com> - 0.10.0-1
- Updated to version 0.10.0
- Changed check from testrb2 to ruby

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Jan Klepek <jan.klepek at, gmail.com>  - 0.8.2-4
- fix for correct EPEL7 build

* Wed Feb 05 2014 Troy Dawson <tdawson@redhat.com> - 0.8.2-3
- Updated all dependencies
- Re-enabled tests

* Wed Feb 05 2014 Troy Dawson <tdawson@redhat.com> - 0.8.2-2
- Updated simplecov-html dependency


* Tue Feb 04 2014 Troy Dawson <tdawson@redhat.com> - 0.8.2-1
- Updated to version 0.8.2
- Update to latest ruby spec guidelines

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Troy Dawson <tdawson@redhat.com> - 0.7.1-7
- Fix to make it build/install on F19+
- Removed testing until ruby2 gems have stabilized

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Troy Dawson <tdawson@redhat.com> - 0.7.1-5
- Correctly declared License

* Fri Nov 30 2012 Troy Dawson <tdawson@redhat.com> - 0.7.1-4
- Removed unneeded rubygem-appraisal dependancy

* Fri Nov 30 2012 Troy Dawson <tdawson@redhat.com> - 0.7.1-3
- Use pushd and pop in the test/check section

* Thu Nov 29 2012 Troy Dawson <tdawson@redhat.com> - 0.7.1-2
- Now with tests

* Mon Nov 19 2012 Troy Dawson <tdawson@redhat.com> - 0.7.1-1
- Update to 0.7.1

* Mon Aug 27 2012 Troy Dawson <tdawson@redhat.com> - 0.6.4-1
- Initial package
