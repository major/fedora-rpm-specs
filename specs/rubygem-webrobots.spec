%global	gem_name	webrobots

Summary:	Ruby library to help write robots.txt compliant web robots
Name:		rubygem-%{gem_name}
Version:	0.1.2
Release:	21%{?dist}

# SPDX confirmed
License:	BSD-2-Clause
URL:		https://github.com/knu/webrobots
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Replace shoulda with shoulda-context, which is enough to execute the test
# suite.
# https://github.com/knu/webrobots/pull/8
Patch0:	rubygem-webrobots-0.1.2-shoulda-context-is-enough-to-execute-the-test-suite.patch

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel 
# %%check
# F-19: kill check until should is rebuilt
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(base64)
BuildRequires:	rubygem(shoulda-context)
BuildRequires:	rubygem(webmock)
BuildRequires:	rubygem(vcr)
BuildRequires:	rubygem(nokogiri)
BuildRequires:	rubygem(racc)
# Add nokogiri dependency
Requires:	rubygem(nokogiri)
Requires:	rubygem(racc)

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
This library helps write robots.txt compliant web robots in Ruby.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1
%gemspec_remove_dep -s %{gem_name}-%{version}.gemspec -g shoulda -d ">= 0"
%gemspec_add_dep -s %{gem_name}-%{version}.gemspec -g shoulda-context -d

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Clean up
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.document \
	.gitignore \
	.travis.yml \
	Gemfile \
	Rakefile \
	test/ \
	%{gem_name}.gemspec \
	%{nil}
popd

%check
pushd .%{gem_instdir}
sed -i.orig \
	-e '/begin/,/end/d' \
	-e '/bundler/d' \
	test/helper.rb

ruby -Ilib:test test/test_webrobots.rb
popd

%files
%dir	%{gem_instdir}/
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 04 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.2-20
- BR: rubygem(base64) explicitly for ruby34

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep  7 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.2-17
- Massive spec file cleanup
- SPDX migration

* Tue Sep 05 2023 Vít Ondruch <vondruch@redhat.com>
- Use rubygem-shoulda-context instead of rubygem-shoulda

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.2-9
- R,BR rubygem(racc)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.2-1
- 0.1.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.1-1
- 0.1.1

* Fri Mar 08 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.0-2
- F-19: rebuild for ruby 2.0.0

* Thu Mar 07 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.0-1
- 0.1.0

* Mon Jan 07 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.13-1
- Initial package
