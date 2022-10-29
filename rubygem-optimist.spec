%global gem_name optimist

# https://github.com/ManageIQ/optimist/issues/111
%bcond_with check

Name:           rubygem-%{gem_name}
Version:        3.0.0
Release:        6%{?dist}
Summary:        Commandline option parser for Ruby

# https://github.com/ManageIQ/optimist/issues/112
License:        MIT
URL:            https://rubygems.org/gems/optimist
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel
%if %{with check}
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(chronic)
%endif

BuildArch:      noarch

%description
%{summary}.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

rm -vr %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml,test}
rm -v %{buildroot}%{gem_cache}

%if %{with check}
%check
ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
%endif

%files
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%dir %{gem_instdir}
%doc %{gem_instdir}/{README.md,History.txt,FAQ.txt}
%{gem_instdir}/{Gemfile,Rakefile,%{gem_name}.gemspec}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 3.0.0-1
- Initial package
