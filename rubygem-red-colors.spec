# Generated from red-colors-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name red-colors

Name:		rubygem-%{gem_name}
Version:	0.3.0
Release:	5%{?dist}

Summary:	Red Colors provides a wide array of features for dealing with colors
License:	MIT

URL:		https://github.com/red-data-tools/red-colors
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
BuildRequires:	rubygem(test-unit)
%if 0%{?fedora} >= 36
BuildRequires:	rubygem(matrix)
%endif
BuildArch:	noarch

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
# rubygem(matrix) is provided by system-default
# On Fedora <= 35, this was in ruby-libs, removing dependency
# On Fedora >= 36, this is provided by ruby-bundled-gems, so don't remove dependency
%if 0%{?fedora} < 36
%gemspec_remove_dep -s %{gem_name}-%{version}.gemspec -g matrix
%endif

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

%changelog
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
