%global gem_name rspec-its

Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 9%{?dist}
Summary: Provides "its" method formerly part of rspec-core
License: MIT
URL: https://github.com/rspec/rspec-its
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix RSpec 3.9 compatibility.
# https://github.com/rspec/rspec-its/pull/75
Patch0: rubygem-rspec-its-1.3.0-Bump-to-RSpec-3.9.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec-core)
BuildRequires: rubygem(rspec-expectations)
BuildRequires: rubygem(aruba)
%if 0%{?fedora} >= 36
BuildRequires: rubygem(matrix)
%endif
BuildArch: noarch

%description
RSpec extension gem for attribute matching.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -Ilib spec
export RUBYOPT="-I${PWD}/lib"
cucumber
popd


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/features
%{gem_instdir}/spec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/script
%doc %{gem_instdir}/README.md
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb  1 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.0-8
- BR: rubygem(aruba) for F-36 (ruby31)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 07 2020 Vít Ondruch <vondruch@redhat.com> - 1.3.0-3
- Fix RSpec 3.9 compatibility to fix FTBFS (rhbz#1800030).

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 15 2019 Pavel Valena <pvalena@redhat.com> - 1.3.0-1
- Update to rspec-its 1.3.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Pavel Valena <pvalena@redhat.com> - 1.2.0-1
- Update to 1.2.0.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 09 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.1.0-1
- Update to rspec-its 1.1.0 (RHBZ #1168743)
- Correct %%license file (RHBZ #1168743)
- Remove f19 and f20 dist conditionals, since we'll only ship on f22 and later.
  (RHBZ #1168743)

* Thu Nov 27 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.0.1-2
- Initial package
