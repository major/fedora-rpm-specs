%global	gem_name	syck

Summary:	Gemified version of Syck from Ruby's stdlib
Name:		rubygem-%{gem_name}
Version:	1.5.1.1
Release:	3%{?dist}

# README.rdoc
# SPDX confirmed
License:	MIT
URL:		http://github.com/tenderlove/syck/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

# MRI only
Requires:	ruby
BuildRequires:	ruby

Requires:	ruby(rubygems)
BuildRequires:	gcc
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
# %% check
BuildRequires:	rubygem(test-unit)
Provides:	rubygem(%{gem_name}) = %{version}

%description
A gemified version of Syck from Ruby's stdlib.  
Syck has been removed from Ruby's stdlib, and this gem is 
meant to bridge the gap for people that haven't
updated their YAML yet.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# Kill syck.bundle
rm -f lib/syck.bundle
sed -i -e \
	's|"lib/syck.bundle",||' \
	%{gem_name}-%{version}.gemspec

# Kill #line for debuginfo rpm generation
sed -i -e '/^#line/d' \
	ext/syck/*.{c,h}

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
rm -f .%{gem_cache}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
pushd .%{gem_instdir}
rm -rf \
    %{gem_name}.gemspec \
    Gemfile* \
    Rakefile \
    ext/ \
    test/ \
    %{nil}
popd
popd

%check
pushd .%{gem_instdir}

cat > test/helper.rb <<EOF
require 'test/unit'
require 'syck'
EOF

ruby \
	-Ilib:test:.:%{buildroot}%{gem_extdir_mri} \
	-Ilib:test:. \
	-e 'Dir.glob( "test/test_*.rb" ).sort.each {|f| require f }' \
    %{nil}

popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_extdir_mri}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5.1.1-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Tue Aug 20 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5.1.1-1
- 1.5.1.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-10
- Fix for C99 -Werror=incompatible-pointer-types
- SPDX confirmation

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-9
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Thu Sep 14 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-8
- Backport upstream patch for Regexp.new 3rd argument removal
  (for ruby33 compatibility)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-4
- Use %%gem_extdir_mri instead of ext for %%check due to ruby3.2 change
  for ext cleanup during build

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-2
- F-36: rebuild against ruby31

* Thu Jan 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-1
- 1.4.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.0-5
- F-34: rebuild against ruby 3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.0-2
- F-32: rebuild against ruby27

* Wed Jan 15 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.0-1
- 1.4.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-13
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.5-10
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-9
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-5
- F-26: rebuild for ruby24
- and ruby24 build fix

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-3
- F-24: rebuild against ruby23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 25 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-1
- 1.0.5

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-7
- F-22: Rebuild for ruby 2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-4
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-2
- Add BR: rubygem(minitest) for %%check

* Sun Mar 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-1
- Initial package
