# Generated from vagrant-adbinfo-0.0.4.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant-adbinfo

Name: %{vagrant_plugin_name}
Version: 0.1.0
Release: 18%{?dist}
Summary: Connection and configuration for a Docker daemon
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/projectatomic/vagrant-adbinfo
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
Requires: vagrant >= 1.9.1
BuildRequires: rubygem(rdoc)
BuildRequires: vagrant >= 1.9.1
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
Vagrant plugin that provides the IP address:port and TLS certificate file
location for a Docker daemon.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{vagrant_plugin_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{vagrant_plugin_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{vagrant_plugin_name}.gemspec

# %%vagrant_plugin_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

# Run the test suite
%check
pushd .%{vagrant_plugin_instdir}

popd

%files
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.*
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/CHANGELOG.md
%doc %{vagrant_plugin_instdir}/CONTRIBUTING.md
%doc %{vagrant_plugin_instdir}/MAINTAINERS
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/Vagrantfile
%{vagrant_plugin_instdir}/vagrant-adbinfo.gemspec
%{vagrant_plugin_instdir}/vagrant-adbinfo.spec

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.0-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Vít Ondruch <vondruch@redhat.com> - 0.1.0-1
- Update to vagrant-adbinfo 0.1.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec  3 2015 Pavel Valena - 0.0.9-3
- Correct upstream URL
- Remove unnecessary BuildRequires

* Thu Dec  3 2015 Pavel Valena - 0.0.9-2
- Shorten summary to pass rpmlint
- Remove unnecessary rubygems-devel from BuildRequires
- Move license file to main package

* Wed Nov 25 2015 Brian Exelbierd - 0.0.9-1
- Fixes cert-generation script existence check, a bug was found where the cert
  was regenerated to often
- Bumps the plugin version to 0.0.9

* Tue Nov 24 2015 Navid Shaikh - 0.0.8-1
- Fixes cert-generation script existence check
- Bumps the plugin version to 0.0.8

* Tue Nov 24 2015 Navid Shaikh - 0.0.7-1
- Fixes adbinfo#40: Handle private networking in ADB for different providers
- Bumps the plugin version to 0.0.7

* Fri Nov 20 2015 Navid Shaikh - 0.0.6-1
- Finds IP address of the guest provisioned via private networking
- Fixes typo in eval command of adbinfo output
- Adds License, Contributing and Maintainers files
- Adds Quick Start and Contact us sections

* Thu Nov 19 2015 Navid Shaikh - 0.0.5-2
- Removes shadow-utils from Requires

* Tue Nov 17 2015 Navid Shaikh - 0.0.5-1
- vagrant-adbinfo#17: adbinfo format should be windows compatible 
- vagrant-adbinfo#18: adbinfo should be possible to evaluate in shell

* Thu Nov 12 2015 Navid Shaikh - 0.0.4-1
- Initial package
