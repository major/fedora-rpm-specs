# Generated from rttool-1.0.3.0.gem by gem2rpm -*- rpm-spec -*-
%global	gem_name	rttool

Name:		rubygem-%{gem_name}
Version:	1.0.3.0
Release:	26%{?dist}

Summary:	Converter from RT into various formats
# See rttool.en.rd
# SPDX confirmed
License:	Ruby OR GPL-2.0-only
# raa is dead
#URL:		http://raa.ruby-lang.org/project/rttool/
URL:		https://github.com/genki/rttool
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(minitest)
BuildRequires:	rubygem(nkf)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(rdtool)
BuildRequires:	rubygem(racc)
Requires:	rubygem(racc)
Requires:	ruby(release)
Requires:	ruby(rubygems)

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
RT is a simple and human-readable table format.
RTtool is a converter from RT into various formats.
RT can be incorporated into RD.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n  %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

# Encoding
for f in \
	rttool.*.*
do
	iconv -f EUC-JP -t UTF-8 -o $f{.utf,}
	touch -r $f{,.utf}
	mv $f{.utf,}
done

# shebang
sed -i \
	-e '\@#![ \t]*/usr/bin/ruby@d' \
	lib/rt/*.rb

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
chmod 0755 bin/rt2

export RUBYOPT="-I$(pwd)/lib"
export PATH=$(pwd)/bin:$PATH
ruby -Ilib:. -e 'gem "minitest" ; Dir.glob("test/test*.rb").each {|f| require f}'

popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/ChangeLog
%license	%{gem_instdir}/GPL
%doc %{gem_instdir}/rttool.*.html
%license	%{gem_instdir}/rttool.*.rd

%{_bindir}/rdrt2
%{_bindir}/rt2
%{gem_instdir}/bin

%{gem_libdir}
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/examples/
%exclude	%{gem_instdir}/test/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Nov 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3.0-25
- BR: rubygem(nkf) explicitly for ruby34

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 05 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3.0-23
- SPDX migration

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3.0-20
- Modernize spec file
- Use minitest5 instead of minitest4

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3.0-13
- R,BR rubygem(racc)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3.0-5
- BR: rubygem(test-unit)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3.0-3
- Force to use minitest ver4 for now

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3.0-1
- Initial package
