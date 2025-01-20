%global gem_name coveralls

Summary:       A Ruby implementation of the Coveralls API
Name:          rubygem-%{gem_name}
Version:       0.8.13
Release:       24%{?dist}
License:       MIT
URL:           https://coveralls.io
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: git
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(base64)
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(multi_json)
BuildRequires: rubygem(pry)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(simplecov)
BuildRequires: rubygem(term-ansicolor)
BuildRequires: rubygem(thor)
BuildRequires: rubygem(vcr)
BuildRequires: rubygem(webmock)
BuildRequires: txt2man
BuildArch:     noarch

%description
Coveralls works with your continuous integration 
server to give you test coverage history and statistics.

This package is a Ruby implementation of the Coveralls API.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n  %{gem_name}-%{version}

# Work around until tins gets updated in Fedora
%gemspec_remove_dep -g tins "~> 1.6.0"
%gemspec_add_dep -g tins ">= 1.0.0"

# Relax JSON and SimpleCov dependency.
# https://github.com/lemurheavy/coveralls-ruby/commit/ddf7ae7c269016b06dfe6800f786a87c3c771ac6
%gemspec_remove_dep -g json "~> 1.8"
%gemspec_add_dep -g json [">= 1.8", "< 3"]
%gemspec_remove_dep -g simplecov "~> 0.11.0"
%gemspec_add_dep -g simplecov "~> 0.11"

# https://github.com/lemurheavy/coveralls-ruby/pull/132
%gemspec_remove_dep -g thor "~> 0.19.1"
%gemspec_add_dep -g thor [">= 0.19.1", "< 2"]

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}

chmod 755 %{buildroot}%{gem_instdir}/Rakefile
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
find %{buildroot}%{gem_instdir}/spec -name *.rb | xargs chmod a-x

# Create man pages
mkdir -p %{buildroot}%{_mandir}/man1
%{buildroot}%{gem_instdir}/bin/coveralls help > helpfile
txt2man -P coveralls -t coveralls -r %{version} helpfile > %{buildroot}%{_mandir}/man1/coveralls.1
rm -f helpfile

# Remove build leftovers.
rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.rspec,.ruby-version,.travis.yml,.yard*}
rm -f %{buildroot}%{gem_instdir}/{Gemfile,coveralls-ruby.gemspec}

%check
pushd ./%{gem_instdir}
# We don't care about code coverage. But on top of it, there was some change
# in Ruby 3.1 causing issues with double loading SimpleCov. Therefore disable
# the code coverage.
# https://github.com/lemurheavy/coveralls-ruby/issues/173
sed -i '/^setup_formatter$/ s/^/#/' spec/spec_helper.rb

# Two tests are not working in koji, but do by hand, skip them
rspec -Ilib --tag ~if spec
popd

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{_bindir}/coveralls
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.13-23
- Add BR: rubygem(base64) explicitly for ruby34

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 17 2022 Vít Ondruch <vondruch@redhat.com> - 0.8.13-16
- Disable code coverage due to Ruby 3.1 compatibility issues.
- Remove the rubygem(rest-client) depednency.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.8.13-9
- Relax Thor dependency.

* Fri Feb 15 2019 Troy Dawson <tdawson@redhat.com> - 0.8.13-8
- Fix FTBFS (#1606179) (#1675910)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Vít Ondruch <vondruch@redhat.com> - 0.8.13-2
- Relax JSON and SimpleCov dependency.

* Tue Mar 08 2016 Troy Dawson <tdawson@redhat.com> - 0.8.13-1
- Updated to version 0.8.13

* Tue Feb 23 2016 Troy Dawson <tdawson@redhat.com> - 0.8.11-1
- Updated to version 0.8.11
- Fix dependencies

* Tue Feb 16 2016 Troy Dawson <tdawson@redhat.com> - 0.8.10-1
- Update to 0.8.11

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Troy Dawson <tdawson@redhat.com> - 0.8.2-1
- Update to 0.8.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jul 18 2014 Troy Dawson <tdawson@redhat.com> - 0.7.0-4
- Spec file tweaks to accomodate different releases (#1121107)

* Mon Jul 07 2014 Troy Dawson <tdawson@redhat.com> - 0.7.0-3
- Spec file tweaks

* Thu Jul 03 2014 Troy Dawson <tdawson@redhat.com> - 0.7.0-2
- Add man page

* Wed Apr 02 2014 Troy Dawson <tdawson@redhat.com> - 0.7.0-1
- Initial package
