%global gem_name rspec-pending_for

Name:           rubygem-%{gem_name}
Version:        0.1.16
Release:        9%{?dist}
Summary:        Mark specs pending or skipped for specific Ruby engine

License:        MIT
URL:            https://github.com/pboling/rspec-pending_for
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/pboling/rspec-pending_for && cd rspec-pending_for
# git checkout v0.1.16
# tar -czf rubygem-rspec-pending_for-0.1.16-specs.tgz spec/
Source1:        %{name}-%{version}-specs.tgz

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(ruby_engine) >= 1.0
BuildRequires:  rubygem(ruby_version) >= 1.0
BuildRequires:  rubygem(simplecov)
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(rubygems)
Requires:       rubygem(rspec-core)
Requires:       rubygem(ruby_engine) >= 1.0
Requires:       rubygem(ruby_engine) < 2
Requires:       rubygem(ruby_version) >= 1.0
Requires:       rubygem(ruby_version) < 2
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations.
%if 0%{?rhel} && 0%{?rhel} <= 7
Note, skip_for() function is not available in rspec <= 2.
%endif


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
tar -xzf %{SOURCE1}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
cp -a spec/ ./%{gem_instdir}
pushd .%{gem_instdir}
rspec -Ilib -rspec_helper spec
rm -rf spec/
popd


%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_instdir}/CODE_OF_CONDUCT.md
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Feb 14 2021 František Dvořák <valtri@civ.zcu.cz> - 0.1.16-1
- Update to 0.1.16 (#1928568)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 František Dvořák <valtri@civ.zcu.cz> - 0.1.9-1
- Update to 0.1.9 (#1537093)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 03 2017 František Dvořák <valtri@civ.zcu.cz> - 0.1.5-1
- Initial package
