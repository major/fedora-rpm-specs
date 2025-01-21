# Generated from vagrant-registration-0.0.7.gem by gem2rpm -*- rpm-spec -*-
%global vagrant_plugin_name vagrant-registration

Name: %{vagrant_plugin_name}
Version: 1.3.1
Release: 18%{?dist}
Summary: Automatic guest registration for Vagrant
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: https://github.com/projectatomic/adb-vagrant-registration
Source0: https://rubygems.org/gems/%{vagrant_plugin_name}-%{version}.gem
Requires: vagrant >= 1.9.1
BuildRequires: vagrant >= 1.9.1
BuildRequires: rubygem(rdoc)
BuildArch: noarch
Provides: vagrant(%{vagrant_plugin_name}) = %{version}

%description
Enables guests to be registered automatically which is especially useful
for RHEL or SLES guests.

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
%vagrant_plugin_install

chmod 644 .%{vagrant_plugin_instdir}/resources/rhn_unregister.py
sed -i 's/^#!\/usr\/bin\/python$//' .%{vagrant_plugin_instdir}/resources/rhn_unregister.py

%install
mkdir -p %{buildroot}%{vagrant_plugin_dir}
cp -a .%{vagrant_plugin_dir}/* \
        %{buildroot}%{vagrant_plugin_dir}/

# We can't run test suite because it requires virtualization
%check
pushd .%{vagrant_plugin_instdir}

popd

%files
%dir %{vagrant_plugin_instdir}
%license %{vagrant_plugin_instdir}/LICENSE
%{vagrant_plugin_libdir}
%{vagrant_plugin_instdir}/locales
%{vagrant_plugin_instdir}/plugins
%{vagrant_plugin_instdir}/resources
%exclude %{vagrant_plugin_cache}
%{vagrant_plugin_spec}

%files doc
%doc %{vagrant_plugin_docdir}
%doc %{vagrant_plugin_instdir}/CHANGELOG.adoc
%{vagrant_plugin_instdir}/Gemfile
%doc %{vagrant_plugin_instdir}/README.adoc
%{vagrant_plugin_instdir}/Rakefile
%{vagrant_plugin_instdir}/vagrant-registration.gemspec

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3.1-17
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Vít Ondruch <vondruch@redhat.com> - 1.3.1-1
- Update to vagrant-registration 1.3.1.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 28 2016 Tomas Hrcka <thrcka@redhat.com> - 1.2.3-1
- Rebase to latest upstream release

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Pavel Valena <pvalena@redhat.com> - 1.1.0-3
- Exclude hidden files from instdir

* Mon Dec 14 2015 Pavel Valena <pvalena@redhat.com> - 1.1.0-2
- Remove shebang from python script and set it non-executable

* Mon Dec 14 2015 Pavel Valena <pvalena@redhat.com> - 1.1.0-1
- Fix macro in changelog
- Drop unnecessary BuildRequires
- Change URL from rubygems.org to github.com
- Include missing %%dir macro
- Update to 1.1.0

* Tue Nov 10 2015 Josef Stribny <jstribny@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Tue Sep 08 2015 Josef Stribny <jstribny@redhat.com> - 0.0.19-2
- Fix virtual provide (rhbz#1243417)

* Tue Sep 08 2015 Josef Stribny <jstribny@redhat.com> - 0.0.19-1
- Update to 0.0.19

* Wed Jun 24 2015 Josef Stribny <jstribny@redhat.com> - 0.0.16-1
- Update to 0.0.16

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Josef Stribny <jstribny@redhat.com> - 0.0.15-1
- Update to 0.0.15

* Wed Jun 10 2015 Josef Stribny <jstribny@redhat.com> - 0.0.14-1
- Update to 0.0.14

* Thu May 28 2015 Josef Stribny <jstribny@redhat.com> - 0.0.13-1
- Update to 0.0.13

* Mon May 18 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.12-1
- New upstream release

* Thu Feb 19 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.8-3
- Changed license string to GPLv2
- Split description to two lines

* Wed Feb 18 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.8-2
- Move README and CHANGELOG to %%doc subpackage
- Re-word description
- Add upstream URL
- Require vagrant at build time

* Wed Feb 18 2015 Tomas Hrcka <thrcka@redhat.com> - 0.0.8-1
- Initial package
