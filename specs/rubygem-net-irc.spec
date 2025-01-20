%global	githash	4cf339fa69652faa2d5a4153b94754aa05543731
%global	shorthash	%(c=%{githash}; echo ${c:0:10})
%global	gitdate	Sun Oct 21 23:43:15 2012 +0900
%global	gitdate_num	20121021

%global	gem_name	net-irc

Name:		rubygem-%{gem_name}
Version:	0.0.9
Release:	27.D%{gitdate_num}git%{shorthash}%{?dist}

Summary:	Library for implementing IRC server and client
# Ruby's
# SPDX confirmed
License:	Ruby OR GPL-2.0-only
URL:		https://github.com/cho45/net-irc

#Source0:	https://rubygems.org/gems/%%{gem_name}-%%{version}.gem
# Let's use the newest git one
# Use tar.gz, convert to gem afterwards
Source0:	https://github.com/cho45/net-irc/archive/%{githash}/%{gem_name}-%{shorthash}.tar.gz
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Source1:	rubygem-net-irc-GPLv2
# Dup string for force_encoding, error detected on rabbirc
Patch0:	net-irc-dup-string-for-force_encoding.patch


BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(rdoc)
BuildRequires:	rubygem(rspec)
BuildRequires:	%{_bindir}/ping
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch

Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
library for implementing IRC server and client


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
#gem unpack %%{SOURCE0}
#%%setup -q -D -T -n  %%{gem_name}-%%{version}
#gem spec %%{SOURCE0} -l --ruby > %%{gem_name}.gemspec

%setup -q -c -T -a 0
cd %{gem_name}-%{githash}
%patch -P0 -p1
sed -i Rakefile \
	-e '\@require.*\(shipit\|sshpublisher\)@d' \
	-e '\@Rake::ShipitTask@,\@end@d' \
	-e 's|rake/gempackagetask|rubygems/package_task|' \
	-e 's|rake/rdoctask|rdoc/task|' \
	-e 's|Rake::GemPackageTask|Gem::PackageTask|' \
	-e 's|git|true|' \
	%{nil}
rake gem <<EOF


EOF
cd pkg/%{gem_name}-%{version}
sed -i lib/net/irc.rb \
	-e '\@^#!.*$@d' \
	%{nil}

# rspec2 -> rspec3
sed -i spec/net-irc_spec.rb \
	-e 's|be_true|be_truthy|' \
	%{nil}

# ruby 2.7 warning: Thread.exclusive is deprecated, use Thread::Mutex
# ruby 3.0: Thread.exclusive no longer available
%if 0%{?fedora} >= 34
grep -rl "Thread\.exclusive" . | \
	xargs sed -i \
	's|Thread\.exclusive|m = Thread::Mutex.new ; m.synchronize|' \
	%{nil}
%endif
	
gem specification -l --ruby ../%{gem_name}-%{version}.gem > %{gem_name}.gemspec

%build
cd %{gem_name}-%{githash}/pkg/%{gem_name}-%{version}
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cd %{gem_name}-%{githash}/pkg/%{gem_name}-%{version}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
install -cpm 644 %{SOURCE1} \
	%{buildroot}%{gem_instdir}/GPLv2

# cleanup
pushd %{buildroot}%{gem_instdir}
# AUTHORS.txt not useful
rm -rf \
	Rakefile AUTHORS.txt \
	spec/

%check
ping -w3 localhost || exit 0

cd %{gem_name}-%{githash}/pkg/%{gem_name}-%{version}
rspec spec/

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-FH-Z]*
%license %{gem_instdir}/GPLv2
%{gem_libdir}
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%{gem_instdir}/examples/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-27.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-26.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 11 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9-25.D20121021git4cf339fa69
- SPDX migration

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-24.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-23.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-22.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-21.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-20.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-19.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9-18.D20121021git4cf339fa69
- Use rspec3 instead of rspec2
- Ruby 3.0: replace removed Thread.exclusive with Thread::Mutex

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-17.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-16.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-15.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-14.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-13.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-12.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-11.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-10.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-9.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9-8.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9-7.D20121021git4cf339fa69
- Use rspec2

* Tue Jun 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9-6.D20121021git4cf339fa69
- Check net status for localhost

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-5.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-4.D20121021git4cf339fa69
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9-3.D20121021git4cf339fa69
- Dup string for force_encoding, error detected on rabbirc

* Mon Dec 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9-2.D20121021git4cf339fa69
- Modify release versioning
- Install GPLv2 text

* Wed Dec 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9-1.git4cf339fa69
- Initial package
