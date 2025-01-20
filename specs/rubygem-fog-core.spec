# Generated from fog-core-1.22.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-core

Name: rubygem-%{gem_name}
Version: 2.6.0
Release: 2%{?dist}
Summary: Shared classes and tests for fog providers and services
License: MIT
URL: https://github.com/fog/fog-core
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/fog/fog-core.git && cd fog-core
# git archive -v -o fog-core-2.6.0-spec.tar.gz v2.6.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(excon)
BuildRequires: rubygem(formatador)
BuildRequires: rubygem(mime-types)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-stub-const)
BuildArch: noarch

%description
Shared classes and tests for fog providers and services.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

# Test suite passes with Excon 0.100.0 just fine. Relax the dependency for now
# so we don't need to bump excon ATM.
%gemspec_remove_dep -g excon "~> 1.0"
%gemspec_add_dep -g excon [">= 0.100.0", "< 2"]

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
ln -s %{builddir}/spec spec

ruby -Ispec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUT*
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/SECURITY.md
%doc %{gem_instdir}/changelog.md
%{gem_instdir}/fog-core.gemspec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 31 2024 Vít Ondruch <vondruch@redhat.com> - 2.6.0-1
- Update to fog-core 2.6.0.
  Resolves: rhbz#2256641

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 04 2023 Vít Ondruch <vondruch@redhat.com> - 2.3.0-1
- Update to fog-core 2.3.0.
  Resolves: rhbz#2061766

* Fri Aug 04 2023 Vít Ondruch <vondruch@redhat.com> - 2.2.4-8
- Fix FTBFS due to Minitest 5.19 incompatibilty.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 04 2022 Vít Ondruch <vondruch@redhat.com> - 2.2.4-4
- Fix FTBFS due to test case broken by different Psych return value.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Pavel Valena <pvalena@redhat.com> - 2.2.4-1
- Update to fog-core 2.2.4.
  Resolves: rhbz#1954713

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Pavel Valena <pvalena@redhat.com> - 2.2.3-1
- Update to fog-core 2.2.3.
  Resolves: rhbz#1784518

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Vít Ondruch <vondruch@redhat.com> - 2.1.2-1
- Update to fog-core 2.1.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.43.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Vít Ondruch <vondruch@redhat.com> - 1.43.0-1
- Update to fog-core 1.43.0.

* Thu Sep 08 2016 Vít Ondruch <vondruch@redhat.com> - 1.42.0-1
- Update to fog-core 1.42.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Vít Ondruch <vondruch@redhat.com> - 1.34.0-1
- Update to fog-core 1.34.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Vít Ondruch <vondruch@redhat.com> - 1.29.0-1
- Update to fog-core 1.29.0.

* Tue Jan 06 2015 Brett Lentz <blentz@redhat.com> - 1.27.2-1
- upstream release 1.27.2

* Mon Sep 29 2014 Brett Lentz <blentz@redhat.com> - 1.24.0-1
- upstream release 1.24.0

* Tue Jul 29 2014 Brett Lentz <blentz@redhat.com> - 1.23.0-1
- upstream release 1.23.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Vít Ondruch <vondruch@redhat.com> - 1.22.0-1
- Initial package
