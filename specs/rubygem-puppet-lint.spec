%global gem_name puppet-lint

Name: rubygem-%{gem_name}
Version: 4.2.1
Release: 5%{?dist}
Summary: Ensure your Puppet manifests conform with the Puppetlabs style guide
License: MIT
URL: https://github.com/puppetlabs/puppet-lint/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/puppetlabs/puppet-lint/issues/225
# Handle ruby3.4 backtrace formatting change
Patch0:  puppet-lint-issue225-ruby34-backtrace-formatting-change.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.7
BuildRequires: rubygem(rspec) >= 3.0
BuildRequires: rubygem(rspec-its) >= 1.0
BuildArch: noarch

%description
Checks your Puppet manifests against the Puppetlabs
style guide and alerts you to any discrepancies.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

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
pushd .%{gem_instdir}

COVERAGE=no rspec spec/unit

popd

%files
%dir %{gem_instdir}
%{_bindir}/puppet-lint
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/rubocop_baseline.yml
%{gem_instdir}/spec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.2.1-4
- Support ruby34 backtrace formatting change

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> - 4.2.1-1
- Updated to 4.2.1 (fixes rhbz#1985967)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 17 01:28:47 CET 2020 Pavel Valena <pvalena@redhat.com> - 2.4.2-1
- Update to puppet-lint 2.4.2.
  Resolves: rhbz#1349208

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Pavel Valena <pvalena@redhat.com> - 2.3.6-1
- Update to puppet-lint 2.3.6.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 14 2015 Russell Harrison <rharrison@fedoraproject.org> 1.1.0-1
- Upstream update to 1.1.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Russell Harrison <rharrison@fedoraproject.org> 0.3.2-3
- Update for Ruby 2.0 in F19+

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 30 2012 Russell Harrison <rharrison@fedoraproject.org> 0.3.2-1
- New upstream version. http://puppet-lint.com/changelog/
- Remove exit code patch. Fixed in upstream

* Tue Sep 25 2012 Russell Harrison <rharrison@fedoraproject.org> 0.2.1-3
- Drop requirement for the puppet package
- Pull in all of rspec as build requires
- Moving files not required at run time to the doc subpackage
- Excluding files not meant for packaging instead of removing them durring install
- Other fixes requested durring package review

* Wed Sep 12 2012 Russell Harrison <rharrison@fedoraproject.org> 0.2.1-2
- Patch to pass exit value to the shell https://github.com/rodjek/puppet-lint/pull/141

* Fri Sep  7 2012 Russell Harrison <rharrison@fedoraproject.org> - 0.2.1-1
- New upstream version
- Updated URL for new upstream website

* Sun Aug 26 2012 Russell Harrison <rharrison@fedoraproject.org> - 0.2.0-1
- Initial package
