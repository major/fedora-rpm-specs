%global gem_name minitest-profile

Name:           rubygem-%{gem_name}
Version:        0.0.2
Release:        %autorelease
Summary:        Outputter to display the slowest tests in a minitest suite
License:        MIT

URL:            https://github.com/nmeans/minitest-profile
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby

BuildRequires:  (rubygem(minitest) >= 5.0 with rubygem(minitest) < 6)

BuildArch:      noarch

%description
Outputter to display the slowest tests in a minitest suite.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ruby -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd


%files
%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}

%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/minitest-profile.gemspec

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}


%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/test


%changelog
%autochangelog
