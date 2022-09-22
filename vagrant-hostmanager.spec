%global vagrant_plugin_name vagrant-hostmanager

Name: vagrant-hostmanager
Version: 1.8.9
Release: 9%{?dist}
BuildArch: noarch

License: MPLv2.0
Summary: Vagrant plugin to manage /etc/hosts
URL:     https://github.com/devopsgroup-io/vagrant-hostmanager
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem

BuildRequires: ruby(release)
BuildRequires: ruby
BuildRequires: rubygem(rdoc)
BuildRequires: vagrant >= 1.9.1

Requires: vagrant >= 1.9.1

Provides: vagrant(vagrant-hostmanager) = %{version}


%description
vagrant-hostmanager is a Vagrant plugin that manages the /etc/hosts file
on guest machines (and optionally the host). Its goal is to enable
resolution of multi-machine environments deployed with a cloud provider
where IP addresses are not known in advance.


%package doc
BuildArch: noarch
Summary: Documentation for %{name}

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
%license %{vagrant_plugin_instdir}/LICENSE
%exclude %{vagrant_plugin_cache}
%dir %{vagrant_plugin_instdir}
%exclude %{vagrant_plugin_instdir}/.gitignore
%{vagrant_plugin_instdir}/locales
%{vagrant_plugin_libdir}
%{vagrant_plugin_spec}


%files doc
%license %{vagrant_plugin_instdir}/LICENSE
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/CHANGELOG.md
%doc %{vagrant_plugin_instdir}/README.md
%{vagrant_plugin_instdir}/Gemfile
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/%{vagrant_plugin_name}.gemspec


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.8.9-1
- Upgrade to 1.8.9 (#1580042).
- https://github.com/devopsgroup-io/vagrant-hostmanager/compare/v1.8.8...v1.8.9
- Update the URL to the new upstream location.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 27 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.8.8-1
- Update to 1.8.8 (#1469848).
- https://github.com/devopsgroup-io/vagrant-hostmanager/compare/v1.8.6...v1.8.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.8.6-1
- Update to 1.8.6 (#1447820).
- Update license to MPLv2.0.
- The doc subpackage no longer requires the main package.
- https://github.com/devopsgroup-io/vagrant-hostmanager/compare/v1.8.5...v1.8.6

* Tue Feb 14 2017 Vít Ondruch <vondruch@redhat.com> - 1.8.5-3
- Drop registration macros for Vagrant 1.9.1 compatibility.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
