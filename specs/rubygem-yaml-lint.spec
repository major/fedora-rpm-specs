# Generated from yaml-lint-0.0.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name yaml-lint
# This commit corresponds to the relase in github which is not tagged :-(
%global commit 8dfc583584e046c54617315734883c887768c6ca

Name:          rubygem-%{gem_name}
Version:       0.1.2
Release:       5%{?dist}
Summary:       Really simple YAML lint
License:       MIT
URL:           https://github.com/Pryz/yaml-lint
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:       https://github.com/Pryz/yaml-lint/archive/%{commit}/yaml-lint-%{commit}.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildArch:     noarch


%description
Check if your YAML files can be loaded.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}

# unpack only the spec and LICENSE from SOURCE1
tar zxf %{SOURCE1} --strip-components 1 \
                   yaml-lint-%{commit}/spec \
                   yaml-lint-%{commit}/LICENSE \
                   yaml-lint-%{commit}/README.md \

# Disable Coverals
sed -i "s/^require 'coveralls'$//" spec/spec_helper.rb
sed -i "s/^Coveralls.wear!//"      spec/spec_helper.rb


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x


%check
rspec -I%{gem_instdir} spec


%files
%dir %{gem_instdir}
%{_bindir}/yaml-lint
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license LICENSE
%doc README.md


%files doc
%doc %{gem_docdir}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 20 2023 Steve Traylen <steve.traylen@cern.ch> - 0.1.2-1
- Upstream to 0.1.2
- Include README, LICENSE and tests(and run them) from upstream
- Clean up .spec file indentation and alignment

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Steve Traylen <steve.traylen@cern.ch> - 0.0.10-1
- Initial package
