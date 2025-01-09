%global	gem_name	unf_ext

Summary:	Unicode Normalization Form support library for CRuby
Name:		rubygem-%{gem_name}
Version:	0.0.9.1
Release:	5%{?dist}
# LICENSE.txt
# SPDX confirmed
License:	MIT
URL:		http://github.com/knu/ruby-unf_ext
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
Requires:	ruby(rubygems)

BuildRequires:	ruby(release)
BuildRequires:	gcc-c++
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
# %%check
BuildRequires:	rubygem(test-unit)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Unicode Normalization Form support library for CRuby.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# Remove the binary extension sources and build leftovers.
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.document \
	.github/ \
	.gitignore \
	Gemfile \
	Rakefile \
	ext/ \
	test/ \
	*.gemspec \
	%{nil}
popd

%check
pushd .%{gem_instdir}
sed -i.orig \
	-e '/begin/,/end/d' \
	-e '/bundler/d' \
	test/helper.rb

sed -i -e '2i gem "test-unit"' test/helper.rb

ruby \
	-Ilib:test:.:%{buildroot}%{gem_extdir_mri} \
	test/test_unf_ext.rb

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md

%dir	%{gem_libdir}
%{gem_libdir}/%{gem_name}.rb
%{gem_libdir}/%{gem_name}/

%{gem_extdir_mri}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9.1-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9.1-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Fri Nov 17 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9.1-1
- 0.0.9.1

* Sun Nov 12 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.9-1
- 0.0.9

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.8.2-4
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.8.2-3
- Use %%gem_extdir_mri instead of ext for %%check due to ruby3.2 change
  for ext cleanup during build

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.8.2-1
- 0.0.8.2

* Sun Mar 13 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.8.1-1
- 0.0.8.1

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.8-3
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.8-1
- 0.0.8

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.7-3
- F-34: rebuild against ruby 3.0

* Wed Aug 05 2020 Merlin Mathesius <mmathesi@redhat.com> - 0.0.7.7-2
- Minor conditional fixes for ELN

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 10 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.7-1
- 0.0.7.7

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.6-3
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.6-1
- 0.0.7.6

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.5-3
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.5-1
- 0.0.7.5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.7.4-5
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.4-4
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 19 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.4-1
- 0.0.7.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.2-4
- F-26: rebuild for ruby24

* Fri Sep  2 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.2-3
- Explicitly mark C-type char array as signed char, ppc defaults char
  to unsigned as well as arm

* Sat Feb  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.2-2
- F-24(C++14): pass -Wno-narrowing for now on arm due to char
  being unsigned by default and narrowing initializer issue

* Fri Feb  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.2-1
- 0.0.7.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.1-3
- F-24: rebuild against ruby23

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.7.1-1
- 0.0.7.1

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-8
- F-22: Rebuild for ruby 2.2

* Fri Nov 14 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-7
- F-21 shoulda is now 3.5.0, fix test case

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-4
- Use minitest/autorun instead of minitest/unit

* Tue Apr 22 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-3
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Wed Sep 25 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-2
- Misc fix

* Fri Mar 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.6-1
- 0.0.6
- Support new ruby packaging guideline

* Sun Jan 06 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.5-1
- Initial package
