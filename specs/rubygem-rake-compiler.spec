%global	gem_name	rake-compiler

%undefine       _changelog_trimtime

Summary:	Rake-based Ruby C Extension task generator
Name:		rubygem-%{gem_name}
Version:	1.3.0
Release:	2%{?dist}
# SPDX confirmed
License:	MIT
URL:		https://github.com/rake-compiler/rake-compiler
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
# Source1 is created by $ bash %%SOURCE2 %%version
Source2:	%{gem_name}-create-missing-test-files.sh

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	ruby(rubygems) >= 1.3.5
BuildRequires:	rubygems-devel
# %%check
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(cucumber)
BuildRequires:	rubygem(rspec) >= 3
# cucumber test needs ruby.h header and compiler
BuildRequires:	gcc
BuildRequires:	ruby-devel
Requires:	ruby(rubygems) >= 1.3.5
Requires:	rubygem(rake) >= 0.8.3
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
rake-compiler aims to help Gem developers while dealing with
Ruby C extensions, simplifiying the code and reducing the duplication.

It follows *convention over configuration* and set an standarized
structure to build and package C extensions in your gems.

This is the result of expriences dealing with several Gems 
that required native extensions across platforms and different 
user configurations where details like portability and 
clarity of code were lacking. 

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1
mv ../%{gem_name}-%{version}.gemspec .

# rpmlint cosmetic
find ./lib/rake -name \*.rb | xargs sed -i -e '\@/usr/bin/env@d'

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

# be_true -> be_truthy, be_false -> be_falsey
grep -rl be_true  features/ | xargs sed -i 's|be_true|be_truthy|'
grep -rl be_false features/ | xargs sed -i 's|be_false|be_falsey|'

# Don't strip binary for default. Also kill unneeded "-pipe" from LDFLAGS
sed -i tasks/bin/cross-ruby.rake \
	-e '\@LDFLAGS=@d'

# Cucumber 7 change
sed -i cucumber.yml -e "s|~@java|'not @java'|"

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
    Gemfile \
    Rakefile \
    appveyor.yml \
    cucumber.yml \
    features/ \
    spec/ \
    tasks/ \
    tmp/ \
    %{nil}
popd

%check
rm -rf .%{gem_instdir}/spec
cp -a spec/ .%{gem_instdir}/

pushd .%{gem_instdir}
ruby -Ilib -S rspec spec/

export CUCUMBER_PUBLISH_QUIET=true
ruby -Ilib -S cucumber
popd

%files
%{_bindir}/rake-compiler

%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/History.md

%{gem_instdir}/bin/
%{gem_libdir}

%{gem_spec}

%files doc
%{gem_docdir}


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Apr 13 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-1
- 1.3.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 01 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.9-1
- 1.2.9

* Sat Oct 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.8-1
- 1.2.8

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb  1 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.7-1
- 1.2.7

* Thu Jan 25 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.6-1
- 1.2.6

* Thu Aug  3 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.5-1
- 1.2.5

* Tue Aug  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.4-1
- 1.2.4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.3-1
- 1.2.3

* Thu May 25 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.2-1
- 1.2.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-1
- 1.2.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 15 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Fri Jan 28 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.9-2
- Rebuild for tagging issue

* Sun Jan 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.9-1
- 1.1.9

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.8-1
- 1.1.8

* Fri Jan 14 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.7-2
- Fix for cucumber 7 syntax change

* Tue Jan  4 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.7-1
- 1.1.7

* Sun Dec 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.6-1
- 1.1.6

* Fri Dec 10 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.3-1
- 1.1.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-1
- 1.1.1
- Don't strip binary for default, and kill unneeded "-pipe" from LDFLAGS

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 26 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.0-1
- 1.1.0

* Tue Dec 24 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.9-1
- 1.0.9

* Tue Oct 15 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.8-1
- 1.0.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.7-2
- Rebuild

* Thu Jan 10 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.7-1
- 1.0.7

* Sun Dec 30 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-1
- 1.0.6

* Thu Dec 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-2
- rebuild

* Wed Sep  5 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-1
- 1.0.5

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-1
- 1.0.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 31 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Sun Jun 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Sun May 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.9-1
- 0.9.9

* Wed May  4 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.8-2
- 0.9.8

* Wed Mar 23 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.7-1
- 0.9.7

* Wed Mar  9 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.6-1
- 0.9.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan  4 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.5-1
- 0.9.5

* Sun Dec 28 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.4-1
- 0.9.4

* Wed Aug 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.3-1
- 0.9.3

* Thu Jun 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-3
- Adjust test suite for ruby 2.1.x

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-1
- 0.9.2

* Thu Aug  8 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.1-1
- 0.9.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-3
- Fix test failure with ruby200

* Fri Feb 22 2013 Vít Ondruch <vondruch@redhat.com> - 0.8.3-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-1
- 0.8.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-2
- Fix BR

* Thu Jan 24 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-1
- 0.8.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.1-1
- 0.8.1

* Tue Apr 03 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.0-3
- Fix conditionals for F17 to work for RHEL 7 as well.

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.0-2
- Rebuild against ruby 1.9

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.8.0-1
- 0.8.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.9-3
- F-17: Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.9-2
- Kill BR: rubygem(rcov) for now

* Sat Jun 11 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.9-1
- 0.7.9
- %%check now uses rspec, not spec

* Sat Apr 30 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.8-1
- 0.7.8

* Mon Apr  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.7-1
- 0.7.7

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.6-1
- 0.7.6

* Tue Nov 30 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.5-2
- 0.7.5
- Move more files to -doc
- Now needs rubygem(isolate) and some other rubygem(foo) for BR

* Wed Aug 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-1
- 0.7.1

* Thu Dec 10 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.0-1
- 0.7.0

* Wed Jul 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.6.0-1
- 0.6.0

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-2
- F-12: Mass rebuild

* Thu Jul  2 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-2
- Restore files under %%{geminstdir}/bin

* Thu Jun 11 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.5.0-1
- Initial package
