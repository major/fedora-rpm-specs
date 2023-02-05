%global gem_name puppet-resource_api

Name: rubygem-%{gem_name}
Version: 1.8.14
Release: 6%{?dist}
Summary: This library provides a simple way to write new native resources for puppet
License: Apache-2.0
URL: https://github.com/puppetlabs/puppet-resource_api
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
Requires: puppet
BuildArch: noarch

%description
This library provides a simple way to write new native resources for puppet.


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
rm -rf %{buildroot}%{gem_instdir}/{.gitignore,.rubocop.yml,.travis.yml,appveyor.yml,codecov.yml}

# %%check can't run since it requires puppet, but puppet requires this package

%files
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/NOTICE
%dir %{gem_instdir}
%exclude %{gem_instdir}/.dependency_decisions.yml
%exclude %{gem_instdir}/.github
%exclude %{gem_instdir}/CODEOWNERS
%exclude %{gem_instdir}/HISTORY.md
%exclude %{gem_instdir}/bin
%exclude %{gem_instdir}/contrib
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%{gem_instdir}/.fixtures.yml
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/puppet-resource_api.gemspec
%exclude %{gem_instdir}/.rspec

%changelog
* Thu Feb 02 2023 License update - 1.8.14-6
- Rebuilt to update license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 1.8.14-1
- Update to 1.8.14
- Remove more unused files
- Drop rspec build dep

* Thu May 14 2020 Breno B Fernandes <brandfbb@gmail.com> - 1.8.13-1
- Bumped version, added puppet as dependency to run it, removed files not necessary for the build

* Thu Mar 05 2020 Breno B Fernandes <brandfbb@gmail.com> - 1.8.12-1
- Initial package
