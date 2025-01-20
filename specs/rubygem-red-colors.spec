# Generated from red-colors-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name red-colors

Name:		rubygem-%{gem_name}
Version:	0.4.0
Release:	3%{?dist}

Summary:	Red Colors provides a wide array of features for dealing with colors
# SPDX confirmed
License:	MIT

URL:		https://github.com/red-data-tools/red-colors
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(matrix)
BuildArch:	noarch
# red-colors contains some json files, reading them requires the below
# also, file inclusion always requires this as:
# json <- colors/colormap_data.rb <- colors.rb
Requires:		rubygem(json)

%description
Red Colors provides a wide array of features for dealing with colors. This
includes conversion between colorspaces, desaturation, and parsing colors.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}/
rm -rf \
	.yardopts \
	Gemfile \
	Rakefile \
	*.gemspec \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
ruby test/run.rb
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc		%{gem_instdir}/README.md

%{gem_libdir}
%{gem_instdir}/data/
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/doc/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 20 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-1
- 0.4.0
- SPDX confirmation

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-7
- Backport upstream patch to suppress unused variables warnings

* Wed Nov  9 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-6
- Explicitly require rubygem(json)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-4
- F-36: don't remove matrix gemspec dependency, now provided by ruby-bundled-gems

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-1
- 0.3.0

* Tue Feb 09 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.1-1
- Initial package
