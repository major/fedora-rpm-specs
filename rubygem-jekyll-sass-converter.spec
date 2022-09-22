%global gem_name jekyll-sass-converter

Name:           rubygem-%{gem_name}
Version:        2.2.0
Release:        %autorelease
Summary:        Basic Sass converter for Jekyll
License:        MIT

URL:            https://github.com/jekyll/jekyll-sass-converter
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{url}/archive/v%{version}/%{gem_name}-%{version}.tar.gz

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby

BuildRequires:  rubygem(jekyll) >= 4.0.0
BuildRequires:  rubygem(minima)
BuildRequires:  rubygem(rspec)

BuildArch:      noarch

%description
A basic Sass converter for Jekyll.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version}

# extract README, LICENSE, and test files not shipped with the gem
mkdir upstream && pushd upstream
tar -xzvf %{SOURCE1}
mv %{gem_name}-%{version}/spec ../spec
mv %{gem_name}-%{version}/README.md ../
mv %{gem_name}-%{version}/LICENSE.txt ../
popd && rm -r upstream


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
rspec spec


%files
%license LICENSE.txt
%doc README.md

%dir %{gem_instdir}

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
%autochangelog
