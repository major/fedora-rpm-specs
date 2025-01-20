# Generated from jbuilder-1.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jbuilder

Name: rubygem-%{gem_name}
Version: 2.11.5
Release: 8%{?dist}
Summary: Create JSON structures via a Builder-style DSL
License: MIT
URL: https://github.com/rails/jbuilder
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activemodel)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(railties)
BuildArch: noarch

%description
Jbuilder gives you a simple DSL for declaring JSON structures that beats
massaging giant hash structures. This is particularly helpful when
the generation process is fraught with conditionals and loops.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Get rid of Bundler.
sed -i '/bundler\/setup/ s/^/#/' test/test_helper.rb

ruby -Ilib:test -e "Dir.glob './test/*_test.rb', &method(:require)"
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/test
%{gem_instdir}/gemfiles
%{gem_instdir}/Appraisals

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Vít Ondruch <vondruch@redhat.com> - 2.11.5-1
- Update Jbuilder 2.11.5.
  Resolves: rhbz#2023081

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Vít Ondruch <vondruch@redhat.com> - 2.11.2-1
- Update Jbuilder 2.11.2.
  Resolves: rhbz#1919351

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 21:17:44 CET 2020 Pavel Valena <pvalena@redhat.com> - 2.10.1-1
- Update to jbuilder 2.10.1.
  Resolves: rhbz#1878373

* Fri Sep 11 2020 Vít Ondruch <vondruch@redhat.com> - 2.10.0-1
- Remove unneeded BR: rubygem(multi_json).

* Thu Aug 20 23:37:59 GMT 2020 Pavel Valena <pvalena@redhat.com> - 2.10.0-1
- Update to jbuilder 2.10.0.
  Resolves: rhbz#1709483

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 2.7.0-1
- Update to 2.7.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 20 2016 Vít Ondruch <vondruch@redhat.com> - 2.5.0-1
- Update Jbuilder 2.5.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Josef Stribny <jstribny@redhat.com> - 2.3.2-1
- Update to 2.3.2

* Mon Jun 29 2015 Josef Stribny <jstribny@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Josef Stribny <jstribny@redhat.com> - 2.2.12-1
- Update to 2.2.12

* Tue Oct 14 2014 Josef Stribny <jstribny@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Mon Aug 18 2014 Josef Stribny <jstribny@redhat.com> - 2.1.3-1
- Update to 2.1.3

* Wed Jul 09 2014 Josef Stribny <jstribny@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Thu Jun 12 2014 Josef Stribny <jstribny@redhat.com> - 2.1.0-1
- Update to jbuilder 2.1.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Josef Stribny <jstribny@redhat.com> - 2.0.4-1
- Update to jbuilder 2.0.4

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 1.5.0-1
- Initial package
