%global	gem_name	mini_portile2

Name:		rubygem-%{gem_name}
Version:	2.8.8
Release:	2%{?dist}

Summary:	Simplistic port-like solution for developers
# SPDX confirmed
License:	MIT
URL:		http://github.com/flavorjones/mini_portile
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	rubygems-devel
# BuildRequires:	rubygem(minitest)
# BuildRequires:	rubygem(minitest-hooks)
#BuildRequires:	rubygem(archive-tar-minitar)
BuildArch:		noarch

%description
Simplistic port-like solution for developers. It provides a standard and
simplified way to compile against dependency libraries without messing up your
system.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.concourse.yml \
	.github/ \
	.gitignore \
	.travis.yml \
	Gemfile \
	Rakefile \
	appveyor.yml \
	concourse/ \
	*.gemspec \
	test/ \
	%{nil}
popd

%check
# Currently minitest-hooks is not available on Fedora,
# exit
exit 0

# This requires net connection, so give up test suite
# without net
# (also just exit without ping)
ping -w3 fedoraproject.org || exit 0

pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.md
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/SECURITY.md

%{gem_libdir}
%{gem_spec}

%files	doc
%doc	%{gem_docdir}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Dec 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.8-1
- 2.8.8

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 04 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.7-1
- 2.8.7

* Mon Apr 15 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.6-1
- 2.8.6

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.5-1
- 2.8.5

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.4-1
- 2.8.4

* Tue Jul 18 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.3-1
- 2.8.3

* Thu May  4 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.2-1
- 2.8.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.1-1
- 2.8.1

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 21 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.8.0-1
- 2.8.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 22 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.1-1
- 2.7.1

* Thu Sep  2 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.7.0-1
- 2.7.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.6.1-1
- 2.6.1

* Sat May  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.1-1
- 2.5.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.0-1
- 2.5.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.4.0-1
- 2.4.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.0-1
- 2.3.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.0-1
- 2.1.0

* Wed Dec 09 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.0.0-1
- Initial package
