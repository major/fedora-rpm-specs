%global gem_name jekyll-asciidoc

Name:           rubygem-%{gem_name}
Version:        3.0.1
Release:        %autorelease
Summary:        Jekyll plugin for using AsciiDoc sources with Asciidoctor
License:        MIT

URL:            https://github.com/asciidoctor/jekyll-asciidoc
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{url}/archive/v%g{version}/%{gem_name}-%{version}.tar.gz
Patch0:         0001-Disable-tests-requiring-pygments.rb.patch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 1.9.3
# Test dependencies
BuildRequires:  rubygem(asciidoctor)
BuildRequires:  rubygem(jekyll)
BuildRequires:  rubygem(rspec)

BuildArch:      noarch

%description
A Jekyll plugin that converts the AsciiDoc source files in your site to HTML
pages using Asciidoctor.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
# Some patches are applied to test files,
# which are only extracted in the following step.
%autosetup -n %{gem_name}-%{version} -p1 -N
%autopatch -p1 -m1

# extract test files not shipped with the gem
mkdir upstream && pushd upstream
tar -xzvf %{SOURCE1}
mv %{gem_name}-%{version}/spec ../spec
popd && rm -r upstream
patch -p1 -s --fuzz=0 --no-backup-if-mismatch -f < %{PATCH0}


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
rspec spec


%files
%license %{gem_instdir}/LICENSE

%dir %{gem_instdir}

%{gem_libdir}

%exclude %{gem_cache}

%{gem_spec}


%files doc
%doc %{gem_docdir}

%doc %{gem_instdir}/CHANGELOG.adoc
%doc %{gem_instdir}/README.adoc
%doc %{gem_instdir}/jekyll-asciidoc.gemspec

%exclude %{gem_instdir}/.yardopts

%{gem_instdir}/Gemfile


%changelog
%autochangelog
