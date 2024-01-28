%global	gem_name	unf

%undefine __brp_mangle_shebangs

Summary:	Wrapper library to bring Unicode Normalization Form support to Ruby/JRuby
Name:		rubygem-%{gem_name}
Version:	0.1.4
Release:	24%{?dist}

# SPDX confirmed
License:	BSD-2-Clause
URL:		https://github.com/knu/ruby-unf
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Drop Shoulda dependency to reduce the dependency chain.
# https://github.com/knu/ruby-unf/commit/c3987f7942bdde5268ec293834ba3b3447217752
Patch0:	rubygem-unf-0.2.0-Use-test-unit-.patch

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel 
# %%check
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(unf_ext)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
This is a wrapper library to bring Unicode Normalization Form support
to Ruby/JRuby.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%patch -P0 -p1
%gemspec_remove_dep -s %{gem_name}-%{version}.gemspec -g shoulda -d ">= 0"
%gemspec_add_dep -s %{gem_name}-%{version}.gemspec -g test-unit -d

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	*.gemspec \
	.gitignore \
	.travis.yml \
	test/ \
	%{nil}
popd


%check
pushd .%{gem_instdir}
sed -i.orig \
	-e '/begin/,/end/d' \
	-e '/bundler/d' \
	test/helper.rb

for f in test/test_*.rb
do
	ruby -Ilib:test:. $f
done
popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-KM-Z]*
%license %{gem_instdir}/LICENSE

%{gem_libdir}/
%{gem_spec}

%files	doc
%doc	%{gem_docdir}

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep  6 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-23
- Massive spec file cleanup
- SPDX migration

* Tue Sep 05 2023 Vít Ondruch <vondruch@redhat.com>
- Drop rubygem-shoulda dependency and use Test::Unit for testing

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 05 2020 Merlin Mathesius <mmathesi@redhat.com> - 0.1.4-16
- Minor conditional fixes for ELN

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  2 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-11
- Remove non-runtime files yet more

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-5
- F-21 shoulda is now 3.5.0, fix test case

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-3
- Use minitest/autorun instead of minitest/unit

* Thu Apr 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-2
- Support Minitest 5.x

* Wed Apr  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.4-1
- 0.1.4

* Sun Oct 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.3-1
- 0.1.3

* Thu Oct  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.2-1
- 0.1.2

* Mon Apr 29 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.1-1
- 0.1.1

* Fri Mar 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.0-1
- 0.1.0

* Sat Jan 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.5-1
- Initial package
