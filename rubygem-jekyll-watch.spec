%global gem_name jekyll-watch

Name:           rubygem-%{gem_name}
Summary:        Rebuild your Jekyll site when a file changes
Version:        2.2.1
Release:        %autorelease
License:        MIT

URL:            https://github.com/jekyll/jekyll-watch
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.1.0

BuildArch:      noarch


%description
Rebuild your Jekyll site when a file changes with the `--watch` switch.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%setup -q -n  %{gem_name}-%{version}


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%exclude %{gem_cache}


%files doc
%doc %{gem_docdir}


%changelog
%autochangelog
