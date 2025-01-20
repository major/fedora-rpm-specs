%global gem_name jmespath

%if 0%{?rhel} && 0%{?rhel} <= 7
%global use_tests 0
%else
%global use_tests 1
%endif

Name:           rubygem-%{gem_name}
Version:        1.6.2
Release:        7%{?dist}
Summary:        JMESPath - Ruby Edition

License:        Apache-2.0
URL:            http://github.com/trevorrowe/jmespath.rb
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/trevorrowe/jmespath.rb && cd jmespath.rb
# git checkout v1.6.2
# tar -czf rubygem-jmespath-1.6.2-repo.tgz spec/ CHANGELOG.md README.md
Source1:        %{name}-%{version}-repo.tgz

BuildArch:      noarch
BuildRequires:  rubygems-devel
%if 0%{?use_tests}
BuildRequires:  rubygem(json)
BuildRequires:  rubygem(rspec) >= 3
BuildRequires:  rubygem(rspec) < 4
%endif
Requires:       rubygem(json)
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Implements JMESPath for Ruby.


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version} -a 1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

cp -a CHANGELOG.md README.md %{buildroot}%{gem_instdir}/


%check
%if 0%{?use_tests}
cp -pr spec/ ./%{gem_instdir}
pushd .%{gem_instdir}
# not using bundler - perform only the test without json dependency
echo "require 'jmespath'" > spec/spec_helper.rb
rspec -Ilib spec
rm -rf spec/
popd
%endif


%files
%dir %{gem_instdir}/
%license %{gem_instdir}/LICENSE.txt
%{_bindir}/jmespath.rb
# required at runtime
%{gem_instdir}/VERSION
%{gem_instdir}/bin/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 František Dvořák <valtri@civ.zcu.cz> - 1.6.2-1
- Update to 1.6.2 (#2148507)
- Install binary executable

* Mon Nov 21 2022 František Dvořák <valtri@civ.zcu.cz> - 1.6.1-3
- Update license field to SPDX identifier

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 07 2022 František Dvořák <valtri@civ.zcu.cz> - 1.6.1-1
- Update to 1.6.1 (#2054384)

* Mon Feb 07 2022 František Dvořák <valtri@civ.zcu.cz> - 1.5.0-1
- Update to 1.5.0 (#2039052)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 František Dvořák <valtri@civ.zcu.cz> - 1.4.0-1
- Update to 1.4.0 (#1564110)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 28 2016 František Dvořák <valtri@civ.zcu.cz> - 1.3.1-2
- Explicit dependency on json

* Thu Aug 25 2016 František Dvořák <valtri@civ.zcu.cz> - 1.3.1-1
- Update to 1.3.1 (#1353780)

* Sun Apr 10 2016 František Dvořák <valtri@civ.zcu.cz> - 1.2.4-1
- Updated to 1.2.4
- Removed older macros for Fedora 20 and 21

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 08 2015 František Dvořák <valtri@civ.zcu.cz> - 1.1.3-1
- Updated to 1.1.3
- Removed multi_json dependency in upstream
- Removed patch, all compliance tests OK now

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 29 2015 František Dvořák <valtri@civ.zcu.cz> - 1.0.2-2
- Removed rubygem(simplecov) BR
- Cleanups

* Fri Dec 05 2014 František Dvořák <valtri@civ.zcu.cz> - 1.0.2-1
- Initial package
