%global gem_name jekyll-toc

Name:           rubygem-%{gem_name}
Version:        0.17.1
Release:        %autorelease
Summary:        Jekyll Table of Contents plugin
License:        MIT

URL:            https://github.com/toshimaru/jekyll-toc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

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
%autosetup -S git -n %{gem_name}-%{version} -p1


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
rake test
popd


%files
%license %{gem_instdir}/LICENSE.md

%dir %{gem_instdir}

%{gem_instdir}/Appraisals
%{gem_instdir}/gemfiles

%{gem_libdir}

%{gem_spec}

%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rubocop.yml
%exclude %{gem_instdir}/.github/


%files doc
%doc %{gem_docdir}

%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/jekyll-toc.gemspec
%{gem_instdir}/test


%changelog
%autochangelog
