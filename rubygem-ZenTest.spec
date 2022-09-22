# Generated from ZenTest-4.1.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ZenTest

Name: rubygem-%{gem_name}
Version: 4.12.1
Release: 2%{?dist}
Summary: Automated test scaffolding for Ruby
License: MIT
URL: https://github.com/seattlerb/zentest
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
ZenTest is an automated test scaffolding for Ruby that provides 4 different
tools: zentest, unit_diff, autotest and multiruby. These tools can be used for
test conformance auditing and rapid XP.

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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Various files marked executable that shouldn't be, and remove needless
# shebangs
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'
find %{buildroot}%{gem_instdir}/test -type f | \
  xargs -n 1 sed -i  -e '/^#!\/usr\/.*\/ruby.*/d'

%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/multigem
%{_bindir}/multiruby
%{_bindir}/unit_diff
%{_bindir}/zentest
%exclude %{gem_instdir}/.*
# Note that the pull-request to separate the license text was declined.
# https://github.com/seattlerb/zentest/pull/67
%doc %{gem_instdir}/README.txt
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/articles
%doc %{gem_instdir}/example*.rb
%doc %{gem_instdir}/example.txt
%{gem_instdir}/test

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 10 2022 Vít Ondruch <vondruch@redhat.com> - 4.12.1-1
- Update to ZenTest 4.12.1.
  Resolves: rhbz#1754346

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Vít Ondruch <vondruch@redhat.com> - 4.11.2-1
- Update to ZenTest 4.11.2.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jun Aruga <jaruga@redhat.com> - 4.11.0-1
- Update to ZenTest 4.11.0.
- Fix test suite for FTBFS (rhbz#1307999).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 10 2014 Vít Ondruch <vondruch@redhat.com> - 4.10.0-1
- Update to ZenTest 4.10.0.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Vít Ondruch <vondruch@redhat.com> - 4.9.0-2
- Rebuid due to error in RubyGems stub shebang.

* Tue Feb 19 2013 Vít Ondruch <vondruch@redhat.com> - 4.9.0-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to ZenTest 4.9.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Mo Morsi <mmorsi@redhat.com> - 4.8.2-1
- update to zentest 4.8.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Vít Ondruch <vondruch@redhat.com> - 4.6.2-2
- Remove Rake dependency.

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.6.2-1
- 4.6.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 09 2011 Mo Morsi - 4.6.0-1
- New upstream version. Minor fixes and enhancements.

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 4.3.3-3
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 26 2010 Matthew Kent <mkent@magoazul.com> - 4.3.3-1
- New upstream version. Minor fixes and enhancements.

* Tue May 4 2010 Matthew Kent <mkent@magoazul.com> - 4.3.1-1
- New upstream version. Minor bugfixes - 1.9 compatibility.

* Sun Jan 24 2010 Matthew Kent <mkent@magoazul.com> - 4.2.1-1
- New upstream version.
- Don't reorganize files, leave as upstream intended.

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-3
- Drop Requires on hoe, only used by Rakefile (#539442).
- Move Rakefile to -doc (#539442).

* Sat Nov 21 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-2
- Better Source (#539442).
- More standard permissions on files.

* Mon Nov 16 2009 Matthew Kent <mkent@magoazul.com> - 4.1.4-1
- Initial package
