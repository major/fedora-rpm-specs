%global vagrant_plugin_name vagrant-openstack-provider

Name:		%{vagrant_plugin_name}
Version:	0.13.0
Release:	15%{?dist}
Summary:	Vagrant plugin for OpenStack provider

License:	MIT
URL:		https://github.com/ggiamarchi/vagrant-openstack-provider
Source0:	https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	vagrant >= 1.9.1
Requires:	vagrant >= 1.9.1
Requires:	rubygem(colorize)
Requires:	rubygem(sshkey)
Requires:	rubygem(terminal-table)
Requires:	rubygem(public_suffix)

BuildArch:	noarch

Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
A Vagrant plugin that adds a provider for provisioning
guest systems in an OpenStack cloud


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
# Upstream pins exact versions of gems. We only want lower bounds on the
# pinning
sed -i -e 's/"=/">=/g' %{vagrant_plugin_name}.gemspec
sed -i -e '1d' stackrc

%build
gem build %{vagrant_plugin_name}.gemspec
%vagrant_plugin_install

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/


%files
%doc CHANGELOG.md
%dir %{vagrant_plugin_instdir}
%doc %{vagrant_plugin_instdir}/example_box
%{vagrant_plugin_instdir}/Vagrantfile
%{vagrant_plugin_instdir}/dummy.box
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%{vagrant_plugin_spec}
%exclude %{vagrant_plugin_cache}
%exclude %{vagrant_plugin_instdir}/.gitignore
%exclude %{vagrant_plugin_instdir}/RELEASE.md
%exclude %{vagrant_plugin_instdir}/functional_tests
%exclude %{vagrant_plugin_instdir}/.rubocop.yml

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/CHANGELOG.md
%{vagrant_plugin_instdir}/spec
%{vagrant_plugin_instdir}/%{name}.gemspec
%{vagrant_plugin_instdir}/stackrc
%{vagrant_plugin_instdir}/Gemfile
%{vagrant_plugin_instdir}/Rakefile


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Greg Hellings <greg.hellings@gmail.com> - 0.13.0-3
- Remove patch
- Mangle gemspec with sed, instead

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 03 2018 Greg Hellings <greg.hellings@gmail.com> - 0.13.0-1
- New upstream version 0.13.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Greg Hellings <greg.hellings@gmail.com> - 0.12.0-1
- New upstream release 0.12.0 BZ#1549356
- Removed now excluded LICENSE file
- Updated patch
- Added dependency on rubygem-public_suffix

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Greg Hellings <greg.hellings@gmail.com> - 0.11.0-2
- Changed designation of LICENSE file to actually a license
- Removed unneeded lines that aren't used in Fedora
- Added description of patch

* Mon Jan 15 2018 Greg Hellings <greg.hellings@gmail.com> - 0.11.0-1
- New package
