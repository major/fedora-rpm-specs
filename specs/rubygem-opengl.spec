%global	gem_name	opengl

%bcond_with bootstrap

# MIT-LICENSE: MIT
# README.rdoc: MIT
# examples/OrangeBook/3Dlabs-License.txt (etc): BSD-3-Clause
# examples/NeHe: KILLED (license unclear)
# examples/RedBook/aapoly.rb: HPND
# examples/misc/OGLBench.rb: GPL-1.0-or-later OR Artistic-1.0-Perl
# examples/misc/plane.rb: HPND
# examples/misc/fbo_test.rb ??? KILLED
# examples/misc/trislam.rb: GPL-1.0-or-later OR Artistic-1.0-Perl

Name:		rubygem-%{gem_name}
Version:	0.10.0
Release:	37%{?dist}

Summary:	An OpenGL wrapper for Ruby
# SPDX confirmed
License:	MIT
URL:		https://github.com/drbrain/opengl
# Source0:	https://rubygems.org/gems/%%{gem_name}-%%{version}.gem
# The above gem file contains files with unclear license,
# we use a regenerated gem as a Source0 with such files
# removed.
# Source0 is generated using Source1.  
Source0:	%{gem_name}-%{version}-clean.gem
Source1:	create-clean-opengl-gem.sh
# http://www.gnu.org/licenses/old-licenses/gpl-1.0.txt
Source2:	GPLv1.rubygem_opengl
# Fix for -Werror=incompatible-pointer-types
Patch0:	opengl-0.10.0-pointer-types.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2303995#c20
# Mesa 24.2.2 swrast with dril does not expose accum buffers anymore
Patch1:	0001-Remove-requirement-for-accum-buffers.patch

# MRI (CRuby) only
BuildRequires:	gcc
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	freeglut-devel
# %%check
%if %{without bootstrap}
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	mesa-dri-drivers
BuildRequires:	rubygem(glu)
BuildRequires:	rubygem(glut)
BuildRequires:	rubygem(matrix)
%endif


%description
An OpenGL wrapper for Ruby. ruby-opengl contains bindings for OpenGL and the
GLU and GLUT libraries.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
License:	MIT AND BSD-3-Clause AND HPND AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
BuildArch:	noarch

%description	doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}-clean
mv ../%{gem_name}-%{version}-clean.gemspec ./%{gem_name}.gemspec

find examples/ -type f -print0 | xargs --null file | \
	grep CRLF | sed -e 's|:.*$||' | \
	while read f
do
	sed -i -e 's|\r||' $f
done

sed -i.minitest \
	-e 's|MiniTest::Unit::TestCase|Minitest::Test|' \
	lib/opengl/test_case.rb

%patch -P0 -p1 -b .types
%if 0%{?fedora} >= 41
%patch -P1 -p1 -b .accum
%endif

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}/
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

install -cpm 644 %{SOURCE2} \
	%{buildroot}%{gem_instdir}/examples/misc/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# cleanups
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gemtest .gitignore .travis.yml \
	Gemfile \
	Manifest.txt \
	Rakefile* \
	*gemspec \
	docs/build_install.txt \
	ext/ \
	test/

find examples/ utils/ -type f -perm /100 \
	-exec chmod ugo-x {} \;

popd

rm -f %{buildroot}%{gem_extdir_mri}/lib/opengl/test_case.rb

%check
%if %{with bootstrap}
exit 0
%endif

pushd .%{gem_instdir}

EXPECTED_TEST_MSG="184 runs, 17\(38\|44\|45\) assertions, 6 failures, [12] errors, 14 skips"

export RUBYLIB=%{buildroot}%{gem_extdir_mri}/:$(pwd)/lib:$(pwd)
# try twice
STATUS_ON_FAILURE=true
for trial in 1 2 ; do
	xvfb-run \
		-s "-screen 0 640x480x24" \
		ruby \
			-e "Dir.glob('test/test_*.rb').each { |f| require f }" \
			2>&1 | tee TEST.log
	cat TEST.log | grep -q "$EXPECTED_TEST_MSG" && break || $STATUS_ON_FAILURE
%ifarch i686
%else
	STATUS_ON_FAILURE=false
%endif
%ifarch s390x
%if 0%{?fedora} == 40
	# Currently mesa on F41, s390x is fairly broken
	STATUS_ON_FAILURE=true
%endif
%endif
done
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/MIT-LICENSE
%doc	%{gem_instdir}/History.md
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_extdir_mri}/

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/examples/
%doc	%{gem_instdir}/utils/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-36
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Sep 06 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-35
- Adjust to mesa 24.2.2 change that swrast with dril does not expose
  accum buffers anymore
- Adjust test result message with recent mesa

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-33
- Enable s390x test on F41 again

* Mon Jun 17 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-32
- Use regex match for test result

* Thu May 09 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-31
- Ignore one more test failure with recent F41 mesa
- Ignore test failure completely for now on F41 s390x mesa

* Fri Feb 23 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-30
- Fix -Werror=incompatible-pointer-types hard

* Thu Feb 22 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-29
- Explicitly add -Wno-error=incompatible-pointer-types only

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-27
- Change -Wincompatible-pointer-types from error to warning

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-26
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Mon Oct  9 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-25
- SPDX migration

* Thu Oct  5 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-24
- Switch to use recent spec file style
- Actually check the count of the test failures

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-21
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-19
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-15
- F-34: rebuild against ruby 3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-12
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-9
- F-30: rebuild against ruby26
- Once disable tests for bootstrap

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.10.0-6
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-5
- Enable tests again

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-4
- F-28: rebuild for ruby25
- Once disable tests for bootstrap

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-1
- Enable tests

* Fri Jun 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-0.1
- 0.10.0
- Once disable tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-10
- Enable test again

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-9
- F-26: rebuild for ruby24
- Once disable test for bootstrap

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-7
- F-24: rebuild against ruby23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-5
- Enable test again

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-4
- F-22: Rebuild for ruby 2.2
- Bootstrap, once disable test

* Sun Jan 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-3
- Enable test

* Sun Jan 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-1
- 0.9.2
- bootstrap, once disabling test

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-4
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Wed Oct 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.0-2
- Misc fixes with review (bug 1024168)

* Tue Oct 29 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.0-1
- Initial package
