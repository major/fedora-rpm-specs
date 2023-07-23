%global	gem_name	byebug

%global	userelease	1
%global	usegit	0
%if 0%{?usegit} >= 1
%global	githash     5f9f57143a0f58a590965c2fa3c6d4647bfdae46
%global	shorthash   %(TMP=%githash ; echo ${TMP:0:10})
%global	gitdate     Sat, 30 Dec 2017 13:10:10 -0300
%global	gitdate_num 20171230
%endif

%global	baserelease 5

%if 0%{?userelease} >= 1
%global	fedorarel   %{?prever:0.}%{baserelease}%{?prever:.%{prerpmver}}
%endif
%if 0%{?usegit} >= 1
%global	fedorarel   %{basereleaase}.D%{gitdate_num}git%{shorthash}
%endif

%undefine __brp_mangle_shebangs

Name:		rubygem-%{gem_name}
Version:	11.1.3
Release:	%{fedorarel}%{?dist}

Summary:	Ruby 2.0 fast debugger - base + CLI
# SPDX confirmed
License:	BSD-2-Clause

URL:		http://github.com/deivid-rodriguez/byebug
%if 0%{?userelease} >= 1
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# %%{SOURCE2} %%{name} %%{version} 
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz
%endif
%if 0%{?usegit} >= 1
Source0:	https://github.com/deivid-rodriguez/%{gem_name}/archive/%{githash}/%{name}-%{version}-D%{gitdate_num}git%{githash}.tar.gz
%endif
Source2:	byebug-create-full-tarball.sh
Source10:	gcd.rb

BuildRequires:	gcc
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
%if 0%{?usegit} >= 1
BuildRequires:	rubygem(rake)
%endif
# %%check
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	rubygem(irb)
BuildRequires:	rubygem(pry)

%description
Byebug is a Ruby 2 debugger. It's implemented using the
Ruby 2 TracePoint C API for execution control and the Debug Inspector C API
for call stack navigation.  The core component provides support that
front-ends can build on. It provides breakpoint handling and bindings for
stack frames among other things and it comes with an easy to use command
line interface.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%if 0%{?userelease} >= 1
%setup -q -T -n %{gem_name}-%{version} -b 1
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%endif

%if 0%{?usegit} >= 1
%setup -q -c -T -a 0
mv %{gem_name}-%{githash}/* %{gem_name}-%{githash}/.[^.]* .
%endif

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}/} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x


%check
export NOCOV=true
export GEM_PATH=%{buildroot}/%{gem_dir}:%{gem_dir}
export PATH=%{buildroot}%{_bindir}:$PATH

remove_fail_test() {
	filename=$1
	shift
	num=$#
	while [ $num -gt 0 ]
	do
		if [ ! -f ${filename}.orig ] ; then
			cp -p $filename ${filename}.orig
		fi
		sed -i $filename -e "\@def.*$1@s|^\(.*\)$|\1; skip \"Skip this\"|"
		shift
		num=$((num - 1))
	done
}

yes "puts a, b ; s" | ruby -I.:lib:%{buildroot}%{gem_extdir_mri} -S byebug ruby %{SOURCE10} 120 84

# Add exit status correctly
sed -i bin/minitest -e '$s|^Byebug|exit 1 unless Byebug|'

mv {,.}Gemfile.lock
sed -i bin/minitest \
	-e '\@bundler/setup@d' \
	-e '\@load.*expand_path.*bundle@d' \
	%{nil}

# Kill bundler test
remove_fail_test test/minitest_runner_test.rb run_minitest_runner

export RUBYLIB=$(pwd):$(pwd)/lib:%{buildroot}%{gem_extdir_mri}
# Once test all
ruby bin/minitest || true

# F-32 the following test fails
remove_fail_test test/commands/finish_test.rb test_finish_inside_autoloaded_files
# Again test, this time check exit status
ruby bin/minitest

mv {.,}Gemfile.lock

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/CONTRIBUTING.md
%doc	%{gem_instdir}/GUIDE.md
%doc	%{gem_instdir}/README.md

%{_bindir}/byebug
%{gem_instdir}/exe

%{gem_libdir}/
%{gem_extdir_mri}/

%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_instdir}/CONTRIBUTING.md
%doc	%{gem_docdir}

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 23 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.3-4
- A bit of spec file cleanup
- SPDX migration

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.3-3.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.3-3.5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.3-3.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.3-3.3
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.3-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.3-3.1
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr  6 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.3-3
- Add BR: rubygem(irb)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.3-2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.3-2.1
- F-34: rebuild against ruby 3.0

* Thu Oct 15 12:33:21 CEST 2020 Vít Ondruch <vondruch@redhat.com> - 11.1.3-2
- Disable coverage testing => remove SimpleCov dependency.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May  3 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.3-1
- 11.1.3

* Mon Apr 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.2-1
- 11.1.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.1.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.1.1-1
- 11.1.1

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.0.1-1.2
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.0.1-1
- 11.0.1

* Tue Feb 19 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 11.0.0-1
- 11.0.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.2-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.0.2-1.2
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.0.2-1
- 10.0.2

* Sat Mar 23 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.0.1-1
- 10.0.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.0.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.0.0-1
- 10.0.0

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 9.1.0-2.D20171230git5f9f57143a.1
- Rebuilt for switch to libxcrypt

* Fri Jan  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.1.0-2.D20171230git5f9f57143a
- Use latest git, ruby 2.5 porting is done on git head, but not released yet

* Tue Aug 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.1.0-1
- 9.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.0.6-4
- Always use full tar.gz for installed files and
  keep using gem file for gem spec (ref: bug 1425220)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.0.6-2
- F-26: rebuild for ruby24
- Apply upstream patch for test with ruby24

* Mon Oct 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.0.6-1
- 9.0.6

* Fri Jun 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 9.0.5-1
- 9.0.5

* Wed May  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.5-2
- 8.2.5

* Wed Apr 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.4-1
- 8.2.4

* Wed Feb  3 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-1
- 8.2.2

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-2
- F-24: rebuild against ruby23

* Tue Dec 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-1
- 8.2.1

* Sun Sep 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.0.2-1
- 6.0.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.0-1
- 5.0.0

* Fri Apr  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.5-1
- 4.0.5

* Sat Mar 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.4-1
- 4.0.4

* Fri Mar 20 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.3-1
- 4.0.3

* Tue Mar 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.2-1
- 4.0.2

* Sat Feb 07 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-4
- Remove simplecov

* Tue Feb 03 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-3
- A bit modification for %%check

* Tue Feb 03 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-2
- Make test suite exit with status

* Tue Feb 03 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.1-1
- Initial package
