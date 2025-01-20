# Generated from thor-0.12.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name thor

Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 9%{?dist}
Summary: Thor is a toolkit for building powerful command-line interfaces
License: MIT
URL: http://whatisthor.com/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The test suite is not shipped with the gem, you may check it out like so:
# git clone https://github.com/erikhuda/thor.git --no-checkout
# cd thor && git archive -v -o thor-1.2.1-spec.txz v1.2.1 spec/
Source1: %{gem_name}-%{version}-spec.txz
# Fix rspec-mocks 3.10.3+ compatibility.
# https://github.com/rails/thor/pull/779/commits/f87021fee1023457bf693dae95ccfe765c3bff61
Patch0: rubygem-thor-1.2.1-Fix-expectations-for-ruby-3-treatment-of-hash-arg.patch
# Fix rspec-expectations 3.11.0+ compatibility.
# https://github.com/rails/thor/pull/782/commits/3da3b44afdf2fa0bd618b87c5d862e9def1d5f4f
Patch1: rubygem-thor-1.2.1-Fix-rspec-mocks-3.11.0-compatibility.patch
# https://github.com/rails/thor/pull/789
# did_you_mean behavior changed in ruby3.2
Patch2: rubygem-thor-1.2.1-did_you_mean-ruby32.patch
# https://github.com/rails/thor/commit/e43a9cd1f9d25ada999e19508216c6052344502f
# Support ruby3.4 error msg formatting change
Patch3: rubygem-thor-1.2.1-ruby34-error-formatting.patch
# ruby package has just soft dependency on rubygem(io-console), while
# Thor always requires it.
Requires: rubygem(io-console)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(io-console)
BuildRequires: rubygem(rake)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: %{_bindir}/git
BuildArch: noarch

%description
Thor is a toolkit for building powerful command-line interfaces.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1

%patch 2 -p1
pushd %{_builddir}
%patch 0 -p1
%patch 1 -p1
%patch 3 -p1
popd

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'

%check
pushd .%{gem_instdir}
cp -r %{_builddir}/spec .

# kill simplecov dependency
sed -i '/simplecov/,/end/ s/^/#/' spec/helper.rb

# Thor does not specify encoding of its imputs, what might cause issues.
# https://github.com/erikhuda/thor/issues/645
LC_ALL=C.UTF-8 rspec -rreadline spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/thor
%license %{gem_instdir}/LICENSE.md
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/.document
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/thor.gemspec

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 19 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-8
- Apply upstream fix for ruby34 error msg formatting change

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.1-3
- Backport upstream patch for ruby3.2 did_you_mean behavior change

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 10 2022 Vít Ondruch <vondruch@redhat.com> - 1.2.1-1
- Update to Thor 1.2.1.
  Resolves: rhbz#2037081

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Pavel Valena <pvalena@redhat.com> - 1.1.0-1
- Update to thor 1.1.0.
  Resolves: rhbz#1918430

* Wed Aug 05 23:45:19 GMT 2020 Pavel Valena <pvalena@redhat.com> - 1.0.1-1
- Update to Thor 1.0.1.
  Resolves: rhbz#1783465

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Vít Ondruch <vondruch@redhat.com> - 0.20.3-1
- Update to Thor 0.20.3.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.19.1-5
- Explicitly set rubygem(io-console) dependency.

* Mon Feb 29 2016 Pavel Valena <pvalena@redhat.com> - 0.19.1-4
- Update rspec dependency to >= 3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 09 2014 Vít Ondruch <vondruch@redhat.com> - 0.19.1-1
- Update to thor 1.19.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jul 25 2013 Josef Stribny <jstribny@redhat.com> - 0.18.1-1
- Update to Thor 0.18.1.

* Mon Mar 04 2013 Josef Stribny <jstribny@redhat.com> - 0.17.0-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to Thor 0.17.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Vít Ondruch <vondruch@redhat.com> - 0.16.0-2
- Disable tests for EL builds.

* Tue Nov 13 2012 Vít Ondruch <vondruch@redhat.com> - 0.16.0-1
- Update to thor 0.16.0.
- Remove rubygem(diff-lcs) dependency, since it is just optional.
- Remove rubygem(ruby2ruby) dependnecy, since it is just optional, to allow
  conversion of Rakefiles to Thorfiles (but it doesnt work withou ParseTree anyway).

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.6-5
- Enable tests.
- Add patches for the failing tests.
- Removed unnecessary ParseTree dependency.

* Mon Jan 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.6-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Mohammed Morsi <mmorsi@redhat.com> - 0.14.6-1
- Updated to latest upstream version

* Wed May 5 2010 Matthew Kent <mkent@magoazul.com> - 0.13.6-1
- New upstream version.

* Fri Dec 18 2009 Matthew Kent <mkent@magoazul.com> - 0.12.0-2
- Add Requires for rubygem(rake) (#542559).
- Upstream replaced Source after the gemcutter migration, update to latest
  (#542559).
- Add Requires for rubygem(diff-lcs) as Thor can take advantage of it for
  colourized diff output (#542559).

* Mon Nov 16 2009 Matthew Kent <mkent@magoazul.com> - 0.12.0-1
- Initial package
