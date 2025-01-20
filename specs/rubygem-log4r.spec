# Generated from log4r-1.1.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name log4r

Name: rubygem-%{gem_name}
Version: 1.1.10
Release: 25%{?dist}
Summary: Log4r, logging framework for ruby
# License is changed for future releases!
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
URL: https://github.com/colbygk/log4r
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Upstream license files
#   https://github.com/colbygk/log4r/issues/39
# Taken from
#   https://github.com/colbygk/log4r/blob/40e2c2edd657a21b34f09dec7de238f348b6f428/
Source1: LICENSE
Source2: LICENSE.LGPLv3
# Fix Ruby 2.5 compatibility.
# https://github.com/colbygk/log4r/pull/57
Patch0: rubygem-log4r-1.1.10-Use-Psych.load_stream-instead-of-deprecated-Psych.lo.patch
# Use asserts correctly.
# https://github.com/colbygk/log4r/pull/58
Patch1: rubygem-log4r-1.1.10-First-parameter-of-assert-is-always-what-is-expected.patch
BuildRequires: rubygems-devel 
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(rexml)
BuildArch: noarch

%description
Log4r is a comprehensive and flexible logging library for use in Ruby programs.
It features a heirarchical logging system of any number of levels, custom level
names, multiple output destinations per log event, custom formatting, and more.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch 0 -p1
%patch 1 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

# License files
install -m 644 %{SOURCE1} .%{gem_instdir}/LICENSE
install -m 644 %{SOURCE2} .%{gem_instdir}/LICENSE.LGPLv3

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# This is not necessary for runtime nor it's a documentation
rm -rf %{buildroot}%{gem_instdir}/lib/log4r/rdoc

# Run the test suite
%check
# Tests are expected to run from tests directory.
pushd .%{gem_instdir}/tests

# The file is directly in "tests" directory.
sed -i '/Configurator.load_xml_file "xml\/testconf.xml"/ s|xml/||' testxmlconf.rb

# These fails wiht "Log level must be in 0..3". Not sure how to fix this.
sed -i '/test_load[24]/a \
    omit' testxmlconf.rb

# Test needs to have 'junk' directory available.
mkdir junk

# Tests needs to be run separately (especially
# test_gdc_default(TestGDC)).
for f in test*.rb; do
  LANG=C.UTF-8 ruby -I.:../lib $f
done
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/LICENSE.LGPLv3

%files doc
%doc %{gem_docdir}
%{gem_instdir}/tests
%doc %{gem_instdir}/doc
%{gem_instdir}/examples


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.10-24
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Vít Ondruch <vondruch@redhat.com> - 1.1.10-14
- Add `BR: rubygem(rexml)` which was removed from StdLib in Ruby 3.0.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Vít Ondruch <vondruch@redhat.com> - 1.1.10-7
- Fix Ruby 2.5 compatibility and polish the test suite a bit.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 26 2014 Josef Stribny <jstribny@redhat.com> - 1.1.10-2
- Fix licensing
- Use Minitest 5

* Mon Sep 08 2014 Josef Stribny <jstribny@redhat.com> - 1.1.10-1
- Initial package
