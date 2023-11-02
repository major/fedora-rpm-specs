# Generated from clockwork-0.7.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name clockwork

Name: rubygem-%{gem_name}
Version: 2.0.4
Release: 10%{?dist}
Summary: A scheduler process to replace cron
License: MIT
URL: http://github.com/Rykian/clockwork
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/Rykian/clockwork/pull/64/commits/43409b7369656c1f412d36ad8f6fda3e178b331e
Patch0: clockwork-pr64-mocha-2.0-compat.patch
# https://github.com/Rykian/clockwork/pull/68
Patch1: clockwork-pr68-ostruct-for-event_store_test.patch
# https://github.com/Rykian/clockwork/pull/85
Patch2: clockwork-pr85-minitest-5_19-compat.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby 
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(tzinfo)
BuildRequires: rubygem(activesupport)
BuildArch: noarch

%description
A scheduler process to replace cron, using a more flexible Ruby syntax running
as a single long-running process.  Inspired by rufus-scheduler and
resque-scheduler.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{_mandir}/man1/
mv .%{gem_instdir}/clockworkd.1* %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Test suite tries executes the binstub; inject relative loadpath
sed -i '2i\$LOAD_PATH.unshift(File.expand_path("../../lib", __FILE__))' \
  bin/clockwork

ruby -Ilib:test -rclockwork -e "Dir.glob('./test/**/*_test.rb').sort.each {|t| require t}"
popd


%files
%dir %{gem_instdir}
%{_bindir}/clockwork
%{_bindir}/clockworkd
%{gem_instdir}/bin
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%doc %{_mandir}/man1/clockworkd.1*
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/test
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/gemfiles
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/example.rb

%changelog
* Tue Oct 31 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.4-10
- Backport upstream fix for mocka 2.0 compatibiltity
- Use upstream patch for ostruct inclusion for event_store_test
- Apply upstream PR for Minitest 5.19 compatibility

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jun 24 2019 Pavel Valena <pvalena@redhat.com> - 2.0.4-1
- Update to clockwork 2.0.4.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 0.7.7-3
- Include LICENSE file
- Drop support for f20

* Fri Aug 22 2014 Josef Stribny <jstribny@redhat.com> - 0.7.7-2
- Add man page

* Tue Jul 15 2014 Josef Stribny <jstribny@redhat.com> - 0.7.7-1
- Initial package
