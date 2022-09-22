%global gem_name minima

Name:           rubygem-%{gem_name}
Version:        2.5.1
Release:        %autorelease
Summary:        Beautiful, minimal theme for Jekyll
License:        MIT

URL:            https://github.com/jekyll/minima
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby
BuildRequires:  rubygems-devel
BuildRequires:  ruby(release)

BuildArch:      noarch

%description
A beautiful, minimal theme for Jekyll.


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


%files
%license %{gem_instdir}/LICENSE.txt

%dir %{gem_instdir}
%{gem_instdir}/_includes
%{gem_instdir}/_layouts
%{gem_instdir}/_sass
%{gem_instdir}/assets

%{gem_spec}

%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md


%changelog
%autochangelog
