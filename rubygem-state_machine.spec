%global gem_name state_machine

%global rubyabi 1.9.1
  
%if 0%{?fedora} >= 17
  %global rubyabi 1.9.1
%endif

%if 0%{?fedora} >= 19
  %global rubyabi 2.0.0
%endif

Summary:       Adds support for creating state machines for attributes on any Ruby class
Name:          rubygem-%{gem_name}
Version:       1.2.0
Release:       %autorelease
License:       MIT
URL:           http://www.pluginaweek.org
Source0:       http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires:      ruby(release)
Requires:      ruby(rubygems)
Requires:      graphviz-ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem-rake
BuildRequires: graphviz-ruby
BuildRequires: ruby-irb
BuildArch:     noarch
Provides:      rubygem(%{gem_name}) = %{version}

%description
Adds support for creating state machines for attributes on any Ruby class

%package doc
Summary: Documentation files, rdoc, ri, examples and tests

%description doc
Documentation files for state_machine, includes RDoc, ri, tests,
examples and another extra documentation files.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version}

# Modify the gemspec if necessary with a patch or sed
# Also apply patches to code if necessary
# %%patch0 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
mkdir -p .%{gem_dir}

# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# gem install compiles any C extensions and installs into a directory
# We set that to be a local directory so that we can move it into the
# buildroot in %%install
%gem_install

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# rm unnecesary files
rm %{buildroot}%{gem_instdir}/.gitignore
rm %{buildroot}%{gem_instdir}/.travis.yml
rm %{buildroot}%{gem_instdir}/.yardopts
rm -r %{buildroot}%{gem_instdir}/gemfiles
rm %{buildroot}%{gem_instdir}/init.rb
rm %{buildroot}%{gem_instdir}/Appraisals

%check
cd %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}
# gem 'appraisal (~> 0.4.0) not available in Fedora
# gem 'rcov' not supported in Ruby 1.9
# test suite needs to be modified to be run in Fedora
echo "Running tests (disabled)"
#rake test
rm %{buildroot}%{gem_instdir}/Gemfile
rm %{buildroot}%{gem_instdir}/state_machine.gemspec

%files
%{gem_libdir}
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_cache}
%doc %{gem_spec}

%files doc
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/test
%doc %{gem_docdir}
%doc %{gem_instdir}/Rakefile

%changelog
%autochangelog
