# Generated from htmlentities-4.0.0.gem by gem2rpm -*- rpm-spec -*-
%global	gem_name		htmlentities

# Some functions removed on 4.2.4. Please don't upgrade this rpm
# to 4.3.0+ on F-14-

Summary:	A module for encoding and decoding (X)HTML entities
Name:		rubygem-%{gem_name}
Version:	4.3.4
Release:	20%{?dist}
License:	MIT
URL:		https://github.com/threedaymonk/htmlentities
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)

BuildRequires:	rubygems-devel
BuildRequires:	rubygem(test-unit)
Requires:	ruby(rubygems)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
HTMLEntities is a simple library to facilitate encoding and 
decoding of named (&yacute; and so on) or numerical (&#123; or &#x12a;) 
entities in HTML and XHTML documents.

%package	doc
Summary:	Documentation for %{name}
# Directory ownership issue
Requires:	%{name} = %{version}-%{release}
Requires:	ruby(rubygems)

%description	doc
This package contains documentation for %{name}.

%package	-n ruby-%{gem_name}
Summary:	Non-Gem support for %{gem_name}
Requires:	%{name} = %{version}-%{release}
Provides:	ruby(%{gem_name}) = %{version}-%{release}

%description	-n ruby-%{gem_name}
This package provides non-Gem support for %{gem_name}.

%prep
# First install rubygems under %%_builddir to execute some
# tests
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# Cleanups
rm -f %{buildroot}%{gem_instdir}/setup.rb

%check
pushd ./%{gem_instdir}/

sed -i -e '2i gem "test-unit"' test/test_helper.rb

ruby -Ilib:. -e 'Dir.glob("test/*.rb").each{|f| require f}'

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%{gem_instdir}/lib/

%{gem_cache}
%{gem_spec}

%files	doc
%{gem_instdir}/perf/
%{gem_instdir}/test/
%{gem_docdir}/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul  6 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.3.4-1
- 4.3.4

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 27 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Jun  9 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.3.2-2
- Rebuild

* Fri Jun  6 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.3.2-1
- Update to 4.3.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.3.1-7
- Clean up

* Tue Mar 05 2013 Vít Ondruch <vondruch@redhat.com> - 4.3.1-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.1-3
- F-17: rebuild against ruby19

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.1-1
- 4.3.1

* Sun Apr 03 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 4.3.0-1
- 4.3.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  1 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.4-1
- 4.2.4

* Fri Jan 14 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.3-1
- 4.2.3

* Sun Nov  6 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.2-1
- 4.2.2

* Sat Apr 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.1-1
- 4.2.1

* Wed Jan 13 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.0-2.respin1
- 4.2.0 (tarball seems respun)

* Thu Aug 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.2.0-1
- 4.2.0

* Fri Aug 21 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.1.0-1
- 4.1.0

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.0.0-3
- F-12: Mass rebuild

* Fri Mar 6 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Cleanups

* Tue Mar 03 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 4.0.0-1
- Initial package
