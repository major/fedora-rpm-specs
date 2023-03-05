%global gem_name sys-filesystem

Name:           rubygem-%{gem_name}
Version:        1.4.3
Release:        %autorelease
Summary:        Interface for gathering filesystem information

License:        Apache-2.0
URL:            https://rubygems.org/gems/sys-filesystem
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildRequires:  rubygems-devel

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

rm -vr %{buildroot}%{gem_instdir}/{certs,spec}
rm -v %{buildroot}%{gem_cache}

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}

%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/{{README,CHANGES,MANIFEST}.md,examples}
%{gem_instdir}/{Gemfile,Rakefile,%{gem_name}.gemspec}

%changelog
%autochangelog
