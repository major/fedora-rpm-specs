%global	gem_name	yard

Name:		rubygem-%{gem_name}
Version:	0.9.37
Release:	2%{?dist}

Summary:	Documentation tool for consistent and usable documentation in Ruby

# lib/yard/parser/ruby/legacy/ruby_lex.rb: under GPL-2.0-only OR Ruby
# lib/yard/rubygems/backports/: MIT OR Ruby
# lib/yard/server/http_utils.rb: BSD 2-Clause
# lib/yard/server/templates/default/fulldoc/html/js/autocomplete.js:
#   MIT OR GPL(version 2??), as this is OR, use MIT for now
# Others are MIT
# SPDX confirmed
License:	MIT AND (MIT OR Ruby) AND BSD-2-Clause AND (GPL-2.0-only OR Ruby)

URL:		http://yardoc.org
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
# Source1 is created by $ bash %%SOURCE2 %%version
Source2:	yard-create-missing-test-files.sh

# The 'irb/notifier' might be required for parsing of some old Ruby code.
# https://github.com/lsegal/yard/blob/v0.9.24/lib/yard/parser/ruby/legacy/irb/slex.rb#L13
Recommends:	rubygem(irb)

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(RedCloth)
BuildRequires:	rubygem(asciidoctor)
BuildRequires:	rubygem(bundler)
BuildRequires:	rubygem(irb)
BuildRequires:	rubygem(rack)
BuildRequires:	rubygem(rake)
BuildRequires:	rubygem(redcarpet)
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(webrick)

BuildArch:		noarch

%description
YARD is a documentation generation tool for the Ruby programming language.
It enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:		noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

pushd %{buildroot}%{gem_instdir}
rm -rf .yardopts* \
	%{nil}
popd

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod 0755
rm -f %{buildroot}%{gem_cache}

%check
# FIXME
# investigate this: was okay with yard 0.9.28
sed -i spec/cli/diff_spec.rb \
	-e '\@"searches for .gem file"@s|\([ \t]it \)|\txit |'
rspec -r spec_helper spec

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LEGAL
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md

%{_bindir}/yard
%{_bindir}/yardoc
%{_bindir}/yri

%{gem_libdir}/
%{gem_instdir}/bin
%{gem_instdir}/po/
%{gem_instdir}/templates/

%{gem_spec}
%{?gem_plugin}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/docs/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.37-1
- 0.9.37

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 01 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.36-1
- 0.9.36 (Fixes CVE-2024-27285)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov 10 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.34-4
- Testsuite: remove invalid yield usage from spec (for ruby3.3)

* Mon Sep 25 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.34-3
- Backport upstream patch for BOM detection change in ruby33

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.34-1
- 0.9.34

* Wed Apr 12 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.33-1
- 0.9.33

* Mon Apr 10 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.32-1
- 0.9.32

* Sun Apr  9 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.29-1
- 0.9.29
- Whitespace cleanup
- SPDX migration

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 08 2022 Vít Ondruch <vondruch@redhat.com> - 0.9.28-1
- Update to YARD 0.9.28.
  Resolves: rhbz#2027537
  Resolves: rhbz#2113713

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 06 2021 Vít Ondruch <vondruch@redhat.com> - 0.9.26-3
- Add `BR: rubygem(irb)`, which was previosly pulled in indirectly.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 18 02:42:33 CET 2020 Pavel Valena <pvalena@redhat.com> - 0.9.26-1
- Update to yard 0.9.26.
  Resolves: rhbz#1830795
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 Vít Ondruch <vondruch@redhat.com> - 0.9.24-1
- Update to YARD 0.9.24.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Vít Ondruch <vondruch@redhat.com> - 0.9.12-3
- Fix FTBFS due to failing test suite (rhbz#1556422).

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Vít Ondruch <vondruch@redhat.com> - 0.9.12-1
- Update to YARD 0.9.12.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Vít Ondruch <vondruch@redhat.com> - 0.9.8-1
- Update to YARD 0.9.8.

* Wed May 25 2016 Jun Aruga <jaruga@redhat.com> - 0.8.7.6-3
- Fix test suite for Ruby 2.3 compatibility. (rhbz#1308100)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 08 2015 Vít Ondruch <vondruch@redhat.com> - 0.8.7.6-1
- Update to YARD 0.8.7.6.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 03 2014 Vít Ondruch <vondruch@redhat.com> - 0.8.7.4-1
- Update to yard 0.8.7.4.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Vít Ondruch <vondruch@redhat.com> - 0.8.7-1
- Update to yard 0.8.7.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Vít Ondruch <vondruch@redhat.com> - 0.8.5.2-1
- Update to yard 0.8.5.2.

* Fri Mar 15 2013 Vít Ondruch <vondruch@redhat.com> - 0.8.2.1-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Vít Ondruch <vondruch@redhat.com> - 0.8.2.1-1
- Update to yard 0.8.2.1.

* Thu May 03 2012 Vít Ondruch <vondruch@redhat.com> - 0.8.1-1
- Update to yard 0.8.1.

* Wed Jan 25 2012 Vít Ondruch <vondruch@redhat.com> - 0.7.4-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Vít Ondruch <vondruch@redhat.com> - 0.7.4-1
- Updated to yard 0.7.4.

* Mon Jul 25 2011 Mo Morsi <mmorsi@redhat.com> - 0.7.2-1
- update to latest upstream release
- fixes to conform to fedora guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.5.3-3
- fixed dependencies/package issues according to guidelines

* Mon Feb 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.5.3-2
- cleaned up macros, other package guideline compliance fixes
- corrected license, added MIT
- include all files and docs, added check/test section

* Mon Feb 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.5.3-1
- Initial package

