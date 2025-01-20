# Generated from mixlib-log-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-log

Name: rubygem-%{gem_name}
Version: 3.0.9
Release: 11%{?dist}
Summary: A gem that provides a simple mixin for log functionality
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/chef/mixlib-log
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/chef/mixlib-log && cd mixlib-log
# git checkout v3.0.9
# tar -czf rubygem-mixlib-log-3.0.9-specs.tgz spec/
Source1: rubygem-mixlib-log-%{version}-specs.tar.gz
# https://github.com/chef/mixlib-log/pull/74
Patch0:  mixlib-log-pr74-ruby33-Logger-support.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem-rspec
BuildArch: noarch

%description
A gem that provides a simple mixin for log functionality.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1
%patch -P0 -p1

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

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .
rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 3.0.9-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 26 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-7
- Apply upstream PR to support ruby3.3 Logger

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Davide Cavalca <dcavalca@fedoraproject.org> - 3.0.9-1
- Upgrade to 3.0.9 and package tests
- Drop el6 and ancient Fedora logic
- Various fixes to follow the latest Ruby packaging policy

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.1-2
- Escape macros in %%changelog

* Sun Jan 21 2018 Julian C. Dunn <jdunn@aquezada.com> - 1.7.1-1
- Upgrade to 1.7.1 (bz#1365126)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Julian C. Dunn <jdunn@aquezada.com> - 1.6.0-1
- Update to 1.6.0

* Fri Mar 08 2013 Josef Stribny <jstribny@redhat.com> - 1.4.1-5
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Julian C. Dunn <jdunn@aquezada.com> - 1.4.1-3
- Exclude %%check from running on F16 since RSpec is too old

* Wed Jan 02 2013 Julian C. Dunn <jdunn@aquezada.com> - 1.4.1-2
- Move extra files into -doc subpackage per review (#823332)

* Fri Dec 21 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.4.1-1
- Rebuilt with 1.4.1, specs are bundled

* Sun Apr 29 2012 Jonas Courteau <rpms@courteau.org> - 1.3.0-1
- Repackaged for fc17
- New upstream version
- Removed check patch
- Modified check - pull tests manually as they've been removed from gem

* Wed Jun 9 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-3
- New patch to enable check again.

* Tue Jun 8 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-2
- Disable check for now.

* Tue Mar 23 2010 Matthew Kent <mkent@magoazul.com> - 1.1.0-1
- New upstream version - moves to jeweler for gem creation.

* Mon Oct 5 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-3
- Missing complete source url (#526181).
- Remove unused ruby_sitelib macro (#526181).
- Remove redundant doc Requires on rubygems (#526181).

* Sun Oct 4 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-2
- Remove redundant path in doc package (#526181).
- Use global over define (#526181).

* Mon Sep 28 2009 Matthew Kent <mkent@magoazul.com> - 1.0.3-1
- Initial package
