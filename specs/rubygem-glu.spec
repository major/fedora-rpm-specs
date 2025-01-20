%global	gem_name	glu

%bcond_with bootstrap

Name:		rubygem-%{gem_name}
Version:	8.3.0
Release:	34%{?dist}

Summary:	Glu bindings for the opengl gem
# SPDX confirmed
License:	MIT
URL:		https://github.com/larskanis/glu
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch1:		rubygem-glu-c99.patch

BuildRequires:	gcc
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
# %%check
%if %{without bootstrap}
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	rubygem(opengl)
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	mesa-dri-drivers
BuildRequires:	rubygem(opengl) >= 0.9
BuildRequires:	rubygem(glut)
BuildRequires:	rubygem(matrix)
%endif

%description
Glu bindings for the opengl gem.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -p1 -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}%{gem_extdir_mri}
rm -f \
	gem_make.out \
	mkmf.log \
	%{nil}
popd


pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gemtest .gitignore .travis.yml \
	Rakefile \
	ext/ \
	test/
popd
rm -f %{buildroot}%{gem_cache}

%check
%if %{without bootstrap}
pushd .%{gem_instdir}

%ifarch %arm
# Currently F41 mesa on s390x seems fairly broken
exit 0
%endif

export RUBYLIB=$(pwd)/lib:$(pwd):%{buildroot}%{gem_extdir_mri}
xvfb-run \
	-s "-screen 0 640x480x24" \
	ruby \
		-e "Dir.glob('test/test_*.rb').each { |f| require f }"
popd
%endif

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/MIT-LICENSE
%doc	%{gem_instdir}/History.rdoc
%doc	%{gem_instdir}/Manifest.txt
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_extdir_mri}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-33
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Sep 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-32
- Enable testsuite for s390x again
- Rebuild with fixed rubygem-opengl adjusted for Mesa 24.2.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 24 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-30
- Skip tests on F41 s390x for now

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 8.3.0-27
- Fix C compatibility issues

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-26
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sun Dec 24 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-25
- Use recent gem2rpm style
- Use recent bootstrap style

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-22
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sun Dec 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-22
- Use %%gem_extdir_mri instead of ext for %%check due to ruby3.2 change
  for ext cleanup during build

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-20
- F-36: rebuild against ruby31
- F-36: BR: rubygem(matrix) for test suite

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-16
- F-34: rebuild against ruby 3.0
- once disable tests for bootstrap

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-13
- Enable tests again

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-12
- F-32: rebuild against ruby27
- Once disable tests for bootstrap

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-9
- F-30: rebuild against ruby26
- Once disable tests for bootstrap

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 8.3.0-6
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-5
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-1
- 8.3.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-4
- Enable test again

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-3
- F-26: rebuild for ruby24
- Once disable test for bootstrap

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-1
- 8.2.2

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-7
- F-24: rebuild against ruby23
- Bootstrap, once disable test

* Tue Jul  7 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-6
- Disable test on arm for now

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-4
- Enable test again

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-3
- F-22: Rebuild for ruby 2.2
- Bootstrap, once disable test

* Sun Jan 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-2
- Enable test

* Thu Dec 18 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-1
- Initial package
