%global gem_name jekyll-toc

Name:           rubygem-%{gem_name}
Version:        0.18.0
Release:        %autorelease
Summary:        Jekyll Table of Contents plugin
License:        MIT

URL:            https://github.com/toshimaru/jekyll-toc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{url}/archive/v%{version}/%{gem_name}-%{version}.tar.gz

# Patch to disable coverage reporting
Patch0:         00-disable-simplecov.patch

BuildRequires:  git-core
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.4.0

BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(jekyll) >= 3.8
BuildRequires:  (rubygem(minitest) >= 5.0 with rubygem(minitest) < 6)
BuildRequires:  (rubygem(nokogiri) >= 1.10 with rubygem(nokogiri) < 2)
BuildRequires:  rubygem(rake)

BuildArch:      noarch

%description
A liquid filter plugin for Jekyll which generates a table of contents.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -N -n %{gem_name}-%{version}

# extract test files not shipped with the gem
mkdir upstream && pushd upstream
tar -xzvf %{SOURCE1}
mv %{gem_name}-%{version}/test ../test
popd && rm -r upstream

%autopatch -p1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
ruby -I"lib:test" -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'


%files
%license %{gem_instdir}/LICENSE.md

%dir %{gem_instdir}

%{gem_instdir}/Appraisals
%{gem_instdir}/gemfiles

%{gem_libdir}

%{gem_spec}

%exclude %{gem_cache}
%exclude %{gem_instdir}/.rubocop.yml


%files doc
%doc %{gem_docdir}

%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/jekyll-toc.gemspec


%changelog
%autochangelog
