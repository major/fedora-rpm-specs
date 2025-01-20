%global	gem_name	parseconfig

Name:			rubygem-%{gem_name}
Version:		1.1.2
Release:		8%{?dist}

Summary:		Config File Parser for Standard Unix/Linux Type Config Files
License:		MIT
URL:			http://github.com/datafolklabs/ruby-parseconfig/
Source0:		https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:		rubygem-parseconfig-%{version}-tests.tar.gz
# Source1 is created by Source2
Source2:		parseconfig-create-test-suite.sh

BuildRequires:	ruby(release)
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygems-devel
BuildArch:		noarch

%description
ParseConfig provides simple parsing of standard configuration files in the
form of 'param = value'.  It also supports nested [group] sections.

%package		doc
Summary:		Documentation for %{name}
Requires:		%{name} = %{version}-%{release}
BuildArch:		noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

# 1.1.2 only
# https://github.com/datafolklabs/ruby-parseconfig/issues/39
sed -i lib/version.rb -e "\@VERSION@s|'.*'|'%{version}'|"

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

cp -a ./tests .%{gem_instdir}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

pushd %{buildroot}
rm -rf  \
	.%{gem_cache} \
	.%{gem_instdir}/tests/ \
	%{nil}

%check
cd tests
ruby ./test_parseconfig.rb
cd ..

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/Changelog
%doc	%{gem_instdir}/README.md
%license	%{gem_instdir}/LICENSE
%{gem_libdir}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2-1
- 1.1.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.8-1
- 1.0.8

* Mon Mar 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-6
- Rewrite spec, update to the modern style

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 BJ Dierkes <derks@datafolklabs.com> - 1.0.4-1
- Latest sources from upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 19 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.2-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 BJ Dierkes <wdierkes@rackspace.com> - 1.0.2-1
- Latest sources from upstream.

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.5.2-6
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 05 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.5.2-3
- Removed comment from Source0, URL no longer changes
- Resolved duplicate file listing

* Mon Apr 05 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.5.2-2
- Added geminstdir to file list
- Requires: ruby(abi) >= 1.8
- Removed check
- Updated for current rubygems download url
- Removed unused macros ruby_sitelib, installroot

* Sat Feb 27 2010 BJ Dierkes <wdierkes@rackspace.com> - 0.5.2-1
- Initial spec, borrowed from rubygem-cobbler
