%global	gem_name	levenshtein

Summary:	Calculates the Levenshtein distance between two byte strings
Name:		rubygem-%{gem_name}
Version:	0.2.2
Release:	39%{?dist}

# LICENSE file
# SPDX confirmed
License:	GPL-2.0-only
URL:		http://www.erikveen.dds.nl/levenshtein/doc/index.html
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)
Requires:	ruby(rubygems) 
BuildRequires:	gcc
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
BuildRequires:	rubygem(test-unit)
Provides:	rubygem(%{gem_name}) = %{version}

%description
Calculates the Levenshtein distance between two byte strings.

The Levenshtein distance is a metric for measuring the amount
of difference between two sequences (i.e., the so called edit
distance). The Levenshtein distance between two sequences is
given by the minimum number of operations needed to transform
one sequence into the other, where an operation is an
insertion, deletion, or substitution of a single element.

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

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}%{gem_extdir_mri}
rm -f \
	gem_make.out \
	mkmf.log \
	%{nil}
popd

# Remove the binary extension sources and build leftovers.
pushd %{buildroot}%{gem_instdir}
rm -rf \
	ext/ \
	test/ \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}

%check
pushd .%{gem_instdir}

export RUBYLIB=$(pwd)/lib:%{buildroot}%{gem_extdir_mri}
ruby ./test/test.rb

popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-KM-Z]*
%license %{gem_instdir}/LICENSE

%{gem_libdir}/
%{gem_extdir_mri}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-39
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-35
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Thu Dec 21 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-34
- Update to the recent gem2rpm style
- Use test-unit instead of Minitest (as original)
- SPDX migration

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-31
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-29
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-27
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-25
- F-34: rebuild against ruby 3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-22
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-19
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.2.2-16
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-15
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-11
- F-26: rebuild for ruby24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-9
- F-24: rebuild against ruby23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-7
- F-22: Rebuild for ruby 2.2

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-4
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-2
- F-19: Rebuild for ruby 2.0.0

* Sat Jan  5 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-1
- Initial package
