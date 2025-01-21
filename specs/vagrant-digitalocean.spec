%global vagrant_plugin_name vagrant-digitalocean

Name: vagrant-digitalocean
Version: 0.9.0
Release: 19%{?dist}
Summary: Vagrant plugin for having Digital Ocean as an provider
License: MIT
URL: https://github.com/devopsgroup-io/vagrant-digitalocean
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
Requires: vagrant >= 1.9.1
Requires: rubygem-highline
Requires: rubygem-faraday
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: vagrant >= 1.9.1
BuildArch: noarch
Provides: vagrant(vagrant-digitalocean) = %{version}


%description
It is a Vagrant provider plugin that supports the management of DigitalOcean
droplets (instances).

%package doc
Summary: Documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
BuildArch: noarch

Provides: bundled(lato-fonts)
# Using OFL license https://www.google.com/fonts/specimen/Source+Code+Pro
Provides: bundled(sourcecodepro-fonts)

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{vagrant_plugin_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{vagrant_plugin_name}.gemspec


%build
gem build %{name}.gemspec
# Despite having install in the name, this macro builds the docs among other
# things, so it belongs here.
%vagrant_plugin_install


%install
# We don't ship the test suite
rm -rf .%{vagrant_plugin_dir}/gems/%{vagrant_plugin_name}-%{version}/test

mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
       %{buildroot}%{vagrant_plugin_dir}/


%files
%license %{vagrant_plugin_instdir}/LICENSE.txt
%exclude %{vagrant_plugin_cache}
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.gitignore
%{vagrant_plugin_instdir}/locales
%{vagrant_plugin_libdir}
%{vagrant_plugin_spec}
%{vagrant_plugin_instdir}/box*


%files doc
%license %{vagrant_plugin_instdir}/LICENSE.txt
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Gemfile
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec
%{vagrant_plugin_instdir}/box/*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 14 2017 Vít Ondruch <vondruch@redhat.com> - 0.9.0-3
- Drop registration macros for Vagrant 1.9.1 compatibility.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 08 2016 Kushal Das <kushal@fedoraproject.org> - 0.9.0-1
- Updates to 0.9.0

* Wed Jun 08 2016 Kushal Das <kushal@fedoraproject.org> - 0.7.10-1
- New package
