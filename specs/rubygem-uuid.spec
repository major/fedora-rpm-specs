%global gem_name uuid

Name:           rubygem-%{gem_name}
Version:        2.3.7
Release:        23%{?dist}
Summary:        UUID generator based on RFC 4122

# Automatically converted from old format: MIT or CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-MIT OR LicenseRef-Callaway-CC-BY-SA
URL:            http://github.com/assaf/uuid
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/assaf/uuid/pull/39
Patch0:         %{name}-tool.patch
# https://github.com/assaf/uuid/pull/36
# Needed for ruby3.2, which removes File.exists? deprecated since ruby 2.1
Patch1:         %{name}-file_exists_deprecation.patch
# https://github.com/assaf/uuid/pull/61
# Compatibility for mocha 2.0
Patch2:         %{gem_name}-pr61-mocha-2.0-compat.patch

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(macaddr)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(test-unit)
%if 0%{?fedora} && 0%{?fedora} <= 20 || 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(release)
Requires:       ruby(rubygems)
Requires:       rubygem(macaddr) >= 1.0
Requires:       rubygem(macaddr) < 2
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
UUID generator for producing universally unique identifiers based on RFC 4122
(http://www.ietf.org/rfc/rfc4122.txt).


%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.


%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
sed -i -e '1s,.*,#!/usr/bin/ruby,' bin/uuid

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec


%build
gem build %{gem_name}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
# rename to fix conflict with uuid package
mv .%{_bindir}/uuid \
        %{buildroot}%{_bindir}/uuid.rb

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x


%check
pushd .%{gem_instdir}
# https://github.com/assaf/uuid/issues/43
sed -i -e "s,'mocha','mocha/setup'," test/*.rb
ruby -Ilib:test -e 'Dir.glob "./test/*.rb", &method(:require)'
popd


%files
%dir %{gem_instdir}/
%dir %{gem_instdir}/bin/
%license %{gem_instdir}/MIT-LICENSE
%{_bindir}/uuid.rb
%{gem_instdir}/bin/uuid
%{gem_libdir}/
%{gem_spec}
%{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/bin/rake
%exclude %{gem_instdir}/bin/yard
%exclude %{gem_instdir}/bin/yardoc
%exclude %{gem_instdir}/bin/yri
%exclude %{gem_instdir}/test/
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.rdoc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.7-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-19
- Apply upstream PR for mocha 2.0 compatibility

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.7-16
- Backport upstream patch for File.exists? removal for ruby3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 08 2015 František Dvořák <valtri@civ.zcu.cz> - 2.3.7-1
- Initial package
